import json
import os
import random
import urllib.request

WEBHOOK_URL = os.getenv("REVENUE_WEBHOOK_URL", "")

if not os.path.exists("master_revenue_output.json"):
    print("Error: master_revenue_output.json not found.")
    exit(1)

with open("master_revenue_output.json", "r") as f:
    data = json.load(f)

products = data.get("data", {}).get("digital_products", [])
affiliates = data.get("data", {}).get("affiliate_campaigns", [])

# Pick 3 random affiliate deals from the 415 catalog for continuous drip marketing
drip_deals = random.sample(affiliates, min(3, len(affiliates)))

print(f"--- REBEL AI 415-PRODUCT DRIP BROADCASTER ---")
print(f"Total Marketplace Products: {len(affiliates)}")
print(f"Selected Drip Offers for this Pass: {len(drip_deals)}")

if WEBHOOK_URL:
    for deal in drip_deals:
        msg = {
            "content": f"🚨 **FEATURED AFFILIATE DEAL** | {deal['product_name']}\n"
                       f"🏷️ **Category:** {deal.get('category', 'Digital')}\n"
                       f"🔗 **Monetized Link:** {deal['monetized_url']}"
        }
        try:
            req = urllib.request.Request(
                WEBHOOK_URL,
                data=json.dumps(msg).encode("utf-8"),
                headers={"Content-Type": "application/json", "User-Agent": "RebelAI-Drip/2.0"}
            )
            urllib.request.urlopen(req)
            print(f"✅ Broadcasted deal: {deal['product_name']}")
        except Exception as e:
            print(f"❌ Dispatch failed: {e}")
else:
    print("\nℹ️ REVENUE_WEBHOOK_URL not set. Current hourly drip selection:\n")
    for deal in drip_deals:
        print(f"  • [{deal.get('category')}] {deal['product_name']}")
        print(f"    Link: {deal['monetized_url']}\n")
