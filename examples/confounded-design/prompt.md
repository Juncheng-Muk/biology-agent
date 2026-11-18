Use $biology-agent to review a proposed single-cell study. Respond in English.

Read `examples/confounded-design/samples.tsv`. All entries are synthetic: each row represents one sample from a distinct donor, and `reported_cells` is an invented count for this example. There are no expression data or existing differential-expression results.

The intended question is whether condition B differs from condition A in cell-type-specific gene expression. The team proposes using an integrated expression matrix, treating every cell as an independent replicate, and interpreting resulting differences as effects of condition.

Please provide a concise study-design audit:

1. Identify the independent biological replicates and describe the condition-by-batch layout.
2. Assess which parts of the proposed inference are supported by the metadata and which are not.
3. Explain whether changing the analysis method can address the identified design limitations.
4. Propose useful work that can be done now, the inputs needed for later analysis, and a sampling design that would support a more defensible comparison.
5. Clearly label the status of the work you actually completed.

This request is for a design assessment and an analysis plan. It does not require expression analysis or literature retrieval.
