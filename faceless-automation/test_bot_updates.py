import requests

token = "8835224707:AAF1sJV-xe_uvnGXLXtH_w223zAg-omMFW4"
url = f"https://api.telegram.org/bot{token}/getUpdates"

print("Querying Telegram getUpdates to locate active chat IDs...")
try:
    res = requests.get(url, timeout=10)
    data = res.json()
    print("Response:", data)
except Exception as e:
    print("Error:", e)
