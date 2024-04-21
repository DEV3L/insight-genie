from loguru import logger

from src.assistants.insight_genie_assistant_service import (
    ASSISTANT_NAME,
    InsightGenieAssistantService,
)
from src.chats.chat import Chat
from src.clients.openai_api import OpenAIClient, build_openai_client
from src.exporters.about.insight_genie_exporter import InsightGenieExporter
from src.exporters.about.persona_exporter import PersonaExporter
from src.exporters.books.books_exporter import BooksExporter
from src.exporters.linkedin.profile_exporter import ProfileExporter

SHOULD_DELETE_ASSISTANT = False


START_MESSAGE = """Hello."""


def export_data():
    BooksExporter().export()
    InsightGenieExporter().export()
    PersonaExporter().export()
    ProfileExporter().export()


def main():
    logger.info(f"Starting {ASSISTANT_NAME}")

    export_data()

    client = OpenAIClient(build_openai_client())
    service = InsightGenieAssistantService(client)

    if SHOULD_DELETE_ASSISTANT:
        logger.info("Removing existing assistant and category files")
        service.delete_assistant()

    assistant_id = service.get_assistant_id()

    logger.info(f"Assistant ID: {assistant_id}")

    chat = Chat(
        client,
        assistant_id,
        start_message=START_MESSAGE,
        # thread_id="abc",
    )

    start_response = chat.start()

    print(f"\n{service.assistant_name}:\n{start_response}")

    while True:
        user_message = input("\nMessage: ")

        if user_message == "exit":
            break

        chat_response = chat.send_user_message(user_message)
        print(f"\n{service.assistant_name}:\n{chat_response}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.info(f"Error: {e}")
