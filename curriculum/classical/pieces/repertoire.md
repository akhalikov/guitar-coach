# 🎼 Pieces — Classical (Werner Vol 1)

Three lanes per the repertoire convention (see `../../../prompts/base.md` → "Repertoire lanes"). Future per-piece detail files will live alongside this file (e.g. `pieces/nocturne.md`, `pieces/etude-1.md`) once any piece reaches the Polishing lane.

---

## Learning

*Actively building, fragile. Needs slow practice and full attention. Pull from here first in normal sessions. Aim for **one** piece here at a time.*

- **Moderato** (p.18–19) — Phase 2. First full hands-together pass at 40 BPM on 2026-05-21. Next target: two clean passes at 50 BPM with metronome before advancing to A Fairy Tale (p.20).

## Polishing

*Playable end-to-end but rough. Working on consistency, feel, dynamics, memory, tone. The longest-tenure lane in classical — Werner specifically advises *staying* with pieces after they're "playable" so they settle.*

- **Nocturne** (p.16) — Phase 1 duet. Played end-to-end with Werner's backing track at pulse on 2026-05-20, eyes on page, no restart. Promoted from Learning 2026-05-23. Needs more sessions for dynamics and memory before Maintenance.

## Maintenance

*Solid, memorized, played at tempo with clean tone and dynamics. Pull from here in low-friction and bad-day mode. Also the lane for the **review piece** block in the daily core — replay one fully-learned piece to keep it warm and aim for higher musicality than last time.*

- **Etude No. 1** (p.14) — Phase 1 open-string etude. Fully functional as of 2026-05-20. Now used as sight reading warmup material. Promoted 2026-05-23.
- **Etude No. 2** (p.15) — Phase 1 etude. Fully functional as of 2026-05-21 (completed eyes-on-page, no restart). Now used as sight reading warmup material. Promoted 2026-05-23.

---

## Lane rules (quick reference)

- **One piece in Learning at a time.** Werner's own advice: "No more than one new piece at a time. Settle on the current before adding another." Two simultaneous Learning pieces is a yellow flag.
- **Short session (<20 min):** pull from Learning first.
- **Low-energy / bad-day mode:** pull from Maintenance first.
- **Promote Learning → Polishing** when the student can play end-to-end without restarting at half tempo, hands together.
- **Promote Polishing → Maintenance** when:
  - Played from memory
  - At target tempo with the metronome
  - With clear melody / accompaniment voicing
  - Dynamics and phrasing present (not just notes)
  - Consistent across multiple sessions

Werner's progression rule: **confident playing, not perfect.** And — critically — keep pieces in your fingers after they're playable. Don't sprint to the next one.

Full lane rules in `../../../prompts/base.md` → "Repertoire lanes".

---

## What the curriculum says about progression

From Werner's own key instructions (`../werner-key-instructions.md`):

- Study Part 1 in order; cover every piece on every page.
- Part 3 (technique routines + scales) runs **alongside** Part 1 from the start — those routines live in the **daily core** (mandatory ~10 min), not as a lane.
- Part 2 (chords) is flexible — interleave or save.
- **Raise the bar each piece:** evenness, tone, phrasing, dynamics. Don't accept the previous standard.

The planned sequence and Current Position marker live in `../werner-vol1-plan.md`. When a piece advances to a new lane, also note it on its `Done?` row in the Werner plan.

---

## Per-piece detail files (when to create them)

Create a `pieces/<piece-slug>.md` file when a piece reaches **Polishing**. The detail file mirrors the per-song format used on the electric side but adapted for classical:

- **Key** (and time signature)
- **Tempo** (current working BPM + target BPM)
- **Page** (in Werner Vol 1)
- **Technique focus** (e.g. p-i-m-a arpeggio, i-m alternation, slurs, dynamics)
- **Hand-position notes** (anything specific — barre, stretch, position shift)
- **Memorization status**
- **Werner video link** (if there is one for this piece)
- **Recordings index** (links to `../../../../guitar-coach-logs/logs/classical/recordings/*` takes of this piece — private repo)
- **Progress log** — dated bullets: first half-tempo run, first memorized, first at tempo, first with dynamics, etc.

A piece in Learning doesn't need its own file yet — the daily logs cover it. Spinning up the file is itself a sign the piece has settled enough to be worth tracking longitudinally.

---

## Logging milestones per piece

Once a `pieces/<piece-slug>.md` exists, dated milestones go in its `Progress log` section — not buried in daily logs. The Saturday weekly review handles **lane promotions** automatically based on the week's evidence (see `../../../prompts/log_templates/weekly.md` → "Repertoire Lane Moves").
