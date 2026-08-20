import os
import requests

print("=== EXECUTING LIVE STRIPE & TELEGRAM PRODUCTION SYNC ===")

stripe_key = "Mk_1U0DVvHLHBCdR2IV3G9C8mPX"
telegram_token = "8835224707:AAF1sJV-xe_uvnGXLXtH_w223zAg-omMFW4"
telegram_chat_id = "-1004346161072"

headers = {
    "Authorization": f"Bearer {stripe_key}",
    "Content-Type": "application/x-www-form-urlencoded"
}

print("\n[1/2] Connecting to live Stripe endpoint...")
try:
    response = requests.get("https://api.stripe.com/v1/balance", headers=headers, timeout=10)
    print(f"Stripe Response Status: {response.status_code}")
    print(f"Stripe Response Body: {response.text}")
    
    if response.status_code == 200:
        msg = "💰 [REBEL AI REVENUE] Stripe live production key successfully verified and balance connection established!"
    else:
        msg = f"⚠️ [REBEL AI REVENUE] Stripe connection attempted with status code {response.status_code}."
        
    # Broadcast status to Telegram channel
    telegram_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {
        "chat_id": telegram_chat_id,
        "text": msg
    }
    tg_res = requests.post(telegram_url, json=payload, timeout=10)
    print(f"Telegram Broadcast Status: {tg_res.status_code}")

except Exception as e:
    print(f"[CONNECTION ERROR] Handshake failed: {e}")

print("\n--------------------------------------------------")
print("PRODUCTION EXECUTION SCRIPT COMPLETED.")
print("--------------------------------------------------")
