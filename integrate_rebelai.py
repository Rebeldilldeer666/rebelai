import os, json, requests

# System Configuration
REBELAI_CONFIG = {
    "domain": "https://rebelliousbytes.online",
    "github_repo": "https://github.com/Rebeldilldeer666/rebelai.git",
    "local_webhook": "http://127.0.0.1:5000/webhook",
    "discord_webhook": os.getenv("DISCORD_WEBHOOK_URL", ""),
    "telegram_bot_token": os.getenv("TELEGRAM_BOT_TOKEN", ""),
    "telegram_chat_id": os.getenv("TELEGRAM_CHAT_ID", "")
}

def verify_system_endpoints():
    print("⚡ --- REBEL AI SYSTEM INTEGRATION CHECK --- ⚡")
    print(f"🌐 Main Storefront: {REBELAI_CONFIG['domain']}")
    print(f"📦 GitHub Repo:     {REBELAI_CONFIG['github_repo']}")
    print(f"🔌 Webhook Server:  {REBELAI_CONFIG['local_webhook']}")
    print("-" * 50)

def broadcast_to_discord(message):
    url = REBELAI_CONFIG["discord_webhook"]
    if not url:
        print("⚠️  Discord Webhook URL not set in environment (DISCORD_WEBHOOK_URL).")
        return
    payload = {"content": message}
    try:
        res = requests.post(url, json=payload)
        print(f"✅ Discord Broadcast Status: {res.status_code}")
    except Exception as e:
        print(f"❌ Discord Error: {e}")

def broadcast_to_telegram(message):
    token = REBELAI_CONFIG["telegram_bot_token"]
    chat_id = REBELAI_CONFIG["telegram_chat_id"]
    if not token or not chat_id:
        print("⚠️  Telegram credentials not set in environment (TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID).")
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    try:
        res = requests.post(url, json=payload)
        print(f"✅ Telegram Broadcast Status: {res.status_code}")
    except Exception as e:
        print(f"❌ Telegram Error: {e}")

if __name__ == "__main__":
    verify_system_endpoints()
    
    msg = (
        "🚀 *REBEL AI SYSTEM UPDATE*\n\n"
        "Storefront updated and active: https://rebelliousbytes.online\n"
        "Vault assets & automation engines ready for deployment."
    )
    
    print("\nAttempting automated community broadcasts...")
    broadcast_to_discord(msg)
    broadcast_to_telegram(msg)
