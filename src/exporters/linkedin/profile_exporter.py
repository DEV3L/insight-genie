import os
import shutil

from loguru import logger

from src.exporters.exporter import (
    BIN_DIR,
    DATA_DIR,
    DATA_FILE_PREFIX,
    create_dir,
    does_data_exist,
)

FILE_NAME = "profile.txt"


class ProfileExporter:
    def export(self):
        if does_data_exist(self.get_file_path()):
            logger.info("Profile data exits. Skipping export.")
            return

        logger.info("Exporting Profile data")
        create_dir(self.get_dir_path(), self.get_file_path())
        self.write_data()

    def write_data(self):
        source_path = f"{DATA_DIR}/linkedin/{FILE_NAME}"
        shutil.copy(source_path, self.get_file_path())

        logger.info(f"Profile data written to file: {self.get_file_path()}")

    def get_dir_path(self):
        return os.path.join(
            BIN_DIR,
            "linkedin",
        )

    def get_file_path(self):
        return os.path.join(
            self.get_dir_path(),
            f"{DATA_FILE_PREFIX}_profile.txt",
        )
