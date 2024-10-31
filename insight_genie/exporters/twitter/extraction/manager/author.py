import base64
import os

from ai_assistant_manager.clients.openai_api import build_openai_client
from loguru import logger

from .base_manager import BaseManager
from .image import MODEL

DATA_PATH = "authors"
PROMPT_PATH = "insight_genie/exporters/twitter/extraction/prompts/AuthorDescriptionPrompt.md"


class Author(BaseManager):
    def __init__(self, title: str, mention: str):
        self.client = build_openai_client()
        self.title = title
        self.mention = mention
        self.encoded_mention = base64.urlsafe_b64encode(self.mention.encode()).decode().replace("=", "")
        self.encoded_filename = f"{self.title}-{self.encoded_mention}.txt"
        self.data_file_path = os.path.join(DATA_PATH, self.encoded_filename)

    def get_author_description(self) -> str:
        if self._data_file_exists(self.data_file_path):
            return self._read_data_file(self.data_file_path)

        self._write_description()
        return self.get_author_description()

    def _write_description(self):
        logger.info(f"Writing author description for `{self.title}` to `{self.data_file_path}`")

        response = self.client.chat.completions.create(
            model=MODEL,
            messages=self._build_messages_payload(PROMPT_PATH, replacement=("{{BOOK_TITLE}}", self.title)),
        )
        text = response.choices[0].message.content

        lines = text.split("\n", 1)
        author = lines[0].strip().replace("`", "")
        content = lines[1].strip() if len(lines) > 1 else ""

        logger.info(f"Author name: `{author}`")
        logger.info(f"Author content: `{content}`")

        with open(self._get_full_data_path(self.data_file_path), "w") as file:
            file.write(self._build_markdown(author, content))

    def _build_markdown(self, author: str, content: str) -> str:
        return f"""#### Author

Author: {author}

##### Description

```markdown
{content}
```
"""
