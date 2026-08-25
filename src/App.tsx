import { useEffect, useState } from 'react'

export default function App(){
  const [stats,setStats]=useState({visitors:0,revenue:0,status:'ONLINE'})
  useEffect(()=>{
    fetch('https://dez-rebel-ai-666.vercel.app').then(r=>r.json()).then(j=>{
      setStats({visitors:j.metrics?.total_visitors||0,revenue:j.metrics?.total_revenue||0,status:j.status||'ONLINE'})
    }).catch(()=>{})
  },[])

  const track=(p:string)=>{
    try{fetch('https://dez-rebel-ai-666.vercel.app/track',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({product:p})})}catch{}
  }

  return (
    <div className="min-h-screen bg-[#050505] text-white antialiased" style={{fontFamily:'JetBrains Mono, monospace'}}>
      <div className="relative min-h-[92vh] flex items-center overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-b from-zinc-900 via-black to-black"></div>
        <div className="relative z-10 max-w-6xl mx-auto px-6 py-16 w-full">
          <div className="inline-flex items-center gap-2 bg-[#0f0f0f] border border-zinc-800 rounded-full px-3 py-1 text-[11px]"><span className="h-2 w-2 bg-green-500 rounded-full animate-pulse inline-block"></span> LIVE_PRODUCTION ONLINE • {stats.visitors} visitors • ${stats.revenue} revenue</div>
          <h1 className="text-[18vw] md:text-[11rem] leading-[0.85] mt-6 font-black" style={{fontFamily:'Anton, sans-serif'}}>DEZ<br/><span className="text-[#ff6a00]">REBEL</span></h1>
          <p className="max-w-xl mt-6 text-zinc-300 text-[14px] leading-6">The uniform for people who refuse to comply. Heavyweight embroidered. Demon Gang. Shipping now.</p>
          <div className="mt-8 flex gap-3">
            <a href="#shop" className="bg-[#ff6a00] text-black font-black px-8 py-4 rounded-full text-[14px]">SHOP DROP - $49</a>
          </div>
        </div>
      </div>
      <div id="shop" className="max-w-6xl mx-auto px-6 py-16">
        <h2 className="text-6xl font-black">DROP 001</h2>
        <div className="grid md:grid-cols-2 gap-6 mt-10">
          <div className="bg-[#111] border border-zinc-800 rounded-[28px] overflow-hidden">
            <div className="h-[420px] bg-gradient-to-br from-zinc-800 to-black flex items-center justify-center text-6xl font-black">HOODIE</div>
            <div className="p-6"><div className="flex justify-between"><h3 className="font-black text-xl">DEMON HOODIE</h3><span className="text-[#ff6a00] font-black">$49</span></div>
            <a href="https://buy.stripe.com/28E14n47GcJN9gg21t18d2H" target="_blank" onClick={()=>track('hoodie')} className="mt-5 block bg-white text-black text-center font-black py-4 rounded-full">BUY NOW - $49</a></div>
          </div>
          <div className="bg-[#111] border border-zinc-800 rounded-[28px] overflow-hidden">
            <div className="h-[420px] bg-gradient-to-br from-orange-900/30 to-black flex items-center justify-center text-6xl font-black">MASK</div>
            <div className="p-6"><div className="flex justify-between"><h3 className="font-black text-xl">DEMON MASK</h3><span className="text-[#ff6a00] font-black">$35</span></div>
            <a href="https://buy.stripe.com/bJebJ19s0h03akk21t18d2I" target="_blank" onClick={()=>track('mask')} className="mt-5 block bg-[#ff6a00] text-black text-center font-black py-4 rounded-full">BUY NOW - $35</a></div>
          </div>
          <div className="bg-[#111] border border-zinc-800 rounded-[28px] overflow-hidden">
            <div className="h-[420px] bg-zinc-900 flex items-center justify-center text-6xl font-black">STICKERS</div>
            <div className="p-6"><div className="flex justify-between"><h3 className="font-black text-xl">STICKER PACK (5)</h3><span className="text-[#ff6a00] font-black">$15</span></div>
            <a href="https://buy.stripe.com/14A3cvaw41153VW8pR18d2J" target="_blank" onClick={()=>track('stickers')} className="mt-5 block bg-zinc-800 text-white text-center font-black py-4 rounded-full">BUY NOW - $15</a></div>
          </div>
          <div className="bg-[#111] border border-orange-500/50 rounded-[28px] overflow-hidden">
            <div className="h-[420px] bg-black flex flex-col items-center justify-center p-8 text-center"><div className="text-[#ff6a00] text-[12px] tracking-[0.3em]">DEMON GANG</div><div className="text-6xl font-black mt-2">UNCUT</div></div>
            <div className="p-6"><div className="flex justify-between"><h3 className="font-black text-xl">UNCUT CLUB</h3><span className="text-[#ff6a00] font-black">$29/mo</span></div>
            <a href="https://buy.stripe.com/28EdR9dIg4dheAAaxZ18d2K" target="_blank" onClick={()=>track('uncut')} className="mt-5 block bg-[#ff6a00] text-black text-center font-black py-4 rounded-full">JOIN - $29/MO</a></div>
          </div>
        </div>
      </div>
    </div>
  )
}
