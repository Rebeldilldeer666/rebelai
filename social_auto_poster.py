import json, requests

PROMO_POSTS = [
    {
        "channel": "Reddit / r/Termux & r/Python",
        "title": "[Free + Open Source] Automated Digital Product Builder in Python for Termux",
        "body": "Built a pure Python script that bundles code, creates READMEs, and zips delivery packages directly on Android Termux.\n\nGrab the starter script or check out the full vault:\nhttps://rebelliousbytes.online"
    },
    {
        "channel": "Telegram Dark Art & Tattoo Drops",
        "title": "⚡ NEW DROP: Gothic & Biomechanical Vector Stencil Pack v2",
        "body": "Clean, thermal-printer ready vector stencils (SVG/PNG) with high-density line work.\n\nInstant Unlocks Available:\nhttps://rebelliousbytes.online"
    },
    {
        "channel": "Discord Developer Webhook",
        "title": "🚀 Solana Mirror Trading & Trailing Stop Bot Core Live",
        "body": "Low-latency asynchronous transaction monitor built for DEX execution in Termux/Linux.\n\nVault Access: https://rebelliousbytes.online"
    }
]

def dispatch_discord_webhook(webhook_url, message_content):
    payload = {"content": message_content}
    response = requests.post(webhook_url, json=payload)
    return response.status_code

print("--- REBEL AI HYPERDRIVE PROMO ENGINE ---")
for idx, post in enumerate(PROMO_POSTS, 1):
    print(f"\n[{idx}] TARGET: {post['channel']}")
    print(f"TITLE: {post['title']}")
    print(f"BODY:\n{post['body']}")
    print("-" * 50)

print("\nCopy-paste these formatted posts directly to your target communities to start driving inbound traffic!")
