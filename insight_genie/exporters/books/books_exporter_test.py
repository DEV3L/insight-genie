from unittest.mock import Mock, patch

import pytest
from ai_assistant_manager.env_variables import ENV_VARIABLES

from insight_genie.exporters.books.books_exporter import FILE_NAME, BooksExporter


@pytest.fixture(name="exporter")
def build_exporter():
    return BooksExporter()


@patch("insight_genie.exporters.books.books_exporter.create_dir")
@patch("insight_genie.exporters.books.books_exporter.does_data_exist")
def test_export_data_exists(mock_does_data_exist, mock_create_dir, exporter):
    mock_does_data_exist.return_value = True

    exporter.export()

    mock_create_dir.assert_not_called()


@patch("insight_genie.exporters.books.books_exporter.create_dir")
@patch("insight_genie.exporters.books.books_exporter.does_data_exist")
def test_export_data_does_not_exist(mock_does_data_exist, mock_create_dir, exporter):
    mock_does_data_exist.return_value = False

    exporter.write_data = Mock()

    exporter.export()

    mock_create_dir.assert_called_once()
    exporter.write_data.assert_called_once()


@patch("insight_genie.exporters.books.books_exporter.shutil")
def test_write_data(mock_shutil, exporter):
    exporter.get_file_path = Mock(return_value="path/to/file")

    exporter.write_data()

    mock_shutil.copy.assert_called_once_with(f"{ENV_VARIABLES.data_dir}/books/{FILE_NAME}", "path/to/file")


def test_get_dir_path(exporter):
    result = exporter.get_dir_path()

    assert result == "bin/books"


def test_get_file_path(exporter):
    result = exporter.get_file_path()

    assert result == f"bin/books/{ENV_VARIABLES.data_file_prefix}_{FILE_NAME}"
