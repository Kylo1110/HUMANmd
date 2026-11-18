# CLI guide

## Install from source

Requires Python 3.10 or newer and [uv](https://docs.astral.sh/uv/getting-started/installation/). From the repository root:

```bash
uv tool install .
```

uv installs the CLI in an isolated tool environment. If `humanmd` is not on your PATH, run `uv tool update-shell` and restart your shell. No virtual-environment activation is needed for the installed command.

**Post-release installation:** `uv tool install humanmd` applies only after the package name is confirmed and the distribution is published. No PyPI publication is claimed.

## Commands

```bash
humanmd init
humanmd init --template minimal
humanmd init --template research
humanmd init -t software
humanmd init --template exploration --path ./existing-project
humanmd templates
humanmd --version
humanmd --help
humanmd init --help
```

`init` defaults to the minimal template in the current directory. `--path` accepts an existing directory as a relative or absolute path; `~` is expanded. It creates only `HUMAN.md`, in UTF-8. Running `humanmd` without a subcommand displays help. Module execution is also supported: in the development environment, run `uv run --locked python -m humanmd init --path ./existing-project`. Both entry points use the same implementation.

The four templates are minimal, research, software, and exploration. Each includes an optional Creator's note prompt for personal motivation; there is no separate creator template. `templates` prints their descriptions. The installed package metadata supplies the version.

## Initialization output

After creating the file, the CLI displays a HUMAN.md header, the selected template, the resolved file location, and a friendly invitation to gather your thoughts: capture the initial idea, note why it matters and what you hope to learn, and share the context with your team and AI collaborators. It closes with a reminder to start small and revisit your thinking as you learn.

Interactive terminals get a compact colored header and success indicator. Output wraps to the terminal width, with a simpler header on narrow screens. Redirecting output or setting `TERM=dumb` disables colors and decorative Unicode; terminals with limited character encodings use ASCII instead. Set `NO_COLOR=1` to disable colors while retaining the layout. No animation, prompt, or extra runtime dependency is required.

## Errors and safety

If `HUMAN.md` already exists, initialization exits nonzero and reports:

```text
HUMAN.md already exists.
Nothing was changed.
```

This protection includes symlinks and directories with that name. Exclusive creation prevents a competing initializer from overwriting a file. There is no `--force` option.

Missing targets, targets that are files, invalid templates, permissions, and other filesystem failures produce concise errors and a nonzero exit status. Invalid templates list valid options. Missing directories are never created. The CLI does not execute project code, change agent instructions, generate intent, or contact external services. After installation it works offline.

## Develop and verify

```bash
uv sync --locked
uv run --locked pytest
uv build
uv run --locked twine check dist/*
```

uv creates `.venv`, installs the project in editable mode, and includes the development tools from `[dependency-groups].dev`. The committed `uv.lock` records resolved versions. `--locked` rejects a stale lockfile instead of silently changing it. Use `uv add --dev PACKAGE` to add a development tool, and `uv lock --upgrade` for an intentional dependency refresh; commit the reviewed lockfile changes.

Tests use temporary directories. Distribution integration tests use standard Python build tooling and uv to install the wheel into a pip-free virtual environment, then invoke the installed CLI and module directly without uv.

After `uv sync --locked` has provisioned the development tools, checks and builds can run offline:

```bash
uv run --offline --locked pytest
uv run --offline --locked python -m build --no-isolation
```

These commands require the environment and cached dependencies to be available already. Initial installation and dependency downloads can require network access; the installed HUMAN.md initializer itself remains fully offline.

## Manual release preparation

Use the [release guide](releasing.md) for the final-commit checks, description preview, artifact hashes, TestPyPI review, and publication sequence. [Draft v0.1.0 release notes](release-notes-0.1.0.md) are prepared for review; they do not announce availability.

1. Review HUMAN.md and the documentation; confirm version, license, and repository metadata.
2. Confirm the `humanmd` distribution name is available or that you control it on PyPI. If unavailable, choose and approve a distribution name before publishing and update metadata and installation instructions consistently.
3. Run tests, build both distributions, inspect their templates, and run `uv run --locked twine check dist/*`.
4. Outside this repository, use `uv tool install /absolute/path/to/humanmd-0.1.0-py3-none-any.whl` to install the built wheel in an isolated environment and run `humanmd --version`, `humanmd templates`, `humanmd init`, and verify module execution through the distribution integration tests. Initialization should also succeed without network access.
5. Configure authorized PyPI credentials or an approved publishing workflow. Obtain explicit publication approval.
6. Only after approval, manually upload the reviewed artifacts using `uv run --locked twine upload dist/*`. Create a GitHub release only if separately authorized.

Package-name availability, PyPI ownership, credentials, and publication approval remain prerequisites. Preparing or pushing this repository does not publish the package.
