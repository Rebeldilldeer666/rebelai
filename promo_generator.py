import json, os

def generate_promos():
    json_path = 'master_revenue_output.json'
    items = []
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
                items = data.get('products', data.get('items', []))
        except Exception:
            pass

    print("\n" + "="*50)
    print("📲 REBEL AI — TIKTOK & SOCIAL PROMO GENERATOR")
    print("="*50)
    print("🔗 LIVE STORE LINK: https://rebelai-storefront.vercel.app\n")
    
    print("📌 TIKTOK BIO COPY:")
    print("🔥 Custom Stencils, Digital Products & Live Tech Deals")
    print("👇 Access the Full Storefront Below:")
    print("https://rebelai-storefront.vercel.app\n")
    
    print("💬 LIVE STREAM OVERLAY / PINNED CHAT PROMPTS:")
    print("• 'Tap bio link to browse our custom stencils & digital toolkits live!'")
    print("• 'Searching 400+ instant digital offers — Link in bio: https://rebelai-storefront.vercel.app'")
    
    if items:
        print("\n🔥 CURRENT FEATURED CATALOG ITEMS:")
        for idx, item in enumerate(items[:3], 1):
            name = item.get('name', item.get('title', f'Item #{idx}'))
            price = item.get('price', 'Featured')
            print(f"  {idx}. {name} — [{price}]")
    print("="*50 + "\n")

if __name__ == '__main__':
    generate_promos()
