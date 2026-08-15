import os
import time
import json
import sys

sys.stdout.reconfigure(line_buffering=True)

CONFIG = {
    "loop_interval_seconds": 30,
    "output_dir": os.path.expanduser("~/termux_output"),
    "status_log": "engine_status.json",
    "asset_dir": os.path.expanduser("~/termux_output/assets")
}

def initialize_environment():
    for d in [CONFIG["output_dir"], CONFIG["asset_dir"]]:
        if not os.path.exists(d):
            os.makedirs(d)
    print("[+] Environment initialized. Asset generation pipeline hot.")

def generate_digital_asset():
    """Generates a high-value markdown micro-asset on each cycle."""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"asset_{timestamp}.md"
    filepath = os.path.join(CONFIG["asset_dir"], filename)
    
    content = f"""# Automated Micro-Asset #{timestamp}
* Generated via Termux Headless Node
* Status: Production Ready
* Target: High-value automation script template & system blueprint.
"""
    with open(filepath, "w") as f:
        f.write(content)
    return filename

def run_headless_cycle():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    asset_name = generate_digital_asset()
    
    payload = {
        "timestamp": timestamp,
        "status": "active_production",
        "last_generated_asset": asset_name,
        "node": "termux-mobile-daemon"
    }
    
    log_path = os.path.join(CONFIG["output_dir"], CONFIG["status_log"])
    with open(log_path, "w") as f:
        json.dump(payload, f, indent=4)
        
    print(f"[{timestamp}] Asset compiled & secured: {asset_name}")

if __name__ == "__main__":
    initialize_environment()
    while True:
        try:
            run_headless_cycle()
        except Exception as e:
            print(f"[!] Exception caught: {e}")
        time.sleep(CONFIG["loop_interval_seconds"])
