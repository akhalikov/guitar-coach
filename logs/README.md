# Practice Logs

Daily and weekly practice journals — one tree per instrument.

## Structure

```
logs/
├── README.md                              (this file)
├── electric/
│   └── YYYY/
│       ├── MM-DD.md                       (daily session log)
│       └── MM-DD-week.md                  (weekly review, written Saturday 18:00)
└── classical/
    ├── recordings/                        (audio/video/photo of practice — classical only)
    │   └── MM-DD-piece-takeN.{m4a,mp4,jpg}
    └── YYYY/
        ├── MM-DD.md                       (daily session log)
        └── MM-DD-week.md                  (weekly review, written Saturday 10:00)
```

## Templates

Daily and weekly templates live in `../prompts/log_templates/` and are shared between both coaches:

- `../prompts/log_templates/daily.md` — daily session log format
- `../prompts/log_templates/weekly.md` — weekly review format

## What the coaches do with these

At the start of every session, the active coach reads the **3 most recent daily logs** for that instrument to remember context. At the weekly review (fires Saturday — classical 10:00, electric 18:00), the coach reads the full week's logs and compares recordings (classical only) to assess actual progress vs. felt progress.

If a week has no logs, the weekly review pings Artur asking how the week went rather than writing a placeholder review.

## Recording naming convention (classical)

`MM-DD-piece-takeN.{ext}`

Examples:
- `05-23-nocturne-take1.m4a`
- `05-23-sitting-position.jpg`
- `06-15-etude-1-take3.mp4`

This makes it easy to grep recordings against log entries by date and piece.
