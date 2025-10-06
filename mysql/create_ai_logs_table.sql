CREATE DATABASE IF NOT EXISTS ai_gcp_sql_bigtable;

USE ai_gcp_sql_bigtable;

CREATE TABLE IF NOT EXISTS analysis_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    source VARCHAR(50),          -- 'CloudSQL' or 'Bigtable'
    record_count INT,
    anomaly_count INT,
    status VARCHAR(50),          -- 'Normal' or 'Anomaly Detected'
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
