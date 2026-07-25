# journal — Personal practice data

Artur's practice data for the guitar coaching system: daily logs, progress markers, recordings, and the generated heatmap. The coaching system itself (prompts, curriculum, CLAUDE.md dispatcher) lives at the repo root, one level up.

**Live practice heatmap:** https://akhalikov.github.io/guitar-coach/journal/practice-heatmap.html — published via GitHub Pages, rebuilt from these logs on every push.

## Layout

```
journal/
├── student-profile.md          name, equipment, started dates, targets
├── practice-heatmap.html       generated contribution graph (open by double-click)
├── tools/gen_heatmap.py        regenerates the heatmap from logs
├── progress/
│   ├── electric.md             current JG module, Stine topic, song rotation, open struggles
│   │                           (also the source of truth for the shared JG/Stine position)
│   ├── acoustic.md             acoustic-only state (lane positions, technique notes)
│   └── classical.md            current Werner position, rolling notes, what's clicking / not
└── logs/
    ├── electric/YYYY/MM-DD.md          daily session log (+ MM-DD-week.md weekly review)
    ├── acoustic/YYYY/MM-DD.md
    └── classical/
        ├── recordings/                 audio / video / photo of practice
        │   └── MM-DD-piece-takeN.{m4a,mp4,jpg}
        └── YYYY/MM-DD.md               daily session log (+ MM-DD-week.md)
```

For a second session on the same day, suffix the file: `MM-DD-2.md`, `MM-DD-3.md`. First session never gets a suffix.

## Conventions

Tag taxonomy, log format, and commit conventions all live in the system files at the repo root — see `../prompts/log_templates/daily.md` and `../prompts/base.md` → "Saving changes". A session is one commit from the repo root (`~/github/guitar-coach`), covering the log, progress update, and heatmap refresh together.
