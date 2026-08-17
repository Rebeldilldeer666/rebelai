import os
from flask import Flask, render_template_string, request, jsonify
import stripe

app = Flask(__name__)
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_live_placeholder")
WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_placeholder")

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Rebel AI | Autopilot Command Center</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-deep: #030712;
            --bg-card: rgba(15, 23, 42, 0.75);
            --accent-cyan: #38bdf8;
            --accent-purple: #818cf8;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-glow: rgba(56, 189, 248, 0.3);
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background-color: var(--bg-deep); color: var(--text-main);
            font-family: 'Inter', sans-serif; min-height: 100vh;
            display: flex; flex-direction: column; align-items: center;
            background-image: radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.08) 0%, transparent 50%);
            padding: 2rem 1rem;
        }
        .container { width: 100%; max-width: 1200px; margin: 0 auto; }
        .header {
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 2.5rem; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 1.5rem;
            flex-wrap: wrap; gap: 1rem;
        }
        .logo-area h1 { font-family: 'Space Grotesk', sans-serif; font-size: 1.8rem; font-weight: 700; color: #f8fafc; }
        .logo-area p { color: var(--text-muted); font-size: 0.85rem; }
        .badge {
            display: inline-flex; align-items: center; gap: 0.5rem;
            background: rgba(56, 189, 248, 0.1); border: 1px solid var(--border-glow);
            padding: 0.35rem 1rem; border-radius: 9999px; font-size: 0.75rem;
            font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--accent-cyan);
        }
        .badge-dot { width: 6px; height: 6px; background-color: var(--accent-cyan); border-radius: 50%; box-shadow: 0 0 8px var(--accent-cyan); animation: pulse 2s infinite; }
        
        .metrics-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; margin-bottom: 2.5rem; }
        .metric-card {
            background: var(--bg-card); backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 1rem; padding: 1.5rem;
            box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);
        }
        .metric-card h3 { color: var(--text-muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem; }
        .metric-card .value { font-family: 'Space Grotesk', sans-serif; font-size: 2.2rem; font-weight: 700; color: var(--accent-cyan); }
        
        .section-title { font-family: 'Space Grotesk', sans-serif; font-size: 1.3rem; font-weight: 600; margin-bottom: 1.2rem; color: #f8fafc; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; margin-bottom: 3rem; }
        .card {
            background: var(--bg-card); backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 1.25rem;
            padding: 2.5rem 2rem; display: flex; flex-direction: column; justify-content: space-between;
            transition: all 0.3s ease;
        }
        .card:hover { transform: translateY(-4px); border-color: var(--border-glow); box-shadow: 0 20px 40px -15px rgba(56, 189, 248, 0.15); }
        .card.featured { border: 1px solid var(--accent-cyan); background: linear-gradient(180deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.9) 100%); }
        .card h2 { font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; font-weight: 700; margin-bottom: 0.5rem; color: #f8fafc; }
        .card p { color: var(--text-muted); font-size: 0.9rem; line-height: 1.5; margin-bottom: 1.5rem; }
        .price { font-family: 'Space Grotesk', sans-serif; font-size: 2.5rem; font-weight: 700; color: var(--accent-cyan); margin-bottom: 1.5rem; }
        .btn {
            display: flex; align-items: center; justify-content: center; width: 100%;
            background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%); color: white;
            padding: 0.85rem 1.5rem; border-radius: 0.75rem; text-decoration: none;
            font-weight: 600; font-size: 0.9rem; box-shadow: 0 4px 14px rgba(14, 165, 233, 0.4); border: none; cursor: pointer;
            transition: filter 0.2s;
        }
        .card.featured .btn { background: linear-gradient(135deg, #38bdf8 0%, #0ea5e9 100%); color: #030712; }
        .btn:hover { filter: brightness(1.1); }
        .footer { text-align: center; color: var(--text-muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 3rem; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 1.5rem; }
        @keyframes pulse { 0% { transform: scale(0.95); opacity: 0.8; } 50% { transform: scale(1.15); opacity: 1; box-shadow: 0 0 12px var(--accent-cyan); } 100% { transform: scale(0.95); opacity: 0.8; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo-area">
                <h1>Rebel AI Command Center</h1>
                <p>Autonomous Digital Pipeline &bull; Zero-Touch Revenue Engine</p>
            </div>
            <div class="badge">
                <span class="badge-dot"></span>
                Autopilot Active
            </div>
        </div>

        <div class="metrics-grid">
            <div class="metric-card">
                <h3>Pipeline Status</h3>
                <div class="value" style="font-size: 1.5rem; margin-top: 0.3rem; color: #34d399;">ONLINE</div>
            </div>
            <div class="metric-card">
                <h3>Target Progress</h3>
                <div class="value">$0 / $1K</div>
            </div>
            <div class="metric-card">
                <h3>Active Webhook Hub</h3>
                <div class="value" style="font-size: 1.5rem; margin-top: 0.3rem; color: #818cf8;">CONNECTED</div>
            </div>
        </div>

        <div class="section-title">Storefront Product Catalog</div>
        <div class="grid">
            <div class="card">
                <div>
                    <h2>Starter Script Pack</h2>
                    <p>Essential mobile automation templates and configuration files to build your foundation.</p>
                </div>
                <div>
                    <div class="price">$27</div>
                    <a href="/checkout?tier=starter" class="btn">Deploy Starter</a>
                </div>
            </div>

            <div class="card featured">
                <div>
                    <h2>Elite Access Bundle</h2>
                    <p>Complete Rebel AI workflow suite, multi-pillar content engines, and real-time revenue trackers.</p>
                </div>
                <div>
                    <div class="price">$97</div>
                    <a href="/checkout?tier=elite" class="btn">Instant Access</a>
                </div>
            </div>

            <div class="card">
                <div>
                    <h2>Custom Deployment</h2>
                    <p>Full hands-on setup, custom logic integration, priority routing, and dedicated scaling support.</p>
                </div>
                <div>
                    <div class="price">$297</div>
                    <a href="/checkout?tier=custom" class="btn">Secure Slot</a>
                </div>
            </div>
        </div>

        <div class="footer">
            Secured via Stripe Webhooks &bull; Rebel AI Systems &copy; 2026
        </div>
    </div>
</body>
</html>
"""

TIERS = {
    'starter': {'name': 'Rebel AI Starter Pack', 'amount': 2700},
    'elite': {'name': 'Rebel AI Elite Access Bundle', 'amount': 9700},
    'custom': {'name': 'Rebel AI Custom Deployment', 'amount': 29700}
}

@app.route('/')
def home():
    return render_template_string(DASHBOARD_HTML)

@app.route('/checkout')
def checkout():
    tier = request.args.get('tier', 'elite')
    product = TIERS.get(tier, TIERS['elite'])
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': product['name']},
                    'unit_amount': product['amount'],
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://rebelai.store/success',
            cancel_url='https://rebelai.store/cancel',
        )
        return jsonify({"checkout_url": session.url})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(f"[+] Automated Fulfillment Triggered for Session: {session.get('id')}")
    return jsonify({'status': 'success'}), 200

@app.route('/success')
def success():
    return "<h1>Payment Successful! Welcome to Rebel AI. Your automated assets are on the way.</h1>"

@app.route('/cancel')
def cancel():
    return "<h1>Checkout Cancelled.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
