# Agent guidance

- Read HUMAN.md before implementation and preserve its documented philosophy.
- Keep the CLI dependency-light and avoid unnecessary features.
- Ask before changing fundamental project direction.
- Suggest human-reviewed updates when findings change the reasoning; no formal Decision Log is required.
- Never silently rewrite human-owned intent.
- Use uv for package management: `uv sync --locked`, `uv run --locked pytest`, and `uv build`. Commit intentional dependency changes in `uv.lock`.
- Run pytest and verify built distributions when changing CLI or packaging behavior.
- Character illustrations must include both a woman and a man depicted as active coders or researchers alongside the AI robot. Give both people equal agency and prominence. Keep the modern pixel-art style and show human thinking before coding in process illustrations. Text-only wordmarks can use a simple pixel grid without characters.
- Keep artwork minimal and positive: simple pixel shapes, restrained colors, generous whitespace, few props, and readable text. Prefer one clear symbol per process step to repeated detailed character scenes.
