import os, json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Product Download Mapping
PRODUCT_DOWNLOADS = {
    "1": "https://rebelliousbytes.online/downloads/obsidianink_vault_v1.zip",
    "2": "https://rebelliousbytes.online/downloads/gothic_steampunk_stencils.zip",
    "3": "https://rebelliousbytes.online/downloads/termux_automation_scripts.zip",
    "4": "https://rebelliousbytes.online/downloads/snake_geometric_vectors.zip",
    "5": "https://rebelliousbytes.online/downloads/solana_bot_core.zip",
    "6": "https://rebelliousbytes.online/downloads/cyber_jellyfish_uikit.zip",
    "7": "https://rebelliousbytes.online/downloads/real_estate_automation.zip",
    "8": "https://rebelliousbytes.online/downloads/metal_rap_stems.zip",
    "9": "https://rebelliousbytes.online/downloads/biomechanical_vectors.zip",
    "10": "https://rebelliousbytes.online/downloads/telegram_bot_suite.zip",
    "11": "https://rebelliousbytes.online/downloads/gothic_flash_bundle.zip",
    "12": "https://rebelliousbytes.online/downloads/python_scraper_engine.zip"
}

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    event = json.loads(payload)

    if event.get('type') == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session.get('customer_details', {}).get('email')
        client_reference_id = session.get('client_reference_id', '1')
        
        download_url = PRODUCT_DOWNLOADS.get(client_reference_id, "https://rebelliousbytes.online")
        
        print(f"⚡ [SUCCESS] Payment Received from: {customer_email}")
        print(f"📦 [DELIVERY] Dispatching Download Link: {download_url}")
        
        # Here you can trigger SendGrid, Mailgun, or SMTP email dispatch

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    print("🚀 Stripe Webhook Delivery Server Live on Port 5000...")
    app.run(host='0.0.0.0', port=5000)
