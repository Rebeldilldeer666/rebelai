import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Real-time metrics storage (in-memory persistent tracking state)
METRICS = {
    "total_visitors": 0,
    "total_revenue": 0.00,
    "active_transactions": 0,
    "status": "LIVE_PRODUCTION"
}

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ONLINE",
        "message": "Rebel AI Live Revenue Engine is active and listening.",
        "metrics": METRICS
    }), 200

@app.route("/track-visit", methods=["POST"])
def track_visit():
    METRICS["total_visitors"] += 1
    return jsonify({"success": True, "visitors": METRICS["total_visitors"]}), 200

@app.route("/stripe-webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_json() or {}
    # Process live incoming payment events from Stripe
    amount = payload.get("data", {}).get("object", {}).get("amount_received", 0) / 100.0
    if amount > 0:
        METRICS["total_revenue"] += amount
        METRICS["active_transactions"] += 1
    return jsonify({"received": True, "revenue": METRICS["total_revenue"]}), 200

@app.route("/metrics", methods=["GET"])
def get_metrics():
    return jsonify(METRICS), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"[*] Starting Live Production Server on port {port}...")
    app.run(host="0.0.0.0", port=port)
