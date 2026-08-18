import sys
import json
import urllib.parse

sys.stdout.reconfigure(line_buffering=True)

def analyze_and_report(target_url):
    print(f"[-] Analyzing target infrastructure: {target_url}")
    parsed_url = urllib.parse.urlparse(target_url)
    domain = parsed_url.netloc
    
    if not domain:
        print("[!] Invalid URL structure provided.")
        return

    # Identify hosting provider signature
    provider = "Unknown"
    abuse_contact = "security@target-host.com"
    
    if "vercel.app" in domain:
        provider = "Vercel"
        abuse_contact = "abuse@vercel.com"
    elif "netlify.app" in domain:
        provider = "Netlify"
        abuse_contact = "abuse@netlify.com"
    elif "github.io" in domain:
        provider = "GitHub"
        abuse_contact = "support@github.com"

    print(f"[+] Host identified: {provider} | Root Domain: {domain}")
    
    # Generate the compliance takedown payload packet
    incident_report = {
        "target_domain": domain,
        "full_url": target_url,
        "hosting_provider": provider,
        "designated_abuse_email": abuse_contact,
        "violation_type": "Phishing / Brand Impersonation / Deceptive Content",
        "action_required": "Immediate Account Suspension and Domain Revocation"
    }
    
    print("\n--- OFFICIAL ABUSE REPORT PAYLOAD ---")
    print(json.dumps(incident_report, indent=4))
    print("---------------------------------------")
    print(f"[✓] Package compiled. Forward this telemetry to {abuse_contact} for rapid takedown.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        analyze_and_report(target)
    else:
        print("Usage: python3 disruptor.py <suspicious_url>")
