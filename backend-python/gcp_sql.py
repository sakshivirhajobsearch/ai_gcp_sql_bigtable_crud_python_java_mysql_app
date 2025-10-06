import mysql.connector

def get_cloud_sql_data():
    conn = mysql.connector.connect(
        host="localhost",         # ✅ use actual IP or localhost
        user="root",              # ✅ your username
        password="admin", # ✅ your password
        database="ai_gcp_sql_bigtable"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cloudsql_table")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
