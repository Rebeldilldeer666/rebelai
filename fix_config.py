import json, subprocess

# Ensure package.json has required scripts and dependencies
pkg = {
  "name": "rebelai",
  "private": True,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^4.3.1",
    "typescript": "^5.5.3",
    "vite": "^5.4.1"
  }
}

with open("package.json", "w") as f:
    json.dump(pkg, f, indent=2)

# Ensure vite.config.ts is clean
vite_config = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})
"""

with open("vite.config.ts", "w") as f:
    f.write(vite_config)

subprocess.run(["git", "add", "package.json", "vite.config.ts"])
subprocess.run(["git", "commit", "-m", "fix: standardize package.json and vite.config.ts for Vercel"])
subprocess.run(["git", "push", "origin", "main"])

print("Build configuration pushed to GitHub!")
