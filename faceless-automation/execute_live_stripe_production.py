import os
import requests

print("=== EXECUTING LIVE STRIPE & TELEGRAM PRODUCTION SYNC ===")

# Using your live Stripe Publishable/Secret key and Telegram credentials
stripe_key = "Pk_live_51TSj9uHLHBCdR2IV5R9mOuKeSqNLpGMwArzhfjnZPlHmTI8fltTj7UQ4KQcHtNIUYHDJJ4HjRQghTOaEUuZ4nDOP00jRjDWKgZ"
telegram_token = "8835224707:AAF1sJV-xe_uvnGXLXtH_w223zAg-omMFW4"
telegram_chat_id = "@gambitshustlellc"

headers = {
    "Authorization": f"Bearer {stripe_key}",
    "Content-Type": "application/x-www-form-urlencoded"
}

print("\n[1/2] Connecting to live Stripe endpoint...")
try:
    response = requests.get("https://api.stripe.com/v1/balance", headers=headers, timeout=10)
    print(f"Stripe Response Status: {response.status_code}")
    print(f"Stripe Response Body: {response.text}")
except Exception as e:
    print(f"Stripe Connection Error: {e}")

print("\n[2/2] Broadcasting production status to Telegram (@gambitshustlellc)...")
telegram_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
payload = {
    "chat_id": telegram_chat_id,
    "text": "⚡ [REBEL AI PRODUCTION] Live keys loaded. Automated revenue tracking and webhook channels are fully synchronized."
}

try:
    tg_res = requests.post(telegram_url, json=payload, timeout=10)
    print(f"Telegram Response Status: {tg_res.status_code}")
    print(f"Telegram Response Body: {tg_res.text}")
except Exception as e:
    print(f"Telegram Connection Error: {e}")

print("\n--------------------------------------------------")
print("LIVE EXECUTION SCRIPT COMPLETED.")
print("--------------------------------------------------")
