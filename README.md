# 🎸 guitar-coach

Personal guitar coaching setup. Two coaches under one roof:

- **Electric guitar**, based on:
    - **JustinGuitar Grades 1–3**
    - **Steve Stine's *Music Theory***
      
- **Classical guitar**, based on:
    - **Bradford Werner's *Classical Guitar Method Volume 1*** 

Both coaches share the same coaching DNA: 
- direct, honest, technical
- slow-first
- stay in curriculum

But differ in repertoire, gear, technique focus, and theory spine. 
The shared logic lives in `prompts/base.md`; the instrument-specific stuff lives in `prompts/electric/SKILL.md` and `prompts/classical/SKILL.md`.

## ⚙️ How a session works

Open this folder with Claude. Say what you want:

- *"Let's practice electric"* → the electric coach activates (reads `prompts/electric/SKILL.md` → `prompts/base.md` → `progress/electric.md` → recent electric logs → proposes a plan)
- *"Let's practice classical"* → the classical coach activates (same loop with classical files)

The coach asks how you're feeling (energy / focus / tension / pain, 1–4) to pick a session mode, then proposes a plan, walks you through it block by block, and writes the daily log and updates the progress file. Saturday weekly reviews fire automatically via scheduled tasks (classical 10:00, electric 18:00).

## 🗄️ Top-level layout

- `prompts/` — coaching logic (shared `base.md` + per-instrument `SKILL.md` + daily/weekly log templates)
- `curriculum/` — reference content per instrument (lesson plans, songs/pieces, equipment, books)
- `progress/` — current state per instrument (what's clicking, what's not, where you are)
- `logs/` — dated practice journals + recordings

For specific paths, see the file map at the bottom of each `SKILL.md` — those are the source of truth (and they're what the coaches actually read).

## ⏯️ The two scheduled tasks

| Task | Cadence | What it does |
|---|---|---|
| `classical-guitar-weekly-review` | Saturday 10:00 local | Reads the week's classical logs, writes the weekly review, advances the Werner position marker, prepares a commit block |
| `electric-guitar-weekly-review` | Saturday 18:00 local | Same for electric — reads week's logs, writes weekly review, ticks completed JG/Stine items, prepares a commit block |

Both tasks run automatically while the Claude app is open. If closed at the scheduled time, they fire on next launch. 
Manage them from the **Scheduled** section in the Cowork sidebar.

## 🎯 Goals

- **Electric:** pass JustinGuitar Grade 3. Read TAB and basic notation. Build a real song repertoire. Improvise a little.
- **Classical:** complete Werner Vol 1 confidently — every piece memorized, played at tempo with clean tone, dynamics, phrasing. Then assess Vol 2.

Both are multi-year projects. The point is daily practice, honest logging, and trusting the curriculum.
