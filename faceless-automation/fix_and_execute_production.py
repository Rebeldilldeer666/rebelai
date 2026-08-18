import os
import requests

print("=== CORRECTING PRODUCTION CREDENTIALS & ENDPOINTS ===")

# As noted in security records, previous keys were deactivated due to public exposure, 
# and a new secret key was issued for your Rebel AI Systems account. 
# Please ensure your live secret key starts with 'rk_live_' or 'sk_live_' 
# and that your Telegram bot has started a conversation with the chat ID or channel.

stripe_key = os.getenv("STRIPE_LIVE_KEY", "sk_live_YOUR_ACTUAL_LIVE_KEY_HERE")
telegram_token = "8835224707:AAF1sJV-xe_uvnGXLXtH_w223zAg-omMFW4"
telegram_chat_id = "@gambitshustlellc"

print(f"\n[INFO] Target Telegram Chat: {telegram_chat_id}")
print("[INFO] Verify that your Stripe Live Key is an active, non-expired key from your dashboard.")

# Test Telegram API Connection with correct chat binding
telegram_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
payload = {
    "chat_id": telegram_chat_id,
    "text": "⚡ [REBEL AI PRODUCTION] System handshake verified. Please ensure the bot is an administrator in the channel or has started a direct chat."
}

try:
    tg_res = requests.post(telegram_url, json=payload, timeout=10)
    print(f"Telegram API Response: {tg_res.status_code} - {tg_res.text}")
except Exception as e:
    print(f"Telegram Connection Error: {e}")

print("\n--------------------------------------------------")
print("ACTION: To resolve the Stripe 401 error, generate a fresh live secret key in your Stripe dashboard and run:")
print("  export STRIPE_LIVE_KEY='sk_live_your_actual_key'")
print("--------------------------------------------------")
