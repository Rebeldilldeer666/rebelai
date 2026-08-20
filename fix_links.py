import re, subprocess

with open("src/App.tsx", "r") as f:
    code = f.read()

# Replace handleBuy function logic to use window.open directly
new_code = code.replace(
    "window.location.href = url;",
    "window.open(url, '_self');"
)

with open("src/App.tsx", "w") as f:
    f.write(new_code)

print("Updated link click handlers in src/App.tsx")

subprocess.run(["git", "add", "src/App.tsx"])
subprocess.run(["git", "commit", "-m", "fix: enforce direct window.open redirection for storefront links"])
subprocess.run(["git", "push", "origin", "main"])

print("Fix deployed to GitHub!")
