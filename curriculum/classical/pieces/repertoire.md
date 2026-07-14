# 🎼 Pieces — Classical (Werner Vol 1)

Three lanes per the repertoire convention (see `../../../prompts/base.md` → "Repertoire lanes"). Future per-piece detail files will live alongside this file (e.g. `pieces/nocturne.md`, `pieces/etude-1.md`) once any piece reaches the Polishing lane.

---

## Learning

*Actively building, fragile. Needs slow practice and full attention. Pull from here first in normal sessions. Aim for **one** piece here at a time.*

- **Ode to Joy** (p.26) — Phase 4. First contact 2026-06-21 (reading bottleneck, H=4). Update 2026-07-14: reading improving, D=2 A=2 on bars 1–8 with note-naming. One more quality session on bars 1–8 before extending to bars 9–16.

## Polishing

*Playable end-to-end but rough. Working on consistency, feel, dynamics, memory, tone. The longest-tenure lane in classical — Werner specifically advises *staying* with pieces after they're "playable" so they settle.*

- **Nocturne** (p.16) — Phase 1 duet. Played end-to-end with Werner's backing track at pulse on 2026-05-20, eyes on page, no restart. Promoted from Learning 2026-05-23. Comfortable and confident with backing track. Needs more sessions for dynamics and full memory.
- **Five Melodies** (p.24) — Phase 3. Complete as of 2026-06-21. All 5 melodies hands-together at 50 BPM. Promoted from Learning 2026-06-21. Target: consistent 60 BPM with dynamics before Maintenance.
- **Spanish Romance — minor section** (Anonymous, outside piece) — Am arpeggio section only; major section deferred. Promoted from Learning 2026-06-21. Update 2026-07-14: tempo drift resolved (Te=1 at 50 BPM); bars 1–6 locked, bars 7–8 blocked by mini→full barre switch (isolation drill in daily core). Bars 9+ also barre-blocked — technique goal, not a lane issue. RH pattern: p-a-m-i.
- **Hurt** (Johnny Cash) — Outside piece / Part 2 spirit (fingerstyle accompaniment). Full song playable end-to-end, all chords and strumming patterns memorized. Added 2026-06-12. Technique focus: clean chord transitions at tempo, steady pulse through the section change. Verse→chorus transition drilled 2026-07-14 after two deferrals — seam held; downgraded to watch.

## Maintenance

*Solid, memorized, played at tempo with clean tone and dynamics. Pull from here in low-friction and bad-day mode. Also the lane for the **review piece** block in the daily core — replay one fully-learned piece to keep it warm and aim for higher musicality than last time.*

- **Etude No. 1** (p.14) — Phase 1 open-string etude. Fully functional as of 2026-05-20. Now used as sight reading warmup material. Promoted 2026-05-23.
- **Etude No. 2** (p.15) — Phase 1 etude. Fully functional as of 2026-05-21 (completed eyes-on-page, no restart). Now used as sight reading warmup material. Promoted 2026-05-23.
- **Moderato** (p.18–19) — Phase 2. Advanced 2026-05-24. Clean at 80 BPM. Promoted to Maintenance 2026-05-25.
- **A Fairy Tale** (p.20) — Phase 2 duet. Advanced 2026-05-25. Clean at 60 BPM, D=2 A=2. Promoted to Maintenance 2026-05-25.

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
