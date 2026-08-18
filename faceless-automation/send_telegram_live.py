import requests

token = "8835224707:AAF1sJV-xe_uvnGXLXtH_w223zAg-omMFW4"
chat_id = "-1004346161072"  # Correct channel ID found via getUpdates for "Rebel AI ecosystem"

url = f"https://api.telegram.org/bot{token}/sendMessage"
payload = {
    "chat_id": chat_id,
    "text": "⚡ [REBEL AI PRODUCTION] Telegram webhook successfully linked and verified! Live broadcast channel active."
}

res = requests.post(url, json=payload)
print("Status:", res.status_code)
print("Response:", res.text)
