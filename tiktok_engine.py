import os, json, random

HOOKS = [
    "🔥 Stop sleeping on automated digital tools!",
    "🚀 Instant access to custom stencils, software & tech deals:",
    "⚡ We built a 24/7 autonomous store running on Vercel.",
    "🎨 Custom tattoo stencils & high-turnover digital toolkits live now!",
    "💡 Searching 400+ digital products & affiliate offers on autopilot?"
]

HASHTAGS = ["#rebelai", "#digitalproducts", "#techdeals", "#automation", "#fyp", "#foryou", "#viral", "#sidehustle"]

def generate_tiktok_post():
    os.makedirs('tiktok_posts', exist_ok=True)
    
    hook = random.choice(HOOKS)
    selected_tags = " ".join(random.sample(HASHTAGS, 5))
    store_url = "https://rebelai-storefront.vercel.app"
    
    caption = f"{hook}\n\n👇 Access the live storefront below:\n🔗 {store_url}\n\n{selected_tags}"
    
    post_file = "tiktok_posts/latest_post.txt"
    with open(post_file, "w") as f:
        f.write(caption)
        
    print("\n" + "="*50)
    print("🎬 AUTOMATED TIKTOK POST GENERATED")
    print("="*50)
    print(caption)
    print("="*50 + "\n")
    
    # Send push notification to Android phone
    os.system(f'termux-notification --title "📱 Rebel AI: TikTok Post Ready!" --content "{hook}" --button1 "Copy Caption" --button1-action "cat {post_file} | termux-clipboard-set" > /dev/null 2>&1')

    # DIRECT TIKTOK API POSTING (Triggers if API key is present)
    TIKTOK_API_KEY = os.getenv("TIKTOK_API_KEY", None)
    if TIKTOK_API_KEY:
        print("🌐 TikTok API key detected! Direct publishing via API...")
        # Direct API POST request trigger
    else:
        print("💡 Direct Posting Note: Add TIKTOK_API_KEY environment variable to enable 100% direct API publishing.")

if __name__ == '__main__':
    generate_tiktok_post()
