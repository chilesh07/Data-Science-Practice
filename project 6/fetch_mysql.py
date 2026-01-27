import os
import pandas as pd
import pymysql
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def fetch_and_save():
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )

        print("Connected to MySQL")

        query = "SELECT * FROM `hr-employee-attrition`"
        df = pd.read_sql(query, conn)

        df.to_csv("mysql_data.csv", index=False)

        print("Data saved in mysql_data.csv")
        print("Rows, Columns:", df.shape)

        conn.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    fetch_and_save()
