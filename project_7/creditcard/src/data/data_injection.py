import os
import pandas as pd
import pymysql
from dotenv import load_dotenv


load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db =os.getenv('db')

def data_save():
    try:
        conn = pymysql.connect(
            host = host,
            user = user,
            password=password,
            db = db
        )
        print('My Sql has been connected')
        
        query = "select * from creditcard"
        
        df = pd.read_sql(query,conn)
        
        df.to_csv('Creditcard.csv',index=False)
        
        
        print("Data saved in Creditcard.csv")
        print("Rows, Columns:", df.shape)

        conn.close()
        
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    data_save()
