---
name: reveting-ghl-workflows
description: >-
  Build Go High Level automation workflows for the Reveting/WinsDay livestream
  content engine — guest CRM pipeline, confirmation sequences, show-day reminders,
  post-show clip delivery, and audience capture automations. Triggers on: "Go High
  Level", "GHL workflow", "GHL automation", "Reveting GHL", "show CRM",
  "guest pipeline automation", "GHL for podcast", "livestream CRM".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: inbound
  tags: [ghl, go-high-level, automation, crm, livestream, content-engine, b2b-marketing]
  related_skills: [linkedin-live-strategy, reveting-streamyard-flows, reveting-calendar-flows, reveting-email-flows, hubspot-setup]
  frameworks:
    - "Jessie Lizak (Reveting) — LinkedIn Live & livestream content engine"
    - "Go High Level — official automation documentation (help.gohighlevel.com)"
    - "HubSpot Academy — CRM Automation"
---

# Reveting GHL Workflows

## Overview

Go High Level (GHL) is the all-in-one CRM, automation, and communication
platform behind many agency-run content programs. For a Reveting-style weekly
show, GHL handles the operational layer: guest pipeline management, automated
confirmation and briefing sequences, show-day reminders, post-show thank-you
and clip delivery, and audience capture from LinkedIn live comments and form
fills. This skill covers the full GHL workflow architecture for a weekly
LinkedIn Live show operation.

## When to Use

- "Set up GHL for a weekly LinkedIn Live show"
- "Automate guest confirmation and pre-show briefing in Go High Level"
- "Build a show-day reminder workflow in GHL"
- "Capture audience leads from LinkedIn Live in GHL"
- "Post-show clip delivery automation"
- "GHL pipeline for podcast guest management"

## Authoritative Foundations

**Jessie Lizak (Reveting) — livestream content engine.** Reveting operates
multiple B2B livestream shows with structured guest pipelines and post-show
follow-up systems. The operational model: every guest moves through a tracked
pipeline (Prospect → Shortlisted → Confirmed → Recorded → Past Guest), and
every show generates automated follow-up for both guests and engaged viewers.
Full workflow maps → `references/ghl-workflow-reference.md`.

**Go High Level — official automation documentation.** GHL Workflows (formerly
called Smart Campaigns) support triggers from form fills, appointment bookings,
calendar confirmations, tags, pipeline stage changes, and inbound SMS/email.
Actions include email sends, SMS sends, task creation, pipeline stage moves,
tag adds, and webhook calls. Documentation: help.gohighlevel.com/support/home.

**HubSpot Academy — CRM Automation.** Lifecycle stage discipline and
workflow trigger patterns from HubSpot Academy inform GHL pipeline design:
contact properties as lifecycle gates, enrollment triggers on stage change,
and unenrollment logic to prevent double-sends.

## Prerequisites

- GHL account (Agency or Location tier with Workflows enabled)
- Show calendar connected to GHL (native GHL calendar or Cal.com webhook)
- Email sending domain authenticated in GHL (SPF/DKIM configured)
- SMS sending number provisioned (Twilio or LC Phone in GHL)
- Guest application form built (GHL Forms or linked external form)

## Step-by-Step Process

### Phase 1: Subaccount and Pipeline Architecture

1. **Create a dedicated Location (subaccount)** in GHL for the show if it
   is client-run; or use a dedicated Pipeline in an existing location.
2. **Build the Guest Pipeline** with 6 stages:

| Stage | Description | Exit trigger |
|---|---|---|
| **Prospect** | Identified potential guest — not yet reached out | Manual move or form fill |
| **Outreach Sent** | Initial invite email sent | Reply or 7-day no response |
| **Shortlisted** | Responded positively, slot not yet confirmed | Calendar booking |
| **Confirmed** | Booking confirmed, episode assigned | Day of recording |
| **Recorded** | Show complete, clips in production | Clip delivery |
| **Past Guest** | Clips sent, relationship archived | — |

3. **Build the Audience Pipeline** with 3 stages:

| Stage | Description |
|---|---|
| **Show Subscriber** | Email captured; receiving episode announcements |
| **Engaged Viewer** | Commented, DMed, or attended 2+ shows |
| **CSQL** | Booked a call or inbound inquiry from show content |

### Phase 2: Contact Tags and Custom Fields

Standard tags for the show CRM:

| Tag | Applied when |
|---|---|
| `show-guest` | Added to guest pipeline |
| `show-confirmed-ep[N]` | Episode number confirmed |
| `show-viewer` | Captured from audience form or DM |
| `show-clip-delivered` | Post-show clip email sent |
| `show-referral` | Guest referred by past guest |

Custom fields on contact record:

| Field | Type | Notes |
|---|---|---|
| Episode Number | Number | Assigned on confirmation |
| Recording Date | Date | From calendar booking |
| Episode Topic | Text | Guest-submitted on application |
| Headshot URL | Text | Uploaded during booking |
| LinkedIn Profile URL | URL | Required for show promotion |
| Guest Bio (short) | Text area | 50-word bio for lower thirds |

### Phase 3: Workflow — Guest Confirmation Sequence

**Trigger:** Pipeline stage moves to "Confirmed" OR calendar appointment confirmed.

**Sequence:**

| Step | Delay | Action |
|---|---|---|
| 1 | Immediate | Send confirmation email (see `reveting-email-flows`) |
| 2 | Immediate | Create task: "Collect headshot + bio for [Guest Name]" |
| 3 | Immediate | Tag contact `show-confirmed-ep[N]` |
| 4 | 2 days before recording | Send pre-show briefing email |
| 5 | 2 days before recording | Send SMS reminder: "Your [Show Name] episode is in 2 days. Reply READY or RESCHEDULE." |
| 6 | 1 day before recording | If no SMS reply: send reminder email |
| 7 | Recording day (1 hour before) | Send SMS: "We go live in 1 hour. Here's your StreamYard link: [link]" |
| 8 | Recording day (30 min before) | Create task: "Tech check with [Guest Name]" |

**Unenrollment:** If contact books a reschedule or cancels, unenroll and move pipeline to Shortlisted.

### Phase 4: Workflow — Show-Day Reminder Sequence

**Trigger:** Calendar event confirmed with event type "Show Recording."

Separate from guest sequence — targets the show *host and production team*:

| Step | Delay | Action |
|---|---|---|
| 1 | 24 hours before | Internal email to host: run-of-show, guest name, talking points |
| 2 | 24 hours before | Internal Slack webhook (if configured): "#show-ops Episode [N] tomorrow at [time]" |
| 3 | 2 hours before | SMS to host: "Episode [N] starts in 2 hours. StreamYard link: [link]" |
| 4 | Post-show (1 hour after end time) | Trigger: "Post-Show" workflow (Phase 5) |

### Phase 5: Workflow — Post-Show Sequence

**Trigger:** Tag `show-recorded-ep[N]` added manually after show ends.

| Step | Delay | Action |
|---|---|---|
| 1 | Immediate | Move guest pipeline to "Recorded" |
| 2 | Immediate | Create task: "Download and clip recording for Ep[N]" |
| 3 | 24 hours | Send guest thank-you email with replay link (see `reveting-email-flows`) |
| 4 | 3-5 days | Send guest clip delivery email (3 clips + carousel for their feed) |
| 5 | 5 days | Move guest pipeline to "Past Guest" |
| 6 | 5 days | Add tag `show-clip-delivered` |
| 7 | 30 days | Create task: "Re-engage [Guest] for referral or next episode" |

### Phase 6: Workflow — Audience Capture

**Trigger:** Form fill on show page OR webhook from LinkedIn comment capture tool.

| Step | Delay | Action |
|---|---|---|
| 1 | Immediate | Add contact to Audience Pipeline at "Show Subscriber" |
| 2 | Immediate | Tag `show-viewer` |
| 3 | Immediate | Send welcome email: "You're on the [Show] list" + replay of latest episode |
| 4 | Weekly (recurring) | Send episode announcement email on show day (see `reveting-email-flows`) |
| 5 | If link clicked 2+ times | Move to "Engaged Viewer" stage |
| 6 | If meeting booked | Move to "CSQL" stage + notify sales/host |

### Phase 7: Reporting Dashboard

Configure the following GHL dashboard widgets:

| Widget | Metric | Target |
|---|---|---|
| Pipeline funnel | Guest stages: Prospect → Past Guest | See conversion per stage |
| Contacts added | New `show-viewer` contacts per month | Growth trend |
| Workflow completion | Guest confirmation sequence completion % | >90% |
| Task completion | Open vs completed show tasks | <5 open at week end |
| Email open rate | Confirmation + briefing sequences | >50% |
| SMS reply rate | Show-day reminder replies | >40% |

## Output Format

GHL show operations kit: 6-stage guest pipeline, 3-stage audience pipeline,
contact tags and custom fields schema, 4 workflow maps (confirmation, show-day,
post-show, audience capture), reporting dashboard spec, and 30-day relationship
task system.

## Quality Check

- [ ] Guest pipeline has 6 stages with clear exit trigger per stage
- [ ] All workflows have unenrollment conditions to prevent double-sends
- [ ] SMS steps have reply-based branching (READY / RESCHEDULE)
- [ ] Custom fields include Episode Number and Recording Date
- [ ] Post-show workflow triggers on manual tag (not time-based) to avoid firing before show ends
- [ ] Audience capture workflow has weekly recurring episode announcement
- [ ] Dashboard includes pipeline funnel and email/SMS open rates
- [ ] Email sending domain SPF/DKIM verified before any sequence goes live

## Common Pitfalls

1. **No unenrollment logic.** Without exit conditions, guests who reschedule
   receive both the old sequence and the new one. Always add "if appointment
   cancelled → unenroll from confirmation sequence."

2. **SMS without opt-in.** GHL SMS requires explicit opt-in consent; use the
   guest application form to capture checkbox consent before any SMS sends.

3. **Tag-based trigger without tag cleanup.** If `show-recorded-ep[N]` is not
   removed after post-show workflow runs, re-adding it later re-triggers the
   sequence. Use "Remove Tag" as the final workflow step.

4. **Single pipeline for guests and audience.** Guests and viewers have
   different journeys; mixing them creates false funnel metrics. Separate pipelines.

5. **No 30-day re-engagement task.** Past guests are the best source of referrals
   and repeat appearances. Build the task — do not rely on memory.

6. **Manual clip delivery.** Clip emails sent ad-hoc get deprioritized; the
   post-show workflow forces the 3-5 day delivery SLA.

7. **Dashboard not reviewed weekly.** GHL dashboards only drive behavior if the
   show ops team looks at them. Schedule a 10-minute Monday ops check.

## Execution Artifacts

- `references/framework-notes.md` — Framework index and authority routing
- `templates/output-template.md` — Deliverable shell for GHL workflow kit
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/ghl-workflow-reference.md` — Pipeline specs, workflow trigger tables, and GHL field reference

## Related Skills

- **linkedin-live-strategy**: Full Reveting content engine playbook (Jessie Lizak)
- **reveting-streamyard-flows**: StreamYard live production setup
- **reveting-calendar-flows**: Guest booking calendar connected to GHL
- **reveting-email-flows**: Email templates that GHL workflows send
- **hubspot-setup**: Alternative CRM if GHL is not in use
