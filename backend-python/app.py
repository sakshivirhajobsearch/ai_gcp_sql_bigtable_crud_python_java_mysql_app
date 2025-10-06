from flask import Flask, jsonify
from gcp_sql import get_cloud_sql_data
from gcp_bigtable import get_bigtable_data
from ai_module import analyze_data
from db import save_analysis_log

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "✅ Flask Backend is Running. Try /gcp/sql/all or /gcp/bigtable/all"

@app.route("/gcp/sql/all", methods=["GET"])
def fetch_sql_data():
    data = get_cloud_sql_data()
    analysis = analyze_data(data)
    save_analysis_log("CloudSQL", analysis["records"], len(analysis["anomalies"]), analysis["status"])
    return jsonify({"data": data, "ai_analysis": analysis})

@app.route("/gcp/bigtable/all", methods=["GET"])
def fetch_bigtable_data():
    data = get_bigtable_data()
    analysis = analyze_data(data)
    save_analysis_log("Bigtable", analysis["records"], len(analysis["anomalies"]), analysis["status"])
    return jsonify({"data": data, "ai_analysis": analysis})

if __name__ == '__main__':
    app.run(debug=True)
