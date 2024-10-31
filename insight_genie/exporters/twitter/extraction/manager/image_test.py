import os
from unittest.mock import MagicMock, patch

from .image import Image

mock_description = "Sample image\nThis is a sample description."


@patch("insight_genie.exporters.twitter.extraction.manager.image.build_openai_client")
def test_get_image_description(mock_build_openai_client: MagicMock):
    image = Image("some_url", "some_title")
    remove_test_file_if_exists(image._get_full_data_path(image.data_file_path))

    mock_client = mock_build_openai_client.return_value
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content=mock_description))]
    )

    description = image.get_image_description()

    assert description is not None
    remove_test_file_if_exists(image._get_full_data_path(image.data_file_path))


def remove_test_file_if_exists(file_path: str) -> None:
    if os.path.exists(file_path):
        os.remove(file_path)
