import React, { useState } from 'react';
import { SpeedInsights } from '@vercel/speed-insights/react';

interface Product {
  id: string;
  title: string;
  category: string;
  price: string;
  sales: number;
  revenue: number;
  paymentUrl: string;
}

export default function App() {
  const [products] = useState<Product[]>([
    { 
      id: '1', 
      title: 'ObsidianInk Dark Art AI Prompt Vault v1', 
      category: 'AI Prompts', 
      price: '$29.00', 
      sales: 64, 
      revenue: 1856.00,
      paymentUrl: 'https://buy.stripe.com/test_1' 
    },
    { 
      id: '2', 
      title: 'Dark Gothic & Steampunk Tattoo Stencil Collection', 
      category: 'Digital Design', 
      price: '$19.99', 
      sales: 48, 
      revenue: 959.52,
      paymentUrl: 'https://buy.stripe.com/test_2' 
    },
    { 
      id: '3', 
      title: 'Termux Python Automation & Bot Scripts', 
      category: 'Software', 
      price: '$49.00', 
      sales: 18, 
      revenue: 882.00,
      paymentUrl: 'https://buy.stripe.com/test_3' 
    },
    { 
      id: '4', 
      title: 'Minimalist Snake & Geometric Line Art Pack', 
      category: 'Digital Design', 
      price: '$14.99', 
      sales: 22, 
      revenue: 329.78,
      paymentUrl: 'https://buy.stripe.com/test_4' 
    }
  ]);

  const handleBuy = (product: Product) => {
    // Direct checkout route
    window.location.href = product.paymentUrl;
  };

  const totalRevenue = products.reduce((sum, item) => sum + item.revenue, 0);

  return (
    <div style={{ padding: '16px', backgroundColor: '#090a0f', color: '#f1f5f9', minHeight: '100vh', fontFamily: 'sans-serif' }}>
      <SpeedInsights />
      <div style={{ marginBottom: '16px', textAlign: 'center' }}>
        <h1 style={{ fontSize: '1.4rem', margin: 0, color: '#38bdf8' }}>REBEL AI</h1>
        <p style={{ fontSize: '0.75rem', color: '#64748b', margin: '4px 0 0 0' }}>AUTONOMOUS OPERATING SYSTEM</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px', marginBottom: '16px' }}>
        <div style={{ backgroundColor: '#0f111a', border: '1px solid #1e293b', padding: '12px', borderRadius: '8px' }}>
          <span style={{ fontSize: '0.7rem', color: '#64748b', display: 'block' }}>REVENUE</span>
          <span style={{ fontSize: '1.1rem', fontWeight: 'bold', color: '#38bdf8' }}>${totalRevenue.toFixed(2)}</span>
        </div>
        <div style={{ backgroundColor: '#0f111a', border: '1px solid #1e293b', padding: '12px', borderRadius: '8px' }}>
          <span style={{ fontSize: '0.7rem', color: '#64748b', display: 'block' }}>EST. FEES</span>
          <span style={{ fontSize: '1.1rem', fontWeight: 'bold', color: '#10b981' }}>$25,500.00</span>
        </div>
      </div>

      <div style={{ backgroundColor: '#0f111a', border: '1px solid #1e293b', padding: '16px', borderRadius: '8px' }}>
        <h3 style={{ margin: '0 0 12px 0', fontSize: '1rem', color: '#38bdf8' }}>Storefront Assets (Tap to Purchase)</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          {products.map((p) => (
            <div key={p.id} onClick={() => handleBuy(p)} style={{ backgroundColor: '#181b26', padding: '12px', borderRadius: '6px', border: '1px solid #0284c7', cursor: 'pointer' }}>
              <div style={{ fontWeight: 'bold', fontSize: '0.9rem', color: '#fff', marginBottom: '4px' }}>{p.title}</div>
              <div style={{ fontSize: '0.8rem', color: '#38bdf8' }}>{p.category} • {p.price} • {p.sales} Sold — <span style={{ textDecoration: 'underline' }}>Buy Now ⚡</span></div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
