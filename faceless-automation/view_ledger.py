import json

with open("revenue_ledger/projection_report.json", "r") as f:
    data = json.load(f)

print("=== ACTIVE REVENUE LEDGER STATUS ===")
for k, v in data.items():
    print(f"{k}: {v}")
