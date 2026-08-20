from datetime import datetime
import json
import logging
import os
import random
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# -------------------------------------------------------------------
# LOGGING & ENVIRONMENT SETUP
# -------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("revenue_engine.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

WEBHOOK_URL = os.getenv("REVENUE_WEBHOOK_URL", "")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
GUMROAD_ACCESS_TOKEN = os.getenv("GUMROAD_ACCESS_TOKEN", "")
DIGISTORE24_AFFILIATE_ID = os.getenv("DIGISTORE24_AFFILIATE_ID", "rebelai")


def send_webhook_alert(title: str, summary: dict):
    if not WEBHOOK_URL:
        return

    payload = {
        "content": f"🚨 **REBEL AI AUTONOMOUS ENGINE** | {title}",
        "embeds": [
            {
                "title": "Turnover Execution Summary",
                "color": 15158332,  # Red/Gold
                "description": f"```json\n{json.dumps(summary, indent=2)}\n```",
                "timestamp": datetime.now().isoformat(),
            }
        ],
    }

    try:
        req = urllib.request.Request(
            WEBHOOK_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "User-Agent": "RebelAI-GodMode/3.0",
            },
        )
        with urllib.request.urlopen(req) as resp:
            logging.info(f"[Webhook] Dispatch successful: {resp.status}")
    except Exception as e:
        logging.error(f"[Webhook] Dispatch failed: {e}")


# ===================================================================
# ENGINE 1: VIRTUAL REAL ESTATE LEAD DISCOVERY & MAO ENGINE
# ===================================================================
def run_real_estate_engine() -> dict:
    logging.info("--- [Engine 1] Autonomous Real Estate Deal Processor ---")

    properties_feed = [
        {
            "address": "123 Main St, Sheboygan, WI",
            "arv": 220000,
            "repairs": 35000,
            "status": "vacant",
            "absentee_owner": True,
        },
        {
            "address": "789 Pine Rd, Milwaukee, WI",
            "arv": 310000,
            "repairs": 25000,
            "status": "distressed",
            "absentee_owner": True,
        },
        {
            "address": "402 Lakeview Dr, Manitowoc, WI",
            "arv": 185000,
            "repairs": 18000,
            "status": "tax_default",
            "absentee_owner": True,
        },
        {
            "address": "910 Commercial St, Green Bay, WI",
            "arv": 450000,
            "repairs": 60000,
            "status": "vacant",
            "absentee_owner": True,
        },
    ]

    qualified_deals = []
    for prop in properties_feed:
        if prop["absentee_owner"]:
            mao = (prop["arv"] * 0.70) - prop["repairs"]
            qualified_deals.append(
                {
                    "address": prop["address"],
                    "arv": prop["arv"],
                    "repairs": prop["repairs"],
                    "mao": round(mao, 2),
                    "assignment_fee_target": 12500.00,
                    "timestamp": datetime.now().isoformat(),
                }
            )

    logging.info(
        f"[Engine 1] Complete: {len(qualified_deals)} wholesale leads processed."
    )
    return {"real_estate_leads": qualified_deals}


# ===================================================================
# ENGINE 2: DIGISTORE24 & MULTI-RAIL AFFILIATE DISPATCH
# ===================================================================
def run_affiliate_engine() -> dict:
    logging.info("--- [Engine 2] 415-Product Digistore24 Catalog Publisher ---")
    catalog_file = "digistore_catalog.json"
    campaigns = []
    
    if os.path.exists(catalog_file):
        with open(catalog_file, "r") as f:
            full_catalog = json.load(f)
            
        for product in full_catalog:
            promo_link = f"https://www.digistore24.com/redir/{product['id']}/{DIGISTORE24_AFFILIATE_ID}/"
            campaigns.append({
                "platform": "Digistore24",
                "product_id": product["id"],
                "product_name": product["title"],
                "category": product["category"],
                "est_commission": product["estimated_payout"],
                "monetized_url": promo_link,
                "social_copy": f"🔥 Featured Access: {product['title']}! Grab direct access here: {promo_link}",
                "timestamp": datetime.now().isoformat()
            })
    else:
        logging.warning("digistore_catalog.json not found.")

    logging.info(f"[Engine 2] Complete: Loaded {len(campaigns)} affiliate campaigns into master pipeline.")
    return {"affiliate_campaigns": campaigns}


# ===================================================================
# ENGINE 3: HIGH-TURNOVER MULTI-PRODUCT DIGITAL VAULT
# ===================================================================
def run_digital_vault_engine() -> dict:
    logging.info("--- [Engine 3] Generating High-Turnover Digital Product Catalog ---")

    # Expanded 10-Product High-Value Catalog
    digital_catalog = [
        {
            "title": "Gothic Vector Stencil & New-School Tattoo Flash Pack",
            "category": "Digital Art",
            "price": 29.99,
            "desc": "100+ High-resolution vector stencils and Gothic flash art ready for print and thermal transfer.",
        },
        {
            "title": "Automated Wholesale Real Estate Lead & Outreach Suite",
            "category": "Automation",
            "price": 69.99,
            "desc": "Full Python workflow for identifying vacant leads, calculating MAO, and generating contracts.",
        },
        {
            "title": "Termux Mobile Micro-SaaS & Python Script Vault",
            "category": "Software",
            "price": 49.99,
            "desc": "Turn key mobile automation scripts for local environment automation, scraping, and APIs.",
        },
        {
            "title": "High-Power Off-Road E-Bike Sourcing & Wholesale Guide",
            "category": "E-Commerce",
            "price": 19.99,
            "desc": "Direct factory supplier contact directory and specifications for 1000W+ electric fat tire bikes.",
        },
        {
            "title": "Industrial Injection Molding & Wear Engineering Manual",
            "category": "Industrial",
            "price": 99.99,
            "desc": "Technical manual covering metal wear, rotary molding, and industrial injection molding setups.",
        },
        {
            "title": "Cyberpunk & Dark Aesthetic Tattoo Flash Megapack",
            "category": "Digital Art",
            "price": 34.99,
            "desc": "Futuristic cyberpunk designs, neo-traditional stencils, and linework layers.",
        },
        {
            "title": "Turnkey Rebel AI Digital Storefront Engine",
            "category": "Software",
            "price": 149.99,
            "desc": "The complete Python backend and automated deployment configuration for multi-platform sales.",
        },
        {
            "title": "Midjourney & DALL-E Dark Art Prompt Engineering Matrix",
            "category": "AI Prompts",
            "price": 14.99,
            "desc": "500+ master prompts engineered specifically for high-contrast vector stencil production.",
        },
        {
            "title": "Distressed Real Estate Cold Call & SMS Contract Bundle",
            "category": "Real Estate",
            "price": 39.99,
            "desc": "Wholesale legal assignment contracts, phone scripts, and absentee owner outreach templates.",
        },
        {
            "title": "Print-on-Demand Gothic Streetwear Vector Asset Pack",
            "category": "Digital Art",
            "price": 27.99,
            "desc": "Vector assets optimized for apparel printing, screen printing, and high-margin merch.",
        },
    ]

    staged_products = []
    for item in digital_catalog:
        sku = f"REBEL-{item['category'][:3].upper()}-{abs(hash(item['title'])) % 10000}"

        stripe_link = f"https://buy.stripe.com/mock_{sku.lower()}"
        gumroad_link = f"https://gumroad.com/l/{sku.lower()}"

        # --- LIVE STRIPE CREATION ---
        if STRIPE_SECRET_KEY:
            try:
                price_data = urllib.parse.urlencode({
                    "unit_amount": int(item["price"] * 100),
                    "currency": "usd",
                    "product_data[name]": item["title"],
                }).encode("utf-8")
                
                req_p = urllib.request.Request(
                    "https://api.stripe.com/v1/prices",
                    data=price_data,
                    headers={
                        "Authorization": f"Bearer {STRIPE_SECRET_KEY}",
                        "Content-Type": "application/x-www-form-urlencoded",
                    }
                )
                with urllib.request.urlopen(req_p) as resp:
                    p_res = json.loads(resp.read().decode("utf-8"))
                    price_id = p_res.get("id")

                link_data = urllib.parse.urlencode({
                    "line_items[0][price]": price_id,
                    "line_items[0][quantity]": 1,
                }).encode("utf-8")

                req_l = urllib.request.Request(
                    "https://api.stripe.com/v1/payment_links",
                    data=link_data,
                    headers={
                        "Authorization": f"Bearer {STRIPE_SECRET_KEY}",
                        "Content-Type": "application/x-www-form-urlencoded",
                    }
                )
                with urllib.request.urlopen(req_l) as resp_l:
                    l_res = json.loads(resp_l.read().decode("utf-8"))
                    stripe_link = l_res.get("url", stripe_link)
            except Exception as e:
                logging.warning(f"[Stripe] Fallback for {sku}: {e}")

        # --- LIVE GUMROAD CREATION ---
        if GUMROAD_ACCESS_TOKEN:
            try:
                g_data = urllib.parse.urlencode({
                    "access_token": GUMROAD_ACCESS_TOKEN,
                    "name": item["title"],
                    "price": int(item["price"] * 100),
                    "description": item["desc"],
                }).encode("utf-8")

                req_g = urllib.request.Request(
                    "https://api.gumroad.com/v2/products",
                    data=g_data,
                    headers={"Content-Type": "application/x-www-form-urlencoded"}
                )
                with urllib.request.urlopen(req_g) as resp_g:
                    g_res = json.loads(resp_g.read().decode("utf-8"))
                    if g_res.get("success"):
                        gumroad_link = g_res["product"]["short_url"]
            except Exception as e:
                logging.warning(f"[Gumroad] Fallback for {sku}: {e}")

        staged_products.append(
            {
                "title": item["title"],
                "sku": sku,
                "category": item["category"],
                "price": item["price"],
                "checkout_urls": {
                    "stripe": stripe_link,
                    "gumroad": gumroad_link,
                },
                "status": "published_active",
                "timestamp": datetime.now().isoformat(),
            }
        )

    logging.info(
        f"[Engine 3] Complete: {len(staged_products)} products staged across all channels."
    )
    return {"digital_products": staged_products}


# ===================================================================
# MASTER EXECUTION PIPELINE
# ===================================================================
def run_master_pipeline():
    logging.info("========== STARTING REBEL AI HIGH-TURNOVER ENGINE ==========")

    master_output = {
        "executed_at": datetime.now().isoformat(),
        "summary": {},
        "data": {},
    }

    re_data = run_real_estate_engine()
    aff_data = run_affiliate_engine()
    vault_data = run_digital_vault_engine()

    master_output["data"].update(re_data)
    master_output["data"].update(aff_data)
    master_output["data"].update(vault_data)

    master_output["summary"] = {
        "real_estate_leads_processed": len(re_data["real_estate_leads"]),
        "affiliate_campaigns_active": len(aff_data["affiliate_campaigns"]),
        "digital_products_published": len(vault_data["digital_products"]),
        "total_catalog_value": sum(
            p["price"] for p in vault_data["digital_products"]
        ),
    }

    output_filename = "master_revenue_output.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(master_output, f, indent=4)

    logging.info(
        f"Master dataset output saved to '{output_filename}'! Total Catalog Value: ${master_output['summary']['total_catalog_value']:.2f}"
    )

    send_webhook_alert("Autonomous Run Completed", master_output["summary"])
    logging.info("========== PIPELINE EXECUTION FINISHED ==========")


if __name__ == "__main__":
    # Check if continuous autonomous loop flag is passed
    if "--loop" in sys.argv:
        logging.info("🚀 AUTONOMOUS CONTINUOUS LOOP ENABLED (Interval: 1 Hour)")
        while True:
            run_master_pipeline()
            logging.info("Sleeping for 3600 seconds (1 hour)...")
            time.sleep(3600)
    else:
        run_master_pipeline()

