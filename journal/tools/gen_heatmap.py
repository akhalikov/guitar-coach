#!/usr/bin/env python3
"""Regenerate practice-heatmap.html from the daily logs in this repo.

Usage:  python3 tools/gen_heatmap.py

Scans logs/<instrument>/<year>/<MM-DD>.md and writes a single self-contained
practice-heatmap.html (data baked in — opens by double-click, no server needed).
Weekly-review files (containing "week") are ignored; multiple sessions on one
day collapse to a single cell per instrument. The page shows one calendar year
at a time with GitHub-style year buttons (floor: 2026).
"""
import json
import os
import re
from datetime import datetime, timezone, date, timedelta

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTRUMENTS = ("classical", "electric", "acoustic")
DATE_RE = re.compile(r"^(?:(\d{4})-)?(\d{2})-(\d{2})(?:-\d+)?\.md$")
FLOOR_YEAR = 2025  # earliest year button


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


def scan_lessons():
    """Read journal/lessons.txt — 'YYYY-MM-DD instrument[,instrument]' per line.

    Returns {date: [instruments]}. '#' comments and blank lines ignored.
    """
    path = os.path.join(REPO, "lessons.txt")
    lessons = {}
    if os.path.isfile(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split()
                date = parts[0]
                if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
                    continue
                insts = []
                if len(parts) > 1:
                    insts = [x.strip() for x in parts[1].split(",") if x.strip() in INSTRUMENTS]
                lessons[date] = sorted(set(insts))
    return {k: lessons[k] for k in sorted(lessons)}


SVG_COLORS = {
    "empty": "#21262d", "classical": "#2f81f7", "acoustic": "#3fb950",
    "electric": "#f78166", "multi": "#bc8cff", "lesson": "#e3b341",
    "bg": "#0d1117", "muted": "#7d8590", "text": "#e6edf3",
}
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def _class_for(insts):
    if not insts:
        return "empty"
    return "multi" if len(insts) > 1 else insts[0]


def render_svg(days, lessons):
    """Static SVG snapshot of the trailing 12 months — embeddable in markdown."""
    end = date.today()
    start = end - timedelta(days=364)
    gs = start - timedelta(days=(start.weekday() + 1) % 7)  # back to Sunday
    weeks, cur = [], gs
    while cur <= end:
        weeks.append([cur + timedelta(days=i) for i in range(7)])
        cur += timedelta(days=7)

    cell, step, left, top = 11, 14, 32, 34
    width = left + len(weeks) * step + 16
    grid_h = 7 * step
    legend_y = top + grid_h + 16
    height = legend_y + 20

    n = len([k for k in days if start <= date.fromisoformat(k) <= end])
    act = sorted({date.fromisoformat(k) for k in list(days) + list(lessons)
                  if start <= date.fromisoformat(k) <= end})
    longest = run = 0
    prev = None
    for d in act:
        run = run + 1 if (prev and (d - prev).days == 1) else 1
        longest = max(longest, run)
        prev = d
    title = (f'{n} practice day{"" if n == 1 else "s"} in the last year'
             f' · longest streak {longest} day{"" if longest == 1 else "s"}')
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
         f'viewBox="0 0 {width} {height}" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">',
         f'<rect width="{width}" height="{height}" rx="10" fill="{SVG_COLORS["bg"]}"/>',
         f'<text x="{left}" y="18" fill="{SVG_COLORS["text"]}" font-size="12" font-weight="600">{title}</text>']

    last_m = -1
    for wi, wk in enumerate(weeks):
        labm = -1
        for d in wk:
            if start <= d <= end and d.day == 1:
                labm = d.month - 1
                break
        if labm < 0 and wi == 0:
            labm = start.month - 1
        if labm >= 0 and labm != last_m:
            p.append(f'<text x="{left + wi * step}" y="{top - 6}" fill="{SVG_COLORS["muted"]}" font-size="9">{MONTHS[labm]}</text>')
            last_m = labm

    for dow, lab in [(1, "Mon"), (3, "Wed"), (5, "Fri")]:
        y = top + dow * step + cell - 1
        p.append(f'<text x="{left - 6}" y="{y}" fill="{SVG_COLORS["muted"]}" font-size="9" text-anchor="end">{lab}</text>')

    for wi, wk in enumerate(weeks):
        for dow, d in enumerate(wk):
            if d < start or d > end:
                continue
            key = d.isoformat()
            uni = sorted(set(days.get(key, [])) | set(lessons.get(key) or []))
            fill = SVG_COLORS[_class_for(uni)]
            x, y = left + wi * step, top + dow * step
            ring = f' stroke="{SVG_COLORS["lesson"]}" stroke-width="1.6"' if lessons.get(key) else ""
            p.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{fill}"{ring}/>')

    lx = left
    for key, label in [("classical", "Classical"), ("acoustic", "Acoustic"),
                       ("electric", "Electric"), ("multi", "Multiple")]:
        p.append(f'<rect x="{lx}" y="{legend_y}" width="10" height="10" rx="2" fill="{SVG_COLORS[key]}"/>')
        p.append(f'<text x="{lx + 14}" y="{legend_y + 9}" fill="{SVG_COLORS["muted"]}" font-size="9">{label}</text>')
        lx += 14 + len(label) * 6 + 14
    p.append(f'<rect x="{lx}" y="{legend_y}" width="10" height="10" rx="2" fill="{SVG_COLORS["empty"]}" stroke="{SVG_COLORS["lesson"]}" stroke-width="1.6"/>')
    p.append(f'<text x="{lx + 14}" y="{legend_y + 9}" fill="{SVG_COLORS["muted"]}" font-size="9">Lesson</text>')
    p.append("</svg>")
    return "\n".join(p) + "\n"


HTML = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Guitar Practice — Contribution Graph</title>
<style>
:root{--bg:#0d1117;--panel:#161b22;--border:#30363d;--text:#e6edf3;--muted:#7d8590;
--empty:#21262d;--classical:#2f81f7;--acoustic:#3fb950;--electric:#f78166;--multi:#bc8cff;--accent:#2f81f7;--lesson:#e3b341;}
*{box-sizing:border-box;}body{margin:0;background:var(--bg);color:var(--text);
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;padding:32px 24px;}
.wrap{max-width:1000px;margin:0 auto;}h1{font-size:20px;font-weight:600;margin:0 0 4px;}
.sub{color:var(--muted);font-size:13px;margin-bottom:24px;}
.card{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:20px;margin-bottom:20px;}
.stats{display:flex;flex-wrap:wrap;gap:28px;}.stat .num{font-size:26px;font-weight:700;}
.stat .lbl{font-size:12px;color:var(--muted);margin-top:2px;}
.ytitle{font-size:14px;font-weight:600;margin:0 0 14px;}
.calrow{display:flex;gap:16px;align-items:flex-start;}
.calmain{min-width:0;flex:1;}
.graph-scroll{overflow-x:auto;padding-bottom:6px;}
table.cal{border-spacing:2px;border-collapse:separate;}table.cal td{width:11px;height:11px;padding:0;}
.cell{width:11px;height:11px;border-radius:2px;background:var(--empty);outline:1px solid rgba(255,255,255,.04);outline-offset:-1px;}
.cell.classical{background:var(--classical);}.cell.acoustic{background:var(--acoustic);}
.cell.electric{background:var(--electric);}.cell.multi{background:var(--multi);}
.cell.lesson{box-shadow:inset 0 0 0 2px var(--lesson);}
.cell.future{background:transparent;outline:none;box-shadow:none;}
.daylabel,.monlabel{color:var(--muted);font-size:10px;}
.daylabel{padding-right:6px;text-align:right;height:11px;}
.monlabel{position:relative;text-align:left;height:14px;font-size:11px;overflow:visible;}
.monlabel span{position:absolute;left:0;top:0;white-space:nowrap;}
.years{display:flex;flex-direction:column;gap:4px;flex:0 0 auto;}
button.yr{all:unset;cursor:pointer;padding:5px 16px;border-radius:7px;font-size:13px;color:var(--text);text-align:center;min-width:56px;}
button.yr:hover{background:#ffffff0d;}
button.yr.active{background:var(--accent);color:#fff;font-weight:600;}
.legend{display:flex;align-items:center;gap:16px;margin-top:14px;flex-wrap:wrap;}
.legend .item{display:flex;align-items:center;gap:6px;font-size:12px;color:var(--muted);}
.sw{width:12px;height:12px;border-radius:3px;display:inline-block;}
.foot{color:var(--muted);font-size:10px;margin-top:10px;text-align:right;}
.tt{position:fixed;pointer-events:none;z-index:10;background:#1c2128;border:1px solid var(--border);
color:var(--text);font-size:12px;padding:6px 9px;border-radius:6px;white-space:nowrap;opacity:0;
transition:opacity .08s;transform:translate(-50%,-130%);}
</style></head><body>
<div class="wrap"><h1>\U0001F3B8 Guitar Practice</h1>
<div class="sub">Contribution graph — one cell per day, colored by instrument. Hover a cell for details.</div>
<div class="card">
<div class="ytitle" id="ytitle"></div>
<div class="calrow">
<div class="calmain">
<div class="graph-scroll"><div id="graph"></div></div>
<div class="legend">
<div class="item"><span class="sw" style="background:var(--classical)"></span> Classical</div>
<div class="item"><span class="sw" style="background:var(--acoustic)"></span> Acoustic</div>
<div class="item"><span class="sw" style="background:var(--electric)"></span> Electric</div>
<div class="item"><span class="sw" style="background:var(--multi)"></span> Multiple</div>
<div class="item"><span class="sw" style="box-shadow:inset 0 0 0 2px var(--lesson);background:var(--empty)"></span> Lesson with teacher</div>
<div class="item"><span class="sw" style="background:var(--empty)"></span> No practice</div>
</div>
</div>
<div class="years" id="years"></div>
</div>
<div class="foot" id="foot"></div>
</div></div>
<div class="tt" id="tt"></div>
<script>
const PAYLOAD = __PAYLOAD__;
const FLOOR_YEAR = __FLOOR__;
const MONTHS=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
const DAYS=["","Mon","","Wed","","Fri",""];const pad=n=>String(n).padStart(2,"0");
const iso=d=>d.getFullYear()+"-"+pad(d.getMonth()+1)+"-"+pad(d.getDate());
const parse=s=>{const[y,m,dd]=s.split("-").map(Number);return new Date(y,m-1,dd);};
const classFor=i=>!i?"":(i.length>1?"multi":i[0]);
const cap=s=>s[0].toUpperCase()+s.slice(1);
const DATA=PAYLOAD.days||{};
const LESSONS=PAYLOAD.lessons||{};
const keys=Object.keys(DATA).sort();
const tt=document.getElementById('tt');

// Year buttons: FLOOR_YEAR .. max(current year, latest data year), newest first
const nowY=new Date().getFullYear();
const dataYears=keys.map(k=>+k.slice(0,4));
const maxY=Math.max(nowY, ...(dataYears.length?dataYears:[nowY]), FLOOR_YEAR);
const years=[];for(let y=maxY;y>=FLOOR_YEAR;y--)years.push(y);

function renderRange(START,END,period){
  const gs=new Date(START);gs.setDate(gs.getDate()-gs.getDay());
  const weeks=[];let cur=new Date(gs);
  while(cur<=END){const w=[];for(let i=0;i<7;i++){w.push(new Date(cur));cur.setDate(cur.getDate()+1);}weeks.push(w);}
  let html='<table class="cal"><tr><td></td>';let lm=-1;
  weeks.forEach((w,wi)=>{
    let labM=-1;
    for(const d of w){if(d>=START&&d<=END&&d.getDate()===1){labM=d.getMonth();break;}}
    if(labM<0&&wi===0)labM=START.getMonth();
    if(labM>=0&&labM!==lm){html+=`<td class="monlabel"><span>${MONTHS[labM]}</span></td>`;lm=labM;}
    else html+='<td class="monlabel"></td>';});
  html+='</tr>';
  for(let dow=0;dow<7;dow++){html+=`<tr><td class="daylabel">${DAYS[dow]}</td>`;
    weeks.forEach(w=>{const d=w[dow];
      if(d<START||d>END){html+='<td><div class="cell future"></div></td>';return;}
      const k=iso(d),pins=DATA[k]||[],lins=LESSONS[k],isL=!!lins;
      const uni=[...new Set([...pins,...(lins||[])])];
      let cls=classFor(uni.length?uni:null);if(isL)cls+=(cls?' ':'')+'lesson';
      const names=uni.map(cap).join(" + ");
      const lab=uni.length?(isL?names+" · Lesson with teacher":names):"No practice";
      html+=`<td><div class="cell ${cls}" data-date="${k}" data-label="${lab}"></div></td>`;});
    html+='</tr>';}
  html+='</table>';
  document.getElementById('graph').innerHTML=html;

  // Stats over [START,END]
  const inWin=k=>{const d=parse(k);return d>=START&&d<=END;};
  const wk=keys.filter(inWin);
  const per={classical:0,acoustic:0,electric:0};
  wk.forEach(k=>DATA[k].forEach(i=>per[i]++));
  const lk=Object.keys(LESSONS).filter(inWin);
  const active=[...new Set([...wk,...lk])].sort();
  let longest=0,run=0,prev=null;
  active.forEach(k=>{const d=parse(k);if(prev&&(d-prev)===86400000)run++;else run=1;longest=Math.max(longest,run);prev=d;});
  const sTxt=wk.length===1?'':'s',lsTxt=longest===1?'':'s';
  document.getElementById('ytitle').textContent=
    `${wk.length} practice day${sTxt} in ${period} · longest streak ${longest} day${lsTxt}`;

  document.querySelectorAll('.cell[data-date]').forEach(c=>{
    c.addEventListener('mousemove',e=>{const d=parse(c.dataset.date);
      const p=d.toLocaleDateString(undefined,{weekday:'short',month:'short',day:'numeric',year:'numeric'});
      tt.textContent=`${c.dataset.label} · ${p}`;tt.style.left=e.clientX+'px';
      tt.style.top=e.clientY+'px';tt.style.opacity=1;});
    c.addEventListener('mouseleave',()=>tt.style.opacity=0);});
}
const CUR=new Date().getFullYear();
function showYear(year){
  if(year===CUR){ // current year → trailing 365 days, GitHub-style
    const END=new Date();const START=new Date();START.setDate(START.getDate()-364);
    renderRange(START,END,'the last year');
  }else{
    renderRange(new Date(year,0,1),new Date(year,11,31),String(year));
  }
}
// Year buttons — newest first, current year selected by default
const ybox=document.getElementById('years');
const clearA=()=>document.querySelectorAll('button.yr').forEach(x=>x.classList.remove('active'));
years.forEach(y=>{
  const b=document.createElement('button');b.className='yr';b.textContent=y;
  b.addEventListener('click',()=>{clearA();b.classList.add('active');showYear(y);location.hash=y;});
  ybox.appendChild(b);
});
document.getElementById('foot').textContent="Generated "+(PAYLOAD.generated||"");

// Default: hash year if valid, else the newest year (top button)
const h=location.hash.replace('#','');
const initial=(/^\\d{4}$/.test(h)&&years.includes(+h))?+h:years[0];
const initBtn=[...ybox.children].find(x=>x.textContent===String(initial));
initBtn.classList.add('active');showYear(initial);
</script></body></html>
"""


def main():
    payload = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "days": scan(),
        "lessons": scan_lessons(),
    }
    out = os.path.join(REPO, "practice-heatmap.html")
    html = HTML.replace("__PAYLOAD__", json.dumps(payload)).replace("__FLOOR__", str(FLOOR_YEAR))
    with open(out, "w") as f:
        f.write(html)
    print(f"Wrote {out} — {len(payload['days'])} practice days")

    svg_out = os.path.join(REPO, "practice-heatmap.svg")
    with open(svg_out, "w") as f:
        f.write(render_svg(payload["days"], payload["lessons"]))
    print(f"Wrote {svg_out}")


if __name__ == "__main__":
    main()
