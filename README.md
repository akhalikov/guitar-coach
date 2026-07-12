# 🎸 guitar-coach

Personal guitar coaching setup. Three coaches under one roof:

- **Electric guitar**, based on:
    - **JustinGuitar Grades 1–3**
    - **Steve Stine's *Music Theory***

- **Acoustic guitar** (Baton Rouge X11LS/F-W-SCR steel-string), based on:
    - **The same JustinGuitar Grades 1–3 + Steve Stine spine as electric** — tracked once, not duplicated (see below)
    - its own repertoire lanes, daily log stream, and unplugged/fingerstyle technique notes

- **Classical guitar**, based on:
    - **Bradford Werner's *Classical Guitar Method Volume 1*** 

All three coaches share the same coaching DNA: 
- direct, honest, technical
- slow-first
- stay in curriculum

But differ in repertoire, gear, technique focus, and theory spine. 
The shared logic lives in `prompts/base.md`; the instrument-specific stuff lives in `prompts/electric/SKILL.md`, `prompts/acoustic/SKILL.md`, and `prompts/classical/SKILL.md`.

### Electric and acoustic share a practice/theory spine

Acoustic isn't a fork of electric's curriculum — it's the same JustinGuitar grade position and Stine theory position, applied on a different guitar. That shared position lives in one place, `guitar-coach-logs/progress/electric.md`, and both coaches read/advance it. What acoustic keeps separate: its own `curriculum/acoustic/songs.md` repertoire lanes (a song can be "Polishing" on electric and untouched on acoustic), its own daily log stream in `guitar-coach-logs/logs/acoustic/`, and a few acoustic-exclusive songs with their own detail files in `curriculum/acoustic/songs/`.

## ⚙️ How a session works

Open this folder with Claude. Say what you want:

- *"Let's practice electric"* → the electric coach activates (reads `prompts/electric/SKILL.md` → `prompts/base.md` → `../guitar-coach-logs/progress/electric.md` → recent electric logs → proposes a plan)
- *"Let's practice acoustic"* → the acoustic coach activates (reads `prompts/acoustic/SKILL.md` → `prompts/base.md` → `../guitar-coach-logs/progress/electric.md` for the shared JG/Stine position → `../guitar-coach-logs/progress/acoustic.md` for acoustic-only state → recent acoustic logs → proposes a plan)
- *"Let's practice classical"* → the classical coach activates (same loop with classical files)

If you just say "JustinGuitar," "Stine," or name a song that's shared between electric and acoustic without naming a guitar, the coach asks which one first — the curriculum content is the same, but progress/logs still need to go to the right stream.

The coach asks how you're feeling (energy / focus / tension / pain, 1–4) to pick a session mode, then proposes a plan, walks you through it block by block, and writes the daily log and updates the progress file. A single Saturday 10:00 scheduled task, `guitar-weekly-review`, reviews all three instruments in one run.

## 🗄️ Two-repo layout

This repo is **public** — coaching system only. Personal practice data lives in a **private sibling repo** called `guitar-coach-logs`:

```
~/
├── guitar-coach/            (this repo — prompts, curriculum, SKILL.md files)
└── guitar-coach-logs/       (private — daily logs, progress markers, recordings)
```

The coach reads from and writes to the sibling repo. Commits happen there too — this public repo only changes when the coaching system itself changes.

- `prompts/` — coaching logic (shared `base.md` + per-instrument `SKILL.md` + daily/weekly log templates)
- `curriculum/` — reference content per instrument (lesson plans, songs/pieces, equipment, books)

If you're forking this for your own use, see `SETUP.md` for how to set up the paired private logs repo.

## ⏯️ The scheduled task

| Task | Cadence | What it does |
|---|---|---|
| `guitar-weekly-review` | Saturday 10:00 local | Runs the weekly review for electric, acoustic, and classical in turn — reads each instrument's week of logs, writes its review, ticks completed JG/Stine items (once, shared between electric and acoustic) or advances the Werner position marker, and prepares one combined commit block. An instrument with no logs that week is skipped, not given a placeholder review. |

One task, one Saturday 10:00 run, covering all three instruments — previously this was two separate tasks (classical at 10:00, electric at 18:00); they've been merged.

The task runs automatically while the Claude app is open. If closed at the scheduled time, it fires on next launch. 
Manage it from the **Scheduled** section in the Cowork sidebar.

## 🎯 Goals

- **Electric:** pass JustinGuitar Grade 3. Read TAB and basic notation. Build a real song repertoire. Improvise a little.
- **Acoustic:** apply the same JustinGuitar/Stine progress to a steel-string context — build unplugged strumming/dynamics and fingerstyle (Travis picking, перебор), and grow an acoustic-specific repertoire alongside the shared songs.
- **Classical:** complete Werner Vol 1 confidently — every piece memorized, played at tempo with clean tone, dynamics, phrasing. Then assess Vol 2.

All three are multi-year projects. The point is daily practice, honest logging, and trusting the curriculum.
