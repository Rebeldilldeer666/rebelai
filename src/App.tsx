import React, { useState } from 'react';
import { SpeedInsights } from '@vercel/speed-insights/react';

interface Product {
  id: string;
  title: string;
  category: string;
  price: string;
  sales: number;
  revenue: number;
}

interface Lead {
  id: string;
  address: string;
  city: string;
  sellerName: string;
  askingPrice: string;
  estAssignmentFee: string;
  status: string;
}

export default function App() {
  const [activeTab, setActiveTab] = useState<'products' | 'generator' | 'wholesale' | 'gateway'>('products');

  const [products, setProducts] = useState<Product[]>([
    { id: '1', title: 'ObsidianInk Dark Art AI Prompt Vault v1', category: 'AI Prompts', price: '$29.00', sales: 64, revenue: 1856.00 },
    { id: '2', title: 'Dark Gothic & Steampunk Tattoo Stencil Collection', category: 'Digital Design', price: '$19.99', sales: 48, revenue: 959.52 },
    { id: '3', title: 'Termux Python Automation & Bot Scripts', category: 'Software', price: '$49.00', sales: 18, revenue: 882.00 },
    { id: '4', title: 'Minimalist Snake & Geometric Line Art Pack', category: 'Digital Design', price: '$14.99', sales: 22, revenue: 329.78 }
  ]);

  const [leads] = useState<Lead[]>([
    { id: '101', address: '1428 S 12th St', city: 'Milwaukee', sellerName: 'J. Miller', askingPrice: '$45,000', estAssignmentFee: '$8,500', status: 'Under Contract' },
    { id: '102', address: '915 Erie Ave', city: 'Sheboygan', sellerName: 'D. Vance', askingPrice: '$62,000', estAssignmentFee: '$10,000', status: 'Outreach Sent' },
    { id: '103', address: '2204 N 24th St', city: 'Milwaukee', sellerName: 'A. Smith', askingPrice: '$38,000', estAssignmentFee: '$7,000', status: 'Prospect' }
  ]);

  const [newTitle, setNewTitle] = useState('');
  const [newPrice, setNewPrice] = useState('');
  const [newCategory, setNewCategory] = useState('AI Prompts');
  const [genNiche, setGenNiche] = useState('Dark Gothic Ink & Stencils');
  const [genOutput, setGenOutput] = useState('');

  const totalRevenue = products.reduce((sum, item) => sum + item.revenue, 0);

  const handleAddProduct = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTitle || !newPrice) return;
    const priceVal = parseFloat(newPrice.replace('$', '')) || 0;
    const item: Product = {
      id: Date.now().toString(),
      title: newTitle,
      category: newCategory,
      price: `$${priceVal.toFixed(2)}`,
      sales: 0,
      revenue: 0
    };
    setProducts([item, ...products]);
    setNewTitle('');
    setNewPrice('');
  };

  const handleGenerateListing = () => {
    setGenOutput(
      `[OBSIDIANINK GENERATED LISTING]\n\nTitle: ${genNiche} Master Vault\nPrice: $29.99\n\nAutomated sales copy generated successfully. Commercial license & deployment guide attached.`
    );
  };

  return (
    <div style={{ padding: '16px', backgroundColor: '#090a0f', color: '#f1f5f9', minHeight: '100vh', fontFamily: 'sans-serif', boxSizing: 'border-box' }}>
      <SpeedInsights />
      
      {/* Mobile Top Header */}
      <div style={{ marginBottom: '16px', textAlign: 'center' }}>
        <h1 style={{ fontSize: '1.4rem', margin: 0, color: '#38bdf8' }}>REBEL AI</h1>
        <p style={{ fontSize: '0.75rem', color: '#64748b', margin: '4px 0 0 0' }}>AUTONOMOUS OPERATING SYSTEM</p>
      </div>

      {/* KPI Cards */}
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

      {/* Mobile Touch Navigation Bar */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '8px', marginBottom: '16px' }}>
        <button 
          onClick={() => setActiveTab('products')} 
          style={{ padding: '12px', borderRadius: '6px', border: 'none', backgroundColor: activeTab === 'products' ? '#0284c7' : '#1e293b', color: '#fff', fontWeight: 'bold', cursor: 'pointer', fontSize: '0.85rem' }}
        >
          📦 Assets ({products.length})
        </button>
        <button 
          onClick={() => setActiveTab('generator')} 
          style={{ padding: '12px', borderRadius: '6px', border: 'none', backgroundColor: activeTab === 'generator' ? '#0284c7' : '#1e293b', color: '#fff', fontWeight: 'bold', cursor: 'pointer', fontSize: '0.85rem' }}
        >
          ⚡ Generator
        </button>
        <button 
          onClick={() => setActiveTab('wholesale')} 
          style={{ padding: '12px', borderRadius: '6px', border: 'none', backgroundColor: activeTab === 'wholesale' ? '#0284c7' : '#1e293b', color: '#fff', fontWeight: 'bold', cursor: 'pointer', fontSize: '0.85rem' }}
        >
          🎯 Leads ({leads.length})
        </button>
        <button 
          onClick={() => setActiveTab('gateway')} 
          style={{ padding: '12px', borderRadius: '6px', border: 'none', backgroundColor: activeTab === 'gateway' ? '#0284c7' : '#1e293b', color: '#fff', fontWeight: 'bold', cursor: 'pointer', fontSize: '0.85rem' }}
        >
          💳 Gateway
        </button>
      </div>

      {/* Tab Content Areas */}
      {activeTab === 'products' && (
        <div style={{ backgroundColor: '#0f111a', border: '1px solid #1e293b', padding: '16px', borderRadius: '8px' }}>
          <h3 style={{ margin: '0 0 12px 0', fontSize: '1rem', color: '#38bdf8' }}>Storefront Assets</h3>
          <form onSubmit={handleAddProduct} style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginBottom: '16px' }}>
            <input 
              type="text" 
              placeholder="Asset Title" 
              value={newTitle} 
              onChange={(e) => setNewTitle(e.target.value)} 
              style={{ backgroundColor: '#181b26', border: '1px solid #1e293b', padding: '10px', color: '#fff', borderRadius: '6px' }}
            />
            <div style={{ display: 'flex', gap: '8px' }}>
              <input 
                type="text" 
                placeholder="Price" 
                value={newPrice} 
                onChange={(e) => setNewPrice(e.target.value)} 
                style={{ flex: 1, backgroundColor: '#181b26', border: '1px solid #1e293b', padding: '10px', color: '#fff', borderRadius: '6px' }}
              />
              <select 
                value={newCategory} 
                onChange={(e) => setNewCategory(e.target.value)} 
                style={{ flex: 1, backgroundColor: '#181b26', border: '1px solid #1e293b', padding: '10px', color: '#fff', borderRadius: '6px' }}
              >
                <option value="AI Prompts">AI Prompts</option>
                <option value="Digital Design">Digital Design</option>
                <option value="Software">Software</option>
              </select>
            </div>
            <button type="submit" style={{ backgroundColor: '#0284c7', color: '#fff', border: 'none', padding: '12px', borderRadius: '6px', fontWeight: 'bold' }}>+ Add Asset</button>
          </form>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {products.map((p) => (
              <div key={p.id} style={{ backgroundColor: '#181b26', padding: '12px', borderRadius: '6px', border: '1px solid #1e293b' }}>
                <div style={{ fontWeight: 'bold', fontSize: '0.9rem', marginBottom: '4px' }}>{p.title}</div>
                <div style={{ fontSize: '0.8rem', color: '#94a3b8' }}>{p.category} • {p.price} • {p.sales} Sold</div>
              </div>
            ))}
          </div>
        </div>
      )}

      {activeTab === 'generator' && (
        <div style={{ backgroundColor: '#0f111a', border: '1px solid #1e293b', padding: '16px', borderRadius: '8px' }}>
          <h3 style={{ margin: '0 0 12px 0', fontSize: '1rem', color: '#38bdf8' }}>Listing Generator</h3>
          <select value={genNiche} onChange={(e) => setGenNiche(e.target.value)} style={{ width: '100%', backgroundColor: '#181b26', border: '1px solid #1e293b', padding: '10px', color: '#fff', borderRadius: '6px', marginBottom: '12px' }}>
            <option value="Dark Gothic Ink & Stencils">Dark Gothic Ink & Stencils</option>
            <option value="AI Prompt Vaults">AI Prompt Vaults</option>
            <option value="Termux Automation Scripts">Termux Automation Scripts</option>
          </select>
          <button onClick={handleGenerateListing} style={{ width: '100%', backgroundColor: '#0284c7', color: '#fff', border: 'none', padding: '12px', borderRadius: '6px', fontWeight: 'bold' }}>Generate Copy</button>
          {genOutput && <pre style={{ marginTop: '12px', backgroundColor: '#181b26', padding: '12px', borderRadius: '6px', color: '#38bdf8', fontSize: '0.8rem', whiteSpace: 'pre-wrap' }}>{genOutput}</pre>}
        </div>
      )}

      {activeTab === 'wholesale' && (
        <div style={{ backgroundColor: '#0f111a', border: '1px solid #1e293b', padding: '16px', borderRadius: '8px' }}>
          <h3 style={{ margin: '0 0 12px 0', fontSize: '1rem', color: '#38bdf8' }}>Wholesale Leads</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {leads.map((l) => (
              <div key={l.id} style={{ backgroundColor: '#181b26', padding: '12px', borderRadius: '6px', border: '1px solid #1e293b' }}>
                <div style={{ fontWeight: 'bold', fontSize: '0.9rem' }}>{l.address} ({l.city})</div>
                <div style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Seller: {l.sellerName} | Fee: <span style={{ color: '#38bdf8' }}>{l.estAssignmentFee}</span></div>
              </div>
            ))}
          </div>
        </div>
      )}

      {activeTab === 'gateway' && (
        <div style={{ backgroundColor: '#0f111a', border: '1px solid #1e293b', padding: '16px', borderRadius: '8px' }}>
          <h3 style={{ margin: '0 0 12px 0', fontSize: '1rem', color: '#38bdf8' }}>Payment Gateways</h3>
          <input type="password" placeholder="Stripe Key" style={{ width: '100%', backgroundColor: '#181b26', border: '1px solid #1e293b', padding: '10px', color: '#fff', borderRadius: '6px', marginBottom: '8px', boxSizing: 'border-box' }} />
          <button style={{ width: '100%', backgroundColor: '#0284c7', color: '#fff', border: 'none', padding: '12px', borderRadius: '6px', fontWeight: 'bold' }}>Save Gateway</button>
        </div>
      )}
    </div>
  );
}
