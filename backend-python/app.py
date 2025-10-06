# app.py
from flask import Flask, jsonify, request
from gcp_bigtable import get_bigtable_data
from gcp_sql import get_sql_data, insert_sql_data
from ai_module import process_text, analyze_numbers

app = Flask(__name__)

# -------------------------
# Homepage route
# -------------------------
@app.route("/", methods=["GET"])
def home():
    return """
    <h1>Welcome to AI + GCP + SQL Backend</h1>
    <p>Available endpoints:</p>
    <ul>
        <li>/gcp/bigtable/all</li>
        <li>/gcp/sql/all?table=analysis_logs</li>
        <li>/gcp/sql/insert</li>
        <li>/ai/process_text</li>
        <li>/ai/analyze_numbers</li>
    </ul>
    """

# -------------------------
# GCP Bigtable endpoint
# -------------------------
@app.route("/gcp/bigtable/all", methods=["GET"])
def fetch_bigtable_data():
    try:
        data = get_bigtable_data()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------------
# SQL endpoints (dynamic table selection)
# -------------------------
@app.route("/gcp/sql/all", methods=["GET"])
def fetch_sql_data():
    try:
        table = request.args.get("table", "analysis_logs")  # default to 'analysis_logs'
        data = get_sql_data(table)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/gcp/sql/insert", methods=["POST"])
def insert_sql():
    try:
        payload = request.json or {}
        table = payload.get("table", "analysis_logs")  # default to 'analysis_logs'
        payload.pop("table", None)  # remove table key before inserting
        insert_sql_data(table, payload)
        return jsonify({"message": f"Inserted successfully into {table}"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------------
# AI endpoints (GET + POST)
# -------------------------
@app.route("/ai/process_text", methods=["GET", "POST"])
def ai_text():
    try:
        if request.method == "POST":
            data = request.json or {}
            text = data.get("text", "")
        else:
            text = "Hello World from browser GET"
        result = process_text(text)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/ai/analyze_numbers", methods=["GET", "POST"])
def ai_numbers():
    try:
        if request.method == "POST":
            data = request.json or {}
            numbers = data.get("numbers", [])
        else:
            numbers = [1, 2, 3, 4, 5]
        result = analyze_numbers(numbers)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------------
# Run Flask
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
