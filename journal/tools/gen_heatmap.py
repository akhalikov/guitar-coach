#!/usr/bin/env python3
"""Regenerate practice-heatmap.html from the daily logs in this repo.

Usage:  python3 tools/gen_heatmap.py

Scans logs/<instrument>/<year>/<MM-DD>.md and writes a single self-contained
practice-heatmap.html (data baked in — opens by double-click, no server needed).
Weekly-review files (containing "week") are ignored; multiple sessions on one
day collapse to a single cell per instrument.
"""
import json
import os
import re
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTRUMENTS = ("classical", "electric", "acoustic")
DATE_RE = re.compile(r"^(?:(\d{4})-)?(\d{2})-(\d{2})(?:-\d+)?\.md$")


def scan():
    days = {}
    logs_root = os.path.join(REPO, "logs")
    for inst in INSTRUMENTS:
        inst_dir = os.path.join(logs_root, inst)
        if not os.path.isdir(inst_dir):
            continue
        for year in os.listdir(inst_dir):
            ydir = os.path.join(inst_dir, year)
            if not (os.path.isdir(ydir) and year.isdigit()):
                continue
            for fname in os.listdir(ydir):
                if "week" in fname:
                    continue
                m = DATE_RE.match(fname)
                if not m:
                    continue
                y = m.group(1) or year
                key = f"{y}-{m.group(2)}-{m.group(3)}"
                days.setdefault(key, set()).add(inst)
    return {k: sorted(days[k]) for k in sorted(days)}


HTML = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Guitar Practice — Contribution Graph</title>
<style>
:root{--bg:#0d1117;--panel:#161b22;--border:#30363d;--text:#e6edf3;--muted:#7d8590;
--empty:#21262d;--classical:#2f81f7;--acoustic:#3fb950;--electric:#f78166;--multi:#bc8cff;}
*{box-sizing:border-box;}body{margin:0;background:var(--bg);color:var(--text);
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;padding:32px 24px;}
.wrap{max-width:960px;margin:0 auto;}h1{font-size:20px;font-weight:600;margin:0 0 4px;}
.sub{color:var(--muted);font-size:13px;margin-bottom:24px;}
.card{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:20px;margin-bottom:20px;}
.stats{display:flex;flex-wrap:wrap;gap:28px;}.stat .num{font-size:26px;font-weight:700;}
.stat .lbl{font-size:12px;color:var(--muted);margin-top:2px;}
.graph-scroll{overflow-x:auto;padding-bottom:6px;}
table.cal{border-spacing:3px;border-collapse:separate;}table.cal td{width:13px;height:13px;padding:0;}
.cell{width:13px;height:13px;border-radius:3px;background:var(--empty);outline:1px solid rgba(255,255,255,.04);outline-offset:-1px;}
.cell.classical{background:var(--classical);}.cell.acoustic{background:var(--acoustic);}
.cell.electric{background:var(--electric);}.cell.multi{background:var(--multi);}
.cell.future{background:transparent;outline:none;}
.daylabel,.monlabel{color:var(--muted);font-size:10px;}
.daylabel{padding-right:6px;text-align:right;height:13px;}.monlabel{text-align:left;height:14px;font-size:11px;}
.legend{display:flex;align-items:center;gap:16px;margin-top:14px;flex-wrap:wrap;}
.legend .item{display:flex;align-items:center;gap:6px;font-size:12px;color:var(--muted);}
.sw{width:12px;height:12px;border-radius:3px;display:inline-block;}
.foot{color:var(--muted);font-size:11px;margin-top:8px;}
.tt{position:fixed;pointer-events:none;z-index:10;background:#1c2128;border:1px solid var(--border);
color:var(--text);font-size:12px;padding:6px 9px;border-radius:6px;white-space:nowrap;opacity:0;
transition:opacity .08s;transform:translate(-50%,-130%);}
</style></head><body>
<div class="wrap"><h1>\U0001F3B8 Guitar Practice</h1>
<div class="sub">Contribution graph — one cell per day, colored by instrument. Hover a cell for details.</div>
<div class="card"><div class="stats" id="stats"></div></div>
<div class="card"><div class="graph-scroll"><div id="graph"></div></div>
<div class="legend">
<div class="item"><span class="sw" style="background:var(--classical)"></span> Classical</div>
<div class="item"><span class="sw" style="background:var(--acoustic)"></span> Acoustic</div>
<div class="item"><span class="sw" style="background:var(--electric)"></span> Electric</div>
<div class="item"><span class="sw" style="background:var(--multi)"></span> Multiple</div>
<div class="item"><span class="sw" style="background:var(--empty)"></span> No practice</div>
</div><div class="foot" id="foot"></div></div></div>
<div class="tt" id="tt"></div>
<script>
const PAYLOAD = __PAYLOAD__;
const MONTHS=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
const DAYS=["","Mon","","Wed","","Fri",""];const pad=n=>String(n).padStart(2,"0");
const iso=d=>d.getFullYear()+"-"+pad(d.getMonth()+1)+"-"+pad(d.getDate());
const parse=s=>{const[y,m,dd]=s.split("-").map(Number);return new Date(y,m-1,dd);};
const classFor=i=>!i?"":(i.length>1?"multi":i[0]);
const DATA=PAYLOAD.days||{};const keys=Object.keys(DATA).sort();
if(keys.length){
const first=parse(keys[0]),lastLog=parse(keys[keys.length-1]),today=new Date();
const end=today>lastLog?today:lastLog;
const START=new Date(first.getFullYear(),first.getMonth(),1);
const END=new Date(end.getFullYear(),end.getMonth()+1,0);
const gs=new Date(START);gs.setDate(gs.getDate()-gs.getDay());
const weeks=[];let cur=new Date(gs);
while(cur<=END){const w=[];for(let i=0;i<7;i++){w.push(new Date(cur));cur.setDate(cur.getDate()+1);}weeks.push(w);}
let html='<table class="cal"><tr><td></td>';let lm=-1;
weeks.forEach(w=>{const f=w[0],m=f.getMonth();
if(m!==lm&&f<=END&&f.getDate()<=7){html+=`<td class="monlabel">${MONTHS[m]}</td>`;lm=m;}
else html+='<td class="monlabel"></td>';});html+='</tr>';
for(let dow=0;dow<7;dow++){html+=`<tr><td class="daylabel">${DAYS[dow]}</td>`;
weeks.forEach(w=>{const d=w[dow];
if(d<START||d>END){html+='<td><div class="cell future"></div></td>';return;}
const k=iso(d),ins=DATA[k],cls=classFor(ins);
const lab=ins?ins.map(s=>s[0].toUpperCase()+s.slice(1)).join(" + "):"No practice";
html+=`<td><div class="cell ${cls}" data-date="${k}" data-label="${lab}"></div></td>`;});
html+='</tr>';}html+='</table>';document.getElementById('graph').innerHTML=html;
const per={classical:0,acoustic:0,electric:0};keys.forEach(k=>DATA[k].forEach(i=>per[i]++));
let longest=0,run=0,prev=null;keys.forEach(k=>{const d=parse(k);
if(prev&&(d-prev)===86400000)run++;else run=1;longest=Math.max(longest,run);prev=d;});
const stats=[["Total practice days",keys.length],["Classical",per.classical],
["Acoustic",per.acoustic],["Electric",per.electric],["Longest daily streak",longest]];
document.getElementById('stats').innerHTML=stats.map(([l,n])=>
`<div class="stat"><div class="num">${n}</div><div class="lbl">${l}</div></div>`).join("");
document.getElementById('foot').textContent="Generated "+(PAYLOAD.generated||"");
const tt=document.getElementById('tt');
document.querySelectorAll('.cell[data-date]').forEach(c=>{
c.addEventListener('mousemove',e=>{const d=parse(c.dataset.date);
const p=d.toLocaleDateString(undefined,{weekday:'short',month:'short',day:'numeric',year:'numeric'});
tt.textContent=`${c.dataset.label} · ${p}`;tt.style.left=e.clientX+'px';
tt.style.top=e.clientY+'px';tt.style.opacity=1;});
c.addEventListener('mouseleave',()=>tt.style.opacity=0);});
}else{document.getElementById('graph').innerHTML="<p style='color:var(--muted)'>No practice logged yet.</p>";}
</script></body></html>
"""


def main():
    payload = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "days": scan(),
    }
    out = os.path.join(REPO, "practice-heatmap.html")
    html = HTML.replace("__PAYLOAD__", json.dumps(payload))
    with open(out, "w") as f:
        f.write(html)
    print(f"Wrote {out} — {len(payload['days'])} practice days")


if __name__ == "__main__":
    main()
