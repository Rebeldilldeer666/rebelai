import json

niches = [
    {
        "category": "AI & Automation Tools",
        "templates": [
            ("Auto-Publishing Python Engine v{}", "⚡ Automate multi-channel social distribution 24/7 on autopilot. Includes turnkey Python scripts."),
            ("AI Prompt Master Suite #{}", "🔥 Unleash 500+ elite system prompts engineered for high-converting marketing & copywriting."),
            ("Web Scraping & Lead Harvester #{}", "🚀 Extract high-intent commercial leads automatically with clean Python scrapers.")
        ]
    },
    {
        "category": "Digital Revenue Blueprints",
        "templates": [
            ("Passive Digital Store Blueprint v{}", "💡 Turn turnkey digital downloads into round-the-clock sales across Gumroad and Digistore24."),
            ("Virtual Asset & Real Estate Tracker #{}", "🏢 Streamline property research, land records, and deal management on autopilot."),
            ("Micro-SaaS & Code Sales Playbook #{}", "📈 Learn how to package, price, and distribute custom automation code for maximum recurring revenue.")
        ]
    },
    {
        "category": "Viral Content & Growth Engines",
        "templates": [
            ("Multi-Channel Viral Hook Vault #{}", "🎯 Over 200 high-converting hooks and post frameworks designed to drive organic traffic."),
            ("Automated Telegram & Social Content System #{}", "🤖 Deploy scheduled post loops across Telegram, Facebook, and Webhooks seamlessly."),
            ("Short-Form Video & Carousel Creator Kit #{}", "📱 Ready-to-use graphics and structured layouts for high-engagement social feeds.")
        ]
    },
    {
        "category": "Developer & Tech Starter Kits",
        "templates": [
            ("Termux Automation Environment Starter #{}", "⚙️ Complete mobile command-line setup for background Python scripts and API integrations."),
            ("REST API Integration Template Suite #{}", "🔌 Pre-built headers, error-handling, and JSON payloads for fast platform connections."),
            ("Full-Stack Dashboard Deployment Kit #{}", "💻 Deploy clean administrative control panels and web storefronts on Vercel instantly.")
        ]
    },
    {
        "category": "High-Performance Productivity",
        "templates": [
            ("Master Operations & Automation Dashboard #{}", "📊 Track system output, automated dispatches, and sales pipelines in one unified view."),
            ("Digital Asset & File Management Vault #{}", "📂 Organize codebase files, environment variables, and store configurations efficiently."),
            ("24/7 Revenue & Workflow Execution Matrix #{}", "🧠 Frameworks to automate repetitive tasks and focus 100% on high-leverage digital strategy.")
        ]
    }
]

catalog = []
product_counter = 1

while product_counter <= 100:
    for niche in niches:
        if product_counter > 100:
            break
        category_name = niche["category"]
        template_title, template_desc = niche["templates"][(product_counter - 1) % len(niche["templates"])]
        
        item_id = f"prod_{product_counter:03d}"
        title = template_title.format(product_counter)
        desc = template_desc.format(product_counter)
        
        catalog.append({
            "id": item_id,
            "category": category_name,
            "title": title,
            "text": f"{desc}\n\n👉 Download Now: https://rebelai.store",
            "url": "https://rebelai.store",
            "image": f"https://picsum.photos/id/{(product_counter % 50) + 1}/800/800"
        })
        product_counter += 1

with open("products.json", "w") as f:
    json.dump(catalog, f, indent=2)

print(f"✅ Success! Created {len(catalog)} digital products in products.json across 5 top niches.")
