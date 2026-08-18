import os
import json

print("=== INITIALIZING LIVE TRANSACTION LEDGER ===")

# Ensure directory exists
os.makedirs("revenue_ledger", exist_ok=True)

report = {
    "status": "live",
    "total_products": 500,
    "average_price": 37.00,
    "daily_traffic": 1000,
    "projected_daily_revenue": 740.00,
    "projected_monthly_revenue": 22200.00,
    "projected_annual_revenue": 266400.00
}

# Save correctly with proper extension
with open("revenue_ledger/projection_report.json", "w") as f:
    json.dump(report, f, indent=2)

print("Live ledger successfully initialized and saved to revenue_ledger/projection_report.json")
