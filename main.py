import os, requests, random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# CONFIG
TG_TOKEN = os.getenv("TG_TOKEN")
TMDB_KEY = os.getenv("TMDB_KEY", "0d229e64116739f9aadacb61d9aff875")

class RealityCompiler:
    @staticmethod
    def analyze_universe(query):
        # Глубокий сбор данных для формирования геймплея
        tmdb = requests.get(f"https://themoviedb.org{TMDB_KEY}&query={query}&language=ru-RU").json()
        item = tmdb['results'][0] if tmdb.get('results') else {"id":0, "media_type":"movie", "title": query}
        
        # Определение жанровых механик (Железная логика)
        q = query.lower()
        if "поттер" in q or "магия" in q:
            mode, tool, task = "WIZARD", "WAND", "Изучите заклинание 'Lumos' и найдите выход из Тайной Комнаты."
        elif "лабиринт" in q or "бегущий" in q:
            mode, tool, task = "RUNNER", "MAP", "Стены закроются через 3 минуты. Найдите выход из сектора 7."
        elif "паук" in q or "marvel" in q:
            mode, tool, task = "HERO", "WEB", "Остановите ограбление и пролетите через город."
        else:
            mode, tool, task = "SURVIVOR", "SCANNER", f"Исследуйте аномалию {query} и соберите данные."

        return {
            "title": item.get('title') or item.get('name'),
            "desc": item.get('overview', "Засекречено ПОРОК."),
            "mode": mode,
            "tool": tool,
            "task": task,
            "id": item['id'],
            "accent": "#00f3ff" if mode == "RUNNER" else "#ffaa00" if mode == "WIZARD" else "#ff0044"
        }

    @staticmethod
    def generate_engine(ctx):
        return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>WCKD_REALITY: {ctx['title']}</title>
    <script src="https://tailwindcss.com"></script>
    <script src="https://cloudflare.com"></script>
    <script src="https://jsdelivr.net"></script>
    <style>
        body {{ margin: 0; background: #000; color: {ctx['accent']}; font-family: 'Syncopate', sans-serif; overflow: hidden; }}
        .hud {{ position: fixed; inset: 0; z-index: 100; pointer-events: none; }}
        .interactive {{ pointer-events: auto; }}
        .inventory-slot {{ border: 1px solid {ctx['accent']}; background: rgba(0,0,0,0.8); backdrop-filter: blur(10px); }}
        #joystick {{ position: fixed; bottom: 40px; left: 40px; width: 80px; height: 80px; border: 2px solid {ctx['accent']}; border-radius: 50%; }}
        .chat-msg {{ position: absolute; background: black; border: 1px solid white; padding: 2px 6px; border-radius: 4px; font-size: 10px; }}
    </style>
</head>
<body>
    <canvas id="render"></canvas>
    
    <div class="hud p-6 flex flex-col justify-between">
        <header class="flex justify-between items-start glass p-4 border border-{ctx['accent']}44 interactive">
            <div>
                <h1 class="text-xl font-black uppercase tracking-tighter italic">{ctx['title']}</h1>
                <p class="text-[9px] opacity-70 italic">MODE: {ctx['mode']}_CORE // PEERS: <span id="peers">1</span></p>
            </div>
            <div class="inventory-slot p-2 text-[10px]">
                EQUIPPED: {ctx['tool']}
            </div>
        </header>

        <div class="flex-1 flex flex-col items-center justify-center text-center">
            <div id="mission-ui" class="bg-black/80 border border-{ctx['accent']} p-4 max-w-xs transition-all">
                <p class="text-[10px] font-bold mb-2 uppercase">[ CURRENT_TASK ]</p>
                <p class="text-xs italic leading-tight">{ctx['task']}</p>
            </div>
        </div>

        <footer class="flex justify-between items-end">
            <div id="joystick" class="interactive"></div>
            <div class="interactive w-1/2">
                <input id="chat" type="text" placeholder="COMM_LINK..." class="w-full bg-black/80 border border-current p-2 text-[10px] outline-none">
            </div>
        </footer>
    </div>

    <script>
        const gun = Gun(['https://herokuapp.com']);
        const room = gun.get('WCKD_UNIVERSE_{ctx['id']}');
        const myId = 'SUBJ_' + Math.random().toString(36).substr(2, 4);

        // --- GRAPHICS ENGINE ---
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{ canvas: document.getElementById('render'), antialias: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);

        // Environment Generation based on Mode
        if("{ctx['mode']}" === "WIZARD") {{
            scene.fog = new THREE.FogExp2(0x110022, 0.05);
            // Генерация замка (математическая)
            for(let i=0; i<50; i++) {{
                const tower = new THREE.Mesh(new THREE.CylinderGeometry(1, 2, 10), new THREE.MeshBasicMaterial({{color: 0x222222, wireframe: true}}));
                tower.position.set(Math.sin(i)*30, 5, Math.cos(i)*30);
                scene.add(tower);
            }}
        }} else if ("{ctx['mode']}" === "RUNNER") {{
            // Логика лабиринта
            for(let i=0; i<100; i++) {{
                const wall = new THREE.Mesh(new THREE.BoxGeometry(4, 10, 4), new THREE.MeshBasicMaterial({{color: '{ctx['accent']}', wireframe: true}}));
                wall.position.set(Math.floor(Math.random()*20)*5 - 50, 5, Math.floor(Math.random()*20)*5 - 50);
                scene.add(wall);
            }}
        }}

        // Players & Sync
        const players = {{}};
        function addPlayer(id) {{
            const group = new THREE.Group();
            const body = new THREE.Mesh(new THREE.BoxGeometry(1, 2, 1), new THREE.MeshBasicMaterial({{color: '{ctx['accent']}'}}));
            group.add(body);
            const msgEl = document.createElement('div');
            msgEl.className = 'chat-msg';
            document.body.appendChild(msgEl);
            players[id] = {{ mesh: group, el: msgEl }};
            scene.add(group);
        }}

        // Movement & Logic
        let pos = {{ x: 0, z: 0 }};
        window.addEventListener('touchmove', (e) => {{
            pos.x += (e.touches[0].clientX - window.innerWidth/2) * 0.0001;
            pos.z += (e.touches[0].clientY - window.innerHeight/2) * 0.0001;
        }});

        function loop() {{
            camera.position.x = pos.x;
            camera.position.z = pos.z;
            camera.position.y = 2;
            
            room.get(myId).put({{ x: pos.x, z: pos.z, m: document.getElementById('chat').value }});
            
            room.map().on((data, id) => {{
                if(!players[id]) addPlayer(id);
                if(data) {{
                    players[id].mesh.position.set(data.x, 1, data.z);
                    const p = players[id].mesh.position.clone().project(camera);
                    players[id].el.style.left = (p.x + 1) * window.innerWidth / 2 + 'px';
                    players[id].el.style.top = (-p.y + 1) * window.innerHeight / 2 + 'px';
                    players[id].el.innerText = id.substr(5) + ": " + (data.m || '...');
                }}
            }});

            renderer.render(scene, camera);
            requestAnimationFrame(loop);
        }}
        
        addPlayer(myId);
        loop();
    </script>
</body>
</html>
"""

    @staticmethod
    async def run(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.message.text
        await update.message.reply_text(f"🌌 [WCKD_ARCHITECT]: Компиляция реальности '{query}'...")
        
        ctx = RealityCompiler.analyze_universe(query)
        html = RealityCompiler.generate_engine(ctx)
        
        filename = f"{query.replace(' ', '_')}_REALITY.html"
        with open(filename, "w", encoding="utf-8") as f: f.write(html)
        
        await update.message.reply_document(
            document=open(filename, "rb"),
            caption=f"✅ **РЕАЛЬНОСТЬ СФОРМИРОВАНА**\n\n• **Режим:** {ctx['mode']}\n• **Задача:** {ctx['task']}\n• **Инструмент:** {ctx['tool']}\n\nСкинь файл другу, чтобы проходить сюжет вместе!"
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TG_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), RealityCompiler.run))
    app.run_polling()
      
