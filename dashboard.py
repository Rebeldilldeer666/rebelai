import json
import os
import sys

# ANSI Colors for High Visibility
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

FILE_PATH = "master_revenue_output.json"

if not os.path.exists(FILE_PATH):
    print(f"{RED}Error: {FILE_PATH} not found. Run ./run.sh first.{RESET}")
    sys.exit(1)

with open(FILE_PATH, "r") as f:
    data = json.load(f)

summary = data.get("summary", {})
executed_at = data.get("executed_at", "N/A")
digital = data.get("data", {}).get("digital_products", [])
real_estate = data.get("data", {}).get("real_estate_leads", [])
affiliate = data.get("data", {}).get("affiliate_campaigns", [])

total_catalog_val = summary.get("total_catalog_value", sum(p.get("price", 0) for p in digital))
total_re_fee = sum(p.get("assignment_fee_target", 10000) for p in real_estate)
grand_total = total_catalog_val + total_re_fee

# Clear terminal screen
print("\033[H\033[J", end="")

print(f"{BOLD}{CYAN}================================================================={RESET}")
print(f"             🔥 REBEL AI MASTER REVENUE DASHBOARD 🔥             ")
print(f"{BOLD}{CYAN}================================================================={RESET}\n")

print(f"{BOLD}Last Engine Sync:{RESET} {executed_at}")
print(f"{BOLD}Daemon Status:{RESET}    {GREEN}● ACTIVE & LOOPING (Hourly Pass){RESET}\n")

print(f"{BOLD}{YELLOW}┌── FINANCIAL PIPELINE METRICS ─────────────────────────────────┐{RESET}")
print(f"│  • {BOLD}Digital Product Catalog Value:{RESET}   {GREEN}${total_catalog_val:,.2f}{RESET}")
print(f"│  • {BOLD}Real Estate Wholesale Fees:{RESET}      {GREEN}${total_re_fee:,.2f}{RESET}")
print(f"│  • {BOLD}Grand Total Pipeline Value:{RESET}     {GREEN}${grand_total:,.2f}{RESET}")
print(f"{BOLD}{YELLOW}└───────────────────────────────────────────────────────────────┘{RESET}\n")

print(f"{BOLD}{CYAN}┌── ENGINE PRODUCTIVITY BREAKDOWN ──────────────────────────────┐{RESET}")
print(f"│  • {BOLD}Digital Assets Active:{RESET}     {len(digital)} Staged Products")
print(f"│  • {BOLD}Wholesale Real Estate Leads:{RESET} {len(real_estate)} Qualified Deals")
print(f"│  • {BOLD}Affiliate Campaign Feeds:{RESET}    {len(affiliate)} Live Offers")
print(f"{BOLD}{CYAN}└───────────────────────────────────────────────────────────────┘{RESET}\n")

print(f"{BOLD}{GREEN}┌── ACTIVE DIGITAL CATALOG & PAYMENT LINKS ────────────────────┐{RESET}")
for idx, p in enumerate(digital, 1):
    print(f"  {CYAN}[{idx:02d}]{RESET} {BOLD}{p['title']}{RESET} | {GREEN}${p['price']}{RESET}")
    print(f"       SKU: {p['sku']}  |  Category: {p['category']}")
    print(f"       Stripe:  {p['checkout_urls']['stripe']}")
    print(f"       Gumroad: {p['checkout_urls']['gumroad']}\n")
print(f"{BOLD}{GREEN}└───────────────────────────────────────────────────────────────┘{RESET}")
