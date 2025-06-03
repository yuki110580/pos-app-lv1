# backend/db.py

import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='rdbs-step4-south-india.mysql.database.azure.com',
            user='tech0sql1',
            password='step4pos-5', 
            database='step4pos',
            ssl_ca='/Users/~/Downloads/DigiCertGlobalRootCA.crt.pem' #あってるか要確認
        )
        return connection
    except Error as e:
        print(f"DB接続エラー: {e}")
        return None
