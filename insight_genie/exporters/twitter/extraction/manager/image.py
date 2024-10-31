import base64
import os

from ai_assistant_manager.clients.openai_api import build_openai_client
from loguru import logger

from .base_manager import MODEL, BaseManager

DATA_PATH = "images"
PROMPT_PATH = "insight_genie/exporters/twitter/extraction/prompts/ImageDescriptionPrompt.md"


class Image(BaseManager):
    def __init__(self, url: str, group_title: str):
        self.client = build_openai_client()
        self.url = url
        self.encoded_url = base64.urlsafe_b64encode(url.encode()).decode().replace("=", "")
        self.title = group_title
        self.encoded_filename = f"{self.title}-{self.encoded_url}.txt"
        self.data_file_path = os.path.join(DATA_PATH, self.encoded_filename)

    def get_image_description(self) -> str:
        if self._data_file_exists(self.data_file_path):
            return self._read_data_file(self.data_file_path)

        self._write_description()
        return self.get_image_description()

    def _write_description(self):
        logger.info(f"Writing image description for `{self.url}` to `{self.data_file_path}`")

        response = self.client.chat.completions.create(
            model=MODEL,
            messages=self._build_messages_payload(PROMPT_PATH, url=self.url),
        )
        text = response.choices[0].message.content

        lines = text.split("\n", 1)
        title = lines[0].strip().replace("`", "")
        content = lines[1].strip() if len(lines) > 1 else ""

        logger.info(f"Image title: `{title}`")
        logger.info(f"Image content: `{content}`")

        with open(self._get_full_data_path(self.data_file_path), "w") as file:
            file.write(self._build_image_markdown(title, content))

    def _build_image_markdown(self, title: str, content: str) -> str:
        return f"""#### {title}

{self.url}

##### Description

```markdown
{content}
```
"""
