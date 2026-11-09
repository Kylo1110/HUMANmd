# Contributing

Read [HUMAN.md](HUMAN.md) and [AGENTS.md](AGENTS.md) before changing the project. Keep adoption simple and human intent human-owned.

Use an issue for a feature proposal, documentation improvement, or real-world example. Explain the problem and why it matters. Discuss fundamental changes in direction with the maintainer before implementing them. Clearly label fictional examples and proposed experiments; do not invent results or adoption claims.

For development, use Python 3.10+ and [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
uv sync --locked
uv run --locked pytest
uv build
uv run --locked twine check dist/*
```

The test-only GitHub Actions workflow covers Linux, Windows, and macOS on Python 3.10 and 3.14. It does not publish packages or change repository settings. See the [release guide](docs/releasing.md) for preparing artifacts and reviewing platform results.

uv creates `.venv` and installs the project in editable mode with its development dependency group. Commit `uv.lock` when dependencies change; use `uv add --dev PACKAGE` for development tools and `uv lock --upgrade` for intentional dependency updates. Review the resulting lockfile diff.

Add meaningful tests for CLI behavior changes and verify bundled templates when changing packaging. Keep the four canonical templates in `src/humanmd/templates/`; do not duplicate them. Check documentation links and suggest updates when meaningful findings change the reasoning; a formal Decision Log is optional.

Submit a focused pull request explaining the problem, resulting behavior, and checks performed. Avoid new runtime dependencies, automation, or unrelated features without a demonstrated need. Contributions are provided under the repository's [MIT license](LICENSE).
