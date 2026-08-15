import json
import os

if not os.path.exists("master_revenue_output.json"):
    print("Error: master_revenue_output.json not found.")
    exit(1)

with open("master_revenue_output.json", "r") as f:
    data = json.load(f)

products = data.get("data", {}).get("digital_products", [])
affiliates = data.get("data", {}).get("affiliate_campaigns", [])

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>REBEL AI | Marketplace & 400+ Digital Offers</title>
    <style>
        body {{ background-color: #0d1117; color: #c9d1d9; font-family: system-ui, -apple-system, sans-serif; margin: 0; padding: 20px; }}
        h1 {{ color: #58a6ff; text-align: center; border-bottom: 2px solid #30363d; padding-bottom: 10px; }}
        .search-box {{ width: 100%; max-width: 600px; margin: 20px auto; display: block; padding: 12px 20px; border-radius: 25px; border: 1px solid #30363d; background: #161b22; color: white; font-size: 16px; outline: none; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 20px; }}
        .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 18px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }}
        .card h3 {{ color: #f0883e; margin-top: 5px; font-size: 1.1em; }}
        .price {{ font-size: 1.2em; color: #7ee787; font-weight: bold; margin: 8px 0; }}
        .tag {{ font-size: 0.75em; background: #21262d; color: #8b949e; padding: 3px 8px; border-radius: 12px; }}
        .btn {{ display: inline-block; padding: 8px 12px; border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 0.85em; text-align: center; margin-top: 10px; }}
        .btn-stripe {{ background: #635bff; color: white; margin-right: 5px; }}
        .btn-gumroad {{ background: #ff90e8; color: black; }}
        .btn-affiliate {{ background: #238636; color: white; width: 100%; box-sizing: border-box; }}
    </style>
    <script>
        function filterCatalog() {{
            let input = document.getElementById('search').value.toLowerCase();
            let cards = document.getElementsByClassName('card');
            for (let i = 0; i < cards.length; i++) {{
                let title = cards[i].innerText.toLowerCase();
                cards[i].style.display = title.includes(input) ? "" : "none";
            }}
        }}
    </script>
</head>
<body>
    <h1>🔥 REBEL AI MARKETPLACE & DIGITAL VAULT 🔥</h1>
    <input type="text" id="search" onkeyup="filterCatalog()" class="search-box" placeholder="🔎 Search 400+ products, courses, stencils, and tools...">

    <h2>📦 Staged Direct Products ({len(products)})</h2>
    <div class="grid">
"""

for p in products:
    html_content += f"""
        <div class="card">
            <span class="tag">{p['sku']} | {p['category']}</span>
            <h3>{p['title']}</h3>
            <div class="price">${p['price']}</div>
            <a href="{p['checkout_urls']['stripe']}" target="_blank" class="btn btn-stripe">Stripe</a>
            <a href="{p['checkout_urls']['gumroad']}" target="_blank" class="btn btn-gumroad">Gumroad</a>
        </div>
"""

html_content += f"""
    </div>
    <h2>⚡ Digistore24 Monetized Offers ({len(affiliates)})</h2>
    <div class="grid">
"""

for a in affiliates:
    cat_name = a.get('category', 'Affiliate Offer')
    html_content += f"""
        <div class="card">
            <span class="tag">{cat_name}</span>
            <h3>{a['product_name']}</h3>
            <div class="price">Est. Payout: ${a.get('est_commission', 25.00)}</div>
            <a href="{a['monetized_url']}" target="_blank" class="btn btn-affiliate">Access Deal Now</a>
        </div>
"""

html_content += """
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Web Storefront rebuilt with search bar and {len(products) + len(affiliates)} total live listings!")
