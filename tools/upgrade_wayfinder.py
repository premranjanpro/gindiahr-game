from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = r'''
/* WAYFINDER ADVANCED MOBILE / DESKTOP MODE */
.wf-advanced-ui{display:grid;grid-template-columns:1fr 250px;gap:12px;align-items:stretch}
.wf-board{position:relative;min-width:0}
.wf-side{background:linear-gradient(180deg,#ecfdf5,#d1fae5);border:2px solid #a7f3d0;border-radius:18px;padding:12px;display:flex;flex-direction:column;gap:10px}
.wf-stat-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}
.wf-stat{background:#fff;border-radius:12px;padding:8px;text-align:center;border:1px solid #d1fae5;font-size:11px}
.wf-stat b{display:block;font-size:18px;color:#047857}
.wf-mini-actions{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.wf-action{border:0;border-radius:12px;padding:10px;font-weight:900;cursor:pointer;background:#059669;color:#fff;touch-action:manipulation}
.wf-action.secondary{background:#fff;color:#047857;border:2px solid #a7f3d0}
.wf-board canvas{width:100%;height:auto;aspect-ratio:1/1;touch-action:none;display:block}
.wf-mobile-controls{display:none}
.wf-fullscreen{position:fixed!important;inset:0!important;width:100vw!important;height:100dvh!important;max-width:none!important;max-height:none!important;border-radius:0!important;padding:10px!important;z-index:20000!important;background:#052e24!important}
.wf-fullscreen .wf-fs-body{height:calc(100dvh - 48px);min-height:0;display:flex;align-items:center;justify-content:center}
.wf-fullscreen .wf-advanced-ui{width:min(1100px,100%);height:100%;grid-template-columns:minmax(0,1fr) 240px}
.wf-fullscreen .wf-board canvas{max-height:calc(100dvh - 70px);width:auto;max-width:100%;margin:auto}
.wf-fs-top{display:flex;justify-content:space-between;align-items:center;color:#fff;height:38px}
.wf-fs-top button{border:0;background:#ffffff22;color:#fff;border-radius:10px;padding:8px 12px;font-weight:800}
@media(max-width:760px){
 .wf-advanced-ui{display:flex;flex-direction:column;gap:8px}
 .wf-side{order:2;padding:7px;border-radius:14px;gap:6px}
 .wf-board{order:1}
 .wf-board canvas{max-height:42dvh;object-fit:contain;background:#ecfdf5}
 .wf-stat-grid{grid-template-columns:repeat(4,1fr);gap:5px}
 .wf-stat{padding:5px 2px;font-size:10px}
 .wf-stat b{font-size:15px}
 .wf-mini-actions{grid-template-columns:repeat(4,1fr);gap:5px}
 .wf-action{padding:8px 4px;font-size:11px}
 .wf-mobile-controls{display:grid;grid-template-columns:repeat(3,48px);grid-template-rows:repeat(2,42px);gap:5px;justify-content:center}
 .wf-mobile-controls button{border:2px solid #a7f3d0;border-radius:11px;background:#fff;color:#047857;font-size:20px;font-weight:900;touch-action:none}
 .wf-mobile-controls button:active{background:#10b981;color:#fff;transform:scale(.94)}
 .wf-fullscreen .wf-advanced-ui{height:calc(100dvh - 48px);display:flex}
 .wf-fullscreen .wf-board{flex:1;display:flex;align-items:center;justify-content:center}
 .wf-fullscreen .wf-board canvas{max-height:calc(100dvh - 190px);max-width:100%;width:auto}
 .wf-fullscreen .wf-side{flex:0 0 auto}
}
@media(max-height:650px) and (max-width:760px){
 .wf-fullscreen .wf-board canvas{max-height:calc(100dvh - 145px)}
 .wf-side{display:grid;grid-template-columns:1fr auto;align-items:center}
 .wf-stat-grid{grid-column:1/-1}
 .wf-mini-actions{grid-column:1}
 .wf-mobile-controls{grid-column:2;grid-row:1/3}
}
'''

if 'WAYFINDER ADVANCED MOBILE / DESKTOP MODE' not in s:
    s = s.replace('</style>', css + '\n</style>', 1)

start = s.index('<!-- WAY FINDER MAZE MODAL -->')
old = '''<div class="game-area">\n                <div class="level-pills">'''
new = '''<div class="game-area">\n                <div class="wf-fs-top" style="display:none" id="wf-fs-top">\n                    <strong>🧭 Way Finder • Adventure Mode</strong>\n                    <button onclick="toggleMazeFullscreen()">✕ Exit</button>\n                </div>\n                <div class="level-pills">'''
pos = s.index(old, start)
s = s[:pos] + s[pos:].replace(old, new, 1)

old_ui = '''<div class="wayfinder-wrap" id="wayfinder-wrap">\n                    <canvas id="wayfinder-canvas" width="380" height="380"></canvas>\n                </div>\n                <div class="feedback" id="maze-feedback" style="margin-top:8px;"></div>\n                \n                <!-- MOBILE D-PAD -->\n                <div class="dpad-container">\n                    <button class="dpad-btn dpad-up" onclick="moveMazePlayer(0, -1)" aria-label="Up">⬆️</button>\n                    <button class="dpad-btn dpad-left" onclick="moveMazePlayer(-1, 0)" aria-label="Left">⬅️</button>\n                    <button class="dpad-btn dpad-center" onclick="showMazeAIHint()" title="AI Hint">💡</button>\n                    <button class="dpad-btn dpad-right" onclick="moveMazePlayer(1, 0)" aria-label="Right">➡️</button>\n                    <button class="dpad-btn dpad-down" onclick="moveMazePlayer(0, 1)" aria-label="Down">⬇️</button>\n                </div>\n\n                <div style="display:flex; gap:10px; margin-top:12px;">\n                    <button class="start-btn" onclick="showMazeAIHint()" style="background:#059669; flex:1; font-size:15px; padding:10px;">🤖 AI Shortest Path Hint</button>\n                    <button class="start-btn" onclick="initMazeGame()" style="background:#E2E8F0; color:var(--text); flex:1; font-size:15px; padding:10px;">🔄 New Maze</button>\n                </div>'''
new_ui = '''<div class="wf-advanced-ui">\n                    <div class="wf-board">\n                        <div class="wayfinder-wrap" id="wayfinder-wrap">\n                            <canvas id="wayfinder-canvas" width="380" height="380"></canvas>\n                        </div>\n                    </div>\n                    <aside class="wf-side">\n                        <div class="wf-stat-grid">\n                            <div class="wf-stat">🐾<b id="wf-stat-steps">0</b><span>Steps</span></div>\n                            <div class="wf-stat">⏱️<b id="wf-stat-time">0</b><span>Time</span></div>\n                            <div class="wf-stat">🦴<b id="wf-stat-treats">0/3</b><span>Treats</span></div>\n                            <div class="wf-stat">🔥<b id="wf-stat-best">—</b><span>Best</span></div>\n                        </div>\n                        <div class="wf-mini-actions">\n                            <button class="wf-action" onclick="showMazeAIHint()">🤖 Hint</button>\n                            <button class="wf-action secondary" onclick="initMazeGame()">🔄 New</button>\n                            <button class="wf-action secondary" onclick="toggleMazeFullscreen()">⛶ Full</button>\n                            <button class="wf-action secondary" onclick="mazeAutoSolveStep()">✨ Assist</button>\n                        </div>\n                        <div class="wf-mobile-controls" aria-label="Maze controls">\n                            <button style="grid-column:2" onclick="moveMazePlayer(0,-1)">⬆️</button>\n                            <button onclick="moveMazePlayer(-1,0)">⬅️</button>\n                            <button onclick="moveMazePlayer(1,0)">➡️</button>\n                            <button style="grid-column:2" onclick="moveMazePlayer(0,1)">⬇️</button>\n                        </div>\n                        <div class="feedback" id="maze-feedback">🐶 Find the way home!</div>\n                    </aside>\n                </div>'''
pos = s.index(old_ui, start)
s = s[:pos] + s[pos:].replace(old_ui, new_ui, 1)

needle = '        function moveMazePlayer(dc, dr) {'
helpers = '''        function updateMazeAdvancedStats() {\n            const values = [\n                document.getElementById('maze-steps')?.textContent || '0',\n                document.getElementById('maze-time')?.textContent || '0',\n                document.getElementById('maze-treats')?.textContent || '0/3',\n                localStorage.getItem('gindia_maze_best_' + mazeCols) || '—'\n            ];\n            ['wf-stat-steps','wf-stat-time','wf-stat-treats','wf-stat-best'].forEach((id,i)=>{\n                const el=document.getElementById(id); if(el) el.textContent=values[i];\n            });\n        }\n        function toggleMazeFullscreen(){\n            const modal=document.getElementById('modal-wayfinder');\n            const top=document.getElementById('wf-fs-top');\n            if(!modal) return;\n            modal.classList.toggle('wf-fullscreen');\n            if(top) top.style.display=modal.classList.contains('wf-fullscreen')?'flex':'none';\n            document.body.style.overflow='hidden';\n            setTimeout(()=>drawMaze(),50);\n        }\n        function mazeAutoSolveStep(){\n            if(!mazeRunning) return;\n            if(!mazeHintPath.length) showMazeAIHint();\n            if(mazeHintPath.length>1){\n                const [nr,nc]=mazeHintPath[1];\n                moveMazePlayer(nc-mazePlayer.c,nr-mazePlayer.r);\n            }\n        }\n\n''' + needle
if 'function updateMazeAdvancedStats()' not in s:
    s = s.replace(needle, helpers, 1)

s = s.replace('''            cellSize = Math.floor(mazeCanvas.width / mazeCols);''', '''            cellSize = Math.floor(mazeCanvas.width / mazeCols);\n            mazeCanvas.style.touchAction = 'none';''', 1)
s = s.replace("document.getElementById('maze-treats').textContent = `0/${mazeTreats.length}`;", "document.getElementById('maze-treats').textContent = `0/${mazeTreats.length}`;\n            updateMazeAdvancedStats();", 1)
s = s.replace("document.getElementById('maze-time').textContent = mazeTimer;", "document.getElementById('maze-time').textContent = mazeTimer;\n                    updateMazeAdvancedStats();", 1)
s = s.replace("document.getElementById('maze-steps').textContent = mazeSteps;", "document.getElementById('maze-steps').textContent = mazeSteps;\n                updateMazeAdvancedStats();", 1)
s = s.replace("mazeVictory();\n                }", "mazeVictory();\n                }\n                updateMazeAdvancedStats();", 1)
s = s.replace("const stars = collectedCount === 3 ? '⭐⭐⭐' : collectedCount >= 1 ? '⭐⭐' : '⭐';", "const stars = collectedCount === 3 ? '⭐⭐⭐' : collectedCount >= 1 ? '⭐⭐' : '⭐';\n            const bestKey='gindia_maze_best_'+mazeCols;\n            const oldBest=parseInt(localStorage.getItem(bestKey)||'999999',10);\n            if(mazeSteps<oldBest) localStorage.setItem(bestKey,String(mazeSteps));\n            updateMazeAdvancedStats();", 1)

# Disable browser scrolling while interacting with the maze and add pointer swipe/tap controls.
s = s.replace("mazeCanvas.ontouchstart = (e) => {\n                const t = e.touches[0];", "mazeCanvas.ontouchstart = (e) => { e.preventDefault();\n                const t = e.touches[0];", 1)
s = s.replace("mazeCanvas.ontouchmove = (e) => {\n                if (!mazeTouchStart) return;", "mazeCanvas.ontouchmove = (e) => { e.preventDefault();\n                if (!mazeTouchStart) return;", 1)
s = s.replace("mazeCanvas.ontouchend = () => { mazeTouchStart = null; };", "mazeCanvas.ontouchend = (e) => { if(e) e.preventDefault(); mazeTouchStart = null; };\n            mazeCanvas.ontouchcancel = () => { mazeTouchStart = null; };\n            let mazePointerStart=null;\n            mazeCanvas.onpointerdown=(e)=>{ mazePointerStart={x:e.clientX,y:e.clientY}; mazeCanvas.setPointerCapture?.(e.pointerId); };\n            mazeCanvas.onpointerup=(e)=>{\n                if(!mazePointerStart) return;\n                const dx=e.clientX-mazePointerStart.x, dy=e.clientY-mazePointerStart.y;\n                if(Math.max(Math.abs(dx),Math.abs(dy))>22){\n                    if(Math.abs(dx)>Math.abs(dy)) moveMazePlayer(dx>0?1:-1,0);\n                    else moveMazePlayer(0,dy>0?1:-1);\n                } else {\n                    const rect=mazeCanvas.getBoundingClientRect();\n                    const x=(e.clientX-rect.left)*(mazeCanvas.width/rect.width);\n                    const y=(e.clientY-rect.top)*(mazeCanvas.height/rect.height);\n                    const c=Math.floor(x/cellSize), r=Math.floor(y/cellSize);\n                    const dc=c-mazePlayer.c, dr=r-mazePlayer.r;\n                    if(Math.abs(dc)+Math.abs(dr)===1) moveMazePlayer(dc,dr);\n                }\n                mazePointerStart=null;\n            };\n            mazeCanvas.onpointercancel=()=>{mazePointerStart=null;};", 1)

p.write_text(s, encoding='utf-8')
print('Way Finder upgrade applied')
