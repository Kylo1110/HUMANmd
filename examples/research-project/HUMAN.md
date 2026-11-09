# HUMAN.md

Fictional research example. All experiments below are proposed, not completed.

## Description
Compare small specialized language models with larger general-purpose models on extracting fields from research abstracts.

## Research Question
Can a smaller specialized model meet the same extraction quality threshold at lower inference cost?

## Hypothesis
A specialized model will achieve field-level F1 within two percentage points of the larger baseline while reducing measured inference cost by at least half. Falling outside either threshold would refute this hypothesis for the chosen dataset.

## Data
Propose a licensed, manually annotated set of public abstracts, split by publication source into training, validation, and held-out test sets. Check permissions and label consistency before use.

## Implementation
Compare a specialized model with a larger general-purpose baseline using a fixed extraction schema and equivalent input information.

## Analysis
Predefine field-level F1, invalid-output rate, latency, and measured cost. Report uncertainty and error categories. Keep the test set untouched until the final evaluation.

## Expected Results
We expect specialization may lower cost; quality parity remains uncertain. Negative results would help identify tasks that still need broader models.

## Decision Log

### YYYY-MM-DD — Limit the first comparison

**Decision:** Start with one extraction task rather than general reasoning benchmarks.

**Reason:** A narrow task makes evaluation feasible and the cost-quality tradeoff easier to interpret.

**Impact:** Findings will apply to this task and dataset, not to all language-model use.
