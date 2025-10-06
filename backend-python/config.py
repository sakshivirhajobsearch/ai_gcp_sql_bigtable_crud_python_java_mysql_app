# config.py

# -----------------------------
# GCP Project & Bigtable config
# -----------------------------
PROJECT_ID = ""
BIGTABLE_INSTANCE_ID = "YOUR_BIGTABLE_INSTANCE_ID"  # <--- replace this
BIGTABLE_TABLE_ID = "YOUR_BIGTABLE_TABLE_NAME"      # <--- replace this

# -----------------------------
# MySQL config
# -----------------------------
MYSQL_HOST = "localhost"        # e.g., "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_USER = "root"             # your MySQL username
MYSQL_PASSWORD = "admin" # your MySQL password
MYSQL_DB = "ai_gcp_sql_bigtable"       # your MySQL database name

# -----------------------------
# AI module settings (optional)
# -----------------------------
AI_MODEL_PATH = "models/my_model.pkl"  # optional
