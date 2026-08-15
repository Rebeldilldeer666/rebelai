#!/bin/bash
echo "🔄 [1/5] Running Content & Revenue Engine..."
if [ -f "content_engine.py" ]; then
    python content_engine.py || true
fi
if [ -f "app.py" ]; then
    python app.py || true
fi

echo "📊 [2/5] Generating Real-Time Analytics Interface..."
python analytics.py

echo "🚀 [3/5] Auto-Deploying Storefront & Analytics to Vercel..."
npx vercel --prod --yes

echo "🎬 [4/5] Running TikTok Traffic Engine..."
python tiktok_engine.py

echo "📲 [5/5] Refreshing Social Promo Output..."
python promo_generator.py
