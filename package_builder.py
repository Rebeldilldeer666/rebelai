import os, json, zipfile

def package_digital_product(product_name, files_dict, readme_content):
    build_dir = f"./build_{product_name.lower().replace(' ', '_')}"
    os.makedirs(build_dir, exist_ok=True)
    
    # Generate README.md
    with open(f"{build_dir}/README.md", "w") as f:
        f.write(readme_content)
        
    # Write product files
    for filename, content in files_dict.items():
        filepath = os.path.join(build_dir, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            f.write(content if isinstance(content, str) else json.dumps(content, indent=2))
            
    # Compress into distribution ZIP package
    zip_filename = f"{product_name.replace(' ', '_')}_Vault_Package.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(build_dir):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, build_dir)
                zipf.write(full_path, arcname)
                
    print(f"✅ Product Package Built Successfully: {zip_filename}")

if __name__ == "__main__":
    package_digital_product(
        product_name="Termux Automation Vault",
        files_dict={
            "config.json": {"version": "1.0.0", "status": "active"},
            "scripts/main.py": "print('Automated System Executing...')"
        },
        readme_content="# Termux Automation Starter Kit\n\n1. Run `python scripts/main.py`\n2. Configure your environment."
    )
