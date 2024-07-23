import os
import shutil

from ai_assistant_manager.env_variables import BIN_DIR, DATA_DIR, DATA_FILE_PREFIX
from ai_assistant_manager.exporters.exporter import (
    create_dir,
    does_data_exist,
)
from loguru import logger

FILE_NAME = "books.json"


class BooksExporter:
    def export(self):
        if does_data_exist(self.get_file_path()):
            logger.info("Book data exits. Skipping export.")
            return

        logger.info("Exporting Book data")
        create_dir(self.get_dir_path(), self.get_file_path())
        self.write_data()

    def write_data(self):
        source_path = f"{DATA_DIR}/books/{FILE_NAME}"
        shutil.copy(source_path, self.get_file_path())

        logger.info(f"Book data written to file: {self.get_file_path()}")

    def get_dir_path(self):
        return os.path.join(
            BIN_DIR,
            "books",
        )

    def get_file_path(self):
        return os.path.join(
            self.get_dir_path(),
            f"{DATA_FILE_PREFIX}_{FILE_NAME}",
        )
