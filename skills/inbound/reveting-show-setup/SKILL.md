---
name: reveting-show-setup
description: >-
  Initialize a new Reveting livestream show with all production variables —
  show constants (set once at launch) and per-episode variables (set per
  recording) that power every email sequence, calendar description, GHL
  workflow, and StreamYard session. Triggers on: "new show setup", "Reveting
  show intake", "show variables", "show onboarding", "set up a new show",
  "new client show", "show constants", "episode variables".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: inbound
  tags: [reveting, show-setup, intake, variables, livestream, production, content-engine]
  related_skills: [linkedin-live-strategy, reveting-streamyard-flows, reveting-calendar-flows, reveting-email-flows, reveting-ghl-workflows]
  frameworks:
    - "Jessie Lizak (Reveting) — LinkedIn Live & livestream content engine"
    - "Go High Level — official automation documentation (help.gohighlevel.com)"
---

# Reveting Show Setup — Master Variable Intake

## Overview

Every Reveting show runs on two tiers of variables. **Tier 1 (Show Constants)**
are defined once when a new show launches and never change unless the show
itself changes. **Tier 2 (Episode Variables)** are filled in by the Production
Assistant before each recording.

Together these two tiers power every downstream system:
- All 7 email templates (T-14 activation through post-production)
- Both calendar description stages (new booking + event published)
- GHL guest pipeline and automation workflows
- StreamYard scene setup and guest invite links
- Post-production asset delivery

## When to Use

- "We have a new client show — what do I need to set up?"
- "What variables do I need before I can run the email sequence?"
- "New show onboarding checklist"
- "Set up show constants in app.reveting.com"
- "Production Assistant needs the episode intake for this week's guest"

## Authoritative Foundations

**Jessie Lizak (Reveting) — livestream content engine.** Reveting's
operational model for running 10+ B2B livestream shows simultaneously
requires a strict variable discipline: show constants locked at launch,
episode variables completed before any email is sent, and the
ww@reveting.com Google Calendar as the single source of truth. The
two-tier system is what allows the Production Assistant to operate
consistently across multiple client shows without confusion.

**Go High Level — official automation documentation.** GHL Workflows,
calendar triggers, and contact pipeline automation all depend on clean
variable data at the contact and appointment level. Custom fields
(Episode Number, Recording Date, Episode Topic) must be populated before
workflow enrollment triggers or the automations fail silently.

## Important Rules

1. **Never email a guest their raw submitted topics.** All topics must be
   edited to fit the show strategy before appearing in any email or
   calendar description.
2. **The ww@reveting.com calendar is the single source of truth.** All
   events must be set in Eastern Time (USA).
3. **Never guess the channel stack.** Pull from the Total Deliverables
   Document every time.
4. **Email 5 (immediate post-show) must go out within 1 hour of show end.**
   Video editors have a 24-hour SLA on clips; Email 6 must not exceed 36
   hours after the show.
5. **Guest LinkedIn follower threshold:** 5,000+ preferred. 1,000–4,999
   requires Production + Marketing Lead confirmation. Below 1,000 is a
   no-go unless no other option exists.
6. **When in doubt → WhatsApp Jessie.**

## Step-by-Step Process

### Phase 1: New Show Launch (Tier 1 — do once)

Complete every field in the Show Constants section of
`templates/output-template.md`:

1. **Show identity:** name, email, calendar account, timezone, day/time, durations
2. **Team:** host, producer, production assistant, signature block
3. **Channel stack:** confirm against Total Deliverables Document which
   platforms the show streams to — never assume
4. **Podcast & replay links:** Spotify, Apple Podcasts, YouTube channel,
   show website
5. **Booking & docs:** booking form link, Total Deliverables doc, client
   outline link, Google Drive root folder, StreamYard account URL, LinkedIn
   invite walkthrough video URL
6. **Guest qualification rules:** minimum follower count, content pillars,
   escalation contact, fallback show links for "not a fit" redirects

Save the completed Tier 1 doc in the show's Google Drive root folder.
Share with all team members. This is the reference document for every
Production Assistant working on this show.

### Phase 2: New Episode (Tier 2 — do per recording)

When a new booking appears in app.reveting.com:

1. Pull guest submission from: Calendars → Appointment List View → click
   guest → 3 dots → View Details → Form Submission
2. Complete Tier 2 (Episode Variables) in `templates/output-template.md`
3. **Edit topics** — do not use raw submitted topics. Format to 3–7 words
   per topic, aligned to show strategy
4. Verify guest LinkedIn followers → fit gate decision
5. If fit: proceed. If not fit: send "Not a Fit" email and stop
6. If info missing: email guest requesting missing info; do not publish event

### Phase 3: Pre-Send Checklist (before each email)

Use the Email Trigger Checklist in `references/reveting-show-variables.md`
to confirm every required variable is populated before each email goes out.
A missing StreamYard link or wrong time zone in Email 3 causes no-shows.

### Phase 4: Calendar Description Updates

Two stages — both documented in `references/reveting-show-variables.md`:
- **Stage 1 (New Booking):** Set immediately; includes placeholder text
  while topics are being formatted
- **Stage 2 (Event Published):** Updated when Production + Marketing Lead
  posts the event; includes finalized title, topics, and all platform links

## Output Format

Completed show setup document: Tier 1 (Show Constants, 30+ variables) and
Tier 2 (Episode Variables, 25+ variables per episode), email trigger
checklist with required variables per email, and calendar description
checklist with required variables per stage.

## Quality Check

- [ ] Tier 1 complete: all show constants filled, no blanks
- [ ] Channel stack confirmed against Total Deliverables Document (not guessed)
- [ ] Total Deliverables Document link populated and accessible
- [ ] Tier 2 complete before any episode email is sent
- [ ] Topics are edited and formatted — NOT raw guest submissions
- [ ] Guest LinkedIn followers verified against fit threshold
- [ ] ww@reveting.com calendar reflects correct Eastern Time
- [ ] StreamYard guest link generated per episode (not reused from previous)
- [ ] Email 5 SLA: within 1 hour of show end
- [ ] Email 6 SLA: within 24 hours, hard max 36 hours

## Common Pitfalls

1. **Reusing the StreamYard guest link from a previous episode.** Each guest
   needs a fresh link — reused links can break or admit the wrong person.

2. **Setting calendar time in guest's local timezone.** All calendar events
   must be set in Eastern Time (USA) regardless of guest timezone.

3. **Skipping Tier 1 and winging it per episode.** Without locked show
   constants, variable errors compound across emails. Complete Tier 1 once,
   correctly.

4. **Pulling topics directly from the booking form into Email 1.** Raw
   submitted topics are self-promotional and misaligned. Always edit first.

5. **Missing the Email 5 one-hour SLA.** The immediate post-show window is
   the highest-engagement moment — delay kills clip sharing momentum.

6. **Not preserving the original guest submission at the bottom of the
   calendar description.** The original submission is the audit trail.
   Always keep it at the bottom, even after the description is updated.

7. **Failing to check app.reveting.com daily.** Automations are unreliable.
   Manual daily check in Calendars → Appointment List View is required.

## Execution Artifacts

- `references/framework-notes.md` — Framework index and authority routing
- `templates/output-template.md` — Master intake form (Tier 1 + Tier 2 + checklists)
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/reveting-show-variables.md` — Full variable definitions, email trigger map, and calendar description templates

## Related Skills

- **reveting-email-flows**: The 7 email templates that consume these variables
- **reveting-calendar-flows**: Calendar booking setup fed by Tier 1 constants
- **reveting-ghl-workflows**: GHL custom fields and pipeline that store Tier 2 data
- **reveting-streamyard-flows**: StreamYard sessions powered by show constants
- **linkedin-live-strategy**: Full Reveting content engine playbook (Jessie Lizak)
