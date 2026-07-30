# ADR-0001: Secure, private, per-user storage for practice data

**Status:** Proposed
**Date:** 2026-07-27
**Deciders:** Artur (solo)

## Context

Guitar Coach is single-tenant and file-based today: all practice data (logs,
progress, streaks, repertoire, lessons) lives as Markdown/JSON in a **public**
Git repo. To turn it into a product it needs secure, private, **per-user**
storage with authentication and access control (see the epic in the tracker).

Constraints and forces gathered for this decision:

- **Solo developer, no time pressure** ("no rush, whenever"). Side project.
  Time is the scarcest resource, and it's better spent on the *product* (the
  consistency/habit features) than on rebuilding auth plumbing.
- **Web dashboard is the only near-term client.** No mobile or wearable in the
  next ~6 months — so cross-platform mobile SDKs are not a deciding factor now.
- **The AI coach stays the write path.** Today the coach (Cowork/Claude) writes
  files; going forward it must write to the datastore programmatically. So the
  store needs a clean server-side write API, not just a browser SDK.
- **Author background:** 15+ years platform engineering — very comfortable with
  Postgres/SQL and wary of lock-in; fully capable of a custom backend, but that
  capability isn't the bottleneck — time is.
- **Cost sensitivity:** should be free or near-free at 1–100 users.
- **Primary driver was left unspecified** — so this ADR recommends a default and
  names the one factor that would flip it (see Trade-off Analysis).

## Decision

Adopt a **managed Postgres Backend-as-a-Service (Supabase)** as the storage +
auth + access-control foundation: a Postgres schema we own, Supabase Auth for
identity, and Row-Level Security (RLS) for per-user isolation. The AI coach
writes server-side; the web dashboard reads via the auto-generated API scoped by
the logged-in user.

This is a recommendation, not a lock-in choice — see the escape hatch under
Consequences.

## Options Considered

### Option A: Managed Postgres BaaS — Supabase (recommended)

Postgres database (schema we design) + Supabase Auth + Row-Level Security, with
an auto-generated REST API (PostgREST) that enforces RLS per request. ([RLS is the
authorization layer, scoped to the user's auth token](https://supabase.com/docs/guides/database/postgres/row-level-security); [auto REST API via PostgREST](https://supabase.com/docs/guides/api).)

| Dimension | Assessment |
|-----------|------------|
| Complexity | Low–Med — write a schema + RLS policies; no auth code to build |
| Cost | Free tier covers 1–100 users; ~$25/mo if/when it matters |
| Scalability | Fine well past personal scale; it's just Postgres |
| Team familiarity | High — real Postgres + SQL, the author's home turf |
| Lock-in | Low — plain Postgres; self-hostable, `pg_dump`-portable |

**Pros:** almost no backend to build; per-user security is declarative (RLS);
real SQL schema (owned, not proprietary); the coach can write server-side with a
service key while the dashboard reads under the user's token; easy migration from
the current Markdown/JSON.
**Cons:** free projects **pause after ~1 week of inactivity** ([source](https://infrafree.dev/en-us/provider/supabase)) — a cold start for a
low-traffic personal app, or pay to avoid; RLS policies need careful testing
(get them wrong and data leaks); some Supabase-specific conventions to learn.

### Option B: Firebase (Firestore) BaaS

Google's BaaS: Firestore (NoSQL document DB) + Firebase Auth + security rules.

| Dimension | Assessment |
|-----------|------------|
| Complexity | Low — managed auth + DB |
| Cost | Generous free tier |
| Scalability | Very high (more than needed) |
| Team familiarity | Low–Med — NoSQL + proprietary query model, not the author's SQL background |
| Lock-in | High — proprietary data model and APIs |

**Pros:** battle-tested; excellent client SDKs (esp. mobile — not needed yet);
generous free tier that doesn't pause.
**Cons:** NoSQL document model is a poorer fit for the relational-ish practice
data and for a platform engineer who thinks in SQL; higher lock-in; its main
advantage (mobile SDKs) isn't relevant near-term.

### Option C: Custom backend (own API + Postgres + auth)

A hand-built service (e.g. Kotlin/Ktor or similar) + Postgres + an auth library.

| Dimension | Assessment |
|-----------|------------|
| Complexity | High — build identity, sessions, access control, deploy/ops |
| Cost | Low infra, high time |
| Scalability | Whatever you build |
| Team familiarity | High (language/stack) |
| Lock-in | None |

**Pros:** total control; strongest portfolio/learning value; no third-party
constraints; uses the author's core skills.
**Cons:** you rebuild auth and access control — exactly the plumbing BaaS gives
free — before writing a single product feature; ongoing ops burden; slowest path
to a second user. On a no-rush side project this mostly *delays the actual
product*.

## Trade-off Analysis

The swing factor is the **primary driver that wasn't picked**:

- If the driver is **ship / spend time on the product** (most likely, given
  "no rush" paired with a solo side project) → **Option A**. It removes auth and
  access-control work while still letting the author own the interesting part (the
  Postgres schema), and it fits the web-first, coach-writes-server-side shape.
- If the driver is explicitly **"build & own it" for learning/portfolio** →
  **Option C** is defensible — and even then you can use Supabase's Postgres as
  the database and build only the API layer, so it's not all-or-nothing.

Firebase (B) loses here: its headline strength is mobile SDKs (not needed soon),
and its NoSQL/proprietary model works against both the data shape and the
author's SQL background.

Web-first + "coach keeps writing" both favor A: the dashboard reads under the
user's token (RLS enforced), and the coach writes server-side with a service
key — no custom API required for either path on day one.

## Consequences

- **Easier:** per-user privacy and access control become configuration (RLS),
  not code; a second user is genuinely close; the web dashboard has a backend to
  build on immediately.
- **Harder:** RLS policies must be tested deliberately; the free tier's inactivity
  pause needs a decision (accept cold start, keep-warm ping, or pay).
- **Escape hatch (low lock-in):** because it's plain Postgres, if Supabase ever
  disappoints, the schema and data move via `pg_dump` to self-hosted Postgres or a
  custom backend — Option C stays open later without a rewrite of the data model.
- **To revisit:** how the coach authenticates to write (service-role key vs. a
  thin write endpoint vs. user token) — a design task inside the epic; and whether
  the public contribution heatmap becomes opt-in per user.

## Action Items

1. [ ] Confirm the primary driver (ship-first → A; build-to-own → C). Absent a
       strong reason, proceed with **A (Supabase)**.
2. [ ] Design the Postgres schema (users, sessions/logs, progress, streaks,
       repertoire/lanes, lessons) — the part worth owning.
3. [ ] Draft RLS policies (owner-only read/write) and a test that proves
       cross-user isolation.
4. [ ] Decide the coach's write mechanism (service key vs. write endpoint).
5. [ ] Write a migration from the current Markdown/JSON into the schema.
6. [ ] Decide free-tier handling (accept pause / keep-warm / paid) before launch.

## Sources

- [Supabase — Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [Supabase — Auth](https://supabase.com/docs/guides/auth)
- [Supabase — Data REST API (PostgREST)](https://supabase.com/docs/guides/api)
- [Supabase free tier notes — inactivity pause](https://infrafree.dev/en-us/provider/supabase)
