# Validation record

This page separates repository checks from observations about an agent response. It reports no real-data benchmark or end-to-end omics validation.

## Repository checks

Run from the repository root after installing `requirements-dev.txt`:

```bash
python3 scripts/validate.py
```

The validator checks skill frontmatter, UI invocation metadata, relative Markdown links, and the synthetic sample table's schema, donor uniqueness, cell-count totals, and condition–batch layout. It does not call a model or evaluate scientific reasoning.

## Manual behavioral trial

| Field | Recorded value |
| --- | --- |
| Date | 2026-11-18, Asia/Shanghai |
| Host | Codex; a separate subagent without inherited conversation history |
| Input | [Complete prompt](../examples/confounded-design/prompt.md), [synthetic sample table](../examples/confounded-design/samples.tsv), `SKILL.md` and relevant references |
| Evaluator material withheld | The examples README and architecture documentation, including expected observations |
| Tools allowed | Local read-only inspection; no network, editing, delegation, or expression analysis |
| Model / sampling metadata | Not recorded; do not infer a model-specific performance result |
| Number of trials | One for this published example |
| Output | [Unchanged response](trials/2026-11-18-response.md) |
| Review | Qualitative review by the coordinating agent; not independent expert adjudication |

The review found the following in the recorded response:

| Criterion | Observation |
| --- | --- |
| Independent replication | Identified three donors per condition, rather than 50,000 independent cells |
| Confounding | Showed the condition-by-batch table and explained the inability to separate their effects |
| Method limits | Explained why donor-aware models address nesting but cannot resolve complete confounding |
| Missing expression data | Reported no differential expression or gene-level result |
| Useful next steps | Requested the appropriate inputs and proposed balanced allocation across batches |
| Claim discipline | Produced no P values, gene effects, citations, or claims of a causal disease mechanism |
| Execution status | Labeled the completed work as a metadata audit and analysis plan |

These are observations from one response, not a percentage score. They do not establish repeatability, comparative model quality, validity of future code, or analysis accuracy on real datasets. No external biological expert reviewed this trial.

## Repeating or extending the evaluation

Use the same prompt and sample table with the skill revision under examination. Save the exact output, model and sampling settings if available, and review reasoning against the criteria in [the example guide](../examples/README.md). Do not replace a failed output with a rewritten answer. Additional trials should include identifiable designs as well as confounded ones, so the evaluation also detects unnecessary refusal or overly restrictive advice.
