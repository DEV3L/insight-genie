import os

from ai_assistant_manager.prompts.prompt import get_prompt

BASE_DATA_PATH = "data/twitter/events"
MODEL = "chatgpt-4o-latest"


class BaseManager:
    def _get_full_data_path(self, file_path: str) -> str:
        return f"{BASE_DATA_PATH}/{file_path}"

    def _data_file_exists(self, file_path: str) -> str:
        return os.path.exists(self._get_full_data_path(file_path))

    def _read_data_file(self, file_path: str) -> str:
        with open(self._get_full_data_path(file_path), "r") as file:
            return file.read()

    def _build_messages_payload(
        self, prompt_path: str, *, replacement: tuple[str, str] = None, url: str = None
    ) -> list[dict]:
        prompt = get_prompt(prompt_path=prompt_path)
        text = prompt.replace(replacement[0], replacement[1]) if replacement else prompt

        content = [
            {"type": "text", "text": text},
        ]
        if url:
            content.append({"type": "image_url", "image_url": {"url": url}})

        return [
            {
                "role": "user",
                "content": content,
            }
        ]
