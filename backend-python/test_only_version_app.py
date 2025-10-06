from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Test app running."

@app.route("/gcp/sql/all", methods=["GET"])
def test_sql():
    return jsonify({"data": [[1, "test", "row"]], "ai_analysis": {"records": 1, "status": "Normal"}})

@app.route("/gcp/bigtable/all", methods=["GET"])
def test_bigtable():
    return jsonify({"data": [{"key": "row1", "value": "data"}], "ai_analysis": {"records": 1, "status": "Normal"}})

if __name__ == '__main__':
    app.run(debug=True)
