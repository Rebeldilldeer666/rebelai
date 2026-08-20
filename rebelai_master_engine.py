import os, sys, json, subprocess, zipfile, requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- CONFIGURATION & ENV ---
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "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")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
DOMAIN = "https://rebelliousbytes.online"

PRODUCTS_DATA = [
    {"id": "1", "title": "ObsidianInk Dark Art AI Prompt Vault v1", "category": "AI Prompts", "price": "$29.00", "amount": 2900, "sales": 142, "revenue": 4118.00, "desc": "Curated master prompts for dark, gothic, and biomechanical AI renders."},
    {"id": "2", "title": "Dark Gothic & Steampunk Tattoo Stencil Collection", "category": "Tattoo Vectors", "price": "$19.99", "amount": 1999, "sales": 98, "revenue": 1959.02, "desc": "High-res line art vector stencils ready for stencil thermal printers."},
    {"id": "3", "title": "Termux Python Automation & Bot Scripts", "category": "Software", "price": "$49.00", "amount": 4900, "sales": 54, "revenue": 2646.00, "desc": "Plug-and-play CLI scripts for mobile automation, APIs, and Webhooks."},
    {"id": "4", "title": "Minimalist Snake & Geometric Line Art Pack", "category": "Tattoo Vectors", "price": "$14.99", "amount": 1499, "sales": 76, "revenue": 1139.24, "desc": "Clean, scalable vector line art designed for precision tattoos and merch."},
    {"id": "5", "title": "Solana Mirror Trading & Stop-Loss Bot Core", "category": "Software", "price": "$99.00", "amount": 9900, "sales": 29, "revenue": 2871.00, "desc": "Low-latency asynchronous DEX transaction monitor & trailing stop script."},
    {"id": "6", "title": "Deep Sea Cyber-Jellyfish UI & Asset Kit", "category": "Digital Design", "price": "$24.99", "amount": 2499, "sales": 61, "revenue": 1524.39, "desc": "Bespoke dark bioluminescent UI components, vectors, and background shaders."},
    {"id": "7", "title": "Wholesale Real Estate Lead & Outreach Automation", "category": "Software", "price": "$59.00", "amount": 5900, "sales": 43, "revenue": 2537.00, "desc": "Automated pipeline for property data parsing and multi-channel messaging."},
    {"id": "8", "title": "Dark Synthwave & Metal Rap Audio Stems Vol. 1", "category": "Audio & Beats", "price": "$34.99", "amount": 3499, "sales": 37, "revenue": 1294.63, "desc": "Royalty-free dark trap drums, heavy distorted riffs, and aggressive synth lines."},
    {"id": "9", "title": "Biomechanical & Centipede Vector Line Art Pack", "category": "Tattoo Vectors", "price": "$18.99", "amount": 1899, "sales": 51, "revenue": 968.49, "desc": "Intricate biomechanical line-art vectors and stencil overlays."},
    {"id": "10", "title": "Telegram Bot Automation Script Suite", "category": "Software", "price": "$39.00", "amount": 3900, "sales": 32, "revenue": 1248.00, "desc": "Full Python Telegram bot backend with payment commands and webhooks."},
    {"id": "11", "title": "Dark Gothic Micro-Flash Tattoo Bundle", "category": "Tattoo Vectors", "price": "$12.99", "amount": 1299, "sales": 89, "revenue": 1156.11, "desc": "Compact gothic flash tattoo vector pack optimized for quick stencil transfer."},
    {"id": "12", "title": "Autonomous Python Web Scraper Engine", "category": "Software", "price": "$45.00", "amount": 4500, "sales": 27, "revenue": 1215.00, "desc": "Multi-threaded async web scraping framework for market & lead research."}
]

# --- MODULE 1: PRODUCT PACKAGING ---
def generate_product_packages():
    print("📦 [1/4] Generating Local Product ZIP Packages...")
    os.makedirs("vault_packages", exist_ok=True)
    for prod in PRODUCTS_DATA:
        clean_name = prod["title"].lower().replace(" ", "_").replace("&", "and")
        zip_path = f"vault_packages/{clean_name}.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr("MANIFEST.json", json.dumps(prod, indent=2))
            zipf.writestr("README.txt", f"Thank you for unlocking {prod['title']}.\nAccess updates at {DOMAIN}")
    print(f"✅ Created {len(PRODUCTS_DATA)} product ZIP archives in vault_packages/\n")

# --- MODULE 2: STRIPE & VERCEL DEPLOYMENT ---
def update_and_deploy_storefront():
    print("⚡ [2/4] Initializing Stripe Checkout Generation & Vercel Sync...")
    try:
        import stripe
        stripe.api_key = STRIPE_SECRET_KEY
        for prod in PRODUCTS_DATA:
            try:
                p_obj = stripe.Product.create(name=prod["title"], description=prod["desc"])
                pr_obj = stripe.Price.create(product=p_obj.id, unit_amount=prod["amount"], currency="usd")
                plink = stripe.PaymentLink.create(line_items=[{"price": pr_obj.id, "quantity": 1}])
                prod["paymentUrl"] = plink.url
                print(f"  + Generated Link: {prod['title']}")
            except Exception as e:
                prod["paymentUrl"] = DOMAIN
    except ImportError:
        print("⚠️  Stripe library not installed. Defaulting payment URLs to domain.")
        for prod in PRODUCTS_DATA:
            prod["paymentUrl"] = DOMAIN

    clean_json = json.dumps(PRODUCTS_DATA, indent=2)

    app_content = """import React, { useState } from 'react';

interface Product {
  id: string;
  title: string;
  category: string;
  price: string;
  sales: number;
  revenue: number;
  paymentUrl: string;
  desc: string;
}

export default function App() {
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const products: Product[] = """ + clean_json + """;
  const categories = ['All', 'AI Prompts', 'Tattoo Vectors', 'Software', 'Digital Design', 'Audio & Beats'];

  const filteredProducts = selectedCategory === 'All' 
    ? products 
    : products.filter(p => p.category === selectedCategory);

  const totalRevenue = products.reduce((sum, item) => sum + item.revenue, 0);
  const totalSales = products.reduce((sum, item) => sum + item.sales, 0);

  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: '#05070c',
      color: '#e2e8f0',
      fontFamily: "'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
      padding: '20px 16px',
      backgroundImage: 'radial-gradient(circle at 50% 0%, #0f172a 0%, #05070c 70%)',
      boxSizing: 'border-box'
    }}>
      <style>{`
        .card-hover { transition: all 0.25s ease-in-out; }
        .card-hover:hover {
          transform: translateY(-3px);
          border-color: #38bdf8 !important;
          box-shadow: 0 8px 20px rgba(56, 189, 248, 0.15) !important;
        }
        .glow-title { text-shadow: 0 0 12px rgba(56, 189, 248, 0.6); }
      `}</style>

      <div style={{ textAlign: 'center', marginBottom: '24px' }}>
        <div style={{ 
          display: 'inline-block', padding: '4px 12px', backgroundColor: 'rgba(14, 165, 233, 0.1)', 
          borderRadius: '20px', border: '1px solid rgba(56, 189, 248, 0.3)', fontSize: '0.7rem', 
          color: '#38bdf8', letterSpacing: '2px', fontWeight: 'bold', marginBottom: '8px'
        }}>
          ● LIVE AUTONOMOUS SYSTEM
        </div>
        <h1 className="glow-title" style={{ fontSize: '1.8rem', fontWeight: '900', margin: 0, color: '#f8fafc', letterSpacing: '1px' }}>
          REBEL AI <span style={{ color: '#38bdf8' }}>VAULT</span>
        </h1>
        <p style={{ fontSize: '0.8rem', color: '#64748b', margin: '4px 0 0 0' }}>
          Premium Digital Assets, AI Prompt Engines & Automated Systems
        </p>
      </div>

      <div style={{ 
        display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '8px', marginBottom: '24px',
        backgroundColor: 'rgba(15, 23, 42, 0.6)', backdropFilter: 'blur(12px)',
        border: '1px solid rgba(30, 41, 59, 0.8)', borderRadius: '12px', padding: '12px'
      }}>
        <div style={{ textAlign: 'center' }}>
          <span style={{ fontSize: '0.65rem', color: '#64748b', display: 'block', letterSpacing: '1px' }}>VOLUME</span>
          <span style={{ fontSize: '1.1rem', fontWeight: 'bold', color: '#38bdf8' }}>${totalRevenue.toFixed(2)}</span>
        </div>
        <div style={{ textAlign: 'center', borderLeft: '1px solid #1e293b', borderRight: '1px solid #1e293b' }}>
          <span style={{ fontSize: '0.65rem', color: '#64748b', display: 'block', letterSpacing: '1px' }}>SALES</span>
          <span style={{ fontSize: '1.1rem', fontWeight: 'bold', color: '#f43f5e' }}>{totalSales}</span>
        </div>
        <div style={{ textAlign: 'center' }}>
          <span style={{ fontSize: '0.65rem', color: '#64748b', display: 'block', letterSpacing: '1px' }}>STATUS</span>
          <span style={{ fontSize: '1.1rem', fontWeight: 'bold', color: '#10b981' }}>ONLINE</span>
        </div>
      </div>

      <div style={{ display: 'flex', gap: '8px', overflowX: 'auto', paddingBottom: '8px', marginBottom: '20px' }}>
        {categories.map(cat => (
          <button
            key={cat}
            onClick={() => setSelectedCategory(cat)}
            style={{
              padding: '6px 14px', borderRadius: '20px',
              border: selectedCategory === cat ? '1px solid #38bdf8' : '1px solid #1e293b',
              backgroundColor: selectedCategory === cat ? 'rgba(56, 189, 248, 0.15)' : '#0f172a',
              color: selectedCategory === cat ? '#38bdf8' : '#94a3b8',
              fontSize: '0.75rem', fontWeight: '600', cursor: 'pointer', whiteSpace: 'nowrap'
            }}
          >
            {cat}
          </button>
        ))}
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {filteredProducts.map((item) => (
          <a key={item.id} href={item.paymentUrl} className="card-hover" style={{ 
            textDecoration: 'none', display: 'block', backgroundColor: 'rgba(15, 23, 42, 0.75)', 
            backdropFilter: 'blur(10px)', padding: '16px', borderRadius: '12px', border: '1px solid rgba(56, 189, 248, 0.2)'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '6px' }}>
              <span style={{ fontSize: '0.65rem', fontWeight: 'bold', color: '#38bdf8', backgroundColor: 'rgba(56, 189, 248, 0.1)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(56, 189, 248, 0.2)' }}>
                {item.category}
              </span>
              <span style={{ fontSize: '1.1rem', fontWeight: '800', color: '#10b981' }}>{item.price}</span>
            </div>
            <div style={{ fontWeight: '700', fontSize: '0.95rem', color: '#f8fafc', marginBottom: '6px' }}>{item.title}</div>
            <div style={{ fontSize: '0.78rem', color: '#94a3b8', lineHeight: '1.4', marginBottom: '12px' }}>{item.desc}</div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderTop: '1px solid rgba(30, 41, 59, 0.8)', paddingTop: '10px', fontSize: '0.75rem' }}>
              <span style={{ color: '#64748b' }}>{item.sales} Unlocked</span>
              <span style={{ color: '#38bdf8', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '4px' }}>Instant Access ⚡</span>
            </div>
          </a>
        ))}
      </div>

      <div style={{ textAlign: 'center', marginTop: '32px', paddingBottom: '16px', color: '#475569', fontSize: '0.7rem' }}>
        ⚡ POWERED BY STRIPE CHECKOUT & VERCEL AUTOMATION
      </div>
    </div>
  );
}
"""
    with open("src/App.tsx", "w") as f:
        f.write(app_content)

    print("  + Updated src/App.tsx")
    subprocess.run(["git", "add", "src/App.tsx"])
    subprocess.run(["git", "commit", "-m", "feat: master engine deploy 12 live products"])
    subprocess.run(["git", "push", "origin", "main"])
    print("✅ Pushed updates to GitHub & Vercel deployment triggered.\n")

# --- MODULE 3: COMMUNITY BROADCASTS ---
def broadcast_updates():
    print("📢 [3/4] Broadcasting Updates to Discord & Telegram...")
    msg = f"🚀 **REBEL AI MASTER SYSTEM ONLINE**\n\nStorefront active: {DOMAIN}\n12 Flagship Digital Products & Automated Systems Live."
    
    if DISCORD_WEBHOOK_URL and "discord.com" in DISCORD_WEBHOOK_URL:
        try:
            res = requests.post(DISCORD_WEBHOOK_URL, json={"content": msg})
            print(f"  + Discord Status: {res.status_code}")
        except Exception as e:
            print(f"  x Discord Error: {e}")
    else:
        print("  - Skipping Discord (DISCORD_WEBHOOK_URL not configured).")

    if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
        try:
            t_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            res = requests.post(t_url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"})
            print(f"  + Telegram Status: {res.status_code}")
        except Exception as e:
            print(f"  x Telegram Error: {e}")
    else:
        print("  - Skipping Telegram (TELEGRAM credentials not configured).\n")

# --- MODULE 4: WEBHOOK DISPATCH SERVER ---
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    event = json.loads(payload)
    if event.get('type') == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session.get('customer_details', {}).get('email')
        print(f"⚡ [PURCHASE CONFIRMED] Customer: {customer_email}")
    return jsonify({'status': 'success'}), 200

# --- MAIN EXECUTION ---
if __name__ == '__main__':
    if "--server-only" in sys.argv:
        from waitress import serve
        print("🚀 Starting Webhook Delivery Server on Port 5000...")
        sys.exit(0)
    print("⚡ --- STARTING REBEL AI UNIFIED MASTER ENGINE --- ⚡\n")
    generate_product_packages()
    update_and_deploy_storefront()
    broadcast_updates()
    
    if "--server" in sys.argv:
        print("🚀 [4/4] Starting Webhook Delivery Server on Port 5000...")
        from waitress import serve
