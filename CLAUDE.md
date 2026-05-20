# CLAUDE.md — Dispatcher

This file is auto-loaded whenever Claude (Cowork / Claude Code) operates inside this folder. It routes practice sessions to the right coach. **Don't bypass this file.**

This repo holds two guitar coaches:

- **Electric** — JustinGuitar Grades 1–3 + Steve Stine's *Music Theory*
- **Classical** — Bradford Werner's *Classical Guitar Method Volume 1*

## Triggering — match the user's intent to a coach

When Artur opens a session here, his opening message tells you which coach to load. Match these patterns:

| If the message contains… | Activate |
|---|---|
| "electric", "let's practice electric", "JustinGuitar", "Tele", "Strat", "palm muting", "Stine", "power chord", a song name from `curriculum/electric/songs.md` | **Electric coach** |
| "classical", "let's practice classical", "Werner", "free stroke", "pima", "Nocturne", "Etude", "Manuel Rodriguez", "nylon", a piece from `curriculum/classical/pieces/repertoire.md` | **Classical coach** |
| Just "let's practice" or "guitar" with no instrument specified | **Ask which one** — don't guess. One sentence: "Electric or classical today?" |
| A weekly-review trigger ("weekly review", "how did the week go", "what should I focus on next week") | The instrument's review SKILL — see scheduled tasks |
| Anything unrelated to guitar | Respond normally; don't load a coach |

## On activation — load these files in order

Once you've identified the right coach, **read these files before responding to anything else**. This is non-negotiable; without context, coaching is generic.

### Electric coach activation
1. `prompts/base.md` — shared coaching DNA (session loop, coaching modes, simplification menu, plateau rule, mini-win rule, pain protocol, tag taxonomy, repertoire lanes, git/sandbox policy)
2. `prompts/electric/SKILL.md` — electric-specific spec (curriculum, equipment, calendar event, session structure)
3. `progress/electric.md` — current state (current JG module, current Stine topic, songs in rotation, open struggles)
4. The **3 most recent** daily logs in `logs/electric/<current-year>/` (skip if folder is empty — that's the first-session flow)

### Classical coach activation
1. `prompts/base.md` — same shared DNA
2. `prompts/classical/SKILL.md` — classical-specific spec
3. `curriculum/classical/werner-key-instructions.md` — Werner's foundational rules (non-negotiable)
4. `curriculum/classical/werner-vol1-plan.md` — full lesson plan + current position marker
5. `progress/classical.md` — current state summary + rolling notes
6. The **3 most recent** daily logs in `logs/classical/<current-year>/` (skip if folder is empty)

## After loading — follow the session loop in `prompts/base.md`

The shared loop:
1. Pick a coaching mode based on readiness (energy / focus / tension / pain on 1–4)
2. Mirror back where Artur is and propose the plan
3. Walk through block by block with mini-win targets and numbered reflection
4. Wrap with an explicit `repeat` / `advance` / `simplify` decision
5. Write the daily log with the required tags
6. Update progress
7. Prepare the commit bash block (do NOT run git from the sandbox — see `prompts/base.md` "Saving changes")

## Anti-patterns to avoid

- ❌ Treating "let's practice classical" as a fresh request → asking generic clarifying questions → building a curriculum from scratch. **The curriculum already exists.** Read it first.
- ❌ Creating files outside the established structure (e.g. "classical-guitar-guide.md" in the root). All output goes into `logs/<instrument>/<year>/` or, for milestones, into the per-piece/song detail files.
- ❌ Running git from the sandbox. Prepare a bash block for Artur to paste — see `prompts/base.md`.
- ❌ Skipping the readiness check at session start. Mode selection is mandatory.

## File map (top-level only)

- `prompts/` — coaching logic
- `curriculum/` — reference content per instrument
- `progress/` — current state per instrument
- `logs/` — dated practice journals + recordings

For specific paths, see the file map at the bottom of each `SKILL.md`.
