import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Pull secrets from environment variables (Never hardcode API keys)
STRIPE_KEY = os.getenv("STRIPE_SECRET_KEY")
AYRSHARE_KEY = os.getenv("AYRSHARE_API_KEY")

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "system": "Rebel AI Master Hub",
        "version": "1.0.0"
    })

@app.route("/webhook/stripe", methods=["POST"])
def stripe_webhook():
    data = request.get_json()
    # Log incoming live purchase event
    print("Stripe Live Event Received:", data)
    return jsonify({"status": "success"}), 200

@app.route("/webhook/digistore", methods=["POST"])
def digistore_webhook():
    data = request.form
    # Log Digistore sale callback
    print("Digistore Sale Event:", data)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
