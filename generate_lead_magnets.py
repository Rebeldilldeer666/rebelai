import os, json, zipfile

lead_magnets = [
    {"name": "Free Dark Art Prompt Sampler Pack", "file": "prompts.json", "data": {"prompts": ["cyberpunk biomechanical snake --ar 16:9", "gothic crow skull vector stencil"]}},
    {"name": "Free Steampunk Tattoo Stencil Sampler", "file": "stencil_info.txt", "data": "High-res line art vector samples for thermal stencil printing."},
    {"name": "Free Termux Utility Starter Script", "file": "starter.py", "data": "print('Termux Environment Verified')" },
    {"name": "Free Minimalist Geometric Vector Pack", "file": "vectors.json", "data": {"type": "SVG line art elements"}},
    {"name": "Free Solana Wallet Tracking Checklist", "file": "checklist.md", "data": "# Solana Bot Setup Guide\n1. RPC Endpoint\n2. Wallet Config"},
    {"name": "Free Cyber-Jellyfish UI Preview Kit", "file": "ui_kit.json", "data": {"color_palette": ["#05070c", "#38bdf8", "#f43f5e"]}},
    {"name": "Free Wholesale Real Estate Cold Text Template", "file": "templates.txt", "data": "Hey [Name], interested in an all-cash offer for [Address]?"},
    {"name": "Free Metal Rap Drum Loop Sampler", "file": "audio_info.txt", "data": "140 BPM Heavy Trap & Metal Drums (WAV Preview)"},
    {"name": "Free AI Image Upscaling Master Guide", "file": "guide.md", "data": "# AI Upscaling Workflow\nBest parameters for high-dpi print."},
    {"name": "Free Python CLI Automation Snippets", "file": "snippets.py", "data": "# Essential Termux Automation Snippets"}
]

os.makedirs("lead_magnets_out", exist_ok=True)

for item in lead_magnets:
    clean_name = item["name"].lower().replace(" ", "_")
    zip_path = f"lead_magnets_out/{clean_name}.zip"
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        content = json.dumps(item["data"], indent=2) if isinstance(item["data"], (dict, list)) else item["data"]
        zipf.writestr(item["file"], content)
        zipf.writestr("README.txt", f"Thank you for downloading {item['name']}!\nVisit https://rebelliousbytes.online for full packages.")
        
    print(f"⚡ Generated Lead Magnet: {zip_path}")

print("\nAll 10 Lead Magnets packaged in lead_magnets_out/")
