import os
<<<<<<< HEAD
import json
import random
import requests
import time

# Rebel AI Master Environment Config (Integrated Token & Channel ID)
TELEGRAM_BOT_TOKEN = "8688057364:AAFC0HYgGMSI2O-MWP_E5WvhXYGmTmEEqZo"
TELEGRAM_CHAT_ID = "@RebelAiStore" # Configured for live distribution
DIGISTORE_LINK = "https://www.digistore24.com/redir/358077/RebelAi/"
STORE_URL = "https://rebelai.store"

class RebelAiProductionEngine:
    def __init__(self):
        self.tg_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"

    def generate_live_post(self):
        hooks = [
            "🔥 TRENDING DIGITAL TOOL: Instant access package available now.",
            "⚡ LIMITED TIME PIPELINE: Scale your automated workflow today.",
            "🚀 HIGH-CONVERTING BLUEPRINT: Grab the complete system setup."
        ]
        selected_hook = random.choice(hooks)
        
        text = f"{selected_hook}\n\nGet instant access and start seeing results:\n👉 {DIGISTORE_LINK}\n\nHub: {STORE_URL}"
        
        return {
            "text": text,
            "image": "https://picsum.photos/id/10/800/800"
        }

    def dispatch(self):
        data = self.generate_live_post()
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "photo": data["image"],
            "caption": data["text"]
        }
        
        try:
            res = requests.post(self.tg_url, data=payload, timeout=30)
            print(f"✅ Rebel AI Live Dispatch: {res.status_code}")
            print(res.text)
        except Exception as e:
            print(f"❌ Rebel AI Dispatch Error: {e}")

if __name__ == "__main__":
    engine = RebelAiProductionEngine()
    engine.dispatch()
=======
from dotenv import load_dotenv

load_dotenv()

STRIPE_LIVE_SECRET_KEY = os.getenv("STRIPE_LIVE_SECRET_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class MasterEngine:
    def __init__(self):
        if not STRIPE_LIVE_SECRET_KEY or not TELEGRAM_BOT_TOKEN:
            print("[!] WARNING: Production keys missing from environment. Check your .env file.")
        else:
            print("[+] MasterEngine initialized securely.")

    def execute(self):
        print("[*] Rebel AI Automation workflows executing at peak efficiency...")

if __name__ == "__main__":
    engine = MasterEngine()
    engine.execute()
>>>>>>> f42ebd781c305aedccf66658052852860deda36d
