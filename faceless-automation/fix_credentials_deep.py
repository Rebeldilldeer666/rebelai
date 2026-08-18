import os
import requests

print("=== DIAGNOSING CREDENTIAL & CHANNEL ERRORS ===")

# 1. Stripe Issue: Keys starting with "Pk_live_" are Publishable Keys. 
# Publishable keys are meant for client-side frontend code (like JS) and cannot access server-side endpoints like /v1/balance.
# Server-side API calls require a Secret Key (which typically starts with "sk_live_").

# 2. Telegram Issue: "Bad Request: chat not found" means either:
# - The bot has never interacted with or been added to @gambitshustlellc.
# - The chat ID needs to be a numeric ID instead of a username, or the bot needs to be an admin/member of that channel.

print("\n[DIAGNOSIS 1] Stripe Key Type:")
print(" - The provided key starts with 'Pk_live_'. This is a Publishable Key.")
print(" - To query backend servers (/v1/balance), you must use a Secret Key starting with 'sk_live_'.")

print("\n[DIAGNOSIS 2] Telegram Chat Binding:")
print(" - Error 400: 'chat not found'. Ensure your Telegram bot has started a conversation or is added to the channel @gambitshustlellc.")

