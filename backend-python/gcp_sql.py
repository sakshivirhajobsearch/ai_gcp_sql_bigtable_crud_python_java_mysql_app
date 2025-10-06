# gcp_sql.py
import mysql.connector
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

# -----------------------------
# Replace 'YOUR_TABLE' with your actual table name
# -----------------------------
TABLE_NAME = "YOUR_TABLE"

def get_sql_data():
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def insert_sql_data(data_dict):
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    cursor = conn.cursor()
    placeholders = ", ".join(["%s"] * len(data_dict))
    columns = ", ".join(data_dict.keys())
    sql = f"INSERT INTO {TABLE_NAME} ({columns}) VALUES ({placeholders})"
    cursor.execute(sql, tuple(data_dict.values()))
    conn.commit()
    cursor.close()
    conn.close()
    return True
