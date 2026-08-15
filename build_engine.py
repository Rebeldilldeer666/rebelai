cat << 'EOF' > master_engine.py
import os
import json
import random
import requests
import time

# Direct Native Config (No Paywalls)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")

class MasterProductionEngine:
    def __init__(self):
        self.tg_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
        self.tg_msg_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    def generate_all_in_one_content(self):
        content_types = ["digital_product", "vlog_script", "social_post", "reel_short"]
        selected_type = random.choice(content_types)
        
        item_id = f"item_{int(time.time())}"
        
        if selected_type == "digital_product":
            return {
                "id": item_id,
                "type": "🚀 DIGITAL PRODUCT",
                "text": "⚡ NEW TOOL RELEASE: Rebel AI Python Engine v2\n\nAutomate multi-channel deployment hands-free.\n\n👉 Access Live: https://rebelai.store",
                "image": "https://picsum.photos/id/10/800/800"
            }
        elif selected_type == "vlog_script":
            return {
                "id": item_id,
                "type": "🎬 VLOG / DEMO SNIPPET",
                "text": "📹 VLOG UPDATE: Building a 24/7 Digital Empire on Mobile\n\nWatch how background automation runs Python scrapers & deployments in real time.\n\n📺 Full Vlog & Resources: https://rebelai.store",
                "image": "https://picsum.photos/id/20/800/800"
            }
        elif selected_type == "social_post":
            return {
                "id": item_id,
                "type": "💡 VALUE INSIGHT",
                "text": "🔥 Stop manually posting content.\n\nSet up direct API webhooks and background daemons to handle distribution on autopilot 24/7.\n\n👉 Get Started: https://rebelai.store",
                "image": "https://picsum.photos/id/30/800/800"
            }
        else: # reel_short
            return {
                "id": item_id,
                "type": "📱 REEL / SHORT CONCEPT",
                "text": "🎬 REEL HOOK: 'How I Automated 100 Digital Products in 15 Minutes'\n\n[Visual: Termux terminal running Python loops]\nCTA: Grab the full script collection below!\n\n👉 Link: https://rebelai.store",
                "image": "https://picsum.photos/id/40/800/800"
            }

    def dispatch(self):
        data = self.generate_all_in_one_content()
        caption = f"{data['type']}\n\n{data['text']}"
        
        # 1. Dispatch to Telegram Channel
        tg_payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "photo": data["image"],
            "caption": caption
        }
        
        try:
            res = requests.post(self.tg_url, data=tg_payload, timeout=30)
            print(f"✅ Telegram Dispatch ({data['type']}): {res.status_code}")
        except Exception as e:
            print(f"❌ Telegram Error: {e}")

        # 2. Dispatch to External Webhook (Discord / Custom API / Vercel Endpoint)
        if DISCORD_WEBHOOK_URL:
            webhook_payload = {
                "content": f"**{data['type']}**\n{data['text']}\n{data['image']}"
            }
            try:
                res_wh = requests.post(DISCORD_WEBHOOK_URL, json=webhook_payload, timeout=30)
                print(f"✅ Webhook Dispatch: {res_wh.status_code}")
            except Exception as e:
                print(f"❌ Webhook Error: {e}")

if __name__ == "__main__":
    engine = MasterProductionEngine()
    engine.dispatch()
EOF

