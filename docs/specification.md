# HUMAN.md convention v0.1

HUMAN.md is a voluntary commitment to keeping human-owned project reasoning visible and traceable as a project develops. It has no fixed structure. It is useful with or without the CLI.

## Naming and location

Use the name `HUMAN.md`, normally in the repository root where people and agents can find it. Use ordinary Markdown. No frontmatter, configuration metadata, parser, or mandatory validation is required.

## Ownership

Humans own the project's purpose and evolving reasoning. Agents may ask questions, identify contradictions, or clarify wording, but must not invent intent or silently replace it. Incomplete answers and uncertainty are legitimate.

## Content

Explain why the project exists, what it hopes to achieve, and how success could be assessed. State relevant assumptions and constraints. The [four templates](../README.md#choose-a-starting-point) are recommendations, not mandatory schemas. Adapt or omit sections as needed. A short note can be the whole document. Link to existing research, proposals, or decisions rather than copying them. Revisit the reasoning when learning changes the approach during experiments, implementation, or maintenance.

An exploratory project can start with a question and a learning goal. Recording the reason for an experiment is enough to choose a deliberate next step; a complete implementation plan is not required. People remain responsible for directing agents, reviewing generated code before using it, and deciding how the resulting software is used.

## Creator's note (optional)

Any HUMAN.md can include a Creator's note: a short account, in the creator's own voice, of why they started the project, why it matters to them, and what they hope to learn or change. A team can write it together or identify individual contributors' perspectives.

This section works with any project type. All four bundled templates include an optional prompt; keep it, leave it blank, or remove it. There is no separate creator template and no required wording or length. It can stand alone or give context to other material in the document.

A creator's note can explain motivation and how the idea develops; an optional Decision Log can record specific changes in reasoning. Agents may help clarify a note supplied by a human, but must not invent personal experiences, beliefs, or motivations. The CLI only copies the prompt.

## Decision Log

A Decision Log is one optional way to explain meaningful changes in goals, assumptions, and approach. Revisions to prose or links to existing notes can serve the same purpose. If you use a log, a date, decision, reason, and impact can make entries easier to follow. Record evidence honestly and distinguish proposed experiments from findings. Git preserves document revisions; the written explanations make the evolution of thinking understandable. There is no need to record every task or code change.

## Agent awareness

Explicitly instruct agents to read HUMAN.md before implementation, use it to guide choices, and request approval before changes that conflict with documented direction. Suggest document updates as evidence changes. A file on its own cannot enforce compliance; see [agent integration](agent-integration.md).
