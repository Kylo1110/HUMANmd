"""Keep GitHub image paths relative and package description URLs absolute."""

from pathlib import Path

from hatchling.metadata.plugin.interface import MetadataHookInterface


class CustomMetadataHook(MetadataHookInterface):
    def update(self, metadata):
        readme = Path(self.root, "README.md").read_text(encoding="utf-8")
        metadata["readme"] = {
            "content-type": "text/markdown",
            "text": readme.replace(
                'src="docs/assets/',
                'src="https://raw.githubusercontent.com/Kylo1110/HUMANmd/main/docs/assets/',
            ),
        }
