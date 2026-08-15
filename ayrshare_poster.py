import os, json, requests

API_KEY = os.getenv("AYRSHARE_API_KEY", "YOUR_AYRSHARE_API_KEY_HERE")
API_URL = "https://api.ayrshare.com/api/post"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def send_post(post_text, media_urls=None, platforms=None):
    if platforms is None:
        platforms = ["twitter", "telegram", "tiktok", "youtube", "bluesky"]
    payload = {"post": post_text, "platforms": platforms}
    if media_urls:
        payload["mediaUrls"] = media_urls
    res = requests.post(API_URL, headers=HEADERS, json=payload)
    print(json.dumps(res.json(), indent=2))

if __name__ == "__main__":
    send_post("Live test from terminal!", media_urls=["https://www.w3schools.com/html/mov_bbb.mp4"])
