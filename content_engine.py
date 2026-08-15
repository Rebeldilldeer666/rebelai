import os
import json
import random
import requests

class DynamicCatalogEngine:
    def __init__(self):
        self.api_key = os.getenv("AYRSHARE_API_KEY")
        self.api_url = "https://api.ayrshare.com/api/post"
        self.platforms = ["telegram", "facebook"]

    def load_catalog(self):
        try:
            with open("products.json", "r") as f:
                return json.load(f)
        except Exception as e:
            return []

    def publish(self):
        if not self.api_key:
            return {"status": "error", "message": "Missing AYRSHARE_API_KEY"}

        catalog = self.load_catalog()
        if not catalog:
            return {"status": "error", "message": "products.json is empty or missing"}

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
            return {
                "status_code": res.status_code,
                "promoted_product_id": selected["id"],
                "title": selected["title"],
                "destination": selected["url"],
                "response": res.json()
            }
        except Exception as e:
            return {"status_code": 500, "error": str(e)}

if __name__ == "__main__":
    engine = DynamicCatalogEngine()
    print(json.dumps(engine.publish(), indent=2))
