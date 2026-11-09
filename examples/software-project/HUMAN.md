# HUMAN.md

Fictional software example. This describes intended behavior, not an existing product.

## Problem
Research experiments become difficult to compare when notes, parameters, and results are scattered across folders.

## Motivation
Researchers should be able to understand an earlier experiment without reconstructing its context from memory.

## Target Users
Individual researchers and small lab teams running local experiments.

## Proposed Approach
A lightweight local tool that groups experiment notes and links to existing artifacts. Keep records readable outside the tool.

## Constraints
Work offline, avoid uploading research data, and require little setup. Do not replace data storage or build a general project management platform.

## Success Criteria
In a proposed trial, a researcher should record an experiment in under two minutes and find its purpose, parameters, and artifact location a week later without help. Observe the trial before claiming success.

## Decision Log

### YYYY-MM-DD — Local records first

**Decision:** Begin with local files rather than a hosted service.

**Reason:** Researchers need access without sharing unpublished data or managing infrastructure.

**Impact:** Shared editing and hosted collaboration are outside the initial scope.
