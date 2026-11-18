#!/usr/bin/env python3
"""Validate the skill package and the synthetic example, without model calls."""

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    check(match is not None, "SKILL.md is missing YAML frontmatter")
    if match:
        metadata = yaml.safe_load(match.group(1))
        check(isinstance(metadata, dict), "Frontmatter must be a mapping")
        if isinstance(metadata, dict):
            check(metadata.get("name") == "biology-agent", "Skill name must be biology-agent")
            description = metadata.get("description")
            check(isinstance(description, str) and 0 < len(description) <= 1024,
                  "Skill description must be a nonempty string of at most 1024 characters")

    ui = yaml.safe_load((ROOT / "agents/openai.yaml").read_text(encoding="utf-8"))
    interface = ui.get("interface", {}) if isinstance(ui, dict) else {}
    short_description = interface.get("short_description", "")
    check(isinstance(short_description, str) and 25 <= len(short_description) <= 64,
          "UI short_description must have 25–64 characters")
    prompt = interface.get("default_prompt", "")
    check(isinstance(prompt, str) and "$biology-agent" in prompt,
          "UI default_prompt must explicitly invoke $biology-agent")

    for path in ROOT.rglob("*.md"):
        if any(part in {".git", ".venv"} for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        check("[TODO:" not in text, f"Unfinished scaffold in {path.relative_to(ROOT)}")
        for target in re.findall(r"\]\(([^\s)]+)\)", text):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            local = target.split("#", 1)[0]
            check(not local.startswith("/"), f"Machine-specific link in {path.relative_to(ROOT)}")
            check((path.parent / local).exists(),
                  f"Broken link in {path.relative_to(ROOT)}: {target}")

    with (ROOT / "examples/confounded-design/samples.tsv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        check(reader.fieldnames == ["sample_id", "donor_id", "condition", "batch", "reported_cells"],
              "Unexpected sample-table schema")
        rows = list(reader)
    check(len(rows) == 6, "Synthetic example must contain six samples")
    check(len({r["sample_id"] for r in rows}) == len(rows), "Duplicate sample IDs")
    check(len({r["donor_id"] for r in rows}) == len(rows), "Example expects distinct donors")
    check(Counter(r["condition"] for r in rows) == {"A": 3, "B": 3}, "Expected three donors per condition")
    cells = [int(r["reported_cells"]) for r in rows]
    check(all(n > 0 for n in cells) and sum(cells) == 50000, "Invented cell counts are inconsistent")
    layout = defaultdict(set)
    for row in rows:
        layout[row["condition"]].add(row["batch"])
    check(dict(layout) == {"A": {"batch_1"}, "B": {"batch_2"}},
          "Example must preserve complete condition–batch confounding")

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: skill metadata, UI metadata, Markdown links, and synthetic example consistency.")
    print("Scope: repository validation only; no model evaluation or omics analysis was run.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(validate())
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
