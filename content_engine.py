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
