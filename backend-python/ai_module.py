import re

def analyze_data(data):
    result = {
        "records": len(data),
        "anomalies": []
    }

    for i, row in enumerate(data):
        if isinstance(row, dict):
            values = row.values()
        else:
            values = row

        if not values or all(str(x).strip() == "" for x in values):
            result["anomalies"].append({"index": i, "issue": "Empty row"})
        elif any("error" in str(x).lower() for x in values):
            result["anomalies"].append({"index": i, "issue": "Contains 'error'"})
        elif any(re.match(r'^\d{10,}$', str(x)) for x in values):
            result["anomalies"].append({"index": i, "issue": "Possible sensitive data"})

    result["status"] = "Anomaly Detected" if result["anomalies"] else "Normal"
    return result
