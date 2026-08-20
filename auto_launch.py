import os, sys, subprocess, time, re, socket, threading

def sync_stripe_webhook(webhook_url):
    stripe_key = os.getenv("STRIPE_SECRET_KEY")
    if not stripe_key:
        print("  ⚠️ Stripe Secret Key missing in .env. Skipping automated Stripe update.")
        return
    try:
        import stripe
        stripe.api_key = stripe_key
        
        endpoints = stripe.WebhookEndpoint.list()
        target_endpoint = None
        for ep in endpoints.data:
            if "rebelai" in (ep.description or "").lower():
                target_endpoint = ep
                break

        if target_endpoint:
            stripe.WebhookEndpoint.modify(
                target_endpoint.id,
                url=webhook_url,
                enabled_events=["checkout.session.completed"]
            )
            print(f"✅ AUTO-SYNC: Updated existing Stripe Webhook ({target_endpoint.id}) -> {webhook_url}")
        else:
            new_ep = stripe.WebhookEndpoint.create(
                url=webhook_url,
                enabled_events=["checkout.session.completed"],
                description="RebelAI Automated Webhook Endpoint"
            )
            print(f"✅ AUTO-SYNC: Created new Stripe Webhook ({new_ep.id}) -> {webhook_url}")
    except Exception as e:
        print(f"  ❌ Auto-Stripe Sync Failed: {e}")

def find_free_port(starting_port=5001):
    for port in range(starting_port, starting_port + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return starting_port

def start_tunnel(port):
    time.sleep(3)
    try:
        proc = subprocess.Popen(
            ["cloudflared", "tunnel", "--url", f"http://127.0.0.1:{port}"],
            stderr=subprocess.PIPE, text=True
        )
        for _ in range(40):
            line = proc.stderr.readline()
            match = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line)
            if match:
                full_url = f"{match.group(0)}/webhook"
                print(f"\n✨ LIVE PUBLIC WEBHOOK URL: {full_url}\n")
                sync_stripe_webhook(full_url)
                break
            time.sleep(0.1)
    except Exception as e:
        print(f"  x Tunnel notice: {e}")

def setup_and_launch():
    print("🚀 --- STARTING ALL-IN-ONE REBEL AI LAUNCHER --- 🚀\n")

    subprocess.run(["pkill", "-9", "-f", "cloudflared"], stderr=subprocess.DEVNULL)
    subprocess.run(["fuser", "-k", "-9", "5000/tcp"], stderr=subprocess.DEVNULL)
    subprocess.run(["fuser", "-k", "-9", "5001/tcp"], stderr=subprocess.DEVNULL)
    time.sleep(2)

    if os.path.exists(".env"):
        from dotenv import load_dotenv
        load_dotenv()
    subprocess.run([sys.executable, "-m", "pip", "install", "flask", "requests", "stripe", "waitress", "python-dotenv", "--quiet"])

    subprocess.run([sys.executable, "rebelai_master_engine.py"])

    active_port = find_free_port(5001)
    print(f"\n🌐 Launching Webhook Server on Port {active_port}...")
    threading.Thread(target=start_tunnel, args=(active_port,), daemon=True).start()

    from waitress import serve
    from rebelai_master_engine import app
    serve(app, host="0.0.0.0", port=active_port)

if __name__ == "__main__":
    setup_and_launch()
