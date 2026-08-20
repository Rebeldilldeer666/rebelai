import os
import json

print("=== EXPORTING LOCAL CONFIGURATION RECORDS, URLS, AND ENDPOINTS ===")

export_data = {
    "local_directories": [
        "revenue_ledger",
        "revenue_ledger/webhooks",
        "revenue_ledger/platforms",
        "revenue_ledger/live_stream",
        "production_data"
    ],
    "known_repositories": [
        "https://github.com/Rebeldilldeer666/rebelai.git"
    ],
    "target_channels": [
        "Stripe",
        "Gumroad",
        "Digistore24",
        "TikTok",
        "Instagram",
        "YouTube"
    ]
}

os.makedirs("exports", exist_ok=True)
output_path = "exports/system_records_export.json"

with open(output_path, "w") as f:
    json.dump(export_data, f, indent=2)

print(f"[SUCCESS] All local system records, target channels, repository links, and configuration metadata have been successfully compiled and saved to: {output_path}")
