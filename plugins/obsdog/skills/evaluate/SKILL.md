---
name: evaluate
description: Validate, run, score, and compare reproducible ObsDog retrieval datasets while preserving immutable runs, judgment provenance, and unjudged results. Use for ObsDog search evaluation or baseline comparison; do not treat model-proposed qrels as human gold.
---

# Evaluate ObsDog

Evaluation datasets are separate from Personal Space telemetry and must remain version-pinned.

## Workflow

1. Inspect `obsdog eval --help` and validate the dataset before a run.
2. Confirm the dataset ID/version, pinned source digests, judgment status, corpus/query/qrel counts, and intended adapter.
3. Write each run to a new path. Never overwrite or edit an immutable run file.
4. Score the exact run against the exact validated dataset.
5. Compare engines only when they use the same corpus, queries, qrels, result limit, and documented query translation.

The current local baselines are ObsDog FTS5 and ripgrep exact/token-OR. Do not claim an Obsidian comparison until a pinned plugin-free adapter and export procedure are present.

## Interpretation

Report nDCG@10, MRR@10, Recall@5/20, Precision@5, zero-result rate, unjudged@10, latency percentiles, query count, qrel count, and judgment provenance. Keep ranking quality separate from observability conformance.

`model_candidate` judgments are hypotheses for pooling and blind human adjudication, not gold labels. Unjudged results are unknown—not irrelevant. Call out small sample sizes and do not infer causality from aggregate scores.

When preparing adjudication, hide engine identity and result rank where practical, preserve assessor and rubric version, and publish accepted judgments as a new immutable `human_adjudicated` dataset version rather than rewriting the candidate dataset.
