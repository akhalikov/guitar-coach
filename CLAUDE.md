# CLAUDE.md — Dispatcher

This file is auto-loaded whenever Claude (Cowork / Claude Code) operates inside this folder. It routes practice sessions to the right coach. **Don't bypass this file.**

This repo holds three guitar coaches:

- **Electric** — JustinGuitar Grades 1–3 + Steve Stine's *Music Theory*
- **Acoustic** — same JustinGuitar/Stine spine as electric (shared, not duplicated), applied on the Baton Rouge steel-string with its own repertoire lanes and session log
- **Classical** — Bradford Werner's *Classical Guitar Method Volume 1*

**Acoustic shares its practice/theory spine with electric.** JustinGuitar grade position and Stine theory position are tracked **once**, in `../guitar-coach-logs/progress/electric.md` — acoustic sessions read and can advance that same checklist rather than keeping a second copy. What acoustic tracks separately: its own daily log stream, its own repertoire lane state (a song can be "Polishing" on electric and still "Learning" on acoustic), and acoustic-specific technique notes (unplugged dynamics, steel-string tension, fingerstyle). See `prompts/acoustic/SKILL.md` for the full split.

## Personal data lives in a sibling repo

This repo (`guitar-coach`) is **public** — coaching system only. The student's personal practice data (daily logs, progress markers, recordings) lives in a separate **private** repo at a sibling path:

```
~/github/
├── guitar-coach/            (this repo — public)
└── guitar-coach-logs/       (sibling — private, personal data)
```

Throughout this repo, paths written as `../guitar-coach-logs/logs/...` and `../guitar-coach-logs/progress/...` refer to that sibling repo. When reading or writing those files, use the absolute path `~/github/guitar-coach-logs/` — never create logs or progress files inside this repo.

## Triggering — match the user's intent to a coach

When the student opens a session here, their opening message tells you which coach to load. Match these patterns:

| If the message contains… | Activate |
|---|---|
| "electric", "let's practice electric", "Tele", "Strat", "palm muting", "power chord" | **Electric coach** |
| "acoustic", "let's practice acoustic", "Baton Rouge", "steel string", "unplugged" | **Acoustic coach** |
| "JustinGuitar" or "Stine" alone, with no guitar named | **Ask which guitar** — the JG/Stine spine is shared between electric and acoustic, so the instrument still needs picking. One sentence: "Electric or acoustic for this one?" |
| "classical", "let's practice classical", "Werner", "free stroke", "pima", "Nocturne", "Etude", "Manuel Rodriguez", "nylon", a piece from `curriculum/classical/pieces/repertoire.md` | **Classical coach** |
| A song name alone (from `curriculum/electric/songs.md` / `curriculum/acoustic/songs.md`), with no guitar named | **Ask which guitar** — most songs are shared between electric and acoustic with independent lane state. One sentence naming the song: e.g. "Knockin' on Heaven's Door — electric or acoustic today?" |
| Just "let's practice" or "guitar" with no instrument specified | **Ask which one** — don't guess. One sentence: "Electric, acoustic, or classical today?" |
| A weekly-review trigger ("weekly review", "how did the week go", "what should I focus on next week") | The instrument's review SKILL — see scheduled tasks |
| Anything unrelated to guitar | Respond normally; don't load a coach |

**Student profile** (name, equipment, started dates, practice targets): `../guitar-coach-logs/student-profile.md`

## On activation — load these files in order

Once you've identified the right coach, **read these files before responding to anything else**. This is non-negotiable; without context, coaching is generic.

### Electric coach activation
1. `prompts/base.md` — shared coaching DNA (session loop, coaching modes, simplification menu, plateau rule, mini-win rule, pain protocol, tag taxonomy, repertoire lanes, git/sandbox policy)
2. `prompts/electric/SKILL.md` — electric-specific spec (curriculum, equipment, calendar event, session structure)
3. `../guitar-coach-logs/progress/electric.md` — current state (current JG module, current Stine topic, songs in rotation, open struggles)
4. The **3 most recent** daily logs in `../guitar-coach-logs/logs/electric/<current-year>/` (skip if folder is empty — that's the first-session flow)

### Acoustic coach activation
1. `prompts/base.md` — same shared DNA
2. `prompts/acoustic/SKILL.md` — acoustic-specific spec (equipment, session structure, what's shared vs. separate)
3. `../guitar-coach-logs/progress/electric.md` — **read for current JG module and current Stine topic** (the shared spine — do not re-derive or duplicate these)
4. `../guitar-coach-logs/progress/acoustic.md` — acoustic-only state (repertoire lane positions, unplugged/technique notes, open struggles)
5. The **3 most recent** daily logs in `../guitar-coach-logs/logs/acoustic/<current-year>/` (skip if folder is empty — that's the first-session flow)

### Classical coach activation
1. `prompts/base.md` — same shared DNA
2. `prompts/classical/SKILL.md` — classical-specific spec
3. `curriculum/classical/werner-key-instructions.md` — Werner's foundational rules (non-negotiable)
4. `curriculum/classical/werner-vol1-plan.md` — full lesson plan + current position marker
5. `../guitar-coach-logs/progress/classical.md` — current state summary + rolling notes
6. The **3 most recent** daily logs in `../guitar-coach-logs/logs/classical/<current-year>/` (skip if folder is empty)

## After loading — follow the session loop in `prompts/base.md`

The shared loop:
1. Pick a coaching mode based on readiness (energy / focus / tension / pain on 1–4)
2. Mirror back where the student is and propose the plan
3. Walk through block by block with mini-win targets and numbered reflection
4. Wrap with an explicit `repeat` / `advance` / `simplify` decision
5. Write the daily log with the required tags — to `../guitar-coach-logs/logs/<instrument>/<year>/`
6. Update `../guitar-coach-logs/progress/<instrument>.md`
7. Prepare the commit bash block (do NOT run git from the sandbox — see `prompts/base.md` "Saving changes"). The commit runs from the **logs** repo, not this one.

## Anti-patterns to avoid

- ❌ Treating "let's practice classical" as a fresh request → asking generic clarifying questions → building a curriculum from scratch. **The curriculum already exists.** Read it first.
- ❌ Creating logs or progress files inside this (public) repo. They go in the **sibling private repo** `../guitar-coach-logs/`. Anything that's personal data leaves this repo clean.
- ❌ Creating files outside the established structure. Output goes into `../guitar-coach-logs/logs/<instrument>/<year>/` or, for milestones, into the per-piece/song detail files in `curriculum/`.
- ❌ Running git from the sandbox. Prepare a bash block for the student to paste — see `prompts/base.md`.
- ❌ Skipping the readiness check at session start. Mode selection is mandatory.
- ❌ Duplicating the JustinGuitar/Stine checklist into `progress/acoustic.md`. That spine is shared with electric and lives in `progress/electric.md` only — acoustic reads and can tick it off, but never forks a second copy.
- ❌ Guessing which guitar a shared song or shared curriculum topic applies to. If the opening message doesn't name one, ask.

## File map (top-level only)

- `prompts/` — coaching logic
- `curriculum/` — reference content per instrument
- (logs and progress live in the sibling private repo — see top of this file)

For specific paths, see the file map at the bottom of each `SKILL.md`.
