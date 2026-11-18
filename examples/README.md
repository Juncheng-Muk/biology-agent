# Try a study-design audit

This example uses **synthetic metadata only**. It contains no participant information, sequencing reads, expression matrix, or biological findings. The cell counts are invented to define the scenario; they are not measured results.

The task is deliberately small: assess whether a proposed two-group single-cell study can support a group-specific expression claim before beginning an analysis.

## Inputs

- [samples.tsv](confounded-design/samples.tsv): six fictional donors, one sample per donor, and 50,000 reported cells in total.
- [prompt.md](confounded-design/prompt.md): the complete task to give the agent.

There are three independent donors in condition A and three in condition B. All A samples were assigned to batch 1, and all B samples to batch 2. No expression data are provided.

## Run the example

After installing the skill, open this repository in a host that supports it. Give the agent the contents of [prompt.md](confounded-design/prompt.md) and access to [samples.tsv](confounded-design/samples.tsv). The prompt requests an English response; the skill otherwise defaults to Chinese.

For a host without skill discovery, provide [SKILL.md](../SKILL.md) as task guidance together with its referenced files and the example inputs. This is a manual adaptation, not a claim that all hosts support the same tools or invocation syntax.

No dataset download, API key, scientific package installation, or numerical analysis is needed to review this metadata. A host may use its normal model service to generate the response.

## What to inspect in the response

These are review criteria, **not a recorded output or benchmark result**:

| Criterion | Expected observation |
| --- | --- |
| Independent replication | Identifies six donors overall and three per condition; does not treat the 50,000 cells as independent biological replicates |
| Confounding | Identifies complete overlap between condition and batch, so their effects cannot be separately estimated from this design |
| Method limits | Does not claim that integration, pseudobulk aggregation, or a model containing both terms will resolve complete confounding |
| Missing data | States that no expression matrix was supplied and that differential expression has not been run |
| Useful next step | Offers a metadata audit and a plan for data inspection; recommends a design with condition representation across batches for the intended group comparison |
| Claim discipline | Does not invent gene effects, P values, citations, or a causal disease mechanism |
| Execution honesty | Distinguishes a design assessment and proposed analysis from completed numerical work |

A response can satisfy these criteria with different wording or a different structure. Evaluate the reasoning rather than matching phrases. If a response implies that pseudobulk alone repairs the batch problem, record that as a substantive failure even if it correctly counts donors.

## Record a trial

To make a manual trial inspectable, save the exact prompt, the skill revision, the host/model identifier if available, the response, and brief notes against the criteria above. Record unavailable metadata as unavailable. Repeat trials and additional designs would be needed to assess reliability; a successful response to this single example does not validate an end-to-end omics workflow.
