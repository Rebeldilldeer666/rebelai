import json
import os

# Sample category generator template for 415 products
categories = ["Software & AI", "Digital Wealth", "Art & Design", "Fitness & Health", "E-Commerce", "Marketing"]

print("⚡ Generating 415-Product Digistore24 Catalog Database...")

catalog = []
# Generating catalog structure for 415 products
for i in range(1, 416):
    category = categories[i % len(categories)]
    prod_id = 500000 + i
    catalog.append({
        "id": str(prod_id),
        "title": f"Digistore24 High-Converting Offer #{i} ({category})",
        "category": category,
        "estimated_payout": round(19.99 + (i * 0.45) % 150, 2)
    })

with open("digistore_catalog.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=4)

print(f"✅ Created digistore_catalog.json with {len(catalog)} active product entries!")
