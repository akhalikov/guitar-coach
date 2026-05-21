# Weekly Review Template

Filename: `../guitar-coach-logs/logs/<instrument>/YYYY/MM-DD-week.md` (use today's Saturday date — written to the **private logs repo**).

The weekly review is **tag-driven** — the coach reads the past 7 daily logs and aggregates the tag block, not the prose. Prose comes second, as commentary on what the tags reveal.

---

## Data the coach must aggregate first

Before writing the review, scan all daily logs from the past 7 days and compute:

1. **`#status/*` distribution** — how many sessions ended `repeat` vs. `advance` vs. `simplify`. A healthy week is mostly `repeat` with at least one `advance`. ≥2 `simplify` calls = something's pushing too hard or readiness was off.
2. **`#issue/*` recurrence** — sort issue slugs by occurrence count. Any slug appearing in ≥half of this week's logs is **sticky**. Any slug appearing in ≥half of the last 6–8 logs (cross-week) is a **plateau candidate** — see `../base.md` plateau rule.
3. **`#mode/*` distribution** — what mode dominated. All `full`? Good. Mostly `bad-day`? Time to investigate why (life stressor? overtraining?).
4. **`#skill/*` coverage** — which skill areas got touched. A week with only `#skill/chords` and nothing else means rhythm/scales/repertoire are starving.
5. **`#lesson/*` movement** — same lesson all week (fine, building deep) or different lessons (fine, broad cycle)? If same lesson + most `#status/repeat` for 2+ weeks = plateau.
6. **Numerical reflection trends** — average D, A, T, Te across sections. If average Difficulty crept up day-by-day, the curriculum is moving faster than the body. If Tension is averaging 3+, something's wrong with technique or fatigue.

---

## Template

```markdown
# Weekly Review — Week of YYYY-MM-DD (electric | classical)

## Sessions This Week
- **Count:** N sessions
- **Total practice time (est.):** ~M minutes
- **Daily logs:** [link] [link] [link] ...
- **Pieces / songs touched:** ...

## Tag Aggregation

### Status distribution
| Status | Count | Notes |
|---|---|---|
| `#status/repeat` | N | (healthy default) |
| `#status/advance` | N | (lessons that moved forward) |
| `#status/simplify` | N | (where we backed off — review why) |

### Recurring issues (sticky this week)
| Issue tag | Sessions | Trajectory (vs. last week) |
|---|---|---|
| `#issue/<slug>` | N | improving / same / worse / new |

### Mode distribution
| Mode | Count |
|---|---|
| `#mode/full` | N |
| `#mode/review-only` | N |
| `#mode/low-friction` | N |
| `#mode/recovery` | N |
| `#mode/bad-day` | N |

### Skill coverage
| Skill | Sessions touched |
|---|---|
| `#skill/chords` | N |
| `#skill/rhythm` | N |
| `#skill/scales` | N |
| `#skill/repertoire` | N |
| (etc.) | |

### Average reflection scores
- **Difficulty:** avg X.X (trend: rising / steady / falling)
- **Accuracy:** avg X.X (trend)
- **Timing:** avg X.X (trend)
- **Tension:** avg X.X (trend) — **flag if ≥3**

## Plateau Watch

Any issue tag appearing in ≥half of the last 6–8 logs (cross-week)? Name it.

- `#issue/<slug>` — appeared in M of last N logs → **plateau** → simplification recommended (see "Plan for next week")
- (or: "No plateaus this week.")

## Progress Made

Concrete improvements named specifically. Cite drill counts where the daily logs tracked them.

- (specific win — "A→D changes: 18/30 clean on Mon → 26/30 by Fri")
- (specific win)

## Songs / Pieces Touched

- (name) — (lane: Learning / Polishing / Maintenance; what changed this week)
- (note any lane changes — "moved from Learning → Polishing on Thursday after first clean end-to-end")

## Theory / Reading Absorbed

- (concept) — landed / partial / didn't land

## Curriculum Movement

- **JustinGuitar / Werner:** completed lessons → (list); next focus → (lesson)
- **Theory / reading:** completed topics → (list); next focus → (topic)

## Coach's Notes

Honest assessment. What's actually improving vs. what only feels like progress? Is the pace right? Is theory landing? Are sessions actually happening daily or only on weekends? Compare recordings if there are takes of the same piece from this week and prior.

- If `#status/simplify` count is ≥2: name what's being pushed too hard.
- If `#mode/bad-day` count is ≥2: name what's draining motivation.
- If average Tension ≥3: name what's causing it (posture, tempo, new technique).
- If a plateau is present: name it and the simplification you're applying.
- If the week was light on practice, say so plainly — note the count and what got in the way.

## Plan for Next Week

### Top 3 Priorities
1. (specific, actionable, measurable — e.g. "Get A chord muting consistent: no stray string 6 noise on 8/10 strums")
2. (specific)
3. (specific)

### Lesson / Piece Movement
- **Stay on:** ...
- **Ready to move on from:** ...
- **New piece / song to introduce:** ...

### Repertoire Lane Moves
- **Promote to Polishing:** ...
- **Promote to Maintenance:** ...
- **Demote / shelve:** ...

### Simplifications to Apply (if plateau detected)
- (which `#issue/` is being addressed)
- (which simplification — slower tempo / fewer chords / smaller chunk / etc.)
- (mini-win target at the simpler level)
```

---

## Behavior rules for the scheduled task

1. **If there are NO daily logs from the past week,** don't write a placeholder review. Send Artur a short notification asking how the week went and prompting him to either log retroactively or open a session. Stop there.
2. **If there ARE logs,** read them all. Aggregate tags first. Write the review. Update `../guitar-coach-logs/progress/<instrument>.md` (tick completed items, advance current focus, refresh "What's clicking" / "What's not", note plateau warnings). Update the per-piece/song file if any milestones hit (those live in `curriculum/` in the public repo).
3. **Promote songs between lanes** based on the week's evidence — don't wait for Artur to do it manually. (Promoted = noted in the review under "Repertoire Lane Moves" + actually updated in `songs.md` / `pieces/repertoire.md`.)
4. **Prepare a commit bash block** per `../base.md` (don't run git from sandbox).
5. **Notify Artur** with the top 3 priorities for the week ahead, a `computer://` link to the review, and a reminder to run the commit block.

Direct and technical. No fluff. If the prior week was light, say so honestly.
