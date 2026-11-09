# Preparing and publishing v0.1.0

Release preparation and publication are separate steps. This guide prepares a reviewable release; uploading to TestPyPI or PyPI, creating tags or GitHub releases, changing repository visibility, and configuring credentials require separate authorization.

## Confirm the prerequisites

- Confirm that `https://github.com/Kylo1110/HUMANmd` is accessible without authentication. An unauthenticated 404 does not establish whether a repository is private, missing, or unavailable through the current connection.
- Confirm that you control the `humanmd` PyPI name or can publish under it. A missing public listing does not guarantee availability; see [PyPI's naming rules](https://docs.pypi.org/project-management/choosing-a-name/).
- Confirm an authorized publishing account and authentication method. A manual scoped API token or a separately approved Trusted Publishing setup can be used. Keep tokens out of files and shell history; do not commit credentials. TestPyPI and PyPI have separate accounts and tokens.
- Review the MIT license, metadata, documentation, and [draft release notes](release-notes-0.1.0.md). Do not claim adoption or experimental results that have not been observed.

## Verify the final commit

```bash
uv sync --locked
uv run --locked pytest -ra
uv build --no-sources
uv run --locked twine check dist/*
```

Before the final build, remove obsolete release files from `dist/` or move them aside. Build from the reviewed commit with a clean working tree. Inspect both archives for the four canonical templates and confirm the source archive contains the latest README, documentation, workflow, and artwork. Record the commit and SHA-256 hashes of the exact artifacts selected for upload.

Check the test-only GitHub Actions matrix for Linux, Windows, and macOS on Python 3.10 and 3.14. It runs on pushes to `main`, pull requests, and manual dispatch with read-only repository permissions. Review skipped tests as well as failures. An unavailable Windows symlink privilege may be reported as a skip; existing-file and directory protection must still pass.

Install the built wheel into an isolated environment outside the repository. Exercise all templates, custom paths, help, version, module execution, offline initialization, and existing-file protection. The distribution tests perform these checks using temporary directories.

## Inspect the description and links

The repository uses relative illustration paths so GitHub can display them in private repositories. During packaging, the metadata hook converts those paths to absolute raw-content URLs in the package description. This keeps one source README; PyPI illustrations still depend on public access to the repository. File links use absolute GitHub URLs. The preview tool below is a development dependency, not part of the installed CLI:

```bash
uv run --locked python -m readme_renderer README.md --output /path/to/preview.html
```

For the final review, also extract the README body from the wheel's `METADATA`, render it with `readme_renderer.markdown.render`, and inspect that HTML. Check links and images separately: a successful metadata check does not establish that external resources can be reached. Verify the packaged README matches the reviewed source except for the illustration URL conversion. PyPI may sanitize HTML differently from GitHub, so the later TestPyPI preview matters.

## After separate publication approval

The commands below upload publicly. Run them only after approval and prerequisite checks. Use the exact reviewed filenames rather than a wildcard that could include unrelated files. With token authentication, enter the appropriate service's API token at the password prompt; do not paste it into a command or commit it. For a first upload, a project-scoped token is only possible after the project exists; use an authorized account token for creation, then replace it with a project-scoped token. See [PyPI API tokens](https://docs.pypi.org/publishing/publishing-to-pypi/#using-an-api-token).

TestPyPI upload:

```bash
uv run --locked twine upload --repository-url https://test.pypi.org/legacy/ --username __token__ dist/humanmd-0.1.0-py3-none-any.whl dist/humanmd-0.1.0.tar.gz
```

After reviewing TestPyPI, production upload with its separate token:

```bash
uv run --locked twine upload --repository-url https://upload.pypi.org/legacy/ --username __token__ dist/humanmd-0.1.0-py3-none-any.whl dist/humanmd-0.1.0.tar.gz
```

For an isolated preview installation, set `UV_TOOL_DIR` and `UV_TOOL_BIN_DIR` to new temporary directories using your shell's environment-variable syntax. Install with `uv tool install --index-url https://test.pypi.org/simple/ humanmd==0.1.0`, then invoke `humanmd` from that temporary bin directory. Use different empty directories for the production check, installing `humanmd==0.1.0` with `--index-url https://pypi.org/simple/`. Initialization must run in an existing empty directory. These checks must use the index artifacts, not the local wheel or a cached tool installation.

1. Upload only the reviewed wheel and source archive to TestPyPI with its own credentials. Preview the project page, check images and links, and install the package into a temporary uv tool environment using TestPyPI as the index. Avoid reusing an existing tool installation during this check.
2. If the TestPyPI preview and installation succeed, upload those same reviewed artifacts to PyPI with the production account. Keep the artifact hashes available for comparison. PyPI filenames cannot be reused after upload; correct problems with a new version rather than trying to replace a release.
3. Verify `uv tool install humanmd` in a fresh tool environment using the default PyPI index, then test `humanmd --version`, `humanmd templates`, and initialization in an empty existing directory.
4. Update the README and CLI guide to reflect actual publication and the final distribution name. Add a PyPI badge only once the public project exists.
5. Create the `v0.1.0` tag at the reviewed release commit and a GitHub release using the reviewed notes. Include the artifact hashes and actual checks performed. Update documentation in a subsequent commit if necessary.

Do not announce installation availability until the production-index check succeeds. Record outstanding authentication, name, visibility, and platform checks explicitly rather than treating them as passed.
