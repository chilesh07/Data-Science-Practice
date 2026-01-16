import sys
import os

sys.path.append(os.path.abspath("src"))

from mlproject.logger import logger
from mlproject.exception import CustomException
from mlproject.componets.data_ingestion import DataIngestion


if __name__ == "__main__":
    logger.info("The execution has started")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logger.exception("Custom Exception occurred")
        raise CustomException(e, sys)
