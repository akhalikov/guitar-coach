# Setup — Forking this for your own practice

This repo is the **coaching system** — prompts, curriculum, log templates, scheduled-task templates. It deliberately contains **no personal practice data**. Your own daily logs, progress markers, and recordings live in a separate **private** repo on your machine.

## The two-repo layout

```
~/work/github/<you>/
├── guitar-coach/            (this fork — public, system)
└── guitar-coach-logs/       (your private repo — your data)
```

The coach reads from `../guitar-coach-logs/progress/<instrument>.md` and `../guitar-coach-logs/logs/<instrument>/YYYY/`, and writes new logs there. The public repo never sees your data.

## One-time setup

1. **Fork this repo** to your own GitHub account (or just clone if you don't plan to contribute back).

   ```bash
   gh repo clone <you>/guitar-coach
   cd guitar-coach
   ```

2. **Create your private logs repo** as a sibling folder:

   ```bash
   cd ..
   mkdir guitar-coach-logs
   cd guitar-coach-logs
   git init
   ```

3. **Bootstrap the folder structure:**

   ```bash
   mkdir -p logs/electric/$(date +%Y) logs/classical/$(date +%Y) logs/classical/recordings progress
   touch logs/electric/$(date +%Y)/.gitkeep logs/classical/$(date +%Y)/.gitkeep logs/classical/recordings/.gitkeep
   ```

4. **Create progress starter files.** The coach reads these every session.

   ```bash
   cat > progress/electric.md <<'EOF'
   # Electric — Current State

   - **Current JustinGuitar module:** Grade 1, Module 1
   - **Current Stine topic:** (chapter / page)
   - **Songs in rotation (Learning / Polishing / Maintenance):** ...
   - **Open struggles:** ...
   EOF

   cat > progress/classical.md <<'EOF'
   # Classical — Current State

   - **Current Werner phase / piece:** Phase 0 — Orientation
   - **Pieces in rotation (Learning / Polishing / Maintenance):** ...
   - **What's clicking:** ...
   - **What's not:** ...
   EOF
   ```

   Fill these in with your actual state. The coach reads them at session start.

5. **Add a README and .gitignore** to your private repo. Any sensible defaults work — keep it private and don't push recordings you wouldn't want public.

6. **Create the private GitHub repo** and push:

   ```bash
   gh repo create guitar-coach-logs --private --source=. --remote=origin --push
   ```

   That's it. Open `~/work/github/<you>/guitar-coach/` in your Claude desktop app (Cowork) and the coach will pick up CLAUDE.md and route from there.

## Path conventions in this repo

Throughout the public repo's prompts and templates, paths like `../guitar-coach-logs/logs/...` refer to your private sibling repo. These are written from the perspective of the public repo's root.

If you put the two repos in different folders (not siblings), you'll need to:
- Update the path references in `CLAUDE.md`, `prompts/base.md`, `prompts/electric/SKILL.md`, `prompts/classical/SKILL.md`, `prompts/log_templates/{daily,weekly}.md`, and the two scheduled tasks
- Or symlink your logs repo into the expected sibling location

The sibling layout is recommended — keeps the relative paths working as-is.

## Where your data goes

- **Daily session log** → `../guitar-coach-logs/logs/<instrument>/YYYY/MM-DD.md`
- **Weekly review** (Saturday) → `../guitar-coach-logs/logs/<instrument>/YYYY/MM-DD-week.md`
- **Current state** (curriculum position, songs in rotation, struggles) → `../guitar-coach-logs/progress/<instrument>.md`
- **Recordings** (classical) → `../guitar-coach-logs/logs/classical/recordings/`

## Two repos = two commits per session (when both change)

If only your logs changed in a session (the usual case), one commit to the logs repo. If you also edited the coaching system (e.g. tweaked a prompt or added a song to `curriculum/`), that's a second commit to the public repo. The coach prints the right bash blocks at session end.

See `prompts/base.md` → "Saving changes" for the conventions.
