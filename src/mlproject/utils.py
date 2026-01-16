import os
import sys
import pandas as pd
from dotenv import load_dotenv
import pymysql

from mlproject.exception import CustomException
from mlproject.logger import logger


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logger.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logger.info("MySQL connection established")

        df = pd.read_sql_query("SELECT * FROM Students", mydb)
        return df

    except Exception as ex:
        raise CustomException(ex, sys)

    finally:
        try:
            mydb.close()
            logger.info("MySQL connection closed")
        except:
            pass

