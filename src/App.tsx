import React, { useState } from 'react';

export default function App() {
  const [status, setStatus] = useState('Online & Ready');

  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: '#0a0a0c',
      color: '#e2e8f0',
      fontFamily: 'system-ui, -apple-system, sans-serif',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '20px'
    }}>
      <div style={{
        backgroundColor: '#121318',
        border: '1px solid #27272a',
        borderRadius: '12px',
        padding: '32px',
        maxWidth: '480px',
        width: '100%',
        boxShadow: '0 10px 25px -5px rgba(0, 0, 0, 0.5)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px' }}>
          <div style={{
            width: '12px',
            height: '12px',
            borderRadius: '50%',
            backgroundColor: '#10b981',
            boxShadow: '0 0 8px #10b981'
          }} />
          <h1 style={{ margin: 0, fontSize: '1.5rem', fontWeight: 700, letterSpacing: '-0.025em' }}>
            RebelAI Workspace
          </h1>
        </div>
        
        <p style={{ color: '#a1a1aa', fontSize: '0.95rem', lineHeight: '1.5', marginBottom: '24px' }}>
          Deployment initial state active. All core routing and Vite HMR dependencies are linked.
        </p>

        <div style={{
          backgroundColor: '#18181b',
          borderRadius: '8px',
          padding: '12px 16px',
          fontSize: '0.875rem',
          color: '#38bdf8',
          border: '1px solid #27272a',
          marginBottom: '20px'
        }}>
          Status: <strong>{status}</strong>
        </div>

        <button 
          onClick={() => setStatus('System Checked & Verified')}
          style={{
            width: '100%',
            backgroundColor: '#2563eb',
            color: '#ffffff',
            border: 'none',
            padding: '12px',
            borderRadius: '6px',
            fontWeight: 600,
            cursor: 'pointer',
            transition: 'background-color 0.2s'
          }}
        >
          Run System Check
        </button>
      </div>
    </div>
  );
}
