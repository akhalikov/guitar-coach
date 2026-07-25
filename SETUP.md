# Setup — Forking this for your own practice

This repo holds both the **coaching system** (prompts, curriculum, log templates, scheduled-task templates) and your **personal practice data** (daily logs, progress markers, recordings). The system lives at the repo root; your data lives in the `journal/` folder.

> Note: your practice data is committed to this repo. If you want it private, keep your fork private.

## The layout

```
~/github/guitar-coach/
├── prompts/     (system — base.md + per-instrument SKILL.md + log templates)
├── curriculum/  (reference content per instrument)
└── journal/     (your data — logs, progress, recordings, heatmap)
```

The coach reads from `journal/progress/<instrument>.md` and `journal/logs/<instrument>/YYYY/`, and writes new logs there.

## One-time setup

1. **Fork this repo** to your own GitHub account (or clone if you don't plan to contribute back).

   ```bash
   gh repo clone <you>/guitar-coach
   cd guitar-coach
   ```

2. **Bootstrap the `journal/` folder structure:**

   ```bash
   mkdir -p journal/logs/electric/$(date +%Y) journal/logs/classical/$(date +%Y) journal/logs/classical/recordings journal/progress
   touch journal/logs/electric/$(date +%Y)/.gitkeep journal/logs/classical/$(date +%Y)/.gitkeep journal/logs/classical/recordings/.gitkeep
   ```

3. **Create progress starter files.** The coach reads these every session.

   ```bash
   cat > journal/progress/electric.md <<'EOF'
   # Electric — Current State

   - **Current JustinGuitar module:** Grade 1, Module 1
   - **Current Stine topic:** (chapter / page)
   - **Songs in rotation (Learning / Polishing / Maintenance):** ...
   - **Open struggles:** ...
   EOF

   cat > journal/progress/classical.md <<'EOF'
   # Classical — Current State

   - **Current Werner phase / piece:** Phase 0 — Orientation
   - **Pieces in rotation (Learning / Polishing / Maintenance):** ...
   - **What's clicking:** ...
   - **What's not:** ...
   EOF
   ```

   Fill these in with your actual state.

4. **Push:**

   ```bash
   git add -A && git commit -m "Bootstrap journal/" && git push
   ```

   That's it. Open `~/github/guitar-coach/` in your Claude desktop app (Cowork) and the coach will pick up CLAUDE.md and route from there.

## Path conventions in this repo

Throughout the prompts and templates, paths like `journal/logs/...` are relative to the repo root. If you rename the `journal/` folder, update the references in `CLAUDE.md`, `prompts/base.md`, `prompts/electric/SKILL.md`, `prompts/classical/SKILL.md`, and `prompts/log_templates/{daily,weekly}.md`.

## Where your data goes

- **Daily session log** → `journal/logs/<instrument>/YYYY/MM-DD.md`
- **Weekly review** (Saturday) → `journal/logs/<instrument>/YYYY/MM-DD-week.md`
- **Current state** (curriculum position, songs in rotation, struggles) → `journal/progress/<instrument>.md`
- **Recordings** (classical) → `journal/logs/classical/recordings/`

## One commit per session

Logs and system files are in the same repo, so a session is normally **one commit** — `git add -A` from the repo root stages your log, the progress update, and the regenerated heatmap together. The coach prints the right bash block at session end.

See `prompts/base.md` → "Saving changes" for the conventions.
