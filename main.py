import os, requests, random, time
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Загрузка конфигов из Railway Variables
TG_TOKEN = os.getenv("TG_TOKEN")
TMDB_KEY = os.getenv("TMDB_KEY")

class UniverseArchitect:
    @staticmethod
    def get_film_dna(query):
        """Извлекает 'ДНК' запроса для генерации уникальных функций"""
        url = f"https://themoviedb.org{TMDB_KEY}&query={query}&language=ru-RU"
        res = requests.get(url).json()
        item = res['results'][0] if res.get('results') else {"id": random.randint(1,999), "title": query, "media_type":"movie"}
        
        # Генерация уникальных параметров на основе ID и названия
        random.seed(item['id'])
        gravity = random.uniform(0.5, 2.0)
        complexity = random.randint(30, 100)
        
        # Логика уникальных функций (AI-Director)
        q = query.lower()
        if "поттер" in q:
            mode, event = "WIZARD_OS", "Dementor Attack"
        elif "лабиринт" in q:
            mode, event = "MAZE_RUNNER", "Wall Shift"
        elif "человек" in q:
            mode, event = "HERO_SYNC", "Villain Ambush"
        else:
            mode, event = "SURVIVAL_CORE", "System Glitch"

        return {
            "title": item.get('title') or item.get('name'),
            "id": item['id'],
            "gravity": gravity,
            "complexity": complexity,
            "mode": mode,
            "event": event,
            "color": "#%06x" % random.randint(0, 0xFFFFFF),
            "desc": item.get('overview', 'No data available.')[:300]
        }

    @staticmethod
    def compile_world(dna):
        """Генерирует монолитный HTML/JS мир с AI-Директором"""
        return f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>EMPEROR_{dna['id']}</title>
    <script src="https://tailwindcss.com"></script>
    <script src="https://cloudflare.com"></script>
    <script src="https://jsdelivr.net"></script>
    <style>
        body {{ margin: 0; background: #000; color: {dna['color']}; font-family: 'Courier New', monospace; overflow: hidden; }}
        .hud {{ position: fixed; inset: 0; z-index: 100; pointer-events: none; }}
        .interactive {{ pointer-events: auto; }}
        .glass {{ background: rgba(0,0,0,0.9); backdrop-filter: blur(20px); border: 1px solid {dna['color']}44; }}
        #event-log {{ position: fixed; top: 100px; left: 50%; transform: translateX(-50%); color: white; background: red; padding: 5px 15px; display: none; font-size: 12px; font-weight: bold; }}
    </style>
</head>
<body>
    <canvas id="stage"></canvas>
    <div id="event-log">WARNING: {dna['event'].upper()} INITIATED!</div>

    <div class="hud p-4 flex flex-col justify-between">
        <header class="flex justify-between glass p-4 interactive">
            <div>
                <h1 class="text-xl font-black uppercase italic tracking-tighter">{dna['title']}</h1>
                <p class="text-[8px] opacity-60">MODE: {dna['mode']} // GRAVITY: {dna['gravity']}</p>
            </div>
            <div id="peers-count" class="text-[10px]">SYNCING_PEERS...</div>
        </header>

        <main class="flex-1 flex flex-col items-center justify-center">
            <div class="glass p-6 border border-{dna['color']} text-[10px] max-w-xs text-center">
                <p class="font-bold mb-2 uppercase italic text-lg">[ MISSION ]</p>
                <p class="leading-tight opacity-80 italic">"{dna['desc']}"</p>
            </div>
        </main>

        <footer class="interactive grid grid-cols-2 gap-2">
            <input id="chat" type="text" placeholder="COMMAND_LINK..." class="bg-black/80 border border-current p-4 text-[10px] outline-none">
            <button onclick="performAction()" class="bg-current text-black font-black uppercase italic text-[10px]">EXECUTE_ACTION</button>
        </footer>
    </div>

    <script>
        const gun = Gun(['https://herokuapp.com']);
        const room = gun.get('EMPEROR_WORLD_{dna['id']}');
        const myId = 'USR_' + Math.random().toString(36).substr(2, 4);

        // --- 3D ENGINE ---
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{ canvas: document.getElementById('stage'), antialias: true, alpha: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);

        // Процедурная генерация ландшафта (БЕЗ ШАБЛОНОВ)
        const geometry = new THREE.BoxGeometry(2, 2, 2);
        const material = new THREE.MeshBasicMaterial({{ color: '{dna['color']}', wireframe: true }});
        for(let i=0; i<{dna['complexity']}; i++) {{
            const box = new THREE.Mesh(geometry, material);
            box.position.set(Math.tan(i)*20, Math.sin(i*0.5)*10, Math.cos(i)*20);
            scene.add(box);
        }}

        // AI-Director Event System
        setInterval(() => {{
            const log = document.getElementById('event-log');
            log.style.display = 'block';
            setTimeout(() => log.style.display = 'none', 3000);
            // Визуальный эффект события
            scene.rotation.y += 0.5;
        }}, 15000);

        // Movement
        let move = {{ x: 0, z: 20 }};
        window.addEventListener('touchmove', (e) => {{
            move.x = (e.touches[0].clientX - window.innerWidth/2) * 0.05;
            move.z = (e.touches[0].clientY - window.innerHeight/2) * 0.05;
        }});

        function loop() {{
            camera.position.x += (move.x - camera.position.x) * 0.1;
            camera.position.z += (move.z - camera.position.z) * 0.1;
            camera.lookAt(0,0,0);
            
            room.get(myId).put({{ x: camera.position.x, z: camera.position.z, msg: document.getElementById('chat').value }});
            renderer.render(scene, camera);
            requestAnimationFrame(loop);
        }}

        function performAction() {{
            alert("ACTION_EXECUTED: {dna['mode']}");
        }}

        loop();
    </script>
</body>
</html>
"""

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    # Отправляем статус "Печатает" для реалистичности
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    try:
        dna = UniverseArchitect.get_film_dna(query)
        html_code = UniverseArchitect.compile_world(dna)
        
        filename = f"EMPEROR_{dna['id']}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_code)
        
        await update.message.reply_document(
            document=open(filename, "rb"),
            caption=f"🏆 **РЕАЛЬНОСТЬ КОНФИГУРИРОВАНА**\n\n🪐 **Мир:** {dna['title']}\n🎭 **Режим:** {dna['mode']}\n⚠️ **Событие:** {dna['event']}\n\n_Мультиплеер и AI-Директор активированы. Открой файл в браузере._"
        )
        os.remove(filename)
    except Exception as e:
        await update.message.reply_text(f"🚧 Ошибка архитектуры: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TG_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("EMPEROR SYSTEM ONLINE")
    app.run_polling()
        
