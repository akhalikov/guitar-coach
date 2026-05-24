# Daily Log Template

Filename pattern (written to the **private logs repo** — sibling folder, not this repo):
```
../guitar-coach-logs/logs/<instrument>/YYYY/MM-DD.md       ← first session of the day
../guitar-coach-logs/logs/<instrument>/YYYY/MM-DD-2.md     ← second session same day
../guitar-coach-logs/logs/<instrument>/YYYY/MM-DD-3.md     ← third session same day
```

If a log already exists for today, increment the suffix. Session 1 never gets a suffix.

---

## Writing timing

- **At session START:** create the file, fill `## Session Start` only. Leave the rest blank.
- **After each block:** ask the numbered reflection and write the block's fields.
- **At session END:** fill `## Tags`, `## Reflection`, and `## Coach's Note`. Then prepare the commit bash block (see `prompts/base.md`).

Skip sections you didn't run rather than leaving them blank (e.g. omit `## Section 5 — Theory` entirely on a short day).

---

## Required tags

Every log has exactly these tags (one line, space-separated):

| Tag | Rule |
|---|---|
| `#roadmap/<name>` | Exactly one. `#roadmap/electric-justinguitar` or `#roadmap/classical-werner` |
| `#lesson/<slug>` | Exactly one. The active lesson/piece. `#lesson/grade-1-mod-3-c-chord`, `#lesson/etude-1`, etc. |
| `#mode/<value>` | Exactly one: `full` / `review-only` / `low-friction` / `recovery` / `bad-day` |
| `#status/<value>` | Exactly one: `repeat` / `advance` / `simplify` |
| `#issue/<slug>` | Zero or more. Recurring problems: `#issue/string-6-buzz`, `#issue/g-to-c-change`, `#issue/pinky-lift` |
| `#review/<lesson-slug>` | Optional. When this session is a spaced-repetition review of an old lesson |
| `#skill/<area>` | Optional: `#skill/chords`, `#skill/rhythm`, `#skill/scales`, `#skill/repertoire`, `#skill/reading`, `#skill/free-stroke`, `#skill/i-m-alternation` |

Tags are machine-readable — the Saturday weekly review counts them. Sloppy tags = inaccurate review.

---

## Template

```markdown
# Practice Log — YYYY-MM-DD (electric | classical)

## Session Start
- **Date:** YYYY-MM-DD ← **auto-fill** from `date '+%Y-%m-%d'`, never ask the student
- **Time:** HH:MM ← **auto-fill** from `date '+%H:%M'`, never ask the student
- **Coaching mode:** full | review-only | low-friction | recovery | bad-day
- **Energy / Focus / Tension / Pain (1-4):** E_ F_ T_ P_
- **Guitar:** (which one — Tele SH / Strat HSS / Manuel Rodríguez T-65)
- **Planned duration:** ~XX min
- **Context notes:** (optional — one line if today's ratings need explanation)

## Plan (proposed at session start)
- Warm-up: ...
- Technique: ...
- Lesson focus: ...
- Song / Application: ...
- Theory / Reading: ...

## Section 1 — Warm-up
- **Target (mini-win):** what "clean" looks like for this block — specific
- **Result:** what actually happened
- **Reflection (1-4):** D_ A_ T_ Te_
  - D=Difficulty (1.very easy 2.manageable 3.challenging 4.too hard)
  - A=Accuracy (1.clean 2.few mistakes 3.frequent 4.fell apart)
  - T=Timing (1.steady 2.off 3.unstable 4.lost pulse)
  - Te=Tension (1.none 2.mild 3.noticeable 4.pain — stop)
  - **If D≥3 or A≥3:** H_ (Hand diagnostic — 1.fretting 2.picking 3.both 4.unsure)

## Section 2 — Technique
- **Target (mini-win):** ...
- **Result:** ...
- **Reflection (1-4):** D_ A_ T_ Te_ (H_ if applicable)

## Section 3 — Lesson Focus
- **Target (mini-win):** ...
- **Result:** ...
- **Reflection (1-4):** D_ A_ T_ Te_ (H_ if applicable)

## Section 4 — Song / Application
- **Song / piece:** ...
- **Lane:** Learning | Polishing | Maintenance
- **Target (mini-win):** ...
- **Result:** ...
- **Reflection (1-4):** D_ A_ T_ Te_ (H_ if applicable)

## Section 5 — Theory / Reading (optional)
- **Concept:** ...
- **How it landed:** got it / partial / didn't land
- **Try again next session?:** yes / no

## Recordings (optional)
- (filename → what's on it)

## Tags
#roadmap/electric-justinguitar #lesson/grade-1-mod-1-a-chord #mode/full #status/repeat #issue/string-6-buzz #skill/chords

## Reflection
- **What clicked:** (1–2 specific things — name the chord, the measure, the BPM)
- **What needs more reps:** (specific, actionable for tomorrow)
- **Repeat / advance / simplify:** repeat — (one-sentence reason). Matches `#status/` tag.
- **Overall (1-4):** _
- **Total actual duration:** ~XX min ← **auto-compute** from `date '+%H:%M'` at session end minus the Session Start `Time`

## Coach's Note
- (one short line for the next session — what to start with tomorrow)
```

---

## Field guidance

### Session Start
- **Date and Time:** **always** captured from the Unix `date` command — never asked from the student. Run `date '+%Y-%m-%d %H:%M'` at session start, parse the two fields. Run `date '+%H:%M'` again at session end to compute `Total actual duration`. A `—` for Time means the coach forgot to run `date` — it's a defect, not a valid state.
- **Coaching mode:** picked at the start based on energy/focus/tension/pain. See `../base.md` for the mode table. State it in chat before the plan.
- **Energy / Focus / Tension / Pain (1-4):** 1=low/none, 2=mild/okay, 3=good/noticeable, 4=high. **If Pain=2 or higher, fire the pain protocol (see `../base.md`).**
- **Context notes:** optional — one line ("after a long day", "second session today", "first time back after 3 days").

### Per-block reflection format

Numbered scale per dimension. The student replies with digits only:

```
D=2 A=1 T=1 Te=1
```

If Difficulty or Accuracy is 3 or 4, the coach immediately asks:

```
Where did the problem come from?
1. Fretting (left hand)
2. Picking (right hand)
3. Both
4. Not sure
```

Record as `H=2`. This routes the next drill to the right hand. **Don't skip this question** — it's the biggest data point per session.

### Mini-win target
What "clean" looks like for this block — specific, narrow, achievable inside the time. Examples:
- "8 down-strums of D, all 4 strings ring, repeat 3 sets"
- "Etude 1 bars 1–4 at 60 BPM, 2 run-throughs with no restart"
- "A→D change × 20, count clean ones, ≥15/20 = win"

If the target is hit early, the coach should remind the student: **"Keep going slowly and cleanly — don't speed up."**

### Status (repeat / advance / simplify)
The single most important field. Forces a commitment.

- **repeat** — same lesson tomorrow, no changes
- **advance** — next lesson tomorrow, this one is solid
- **simplify** — drop one variable per the simplification menu (see `../base.md`), retry tomorrow

This becomes the `#status/` tag — the weekly review counts the distribution to spot patterns.

### Issue tags
One per recurring problem. Use stable slugs — same issue gets the same slug across sessions so the weekly review can count occurrences. Examples:
- `#issue/string-6-buzz`
- `#issue/g-to-c-change`
- `#issue/pinky-lift`
- `#issue/i-m-evenness`
- `#issue/right-hand-tension`

A plateau is when the same `#issue/` appears in ≥half of the last 6–8 logs (see `../base.md`).

### Coach's Note
One sentence the next session starts with. Not a summary — a forward-looking instruction.
- Good: "Start tomorrow with A→D at 50 BPM, then build back to 60"
- Bad: "Today was productive"

---

## Filled-in example (for reference)

```markdown
# Practice Log — 2026-05-23 (electric)

## Session Start
- **Date:** 2026-05-23
- **Time:** 09:15
- **Coaching mode:** full
- **Energy / Focus / Tension / Pain (1-4):** E3 F3 T1 P1
- **Guitar:** Squier Affinity Tele SH
- **Planned duration:** ~25 min
- **Context notes:** Saturday morning, fresh.

## Plan
- Warm-up: chromatic 1-2-3-4 on string 6 at 60 BPM
- Technique: A chord muting drill (8 down-strums × 4)
- Song: Knockin' on Heaven's Door — first attempt
- Theory: open string names (E A D G B E)

## Section 1 — Warm-up (3 min)
- **Target:** clean 1-2-3-4 ascending and descending, no fret buzz
- **Result:** clean ascending; descending had buzz on pinky-to-ring transition
- **Reflection:** D=2 A=2 T=1 Te=1

## Section 2 — Technique (10 min)
- **Target:** 8 down-strums of A, no stray string 6 noise. Aim for 3 sets of 8 clean.
- **Result:** 2 sets clean, 1 set had string 6 ring through 3 times
- **Reflection:** D=3 A=3 T=2 Te=2  H=1 (fretting hand thumb not muting string 6)

## Section 3 — Song (8 min)
- **Song / piece:** Knockin' on Heaven's Door
- **Lane:** Learning
- **Target:** play G-D-C loop 4 times, even strumming, no stops
- **Result:** got through 2 loops cleanly, lost the strum on the 3rd
- **Reflection:** D=2 A=2 T=3 Te=2

## Section 5 — Theory (3 min)
- **Concept:** open string names — E A D G B E (lowest to highest)
- **How it landed:** got it
- **Try again next session?:** no

## Tags
#roadmap/electric-justinguitar #lesson/grade-1-mod-1-a-chord #mode/full #status/repeat #issue/string-6-buzz #skill/chords #skill/rhythm

## Reflection
- **What clicked:** open string names landed fast; A chord finger shape itself is solid
- **What needs more reps:** thumb position to mute string 6 — that's the whole issue
- **Repeat / advance / simplify:** repeat — A chord muting needs another session before I can call it solid
- **Overall (1-4):** 2
- **Total actual duration:** ~24 min

## Coach's Note
- Tomorrow: start with the thumb-mute drill (no strumming, just place the chord and pluck each string one at a time, check that string 6 is dead). Then resume the 8-down-strums target.
```
