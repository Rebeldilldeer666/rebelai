import React, { useState } from 'react';

interface Product {
  id: string;
  title: string;
  category: string;
  price: string;
  sales: number;
  revenue: number;
  status: 'Active' | 'Draft';
}

interface Lead {
  id: string;
  address: string;
  city: string;
  sellerName: string;
  askingPrice: string;
  estAssignmentFee: string;
  status: 'Prospect' | 'Outreach Sent' | 'Under Contract' | 'Assigned';
}

export default function App() {
  const [activeTab, setActiveTab] = useState<'products' | 'generator' | 'wholesale' | 'gateway'>('products');

  // Digital Products Pre-Populated with your Asset Inventory
  const [products, setProducts] = useState<Product[]>([
    { id: '1', title: 'ObsidianInk Dark Art AI Prompt Vault v1', category: 'AI Prompts', price: '$29.00', sales: 64, revenue: 1856.00, status: 'Active' },
    { id: '2', title: 'Dark Gothic & Steampunk Tattoo Stencil Collection', category: 'Digital Design', price: '$19.99', sales: 48, revenue: 959.52, status: 'Active' },
    { id: '3', title: 'Termux Python Automation & Bot Scripts', category: 'Software', price: '$49.00', sales: 18, revenue: 882.00, status: 'Active' },
    { id: '4', title: 'Minimalist Snake & Geometric Line Art Pack', category: 'Digital Design', price: '$14.99', sales: 22, revenue: 329.78, status: 'Active' }
  ]);

  // Real Estate Wholesale Pipeline Pre-Populated for Targeted Markets
  const [leads, setLeads] = useState<Lead[]>([
    { id: '101', address: '1428 S 12th St', city: 'Milwaukee', sellerName: 'J. Miller', askingPrice: '$45,000', estAssignmentFee: '$8,500', status: 'Under Contract' },
    { id: '102', address: '915 Erie Ave', city: 'Sheboygan', sellerName: 'D. Vance', askingPrice: '$62,000', estAssignmentFee: '$10,000', status: 'Outreach Sent' },
    { id: '103', address: '2204 N 24th St', city: 'Milwaukee', sellerName: 'A. Smith', askingPrice: '$38,000', estAssignmentFee: '$7,000', status: 'Prospect' }
  ]);

  // Form States
  const [newTitle, setNewTitle] = useState('');
  const [newPrice, setNewPrice] = useState('');
  const [newCategory, setNewCategory] = useState('AI Prompts');

  // AI Generator States
  const [genNiche, setGenNiche] = useState('Dark Gothic Ink');
  const [genOutput, setGenOutput] = useState('');

  // Calculations
  const totalRevenue = products.reduce((sum, item) => sum + item.revenue, 0);
  const totalSales = products.reduce((sum, item) => sum + item.sales, 0);

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
      revenue: 0,
      status: 'Active'
    };
    setProducts([item, ...products]);
    setNewTitle('');
    setNewPrice('');
  };

  const handleGenerateListing = () => {
    setGenOutput(
      `==================================================\nOBSIDIANINK AUTOMATED SALES LISTING GENERATOR\n==================================================\n\nTitle: Exclusive ${genNiche} Master Collection\n\nDescription:\nTransform your creative workflow with this curated series of high-converting, precision-engineered assets. Designed explicitly for artists, creators, and automated storefronts requiring dark aesthetic perfection.\n\nIncluded Files:\n- Commercial License Included\n- High-Resolution Stencil Overlay Files\n- Optimized Midjourney / Stable Diffusion Master Prompts\n- Setup & Deployment Quickstart Guide\n\nSuggested Launch Price: $29.99\nCheckout Route: Direct Digital Fulfillment via Stripe Link`
    );
  };

  return (
    <div style={styles.container}>
      {/* Sidebar Navigation */}
      <aside style={styles.sidebar}>
        <div style={styles.brandRow}>
          <div style={styles.brandGlow} />
          <h2 style={styles.brandText}>REBEL AI</h2>
        </div>
        <p style={styles.brandSub}>Autonomous Operating System</p>

        <nav style={styles.navStack}>
          <button style={activeTab === 'products' ? styles.navActive : styles.navBtn} onClick={() => setActiveTab('products')}>
            📦 Digital Assets ({products.length})
          </button>
          <button style={activeTab === 'generator' ? styles.navActive : styles.navBtn} onClick={() => setActiveTab('generator')}>
            ⚡ AI Listing Generator
          </button>
          <button style={activeTab === 'wholesale' ? styles.navActive : styles.navBtn} onClick={() => setActiveTab('wholesale')}>
            🎯 Wholesale Pipeline ({leads.length})
          </button>
          <button style={activeTab === 'gateway' ? styles.navActive : styles.navBtn} onClick={() => setActiveTab('gateway')}>
            💳 Payment Gateways
          </button>
        </nav>

        <div style={styles.sidebarFooter}>
          <p style={styles.footerText}>Environment: Termux Local</p>
          <p style={styles.footerText}>Status: Production Live</p>
        </div>
      </aside>

      {/* Main Content Workspace */}
      <main style={styles.main}>
        {/* Global Key Performance Indicators */}
        <div style={styles.kpiGrid}>
          <div style={styles.kpiCard}>
            <span style={styles.kpiLabel}>Total Platform Revenue</span>
            <span style={styles.kpiValue}>${totalRevenue.toLocaleString('en-US', { minimumFractionDigits: 2 })}</span>
          </div>
          <div style={styles.kpiCard}>
            <span style={styles.kpiLabel}>Digital Units Sold</span>
            <span style={styles.kpiValue}>{totalSales}</span>
          </div>
          <div style={styles.kpiCard}>
            <span style={styles.kpiLabel}>Est. Wholesale Assignment Value</span>
            <span style={styles.kpiValue}>$25,500.00</span>
          </div>
        </div>

        {/* Tab 1: Products */}
        {activeTab === 'products' && (
          <div style={styles.panel}>
            <h3 style={styles.panelTitle}>ObsidianInk Storefront Assets</h3>
            
            <form onSubmit={handleAddProduct} style={styles.formInline}>
              <input 
                type="text" 
                placeholder="Asset Title (e.g., Steampunk Bat Vector Stencils)" 
                value={newTitle}
                onChange={(e) => setNewTitle(e.target.value)}
                style={styles.inputFlex}
              />
              <input 
                type="text" 
                placeholder="Price (e.g., 24.99)" 
                value={newPrice}
                onChange={(e) => setNewPrice(e.target.value)}
                style={styles.inputSmall}
              />
              <select value={newCategory} onChange={(e) => setNewCategory(e.target.value)} style={styles.inputSelect}>
                <option value="AI Prompts">AI Prompts</option>
                <option value="Digital Design">Digital Design</option>
                <option value="Software">Software & Scripts</option>
              </select>
              <button type="submit" style={styles.btnPrimary}>+ Launch Asset</button>
            </form>

            <table style={styles.table}>
              <thead>
                <tr>
                  <th style={styles.th}>Title</th>
                  <th style={styles.th}>Category</th>
                  <th style={styles.th}>Price</th>
                  <th style={styles.th}>Sales</th>
                  <th style={styles.th}>Gross Revenue</th>
                  <th style={styles.th}>Status</th>
                </tr>
              </thead>
              <tbody>
                {products.map((p) => (
                  <tr key={p.id} style={styles.tr}>
                    <td style={styles.td}><strong>{p.title}</strong></td>
                    <td style={styles.td}>{p.category}</td>
                    <td style={styles.td}>{p.price}</td>
                    <td style={styles.td}>{p.sales}</td>
                    <td style={styles.td}>${p.revenue.toFixed(2)}</td>
                    <td style={styles.td}><span style={styles.badgeActive}>{p.status}</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {/* Tab 2: Copy Generator */}
        {activeTab === 'generator' && (
          <div style={styles.panel}>
            <h3 style={styles.panelTitle}>Autonomous Product & Ad Copy Engine</h3>
            <div style={styles.formInline}>
              <select value={genNiche} onChange={(e) => setGenNiche(e.target.value)} style={styles.inputFlex}>
                <option value="Dark Gothic Ink & Stencils">Dark Gothic Ink & Stencils</option>
                <option value="AI Prompt Engineering Vaults">AI Prompt Engineering Vaults</option>
                <option value="Termux Python Automation Scripts">Termux Python Automation Scripts</option>
                <option value="Real Estate Wholesaling Outreach">Real Estate Wholesaling Outreach</option>
              </select>
              <button onClick={handleGenerateListing} style={styles.btnPrimary}>Generate Copy Suite</button>
            </div>

            {genOutput && <pre style={styles.codeBlock}>{genOutput}</pre>}
          </div>
        )}

        {/* Tab 3: Wholesale Pipeline */}
        {activeTab === 'wholesale' && (
          <div style={styles.panel}>
            <h3 style={styles.panelTitle}>Automated Real Estate Wholesaling Pipeline</h3>
            <table style={styles.table}>
              <thead>
                <tr>
                  <th style={styles.th}>Property Address</th>
                  <th style={styles.th}>Market</th>
                  <th style={styles.th}>Seller</th>
                  <th style={styles.th}>Asking Price</th>
                  <th style={styles.th}>Est. Fee</th>
                  <th style={styles.th}>Stage</th>
                </tr>
              </thead>
              <tbody>
                {leads.map((l) => (
                  <tr key={l.id} style={styles.tr}>
                    <td style={styles.td}><strong>{l.address}</strong></td>
                    <td style={styles.td}>{l.city}</td>
                    <td style={styles.td}>{l.sellerName}</td>
                    <td style={styles.td}>{l.askingPrice}</td>
                    <td style={styles.td} style={{ color: '#38bdf8', fontWeight: 'bold' }}>{l.estAssignmentFee}</td>
                    <td style={styles.td}><span style={styles.badgeActive}>{l.status}</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {/* Tab 4: Gateway Settings */}
        {activeTab === 'gateway' && (
          <div style={styles.panel}>
            <h3 style={styles.panelTitle}>Instant Automated Payment & Delivery Routing</h3>
            <p style={{ color: '#94a3b8', fontSize: '0.9rem', marginBottom: '16px' }}>
              Connect payment gateways to generate shareable checkout links and dispatch digital items automatically upon receipt.
            </p>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', maxWidth: '400px' }}>
              <input type="password" placeholder="Stripe Secret API Key (sk_live_...)" style={styles.inputFlex} />
              <input type="text" placeholder="Webhook Secret (whsec_...)" style={styles.inputFlex} />
              <button style={styles.btnPrimary}>Save & Activate Gateway</button>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

// Visual Styling System
const styles: { [key: string]: React.CSSProperties } = {
  container: { display: 'flex', minHeight: '100vh', backgroundColor: '#090a0f', color: '#f1f5f9', fontFamily: 'system-ui, sans-serif' },
  sidebar: { width: '270px', backgroundColor: '#0f111a', borderRight: '1px solid #1e293b', padding: '24px', display: 'flex', flexDirection: 'column' },
  brandRow: { display: 'flex', alignItems: 'center', gap: '10px' },
  brandGlow: { width: '10px', height: '10px', borderRadius: '50%', backgroundColor: '#0284c7', boxShadow: '0 0 12px #0284c7' },
  brandText: { margin: 0, fontSize: '1.3rem', fontWeight: 800, letterSpacing: '1.5px', color: '#f8fafc' },
  brandSub: { color: '#64748b', fontSize: '0.75rem', marginTop: '2px', marginBottom: '28px', textTransform: 'uppercase', letterSpacing: '1px' },
  navStack: { display: 'flex', flexDirection: 'column', gap: '8px', flex: 1 },
  navBtn: { backgroundColor: 'transparent', border: 'none', color: '#94a3b8', padding: '12px 14px', textAlign: 'left', borderRadius: '6px', cursor: 'pointer', fontSize: '0.9rem' },
  navActive: { backgroundColor: '#1e293b', border: 'none', color: '#38bdf8', padding: '12px 14px', textAlign: 'left', borderRadius: '6px', fontWeight: 'bold', fontSize: '0.9rem' },
  sidebarFooter: { paddingTop: '16px', borderTop: '1px solid #1e293b' },
  footerText: { color: '#475569', fontSize: '0.75rem', margin: '2px 0' },
  main: { flex: 1, padding: '32px' },
  kpiGrid: { display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '16px', marginBottom: '24px' },
  kpiCard: { backgroundColor: '#0f111a', border: '1px solid #1e293b', padding: '20px', borderRadius: '8px' },
  kpiLabel: { color: '#64748b', fontSize: '0.8rem', display: 'block', marginBottom: '6px', textTransform: 'uppercase' },
  kpiValue: { fontSize: '1.6rem', fontWeight: 800, color: '#38bdf8' },
  panel: { backgroundColor: '#0f111a', border: '1px solid #1e293b', padding: '24px', borderRadius: '8px' },
  panelTitle: { margin: '0 0 20px 0', color: '#f8fafc', fontSize: '1.1rem' },
  formInline: { display: 'flex', gap: '10px', marginBottom: '20px' },
  inputFlex: { flex: 1, backgroundColor: '#181b26', border: '1px solid #1e293b', padding: '12px', color: '#fff', borderRadius: '6px' },
  inputSmall: { width: '100px', backgroundColor: '#181b26', border: '1px solid #1e293b', padding: '12px', color: '#fff', borderRadius: '6px' },
  inputSelect: { backgroundColor: '#181b26', border: '1px solid #1e293b', padding: '12px', color: '#fff', borderRadius: '6px' },
  btnPrimary: { backgroundColor: '#0284c7', color: '#fff', border: 'none', padding: '12px 20px', borderRadius: '6px', fontWeight: 'bold', cursor: 'pointer' },
  table: { width: '100%', borderCollapse: 'collapse', marginTop: '8px' },
  th: { padding: '12px', color: '#64748b', fontSize: '0.8rem', textAlign: 'left', borderBottom: '1px solid #1e293b', textTransform: 'uppercase' },
  tr: { borderBottom: '1px solid #181b26' },
  td: { padding: '12px', color: '#cbd5e1', fontSize: '0.875rem' },
  badgeActive: { backgroundColor: '#0369a1', color: '#e0f2fe', padding: '4px 8px', borderRadius: '4px', fontSize: '0.75rem', fontWeight: 600 },
  codeBlock: { backgroundColor: '#181b26', border: '1px solid #1e293b', padding: '16px', borderRadius: '6px', color: '#38bdf8', fontSize: '0.85rem', lineHeight: '1.5', whiteSpace: 'pre-wrap', marginTop: '16px' }
};
