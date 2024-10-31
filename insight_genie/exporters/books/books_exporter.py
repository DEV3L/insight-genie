import os
import shutil

from ai_assistant_manager.env_variables import ENV_VARIABLES
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
        source_path = f"{ENV_VARIABLES.data_dir}/books/{FILE_NAME}"
        shutil.copy(source_path, self.get_file_path())

        logger.info(f"Book data written to file: {self.get_file_path()}")

    def get_dir_path(self):
        return os.path.join(
            ENV_VARIABLES.bin_dir,
            "books",
        )

    def get_file_path(self):
        return os.path.join(
            self.get_dir_path(),
            f"{ENV_VARIABLES.data_file_prefix}_{FILE_NAME}",
        )
