from ai_assistant_manager.chats.chat import ChatResponse
from ai_assistant_manager.exporters.files.files_exporter import FilesExporter

PROMPT_PATH = "prompts/prompt.md"

files = [
    ("insight-genie-product-definition.txt", "files"),
    ("linkedin-profile.txt", "files"),
    ("persona.txt", "files"),
    ("README.txt", "files"),
    ("books.json", "files/books"),
]


code = [
    ("ai-assistant-manager.txt", "files/code"),
    ("ai-code-summary.txt", "files/code"),
    ("insight-genie.txt", "files/code"),
]

summaries = [
    ("Event Summary - The Agile Samurai - How Agile Masters Deliver Great Software.txt", "twitter/event_summaries"),
]


def export_data():
    [FilesExporter(file, directory=directory).export() for (file, directory) in files]
    [FilesExporter(file, directory=directory).export() for (file, directory) in code]
    [FilesExporter(file, directory=directory).export() for (file, directory) in summaries]


def print_response(response: ChatResponse, name: str):
    print(f"\n{name}:\n{response.message}")
    print(f"\nTokens: {response.token_count}")
