# Agent integration

For Codex and other AI agents, place this instruction in the guidance your agent actually reads, such as your project's AGENTS.md:

> Before implementation, read HUMAN.md. Treat it as the human-owned source of project intent. Use it to guide decisions. If a proposed change conflicts with documented goals or assumptions, ask for human approval. Suggest updates when new findings challenge the original reasoning.

HUMAN.md alone does not enforce behavior or register an integration. Agents must be explicitly instructed to read it. The initializer never modifies AGENTS.md automatically.

Use documented goals to evaluate implementation choices. Challenge assumptions constructively and distinguish a routine implementation choice from changing who the project serves or why it exists. For a fundamental conflict, explain the conflict and ask the human to decide before implementing that change.

When evidence challenges an assumption, suggest a human-reviewed update explaining the evidence, proposed change, and consequences. This can be a revised note, a link to findings, or an optional Decision Log entry. Do not silently rewrite the original reasoning or present unapproved ideas as human decisions.

This repository's [AGENTS.md](../AGENTS.md) is a concise example; its [creator's note](../HUMAN.md#a-note-from-the-creator) describes the reasoning behind the idea.
