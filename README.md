# guitar-coach

Personal electric guitar coaching setup. This repo is the persistent memory and practice journal for Artur's guitar journey, started December 2025.

## What's in here

- **`SKILL.md`** — the coaching brain. Defines how Claude runs a practice session, interleaves theory with practice, and logs progress. Read by Claude at the start of every session.
- **`progress.md`** — current state. Which JustinGuitar module, which theory topic, songs in rotation, what's clicking, what isn't. Updated after every session.
- **`equipment.md`** — guitars (Tele SH, Strat HSS), amp (Yamaha THR5), pedal (BOSS SD-1), accessories.
- **`songs.md`** — song index: foundation 5, composition group, improvisation group. Points to per-song files.
- **`songs/`** — one detail file per song with chords, tone settings (which guitar, pickup position, THR5 settings, SD-1 on/off), key, tempo, focus points, pentatonic for improv, and lesson + backing-track links.
- **`curriculum/`** — the two curricula being followed:
  - `justinguitar-grades.md` — JustinGuitar Grade 1, 2, and 3 module/lesson outlines (free at [justinguitar.com](https://www.justinguitar.com/guitar-lessons))
  - `theory-book.md` — module/page map for *Music Theory* by Steve Stine (GuitarZoom)
  - `interleaving.md` — how theory topics pair with practice lessons so theory always feels applied
  - `session-templates.md` — 15-, 25-, and 45-minute session shapes
- **`logs/YYYY/MM-DD.md`** — dated practice journals. Honest, scannable. What was worked, what clicked, what needs more reps tomorrow.

## How a session works

Open this folder with Claude and say something like *"let's practice"* or *"I have 25 minutes"*. Claude reads `SKILL.md` and `progress.md`, proposes a plan (warm-up → technique → song → theory snippet), walks through each block, then writes the session log and updates `progress.md`.

The whole point is: short, daily, honest, and the curriculum stays in charge.

## The two spines

- **Practice** — JustinGuitar Grades 1–3, in order. Free, well-sequenced beginner course.
- **Theory** — *Music Theory* by Steve Stine. Read the book separately; Claude pulls one applied concept into each session.

## The goal

Get fluent on the electric, build a real repertoire, and actually understand what's happening musically — not just memorize shapes. Pass JustinGuitar Grade 3. Read TAB and basic notation comfortably. Improvise a little.
