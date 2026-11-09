# HUMAN.md v0.1.0 — prepared release notes

Status: draft for review. This document does not announce a published package or GitHub release.

HUMAN.md is a voluntary commitment to keeping a research or software project's reasoning visible and traceable as it develops. Its structure can follow the project: notes, questions, reflections, and links to existing work can all help explain changes in direction. It welcomes unanswered questions and deliberate experiments.

## Included in this release

- An open Markdown convention, agent guidance, and fictional research and software examples.
- Four bundled templates: minimal, research, software, and exploration. Each includes a Creator's note prompt and a Decision Log; both are optional starting points, with no required schema.
- A Python 3.10+ initializer with no runtime dependencies: `humanmd init`, template selection, custom existing directories, template listing, version, and help.
- Exclusive UTF-8 file creation that protects existing HUMAN.md files, including symlinks. No overwrite option or automatic edits to agent instructions.
- An existing-entry check for Windows directory and dangling-symlink behavior before exclusive creation.
- Offline initialization with a compact terminal presentation, plain redirected output, ASCII fallbacks, and `NO_COLOR` support.
- uv-based development with a committed lockfile and a test-only CI matrix for Linux, Windows, and macOS on Python 3.10 and 3.14. CI configuration alone is not evidence that all platforms have passed.

## Before announcing availability

Confirm the public repository and package name, complete the checks in [the release guide](releasing.md), and verify installation from the published distribution. Once publication succeeds, replace the draft status with the actual release date and results, and update the README's post-release installation notice.

The convention and CLI remain small: the tool copies prompts; people supply the reasoning. Licensed under MIT.
