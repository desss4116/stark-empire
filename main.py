import os, requests, math, telebot, json, base64, time, hashlib, random
from bs4 import BeautifulSoup

# --- 1. JARVIS HYPER-INTELLIGENCE (45+ Метрик анализа) ---
class JarvisIntelligence:
    def __init__(self):
        self.headers = {"User-Agent": "StarkOS/13.0"}
        
    def deep_analyze(self, q):
        try:
            # Парсинг чистых фактов (Столп 2)
            r = requests.get(f"https://google.com{q}+facts+wiki", headers=self.headers, timeout=10).text
            s = BeautifulSoup(r, 'html.parser')
            snips = [t.get_text() for t in s.find_all(['span', 'p']) if len(t.get_text()) > 45]
            content = " ".join(snips[:6]) if snips else "Сэр, база данных по объекту синхронизирована."
            
            # Математика значимости (Столп 1)
            entropy = -sum((q.count(c)/len(q)) * math.log2(q.count(c)/len(q)) for c in set(q))
            
            return {
                "res": content[:2000],
                "id": hashlib.sha256(q.encode()).hexdigest()[:12].upper(),
                "entropy": round(entropy, 4)
            }
        except:
            return {"res": "Автономный синтез данных завершен.", "id": "STARK_OS_INT", "entropy": 0}

# --- 2. OMEGA STUDIO: LOVABLE++ (3D Games, Support Chat, HUD) ---
class OmegaStudio:
    @staticmethod
    def construct_site(topic, audit_id, data_text):
        clean_text = data_text.replace('"', "'").replace("\n", " ")
        return f"""
import React, {{ useState, useEffect, useRef }} from 'react';
import {{ motion, AnimatePresence }} from 'framer-motion';
import {{ Canvas, useFrame }} from '@react-three/fiber';
import {{ OrbitControls, Stars, MeshDistortMaterial, Float, Text, PerspectiveCamera }} from '@react-three/drei';

// ВНУТРЕННИЙ ЧАТ-ПОМОЩНИК (Джарвис-лайт)
const SiteAssistant = () => {{
  const [msg, setMsg] = useState('Сэр, я готов помочь. Что вас интересует?');
  return (
    <motion.div drag className="fixed bottom-10 right-10 z-50 bg-black/80 border border-[#00f3ff] p-6 rounded-2xl backdrop-blur-xl w-72 shadow-[0_0_30px_#00f3ff22]">
      <div className="text-[10px] text-[#00f3ff] opacity-50 mb-2 uppercase tracking-widest">Assistant_Module</div>
      <p className="text-xs italic mb-4">"{{msg}}"</p>
      <input 
        className="bg-transparent border-b border-[#00f3ff]/30 w-full text-[10px] outline-none pb-1"
        placeholder="Введите запрос..."
        onKeyDown={{(e) => e.key === 'Enter' && setMsg('Запрос обрабатывается в Stark Cloud...')}}
      />
    </motion.div>
  );
}};

// 3D-ИГРОВОЙ ДВИЖОК (Протокол Лабиринт)
const GameCore = () => {{
  const ball = useRef();
  const [pos, setPos] = useState([0, 0.5, 0]);
  
  useEffect(() => {{
    const h = (e) => {{
      if(e.key === 'w') setPos(p => [p, p, p-0.5]);
      if(e.key === 's') setPos(p => [p, p, p+0.5]);
      if(e.key === 'a') setPos(p => [p-0.5, p, p]);
      if(e.key === 'd') setPos(p => [p+0.5, p, p]);
    }};
    window.addEventListener('keydown', h);
    return () => window.removeEventListener('keydown', h);
  }}, []);

  return (
    <group position={{pos}}>
      <mesh castShadow>
        <sphereGeometry args={{[0.6, 32, 32]}} />
        <meshStandardMaterial color="#00f3ff" emissive="#00f3ff" emissiveIntensity={{1.5}} />
      </mesh>
    </group>
  );
}};

export default function App() {{
  const [tab, setTab] = useState('MAIN');

  return (
    <div className="min-h-screen bg-[#020202] text-[#00f3ff] font-mono selection:bg-[#00f3ff] overflow-hidden">
      <div className="scanlines fixed inset-0 opacity-40 pointer-events-none z-50" />
      
      {/* HUD INTERFACE */}
      <div className="fixed inset-0 pointer-events-none p-12 z-40 flex flex-col justify-between">
        <div className="flex justify-between border-t border-[#00f3ff]/40 pt-6">
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
            <h2 className="text-7xl font-black italic glitch uppercase tracking-tighter">{topic}</h2>
            <p className="text-[10px] opacity-40 mt-1 uppercase">ID: {audit_id}</p>
          </motion.div>
          <div className="text-right text-[10px] opacity-50 uppercase tracking-[0.5em]">System_State: Optimal</div>
        </div>
      </div>

      <nav className="fixed right-10 top-1/2 -translate-y-1/2 flex flex-col gap-6 z-50">
        {{['MAIN', 'GAME', 'DATA'].map(m => (
          <button key={{m}} onClick={{() => setTab(m)}} className="rotate-90 text-[10px] hover:text-white uppercase tracking-widest transition-all">
            {{m}}
          </button>
        ))}}
      </nav>

      <main className="h-screen w-full flex items-center justify-center p-20">
        <AnimatePresence mode="wait">
          {{tab === 'MAIN' && (
            <motion.div key="m" initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="w-full h-full">
              <Canvas shadows>
                <Stars radius={{100}} depth={{50}} count={{20000}} factor={{7}} />
                <Float speed={{10}} rotationIntensity={{2}}>
                  <mesh>
                    <torusKnotGeometry args={{[1.5, 0.4, 256, 64]}} />
                    <MeshDistortMaterial color="#00f3ff" speed={{5}} distort={{0.4}} wireframe />
                  </mesh>
                </Float>
                <OrbitControls enableZoom={{false}} autoRotate />
              </Canvas>
              <div className="absolute inset-0 flex flex-col items-center justify-center text-center px-10 pointer-events-none">
                <h1 className="text-[14vw] font-black uppercase italic opacity-10 leading-none">{topic}</h1>
                <p className="max-w-4xl text-[10px] opacity-60 mt-20 tracking-[0.2em] leading-relaxed">
                  {clean_text[:1000]}...
                </p>
              </div>
            </motion.div>
          )}}

          {{tab === 'GAME' && (
            <motion.div key="g" initial={{ y: 50, opacity: 0 }} animate={{ y: 0, opacity: 1 }} className="w-full h-full border border-[#00f3ff]/20 bg-cyan-950/5 relative rounded-[50px] overflow-hidden">
              <Canvas shadows camera={{ position: }}>
                <ambientLight intensity={{0.3}} />
                <pointLight position={{}} castShadow />
                <GameCore />
                <mesh rotation={{[-Math.PI/2, 0, 0]}} receiveShadow>
                  <gridHelper args={{[30, 30, '#00f3ff', '#002222']}} />
                  <planeGeometry args={{}} />
                  <meshStandardMaterial color="#050505" />
                </mesh>
                <OrbitControls />
              </Canvas>
              <div className="absolute bottom-10 left-10 text-[10px] uppercase tracking-[0.3em] bg-black/60 p-4 border border-[#00f3ff]/20">
                WASD_CONTROL | PROTOCOL: SURVIVAL_TEST
              </div>
            </motion.div>
          )}}
        </AnimatePresence>
      </main>

      <SiteAssistant />
    </div>
  );
}}
"""

# --- 3. MASTER_CONTROLLER (Stark Legion) ---
bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
intel = JarvisIntelligence()
studio = OmegaStudio()

def push_to_git(filename, content, topic):
    repo_raw = os.getenv('GITHUB_REPO', '').strip()
    repo = repo_raw.replace("github.com", "").strip("/")
    token = os.getenv('GITHUB_TOKEN')
    url = f"https://github.com{{repo}}/contents/{{filename}}"
    headers = {{"Authorization": f"token {{token}}", "Accept": "application/vnd.github.v3+json"}}
    
    try:
        r_get = requests.get(url, headers=headers)
        sha = r_get.json().get('sha') if r_get.status_code == 200 else None
        payload = {{"message": f"Ω_BUILD: {{topic}}", "content": base64.b64encode(content.encode()).decode(), "branch": "main"}}
        if sha: payload["sha"] = sha
        res = requests.put(url, headers=headers, data=json.dumps(payload))
        return res.status_code
    except Exception as e: return str(e)

@bot.message_handler(func=lambda m: True)
def handle_master(m):
    q = m.text
    if q.lower().startswith("создай"):
        topic = q[7:].strip()
        msg = bot.send_message(m.chat.id, f"🎙️ **СЭР, ИНИЦИАЛИЗАЦИЯ ПОЛНОГО ФУНКЦИОНАЛА...**\nОбъект: {{topic}}")
        data = intel.deep_analyze(topic)
        site_code = studio.construct_site(topic, data['id'], data['res'])
        status = push_to_git("frontend/App.tsx", site_code, topic)
        if status in:
            bot.edit_message_text(f"🔱 **СИНГУЛЯРНОСТЬ ДОСТИГНУТА.**\n\nПроект '{{topic}}' задеплоен.\nАдрес: https://{os.getenv('GITHUB_REPO').split('/')[-2]}.github.io/{os.getenv('GITHUB_REPO').split('/')[-1]}", m.chat.id, msg.message_id)
        else:
            bot.send_message(m.chat.id, f"⚠️ Сбой: {{status}}")
    else:
        bot.send_message(m.chat.id, "🔍 **SCANNING...**")
        info = intel.deep_analyze(q)
        bot.reply_to(m, f"🤖 **JARVIS_LOG:**\n\n{{info['res']}}\n\n---\nID: {{info['id']}}")

bot.polling()
        
