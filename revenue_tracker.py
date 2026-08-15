import os
import json
from datetime import datetime

LEDGER_FILE = "revenue_ledger.json"

class RevenueTracker:
    def __init__(self):
        self.ledger_file = LEDGER_FILE
        self.init_ledger()

    def init_ledger(self):
        if not os.path.exists(self.ledger_file):
            data = {
                "total_revenue": 0.00,
                "total_sales": 0,
                "transactions": []
            }
            with open(self.ledger_file, "w") as f:
                json.dump(data, f, indent=2)

    def log_sale(self, product_name, amount, platform="Stripe/Digistore"):
        with open(self.ledger_file, "r") as f:
            data = json.load(f)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sale_entry = {
            "timestamp": timestamp,
            "product": product_name,
            "amount": float(amount),
            "platform": platform
        }

        data["transactions"].append(sale_entry)
        data["total_revenue"] += float(amount)
        data["total_sales"] += 1

        with open(self.ledger_file, "w") as f:
            json.dump(data, f, indent=2)

        print(f"💰 SALE RECORDED! +${amount:.2f} | Total Revenue: ${data['total_revenue']:.2f}")

    def get_summary(self):
        with open(self.ledger_file, "r") as f:
            data = json.load(f)
        
        print("==========================================")
        print("📊 REBEL AI - 72-HOUR REVENUE TRACKER")
        print("==========================================")
        print(f"💵 Total Revenue: ${data['total_revenue']:.2f}")
        print(f"📦 Total Sales:   {data['total_sales']}")
        print("------------------------------------------")
        print("Recent Transactions:")
        for tx in data["transactions"][-5:]:
            print(f"[{tx['timestamp']}] {tx['product']} - ${tx['amount']:.2f} ({tx['platform']})")
        print("==========================================")

if __name__ == "__main__":
    tracker = RevenueTracker()
    # Example test log to verify functionality
    # tracker.log_sale("Rebel AI Python Engine v2", 29.99, "Direct Store")
    tracker.get_summary()
