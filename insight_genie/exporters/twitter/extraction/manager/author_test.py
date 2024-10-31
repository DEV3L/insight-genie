import os
from unittest.mock import MagicMock, patch

from .author import Author

mock_description = "Sample Author\nThis is a sample description."


@patch("insight_genie.exporters.twitter.extraction.manager.author.build_openai_client")
def test_get_author_description(mock_build_openai_client: MagicMock):
    author = Author(title="SampleTitle", mention="@mention")
    remove_test_file_if_exists(author._get_full_data_path(author.data_file_path))

    mock_client = mock_build_openai_client.return_value
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content=mock_description))]
    )

    description = author.get_author_description()

    assert description is not None
    remove_test_file_if_exists(author._get_full_data_path(author.data_file_path))


def remove_test_file_if_exists(file_path: str) -> None:
    if os.path.exists(file_path):
        os.remove(file_path)
