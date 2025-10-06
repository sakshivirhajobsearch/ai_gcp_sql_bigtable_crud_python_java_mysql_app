import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="ai_gcp_sql_bigtable"
    )

def save_analysis_log(source, record_count, anomaly_count, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO analysis_logs (source, record_count, anomaly_count, status)
        VALUES (%s, %s, %s, %s)
    """, (source, record_count, anomaly_count, status))
    conn.commit()
    cursor.close()
    conn.close()
