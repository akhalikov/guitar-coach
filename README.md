# guitar-coach

Personal guitar coaching setup. Two coaches under one roof:

- **Electric guitar**
    - Working through **JustinGuitar Grades 1–3** + **Steve Stine's *Music Theory*** in parallel (since December 2025).
      
- **Classical guitar**
    - Working through **Bradford Werner's *Classical Guitar Method Volume 1*** (since April 2026).

Both coaches share the same coaching DNA: 
- direct, honest, technical
- slow-first
- stay in curriculum

But differ in repertoire, gear, technique focus, and theory spine. 
The shared logic lives in `prompts/base.md`; the instrument-specific stuff lives in `prompts/electric/SKILL.md` and `prompts/classical/SKILL.md`.

## How a session works

Open this folder with Claude. Say what you want:

- *"Let's practice electric"* → the electric coach activates (reads `prompts/electric/SKILL.md` → `prompts/base.md` → `progress/electric.md` → recent electric logs → proposes a plan)
- *"Let's practice classical"* → the classical coach activates (same loop with classical files)

The coach proposes a session plan, walks you through it block by block, then writes the daily log and updates the progress file. Saturday weekly reviews fire automatically via scheduled tasks (classical 10:00, electric 18:00).

## File map

```
guitar-coach/
├── README.md                                        ← this file
├── .gitignore                                       ← keeps book PDFs out of git
│
├── prompts/                                         ← coaching logic
│   ├── base.md                                      ← shared coaching DNA (session loop, tone, git policy)
│   ├── log_templates/
│   │   ├── daily.md
│   │   └── weekly.md
│   ├── electric/SKILL.md                            ← electric coach entry point
│   └── classical/SKILL.md                           ← classical coach entry point
│
├── curriculum/                                      ← reference content per instrument
│   ├── electric/
│   │   ├── equipment.md                             ← Tele SH, Strat HSS, THR5, SD-1
│   │   ├── songs.md                                 ← song index
│   │   ├── songs/                                   ← per-song detail files
│   │   ├── justinguitar-grades.md
│   │   ├── theory-book.md                           ← Steve Stine module/page map
│   │   ├── interleaving.md                          ← theory ↔ practice pairings
│   │   └── session-templates.md                     ← 15/25/45 min session shapes
│   └── classical/
│       ├── werner-key-instructions.md               ← Werner's foundational rules
│       ├── werner-vol1-plan.md                      ← lesson-by-lesson plan + current position
│       ├── pieces/                                  ← future per-piece detail files
│       └── book/
│           ├── README.md
│           └── Classical-Guitar-Method-Vol1-Werner.pdf  ← local-only (gitignored)
│
├── progress/                                        ← current state per instrument
│   ├── electric.md
│   └── classical.md
│
└── logs/                                            ← dated practice journals + recordings
    ├── README.md
    ├── electric/YYYY/
    │   ├── MM-DD.md                                 ← daily logs
    │   └── MM-DD-week.md                            ← weekly reviews
    └── classical/
        ├── recordings/                              ← audio/video/photo takes
        └── YYYY/
            ├── MM-DD.md
            └── MM-DD-week.md
```

## The two scheduled tasks

| Task | Cadence | What it does |
|---|---|---|
| `classical-guitar-weekly-review` | Saturday 10:00 local | Reads the week's classical logs, writes the weekly review, advances the Werner position marker, prepares a commit block |
| `electric-guitar-weekly-review` | Saturday 18:00 local | Same for electric — reads week's logs, writes weekly review, ticks completed JG/Stine items, prepares a commit block |

Both tasks run automatically while the Claude app is open. If closed at the scheduled time, they fire on next launch. Manage them from the **Scheduled** section in the Cowork sidebar.

## A note on commits

The Cowork shell sandbox has trouble running git operations on this repo (permission issues on `.git/objects` lock files, no SSH credentials for push). **Both coaches prepare a `bash` block at the end of each session and Artur pastes it into his terminal** — that's the source of truth for commits. See `prompts/base.md` for the convention.

Commits always include the Claude co-author trailer:

```
<commit subject>

Co-Authored-By: Claude <noreply@anthropic.com>
```

## Goals

- **Electric:** pass JustinGuitar Grade 3. Read TAB and basic notation. Build a real song repertoire. Improvise a little.
- **Classical:** complete Werner Vol 1 confidently — every piece memorized, played at tempo with clean tone, dynamics, phrasing. Then assess Vol 2.

Both are multi-year projects. The point is daily practice, honest logging, and trusting the curriculum.
