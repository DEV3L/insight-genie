from ai_assistant_manager.chats.chat import ChatResponse
from ai_assistant_manager.exporters.files.files_exporter import FilesExporter

PROMPT_PATH = "prompts/prompt.md"

files = [
    ("about.txt", "files"),
    ("persona.txt", "files"),
    ("profile.txt", "files"),
]


def export_data():
    [FilesExporter(file, directory=directory).export() for (file, directory) in files]


def print_response(response: ChatResponse, name: str):
    print(f"\n{name}:\n{response.message}")
    print(f"\nTokens: {response.token_count}")
