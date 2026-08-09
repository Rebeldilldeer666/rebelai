import React, { useState } from 'react';

interface Product {
  id: string;
  title: string;
  category: string;
  price: string;
  sales: number;
  revenue: number;
  paymentUrl: string;
  desc: string;
}

export default function App() {
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const products: Product[] = [
  {
    "id": "1",
    "title": "ObsidianInk Dark Art AI Prompt Vault v1",
    "category": "AI Prompts",
    "price": "$29.00",
    "amount": 2900,
    "sales": 142,
    "revenue": 4118.0,
    "desc": "Curated master prompts for dark, gothic, and biomechanical AI renders.",
    "paymentUrl": "https://buy.stripe.com/6oU7sLeMk115500cG718c1B"
  },
  {
    "id": "2",
    "title": "Dark Gothic & Steampunk Tattoo Stencil Collection",
    "category": "Tattoo Vectors",
    "price": "$19.99",
    "amount": 1999,
    "sales": 98,
    "revenue": 1959.02,
    "desc": "High-res line art vector stencils ready for stencil thermal printers.",
    "paymentUrl": "https://buy.stripe.com/14AcN58nW2596445dF18c1C"
  },
  {
    "id": "3",
    "title": "Termux Python Automation & Bot Scripts",
    "category": "Software",
    "price": "$49.00",
    "amount": 4900,
    "sales": 54,
    "revenue": 2646.0,
    "desc": "Plug-and-play CLI scripts for mobile automation, APIs, and Webhooks.",
    "paymentUrl": "https://buy.stripe.com/4gM28r47GfVZ2RSdKb18c1D"
  },
  {
    "id": "4",
    "title": "Minimalist Snake & Geometric Line Art Pack",
    "category": "Tattoo Vectors",
    "price": "$14.99",
    "amount": 1499,
    "sales": 76,
    "revenue": 1139.24,
    "desc": "Clean, scalable vector line art designed for precision tattoos and merch.",
    "paymentUrl": "https://buy.stripe.com/8x26oHgUs7ptgIIdKb18c1E"
  },
  {
    "id": "5",
    "title": "Solana Mirror Trading & Stop-Loss Bot Core",
    "category": "Software",
    "price": "$99.00",
    "amount": 9900,
    "sales": 29,
    "revenue": 2871.0,
    "desc": "Low-latency asynchronous DEX transaction monitor & trailing stop script.",
    "paymentUrl": "https://buy.stripe.com/bJe28r0Vu7pt2RSeOf18c1F"
  },
  {
    "id": "6",
    "title": "Deep Sea Cyber-Jellyfish UI & Asset Kit",
    "category": "Digital Design",
    "price": "$24.99",
    "amount": 2499,
    "sales": 61,
    "revenue": 1524.39,
    "desc": "Bespoke dark bioluminescent UI components, vectors, and background shaders.",
    "paymentUrl": "https://buy.stripe.com/cNi00j6fO6lpfEEgWn18c1G"
  },
  {
    "id": "7",
    "title": "Wholesale Real Estate Lead & Outreach Automation",
    "category": "Software",
    "price": "$59.00",
    "amount": 5900,
    "sales": 43,
    "revenue": 2537.0,
    "desc": "Automated pipeline for property data parsing and multi-channel messaging.",
    "paymentUrl": "https://buy.stripe.com/3cI14naw4fVZ9ggfSj18c1H"
  },
  {
    "id": "8",
    "title": "Dark Synthwave & Metal Rap Audio Stems Vol. 1",
    "category": "Audio & Beats",
    "price": "$34.99",
    "amount": 3499,
    "sales": 37,
    "revenue": 1294.63,
    "desc": "Royalty-free dark trap drums, heavy distorted riffs, and aggressive synth lines.",
    "paymentUrl": "https://buy.stripe.com/bJe3cv6fO9xB1NO5dF18c1I"
  },
  {
    "id": "9",
    "title": "Biomechanical & Centipede Vector Line Art Pack",
    "category": "Tattoo Vectors",
    "price": "$18.99",
    "amount": 1899,
    "sales": 51,
    "revenue": 968.49,
    "desc": "Intricate biomechanical line-art vectors and stencil overlays.",
    "paymentUrl": "https://buy.stripe.com/eVq14n7jS1151NO6hJ18c1J"
  },
  {
    "id": "10",
    "title": "Telegram Bot Automation Script Suite",
    "category": "Software",
    "price": "$39.00",
    "amount": 3900,
    "sales": 32,
    "revenue": 1248.0,
    "desc": "Full Python Telegram bot backend with payment commands and webhooks.",
    "paymentUrl": "https://buy.stripe.com/4gM6oHaw4dNR2RS21t18c1K"
  },
  {
    "id": "11",
    "title": "Dark Gothic Micro-Flash Tattoo Bundle",
    "category": "Tattoo Vectors",
    "price": "$12.99",
    "amount": 1299,
    "sales": 89,
    "revenue": 1156.11,
    "desc": "Compact gothic flash tattoo vector pack optimized for quick stencil transfer.",
    "paymentUrl": "https://buy.stripe.com/aFa28r7jSfVZakk9tV18c1L"
  },
  {
    "id": "12",
    "title": "Autonomous Python Web Scraper Engine",
    "category": "Software",
    "price": "$45.00",
    "amount": 4500,
    "sales": 27,
    "revenue": 1215.0,
    "desc": "Multi-threaded async web scraping framework for market & lead research.",
    "paymentUrl": "https://buy.stripe.com/9B68wP8nWeRVgII9tV18c1M"
  }
];
  const categories = ['All', 'AI Prompts', 'Tattoo Vectors', 'Software', 'Digital Design', 'Audio & Beats'];

  const filteredProducts = selectedCategory === 'All' 
    ? products 
    : products.filter(p => p.category === selectedCategory);

  const totalRevenue = products.reduce((sum, item) => sum + item.revenue, 0);
  const totalSales = products.reduce((sum, item) => sum + item.sales, 0);

  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: '#05070c',
      color: '#e2e8f0',
      fontFamily: "'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
      padding: '20px 16px',
      backgroundImage: 'radial-gradient(circle at 50% 0%, #0f172a 0%, #05070c 70%)',
      boxSizing: 'border-box'
    }}>
      <style>{`
        .card-hover { transition: all 0.25s ease-in-out; }
        .card-hover:hover {
          transform: translateY(-3px);
          border-color: #38bdf8 !important;
          box-shadow: 0 8px 20px rgba(56, 189, 248, 0.15) !important;
        }
        .glow-title { text-shadow: 0 0 12px rgba(56, 189, 248, 0.6); }
      `}</style>

      <div style={{ textAlign: 'center', marginBottom: '24px' }}>
        <div style={{ 
          display: 'inline-block', padding: '4px 12px', backgroundColor: 'rgba(14, 165, 233, 0.1)', 
          borderRadius: '20px', border: '1px solid rgba(56, 189, 248, 0.3)', fontSize: '0.7rem', 
          color: '#38bdf8', letterSpacing: '2px', fontWeight: 'bold', marginBottom: '8px'
        }}>
          ● LIVE AUTONOMOUS SYSTEM
        </div>
        <h1 className="glow-title" style={{ fontSize: '1.8rem', fontWeight: '900', margin: 0, color: '#f8fafc', letterSpacing: '1px' }}>
          REBEL AI <span style={{ color: '#38bdf8' }}>VAULT</span>
        </h1>
        <p style={{ fontSize: '0.8rem', color: '#64748b', margin: '4px 0 0 0' }}>
          Premium Digital Assets, AI Prompt Engines & Automated Systems
        </p>
      </div>

      <div style={{ 
        display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '8px', marginBottom: '24px',
        backgroundColor: 'rgba(15, 23, 42, 0.6)', backdropFilter: 'blur(12px)',
        border: '1px solid rgba(30, 41, 59, 0.8)', borderRadius: '12px', padding: '12px'
      }}>
        <div style={{ textAlign: 'center' }}>
          <span style={{ fontSize: '0.65rem', color: '#64748b', display: 'block', letterSpacing: '1px' }}>VOLUME</span>
          <span style={{ fontSize: '1.1rem', fontWeight: 'bold', color: '#38bdf8' }}>${totalRevenue.toFixed(2)}</span>
        </div>
        <div style={{ textAlign: 'center', borderLeft: '1px solid #1e293b', borderRight: '1px solid #1e293b' }}>
          <span style={{ fontSize: '0.65rem', color: '#64748b', display: 'block', letterSpacing: '1px' }}>SALES</span>
          <span style={{ fontSize: '1.1rem', fontWeight: 'bold', color: '#f43f5e' }}>{totalSales}</span>
        </div>
        <div style={{ textAlign: 'center' }}>
          <span style={{ fontSize: '0.65rem', color: '#64748b', display: 'block', letterSpacing: '1px' }}>STATUS</span>
          <span style={{ fontSize: '1.1rem', fontWeight: 'bold', color: '#10b981' }}>ONLINE</span>
        </div>
      </div>

      <div style={{ display: 'flex', gap: '8px', overflowX: 'auto', paddingBottom: '8px', marginBottom: '20px' }}>
        {categories.map(cat => (
          <button
            key={cat}
            onClick={() => setSelectedCategory(cat)}
            style={{
              padding: '6px 14px', borderRadius: '20px',
              border: selectedCategory === cat ? '1px solid #38bdf8' : '1px solid #1e293b',
              backgroundColor: selectedCategory === cat ? 'rgba(56, 189, 248, 0.15)' : '#0f172a',
              color: selectedCategory === cat ? '#38bdf8' : '#94a3b8',
              fontSize: '0.75rem', fontWeight: '600', cursor: 'pointer', whiteSpace: 'nowrap'
            }}
          >
            {cat}
          </button>
        ))}
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {filteredProducts.map((item) => (
          <a key={item.id} href={item.paymentUrl} className="card-hover" style={{ 
            textDecoration: 'none', display: 'block', backgroundColor: 'rgba(15, 23, 42, 0.75)', 
            backdropFilter: 'blur(10px)', padding: '16px', borderRadius: '12px', border: '1px solid rgba(56, 189, 248, 0.2)'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '6px' }}>
              <span style={{ fontSize: '0.65rem', fontWeight: 'bold', color: '#38bdf8', backgroundColor: 'rgba(56, 189, 248, 0.1)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(56, 189, 248, 0.2)' }}>
                {item.category}
              </span>
              <span style={{ fontSize: '1.1rem', fontWeight: '800', color: '#10b981' }}>{item.price}</span>
            </div>
            <div style={{ fontWeight: '700', fontSize: '0.95rem', color: '#f8fafc', marginBottom: '6px' }}>{item.title}</div>
            <div style={{ fontSize: '0.78rem', color: '#94a3b8', lineHeight: '1.4', marginBottom: '12px' }}>{item.desc}</div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderTop: '1px solid rgba(30, 41, 59, 0.8)', paddingTop: '10px', fontSize: '0.75rem' }}>
              <span style={{ color: '#64748b' }}>{item.sales} Unlocked</span>
              <span style={{ color: '#38bdf8', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '4px' }}>Instant Access ⚡</span>
            </div>
          </a>
        ))}
      </div>

      <div style={{ textAlign: 'center', marginTop: '32px', paddingBottom: '16px', color: '#475569', fontSize: '0.7rem' }}>
        ⚡ POWERED BY STRIPE CHECKOUT & VERCEL AUTOMATION
      </div>
    </div>
  );
}
