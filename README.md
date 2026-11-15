<p align="center">
  <img src="docs/assets/humanmd-banner.png" width="100%" alt="HUMAN.md — Code is getting cheaper. Thinking isn't. A pixel-art woman and man, depicted as developers or researchers, collaborate with a friendly robot over a shared intent document.">
</p>

<p align="center">
  <a href="https://github.com/Kylo1110/HUMANmd/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-teal.svg?style=flat-square" alt="License: MIT"></a>
  <a href="https://github.com/Kylo1110/HUMANmd/blob/main/pyproject.toml"><img src="https://img.shields.io/badge/python-3.10%2B-blue.svg?style=flat-square" alt="Python: 3.10+"></a>
  <a href="https://github.com/Kylo1110/HUMANmd/blob/main/pyproject.toml"><img src="https://img.shields.io/badge/version-0.1.0-orange.svg?style=flat-square" alt="Version: 0.1.0"></a>
  <a href="https://github.com/Kylo1110/HUMANmd/blob/main/docs/cli.md#errors-and-safety"><img src="https://img.shields.io/badge/works-offline-teal.svg?style=flat-square" alt="Works offline"></a>
</p>

<p align="center">
  <a href="https://github.com/Kylo1110/HUMANmd#get-started">Get started</a> ·
  <a href="https://github.com/Kylo1110/HUMANmd/blob/main/docs/specification.md">Specification</a> ·
  <a href="https://github.com/Kylo1110/HUMANmd/blob/main/docs/agent-integration.md">Agent guidance</a> ·
  <a href="https://github.com/Kylo1110/HUMANmd#contributing">Contribute</a>
</p>

## Code explains how. HUMAN.md explains why.

Research and software projects begin with ideas, questions, and assumptions. Those change as we experiment, build, and learn. HUMAN.md is a commitment to keeping that thinking visible and traceable as a project develops, using a human-owned Markdown file to explain why the work matters and how its direction evolves.

**Keep the reasoning behind your project visible as it develops.**

## A note from the creators

In a world that keeps moving faster, HUMAN.md is an invitation to slow down for a moment. Take a pen or an iPad, make a cup of coffee or tea, and think about what you want your project to achieve. We hope it can become a small fireplace for you and your team—a place to gather your thoughts, question assumptions, and return as the project develops.

**There is no perfect structure to fill in. Give the thinking a place to happen.**

Agents can help us explore and challenge ideas, while we remain responsible for directing their work, reviewing the results, and how we use the code. We don't claim HUMAN.md is an established standard, a proven solution, or the right workflow for every project. We want to learn whether a small Markdown file can help, and we invite you to help shape it. Our [creator's note](https://github.com/Kylo1110/HUMANmd/blob/main/HUMAN.md#a-note-from-the-creator) shares the personal thinking behind the idea.

## Before the first line of code

**Start with a reason for the next step.**

<p align="center">
  <img src="docs/assets/think-before-code.png" width="100%" alt="A blonde woman researcher and a man researcher, wearing lab coats and holding research notes, work with an AI robot through six steps: find the purpose, question assumptions, define success, write HUMAN.md, make a human decision, then build. A return loop from the decision to the questions shows reflection and refinement before proceeding.">
</p>

<p align="center"><strong>Purpose → Questions → Success → HUMAN.md → Human decision → Code</strong></p>

**Your first step may be an experiment. Write down what you want to learn before asking an agent to build it.**

The diagram is a guide to choosing a deliberate next step, including an experiment. Its loop makes room to revisit questions, assumptions, and intended outcomes before proceeding. Start with the question, the assumptions you want to test, and what you will look for in the results. You can begin with open questions and revise the approach as you learn; an exhaustive plan is not required. This reflection continues during experiments, implementation, and maintenance: when you learn something that changes the approach, explain what changed and why.

HUMAN.md follows three simple principles:

1. Human First. People own the project's purpose and direction. AI can help clarify ideas while keeping that intent explicit.
2. Agent Aware. Give agents the goals and context they need to challenge assumptions constructively and ask before fundamentally changing direction.
3. Living Document. When your understanding changes, update HUMAN.md. Record meaningful decisions, not every code change.

**AI can propose. Humans decide.**

## One file. A different purpose.

Your README may already explain why the project exists. HUMAN.md gives that reasoning a dedicated home when it helps to keep ideas, assumptions, and decisions together. Link to existing explanations and research notes rather than maintaining duplicate versions. The roles below can overlap; they are useful distinctions, not strict boundaries.

| File | Purpose |
| --- | --- |
| `README.md` | What the project does and how to use it. |
| `AGENTS.md` | How AI agents should work in the project. |
| `CHANGELOG.md` | What changed in the software. |
| `HUMAN.md` | Why the project exists, what it aims to achieve, and how its reasoning evolves. |

## Get started

Start with a Markdown file in whatever form helps you explain your thinking. The headings below are one option; a short note can work too. The CLI is an optional convenience for copying a template.

### Option 1 — Start with Markdown

Create a `HUMAN.md` in your project root:

```markdown
# HUMAN.md

## Why?
Why does this project exist?

## What?
What are we trying to achieve?

## How will we know?
What would success look like?
```

That's enough to begin. Add more detail as your thinking develops. There are no mandatory sections or rigid schemas. You can include an optional Creator's note to explain, in your own words, what brought you to the project and why it matters to you. See the [voluntary specification](https://github.com/Kylo1110/HUMANmd/blob/main/docs/specification.md).

<details>
<summary>A small example: organizing research experiments</summary>

This fictional example shows the kind of reasoning you might write. Its success criteria are proposed, not measured results.

```markdown
# HUMAN.md

## Why?
Our experiment notes are scattered across folders. We want to understand
earlier experiments without reconstructing their context from memory.

## What?
A lightweight local tool for researchers to group notes and link artifacts,
without uploading unpublished data.

## How will we know?
In a trial, a researcher should be able to record an experiment in under
two minutes and find its purpose, parameters, and artifacts a week later.
```

See the [full software example](https://github.com/Kylo1110/HUMANmd/blob/main/examples/software-project/HUMAN.md) for constraints and an initial decision.

</details>

### Option 2 — Use the CLI

HUMAN.md also includes a small Python CLI that creates a template for you. Install directly from this repository using [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python 3.10+):

```bash
git clone https://github.com/Kylo1110/HUMANmd.git
uv tool install ./HUMANmd
```

Then, inside your project:

```bash
humanmd init
```

Initialization shows the template, file location, and three next steps. Interactive terminals get a colored header; redirected output stays plain. For example:

```text
  HUMAN.md
  Code is getting cheaper. Thinking isn't.

  + Created HUMAN.md (minimal)
  Location: /path/to/your-project/HUMAN.md

  BEFORE YOU BUILD
  01  Open HUMAN.md and write why this project exists.
  02  Define success, or what you want to learn.
  03  Ask your agent to read it before implementation.

  AI can propose. Humans decide.
```

Or choose a template:

```bash
humanmd init --template research
humanmd init --template software
humanmd init --template exploration
```

Other commands:

```bash
humanmd templates
humanmd init -t software --path ./existing-project
humanmd --help
```

Once published to PyPI, the intended installation command will be:

```bash
uv tool install humanmd
```

*PyPI publication and package-name availability are not yet confirmed.* The CLI works offline, requires no API key or runtime dependencies, and never overwrites an existing `HUMAN.md`. Target directories must already exist.

**The CLI offers a starting point. You provide the thinking.**

## Choose a starting point

Different projects begin with different questions.

| Template | Best for |
| --- | --- |
| [Minimal](https://github.com/Kylo1110/HUMANmd/blob/main/src/humanmd/templates/minimal.md) | Purpose, goals, and success criteria. |
| [Research](https://github.com/Kylo1110/HUMANmd/blob/main/src/humanmd/templates/research.md) | Research questions, hypotheses, data, and evaluation. |
| [Software](https://github.com/Kylo1110/HUMANmd/blob/main/src/humanmd/templates/software.md) | Problems, users, constraints, and desired outcomes. |
| [Exploration](https://github.com/Kylo1110/HUMANmd/blob/main/src/humanmd/templates/exploration.md) | Early ideas, assumptions, and experiments. |

These are starting points, not rules. Adapt them to your project. All four templates include an optional Creator's note. It works with any project type: keep it, leave it blank, or remove it. See the [Creator's note guidance](https://github.com/Kylo1110/HUMANmd/blob/main/docs/specification.md#creators-note-optional). See the fictional [research](https://github.com/Kylo1110/HUMANmd/blob/main/examples/research-project/HUMAN.md) and [software](https://github.com/Kylo1110/HUMANmd/blob/main/examples/software-project/HUMAN.md) examples.

## Give your AI agents context

Give agents the purpose as well as the task. Add this instruction to your `AGENTS.md` or equivalent agent configuration:

> Before implementation, read HUMAN.md. Treat it as the human-owned source of project intent. Use it to guide decisions. If a proposed change conflicts with documented goals or assumptions, ask for human approval. Suggest updates when new findings challenge the original reasoning.

HUMAN.md doesn't automatically enforce agent behavior, and the CLI doesn't modify agent instructions. See the [agent integration guide](https://github.com/Kylo1110/HUMANmd/blob/main/docs/agent-integration.md).

## When your thinking changes, write it down

When evidence challenges an assumption or a better approach emerges, explain what changed and why. You can revise a note, link to an experiment or discussion, or use an optional Decision Log like this:

```markdown
### 2026-11-08 — Markdown first

**Decision:** Keep the convention in ordinary Markdown
and the CLI dependency-free.

**Reason:** Intent should remain accessible without
a service or special tooling.

**Impact:** Anyone can adopt HUMAN.md with a single
file, even without installing the CLI.
```

Git preserves revisions; your explanations make the changes in reasoning understandable. Focus on what changes your understanding or direction, without documenting every task, refactor, or bug fix. Our [creator's note](https://github.com/Kylo1110/HUMANmd/blob/main/HUMAN.md#a-note-from-the-creator) describes how this idea developed.

**Keep a record of what you learned and why your direction changed.**

## Keep it simple

A few honest sentences can be enough. Templates, headings, and Decision Logs are optional tools. Adapt the structure as your project develops, leave questions open, and add detail when it helps. HUMAN.md complements Git history and your existing documentation; it provides context rather than enforcing a workflow or guaranteeing agent behavior. The CLI only copies templates and does not generate project intent.

A [recent study of repository-level context files](https://arxiv.org/html/2602.11988v3) found that they did not generally improve coding agents' task success. For us, that's a reminder to focus HUMAN.md on making human intent explicit, rather than adding documentation for its own sake.

## Contributing

HUMAN.md is an early open-source convention, and the goal is to keep it simple and useful. Contributions are welcome: improve a template, clarify the documentation, suggest better agent guidance, or share how you're using HUMAN.md. See [CONTRIBUTING.md](https://github.com/Kylo1110/HUMANmd/blob/main/CONTRIBUTING.md) and the [project philosophy](https://github.com/Kylo1110/HUMANmd/blob/main/docs/philosophy.md).

For CLI details and release preparation, see the [CLI guide](https://github.com/Kylo1110/HUMANmd/blob/main/docs/cli.md). Licensed under [MIT](https://github.com/Kylo1110/HUMANmd/blob/main/LICENSE).

## Thank you

Thank you to [@butterpear](https://github.com/butterpear), [@justinw98](https://github.com/justinw98), and [@sinwarmer](https://github.com/sinwarmer) for brainstorming and discussing this idea. Your questions and perspectives helped shape HUMAN.md.

<p align="center">
  <img src="docs/assets/humanmd-footer.png" width="640" alt="A woman researcher, man developer, and friendly robot assemble HUMAN.md from dark blocks on a complete grid, with pale outlines marking the unfilled cells.">
</p>

---

<p align="center">
  <em>What we build may change.</em><br>
  <em>The whys behind it remain.</em>
</p>

<p align="center">
  <em>To the humans behind the whys.</em>
</p>
