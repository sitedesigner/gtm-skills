---
name: reveting-calendar-flows
description: >-
  Configure calendar and booking flows for a weekly LinkedIn Live show — show
  slot management, guest application and booking pages, pre-show briefing calls,
  automated reminders, and no-show recovery. Triggers on: "calendar booking",
  "guest booking", "show scheduling", "Calendly for podcast", "GHL calendar",
  "Cal.com show booking", "live show calendar", "guest booking page".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: inbound
  tags: [calendar, booking, scheduling, guest-management, livestream, content-engine, b2b-marketing]
  related_skills: [linkedin-live-strategy, reveting-streamyard-flows, reveting-email-flows, reveting-ghl-workflows, webinar-strategy]
  frameworks:
    - "Jessie Lizak (Reveting) — LinkedIn Live & livestream content engine"
    - "Calendly — official scheduling documentation (calendly.com)"
    - "Outreach — Sales Engagement Cadence Design"
---

# Reveting Calendar Flows

## Overview

A consistent weekly show lives or dies on scheduling discipline. Reveting's
WinsDay model runs a **fixed recurring slot** (same day, same time, every week)
so the audience builds a habit — and the production team builds a workflow. This
skill covers the calendar architecture: guest booking pages, briefing call
scheduling, automated reminders (email and SMS), no-show recovery, and the
weekly slot protection that keeps the show on schedule without constant manual
coordination.

## When to Use

- "How do I set up a guest booking page for my show?"
- "Build a Calendly or Cal.com flow for LinkedIn Live guests"
- "What reminder sequence should I send before show recording?"
- "How do I handle no-shows for weekly live guests?"
- "Protect my weekly show slot from being overbooked"
- "Set up GHL Calendar for podcast guest bookings"

## Authoritative Foundations

**Jessie Lizak (Reveting) — livestream content engine.** WinsDay runs on a
fixed weekly cadence with structured guest scheduling: a booking page collects
bio, topic, headshot, and LinkedIn URL before confirmation; a 15-minute briefing
call precedes every episode; and no-show recovery uses a warm "let's reschedule"
email rather than a cold cancellation. Full booking flow → `references/calendar-booking-reference.md`.

**Calendly — official scheduling documentation.** Calendly publishes event type
configuration, routing form documentation, reminder sequence specs, and
integration guides at calendly.com/blog and developer.calendly.com. Calendly
routing forms allow pre-qualification before a booking link appears. Integrations:
HubSpot, Salesforce, GHL (via Zapier/Webhooks), Zoom, and Google Meet.

**Outreach — Sales Engagement Cadence Design.** Multi-touch reminder cadences
from Outreach's cadence design framework: 1 week + 24h + 1h before event
is the validated sequence for high no-show prevention. The pattern applies
equally to sales demos and show guest bookings.

## Prerequisites

- Calendar platform selected: GHL Calendar (if using GHL), Cal.com (open source), or Calendly (Pro+ for routing)
- GHL account or webhook-capable CRM for booking data sync
- Email sending configured (SPF/DKIM) for automated reminders
- SMS number provisioned for day-of reminders (optional but high-impact)
- Show slot locked: day of week and time fixed for minimum 8-week commitment

## Step-by-Step Process

### Phase 1: Show Slot Architecture

1. **Lock the weekly recording slot** before building any booking page:
   - Same day of week (e.g., every Wednesday)
   - Same time (e.g., 12:00 PM ET)
   - Duration: 60 min show + 15 min buffer = 75 min blocked
   - Recurring block on host calendar (Google Calendar or Outlook)
2. **Separate show time from LinkedIn Live broadcast time:**
   - Record with guest: Wednesday 12:00 PM ET
   - Go live on LinkedIn: same time if live-to-tape; or post-production clip
     releases on a scheduled day (e.g., Thursday 9:00 AM)
3. **Buffer days:** Block the day before (final prep) and the morning after
   (download, handoff to repurposing team).

### Phase 2: Guest Booking Page

Create a dedicated booking page for show guests — not a generic calendar link.

**Platform setup (Calendly example):**
1. Create a new Event Type: "WinsDay Guest Slot — 60 min Recording"
2. Set availability: show day only, single weekly slot
3. **Add intake form questions** (required):
   - First and last name
   - Company and title
   - Short bio (50 words — explain this will appear in show notes)
   - Episode topic / what you want to share (2-3 sentences)
   - LinkedIn profile URL
   - Headshot upload link or instructions (e.g., Google Drive folder link)
   - "I consent to receive SMS reminders" (checkbox — required for SMS workflow)
4. Set confirmation redirect to a thank-you page with:
   - What happens next (briefing call, StreamYard link, etc.)
   - Show prep checklist (camera, headset, browser requirements)
5. Connect to CRM: Calendly webhook → GHL (see `reveting-ghl-workflows`)

**Platform setup (GHL Calendar):**
1. Create Calendar under "Calendars" → "Create Calendar"
2. Type: Personal (for single host) or Round Robin (for multi-host)
3. Set slot: 60 min, buffer 15 min after
4. Set availability: show day and time only
5. Enable confirmation email (built-in) + SMS reminder (if LC Phone configured)
6. Add custom form fields matching Calendly intake questions above
7. Connect to Guest Pipeline: auto-move contact to "Shortlisted" on booking

**Platform setup (Cal.com):**
1. Create Event Type: "Show Guest Slot"
2. Duration: 60 min
3. Availability: custom schedule (show day only)
4. Booking questions: same intake fields as above
5. Webhooks → GHL or n8n for CRM sync

### Phase 3: Briefing Call Booking

**Optional but recommended:** Schedule a 15-minute pre-show briefing call
5-7 days before the recording date.

1. Create a separate Event Type: "WinsDay Pre-Show Briefing — 15 min"
2. Availability: flexible (any business day, excluding show day)
3. Form: minimal — name, episode number auto-populated from main booking
4. Purpose: tech check, topic refinement, rapport building
5. Include meeting link (Zoom, Google Meet, or GHL's built-in video)
6. **Send briefing call invite** automatically via GHL workflow 7 days before
   recording (see `reveting-ghl-workflows` Phase 3)

### Phase 4: Automated Reminder Sequence

Use Outreach-style cadence timing for show-day reliability:

| Reminder | Timing | Channel | Content |
|---|---|---|---|
| Booking confirmation | Immediately | Email | Confirmation + prep checklist + StreamYard test link |
| Briefing call invite | 7 days before | Email | Calendar link for 15-min pre-show call |
| Episode reminder | 3 days before | Email | Topic summary + what to prepare |
| Day-before reminder | 24 hours before | Email + SMS | "Tomorrow at [time]. StreamYard link: [url]" |
| Show-day reminder | 1 hour before | SMS | "In 1 hour. Link: [url]. Reply READY or HELP" |
| Tech check prompt | 15 min before | SMS | "Tech check now. Click link and test camera/mic" |

GHL workflow implementation: see `reveting-ghl-workflows` Phase 3.

### Phase 5: No-Show Recovery

Not every guest shows up. Recovery protocol:

**No response at start time:**
1. Wait 5 minutes → send SMS: "Hey [Name], we're live in the studio! Joining?"
2. Wait 10 minutes → call or voicemail (host or producer)
3. At T+15: producer holds show slot; host solo segment or reschedule episode

**Post no-show recovery (within 4 hours):**
1. Send warm email: "Life happens — let's find another slot" + rebooking link
2. Move guest pipeline to "Shortlisted" in GHL
3. Log reason (no-show) in contact notes for pattern tracking
4. If no response in 7 days: send final check-in; after 14 days, move to "cold" tag

**Prevention (reduce no-shows to <5%):**
- Verbal commitment on briefing call: "Are you confirmed for [date/time]?"
- Day-of SMS with direct reply option (READY or RESCHEDULE)
- Show producer assigned to monitor chat 30 min before show

### Phase 6: Multi-Host and Co-Host Coordination

For shows with rotating hosts or co-hosts:

1. **Shared calendar:** Single Google Calendar or GHL Calendar with all hosts
   as co-owners; booking page shows only slots when ALL hosts are available
2. **Round Robin:** Cal.com or Calendly round robin distributes guest slots
   across multiple hosts automatically
3. **Handoff protocol:** Booking confirmation CC's all hosts and producers
4. **Episode ownership:** One host = one episode; no last-minute swaps without
   48-hour notice to guest and team
5. **Shared prep doc:** Google Doc or Notion template per episode; auto-created
   by GHL workflow on booking confirmation

## Output Format

Show calendar system: weekly slot architecture (fixed day/time/buffer), guest
booking page setup (platform choice, intake fields, CRM sync), briefing call
booking page, 6-touch reminder sequence design, no-show recovery protocol,
and multi-host coordination rules.

## Quality Check

- [ ] Weekly show slot locked and recurring calendar block created
- [ ] Guest booking page includes all 6 intake fields (bio, topic, headshot, LinkedIn, SMS consent)
- [ ] Booking confirmed email includes prep checklist and StreamYard test instructions
- [ ] Reminder sequence covers: confirmation + 3 days + 24h + 1h + 15 min
- [ ] SMS reminders include READY / RESCHEDULE reply option
- [ ] No-show protocol defined and assigned to a responsible person
- [ ] CRM sync from booking to GHL guest pipeline confirmed working
- [ ] Briefing call scheduled 5-7 days before recording (not day-before)

## Common Pitfalls

1. **Generic calendar link.** Sending a generic "30-min meeting" link to guests
   signals low effort. A dedicated "Show Guest Slot" page with show branding
   sets the right expectation.

2. **No intake form.** Collecting bio, headshot, and topic at booking time
   eliminates 90% of pre-show admin — don't defer to "we'll handle it later."

3. **Single reminder email.** One confirmation email has a 30-40% open rate;
   the 6-touch sequence (including SMS) is what pushes no-show rates below 5%.

4. **Show slot not protected.** If the host's calendar allows other meetings to
   book over the show slot, the episode gets preempted. Recurring block +
   show-day booking blackout is required.

5. **Briefing call same day as show.** Last-minute briefings mean topic changes
   can't be prepped for; run them 5-7 days before.

6. **No rebooking link in no-show recovery email.** The recovery email must
   include an immediate rebooking link — friction in rescheduling loses guests.

7. **Headshot collected after booking.** Waiting until the show week to collect
   headshots delays graphic production. Collect at booking time.

## Execution Artifacts

- `references/framework-notes.md` — Framework index and authority routing
- `templates/output-template.md` — Deliverable shell for calendar flow design
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/calendar-booking-reference.md` — Platform comparison, intake field specs, and reminder cadence tables

## Related Skills

- **linkedin-live-strategy**: Full Reveting content engine playbook (Jessie Lizak)
- **reveting-ghl-workflows**: GHL automation triggered by calendar bookings
- **reveting-email-flows**: Email copy for confirmation and reminder sequences
- **reveting-streamyard-flows**: StreamYard tech check linked from booking confirmation
- **webinar-strategy**: Overlapping calendar and registration patterns for webinars
