<<<<<<< HEAD
import time
import random
import os

URL = "https://commit-britain-nyc-mai.trycloudflare.com"
CATEGORIES = {
    "motivational": ["Hook: Nobody is coming to save you. Build your own system."],
    "factual_funny": ["Hook: Humans spend 3 years of their lives on the toilet. Automate instead."],
    "rebel_rebellion": ["Hook: The 9-to-5 matrix is a rigged game. Here is your escape."]
}

print("[+] Rebel AI Autopilot Content Engine Active.")
while True:
    cat = random.choice(list(CATEGORIES.keys()))
    hook = random.choice(CATEGORIES[cat])
    entry = f"\n[CATEGORY: {cat.upper()}]\n{hook}\nCTA: Get the Rebel AI Suite at {URL}\n"
    with open("content_calendar.txt", "a") as f:
        f.write(entry)
    time.sleep(30)
=======
import os
import json
import random
import requests
import time

class BypassEngine:
    def __init__(self):
        self.api_key = os.getenv("AYRSHARE_API_KEY")
        self.api_url = "https://api.ayrshare.com/api/post"
        self.platforms = ["telegram", "facebook"]

    def load_catalog(self):
        try:
            with open("products.json", "r") as f:
                return json.load(f)
        except Exception:
            return []

    def publish(self):
        if not self.api_key:
            return {"status": "error", "message": "AYRSHARE_API_KEY missing"}

        catalog = self.load_catalog()
        if not catalog:
            return {"status": "error", "message": "Catalog empty"}

        selected = random.choice(catalog)
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "post": selected["text"],
            "platforms": self.platforms,
            "mediaUrls": [selected["image"]]
        }

        try:
            res = requests.post(self.api_url, headers=headers, json=payload, timeout=30)
            data = res.json()
            
            # Handle Free Tier Limit Hit
            if res.status_code == 429 or "exceeded" in str(data).lower():
                print("⚠️ AYRSHARE FREE TIER LIMIT REACHED. ENTERING COOLDOWN...")
                return {"status": "rate_limited", "message": "Daily API cap reached. Pausing until reset."}

            return {
                "status_code": res.status_code,
                "title": selected["title"],
                "response": data
            }
        except Exception as e:
            return {"status_code": 500, "error": str(e)}

if __name__ == "__main__":
    engine = BypassEngine()
    print(json.dumps(engine.publish(), indent=2))
>>>>>>> f42ebd781c305aedccf66658052852860deda36d
