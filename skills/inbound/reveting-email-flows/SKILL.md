---
name: reveting-email-flows
description: >-
  Design and deploy email sequences for the Reveting/WinsDay livestream content
  engine — guest outreach and booking confirmation, pre-show briefing, audience
  show promotion, post-show replay delivery, clip follow-up, and ongoing episode
  nurture. Triggers on: "show email sequence", "podcast email", "LinkedIn Live
  email", "guest outreach email", "Reveting email", "show nurture sequence",
  "episode announcement email", "post-show follow-up".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: inbound
  tags: [email, sequences, nurture, livestream, guest-outreach, content-engine, b2b-marketing]
  related_skills: [linkedin-live-strategy, reveting-calendar-flows, reveting-ghl-workflows, cold-email-strategy, mql-nurture]
  frameworks:
    - "Jessie Lizak (Reveting) — LinkedIn Live & livestream content engine"
    - "Outreach — Sales Engagement Cadence Design"
    - "HubSpot Academy — CRM Automation"
---

# Reveting Email Flows

## Overview

The Reveting content engine runs on three relationship layers — guests, audience,
and pipeline — each requiring distinct email sequences. Guest emails manage the
pre-show relationship (outreach → confirmation → briefing → thank-you → clips).
Audience emails build a weekly viewing habit (promotion → replay → clips → newsletter).
Pipeline emails convert engaged viewers into conversations. This skill maps all
six email sequence types, with subject lines, timing, and copy frameworks for each.

## When to Use

- "Write guest outreach emails for my LinkedIn Live show"
- "Build a pre-show briefing email sequence"
- "Create a weekly show promotion email"
- "Post-show replay and clip delivery email templates"
- "Ongoing newsletter sequence for show audience"
- "Re-engage cold show subscribers"

## Authoritative Foundations

**Jessie Lizak (Reveting) — livestream content engine.** Reveting's show
operations include structured guest outreach (personalized warm intro →
booking → briefing), post-show follow-up (replay + clip delivery), and
ongoing audience nurture that keeps the show top of mind between episodes.
The model: treat guests as champions, not transactions; treat viewers as a
community, not a list. Full sequence map → `references/reveting-email-sequences.md`.

**Outreach — Sales Engagement Cadence Design.** Multi-touch cadence timing
and channel mixing from Outreach's cadence design framework: 3-5 touch guest
outreach before declaring "no response," reminder sequences at 1 week / 24h /
1h before event, and a post-show 3-touch follow-up (thank-you → clips → 30-day
re-engage). These timing benchmarks are adapted for show guest relationships
rather than sales demos.

**HubSpot Academy — CRM Automation.** Lifecycle email best practices: trigger
on action (booking confirmed, tag added, pipeline stage change) rather than
on time alone; unenrollment conditions prevent double-sends; A/B test subject
lines in the weekly audience email to improve open rates over time.

## Prerequisites

- Email sending configured (SPF/DKIM authenticated domain)
- GHL, HubSpot, or equivalent CRM with workflow automation
- Guest pipeline active (see `reveting-ghl-workflows`)
- Calendar booking page live (see `reveting-calendar-flows`)
- Show replay URL or recording link system established
- Weekly episode clips ready within 48-72 hours of each show

## Step-by-Step Process

### Phase 1: Email Architecture Map

Six sequence types for the complete Reveting email system:

| Sequence | Audience | Trigger | Steps | Owner |
|---|---|---|---|---|
| **1. Guest Outreach** | Prospective guests | Manual outreach | 3 touches | Host / show producer |
| **2. Booking Confirmation** | Confirmed guests | Calendar booking | 1 immediate | GHL automation |
| **3. Pre-Show Briefing** | Confirmed guests | T-7 days | 2 emails | GHL automation |
| **4. Show Promotion** | Email subscribers | T-5 days before show | 2 emails | GHL/newsletter tool |
| **5. Post-Show** | Guests + subscribers | Show day +24h | 3 emails | GHL automation |
| **6. Ongoing Nurture** | All subscribers | Weekly recurring | Ongoing | GHL/newsletter tool |

### Phase 2: Sequence 1 — Guest Outreach (3-Touch)

Sent to prospective guests before they book. Personalized, short, and
conversation-first.

**Touch 1 — Introduction (Day 1)**

Subject: `[First Name], quick question about [Episode Topic]`

Body framework:
```
Hi [First Name],

I host [Show Name] — a weekly LinkedIn Live where [ICP description] share
[topic area]. Thought you'd be a great fit based on [specific recent post
or achievement — 1 sentence].

30-minute conversation, 3-5 talking points you control, and I'll send you
3 clips to share with your audience afterward.

Interested? Here's the booking link: [URL]

[Host Name]
```

**Touch 2 — Follow-up (Day 4)**

Subject: `Re: [First Name], quick question about [Episode Topic]`

Body framework:
```
Hey [First Name] — bumping this up in case it got buried.

Previous episode with [Past Guest Name] got [X] views and generated
[Y comments / DMs] — I'd love to create something similar with your
[expertise/story].

[Booking link]

[Host Name]
```

**Touch 3 — Final check (Day 9)**

Subject: `Last note — [Show Name] guest spot`

Body framework:
```
[First Name] — last follow-up on this.

If now's not a good time, no worries. I'll check back in a few months.
If you're open to it, grab a slot here: [URL]

Either way, great work on [recent achievement].

[Host Name]
```

### Phase 3: Sequence 2 — Booking Confirmation (Immediate)

**Trigger:** Calendar booking confirmed (GHL workflow — see `reveting-ghl-workflows`).

Subject: `You're confirmed for [Show Name] — here's what's next`

Body framework:
```
Hi [First Name],

You're confirmed for [Show Name] on [Date] at [Time TZ].

Here's your prep checklist:
- ✓ StreamYard link (click to test now): [StreamYard guest link]
- ✓ Browser: Use Chrome or Firefox only
- ✓ Equipment: Headset or wired earbuds, 720p+ webcam
- ✓ Background: Clean or virtual background
- ✓ Send headshot + short bio by [deadline — 5 days before]: [upload link]

We'll have a 15-minute briefing call before the episode —
look for a separate calendar invite from [Producer Name].

Any questions? Reply to this email.

See you on [Date],
[Host Name]
```

### Phase 4: Sequence 3 — Pre-Show Briefing (2 Emails)

**Email 1 — Briefing invite (T-7 days)**

Subject: `Pre-show briefing for your [Show Name] episode`

Body framework:
```
Hi [First Name],

Your episode is in 7 days — [Date] at [Time TZ].

Book your 15-minute pre-show briefing with me here:
[Briefing call booking link]

On the call we'll:
- Confirm your 3-5 talking points
- Review the show format and what to expect
- Do a quick tech check on StreamYard

If none of those times work, reply and I'll find an alternative.

[Host Name]
```

**Email 2 — Episode prep (T-3 days)**

Subject: `3 days to your [Show Name] episode — quick read`

Body framework:
```
Hi [First Name],

Your episode is in 3 days. Here's your final prep:

YOUR EPISODE
Topic: [Episode Topic]
Date: [Date] at [Time TZ]
Your StreamYard link: [guest link]

TALKING POINTS WE'LL COVER
1. [Point 1]
2. [Point 2]
3. [Point 3]

The conversation is yours to guide — these are starting points.
Audience questions will come in live; I'll weave them in.

See you [Day],
[Host Name]
```

### Phase 5: Sequence 4 — Show Promotion (2 Emails to Audience)

**Email 1 — Episode preview (T-5 days before show)**

Subject: `[Show Name] this [Day] — [Guest First Name] on [Topic Hook]`

Body framework:
```
Hey [First Name],

This [Day] on [Show Name]:

[Guest Full Name], [Title] at [Company], joins us to talk about
[1-2 sentence episode hook — what the audience will learn].

Join live on LinkedIn: [LinkedIn Live event link]
[Date] at [Time TZ] — set a reminder

Or subscribe to catch the replay: [YouTube or podcast link]

See you live,
[Host Name]
```

**Email 2 — Day-of reminder (Show day, 2 hours before)**

Subject: `We're live in 2 hours — [Guest First Name] + [Show Name]`

Body framework:
```
Hey [First Name],

Reminder: [Show Name] starts in 2 hours.

[Date] at [Time TZ] — LinkedIn Live
[Guest First Name] is joining us to talk about [topic hook, one sentence].

→ Watch live: [LinkedIn Live link]

[Host Name]
```

### Phase 6: Sequence 5 — Post-Show (3 Emails)

**Email 1 — Guest thank-you + replay (Guest, T+24 hours)**

Subject: `[Show Name] is live — your episode + replay link`

Body framework:
```
Hi [First Name],

Your [Show Name] episode is live on LinkedIn. The replay is getting
great engagement.

→ Watch and share: [replay link]

A few highlights from your episode:
- [Key moment or quote]
- [Key moment or quote]

Clips from your conversation will be ready in [X] days —
I'll send them directly so you can share with your audience.

Thank you for showing up and sharing so openly. Your perspective
on [topic] added real value to our community.

[Host Name]
```

**Email 2 — Clip delivery (Guest + subscribers, T+4 days)**

Subject: `Your 3 clips from [Show Name] — ready to post`

Body framework (for guest):
```
Hi [First Name],

Your clips from [Show Name] are ready. These are your best moments —
native-format and ready to post directly to LinkedIn.

CLIP 1: [title / hook] → [download or Drive link]
CLIP 2: [title / hook] → [download or Drive link]
CLIP 3: [title / hook] → [download or Drive link]

Suggested caption for Clip 1:
"[Hook line pulled from clip]. We talked about this on [Show Name]
this week. Full replay: [link]"

The best time to post: next [day] between 7-9 AM or 12-1 PM
(highest LinkedIn feed reach per van der Blom data).

Thank you again,
[Host Name]
```

**Email 3 — Audience replay + newsletter (Subscribers, T+3 days)**

Subject: `[Episode number] [Guest First Name] on [Topic Hook] — replay + key takeaways`

Body framework:
```
Hey [First Name],

In case you missed it — here's [Episode number] of [Show Name].

[Guest Full Name] from [Company] joined us to talk about [topic].

TOP TAKEAWAYS:
→ [Takeaway 1 — one sentence]
→ [Takeaway 2 — one sentence]
→ [Takeaway 3 — one sentence]

Watch the replay: [YouTube or LinkedIn replay link]
Listen on podcast: [Podcast RSS or Spotify link]

Next week: [Brief teaser for next guest or topic]

[Host Name]
```

### Phase 7: Sequence 6 — Ongoing Nurture (Weekly)

**Weekly episode announcement (every show week)**

Sent 5 days before each episode to all subscribers:

- Subject: `[Show Name] this [Day]: [Guest Name] on [Topic Hook]`
- Body: Guest spotlight (3 sentences), live link, podcast/YouTube fallback
- Always include: "Forward to someone who would love this"

**Monthly digest (optional, non-show months or low-cadence)**

- Subject: `[Month] on [Show Name] — 4 episodes, top moments`
- Body: Episode list with replay links + 1 community question or insight

**Re-engagement sequence (inactive >60 days)**

3-touch re-engagement for subscribers who haven't opened in 60+ days:

| Touch | Subject | Strategy |
|---|---|---|
| 1 | `Still interested in [Show Name]?` | Simple check-in with replay |
| 2 | `Our most-watched episode of the year` | High-value content resend |
| 3 | `We'll miss you — unsubscribe anytime` | Permission remover + final CTA |

If no open or click after touch 3: suppress from active list (do not delete —
they may re-engage from LinkedIn or social).

## Output Format

Reveting email system: 6-sequence architecture map, copy frameworks for all
11 email variants (guest outreach ×3, confirmation, pre-show ×2, promotion ×2,
post-show ×3), weekly episode announcement template, and re-engagement sequence.

## Quality Check

- [ ] Guest outreach is personalized (1 specific detail per touch) — not blast copy
- [ ] Booking confirmation includes prep checklist and StreamYard test link
- [ ] Briefing email sent at T-7 days (not T-1)
- [ ] Clip delivery email includes specific file links (not "coming soon")
- [ ] Weekly audience email includes live link + podcast/YouTube fallback
- [ ] Post-show replay email sent within 24 hours of show end
- [ ] Re-engagement sequence has 3 touches with suppression at the end
- [ ] All automated sequences have CRM unenrollment conditions (see `reveting-ghl-workflows`)
- [ ] Subject lines are conversation-first, not broadcast-announcement style

## Common Pitfalls

1. **Generic guest outreach.** A guest outreach email that could have been sent
   to anyone gets a <5% reply rate. One sentence of specific context (recent
   post, shared connection, achievement) doubles replies.

2. **Booking confirmation without prep checklist.** Guests who don't know about
   browser requirements or headshot deadlines create last-minute admin.

3. **No briefing email at T-7.** Sending prep info 24 hours before the show
   leaves no time for topic refinement or tech issues.

4. **Clip delivery delayed past 5 days.** Guests lose momentum to share clips
   if they arrive more than 5 days after the show. Set an SLA.

5. **Weekly email sent morning-of.** Promoting the show 2+ hours before go-live
   only — not 5 days before — misses everyone who doesn't check email daily.

6. **No subject line testing.** The weekly audience email is the best A/B
   testing opportunity in the system; not testing it leaves open-rate gains
   on the table.

7. **Treating guests like leads.** Post-show emails to guests should feel like
   a thank-you from a peer, not a nurture sequence from a CRM. Keep the voice warm.

8. **No re-engagement logic.** Without a re-engagement sequence and suppression,
   the list grows stale and deliverability erodes over time.

## Execution Artifacts

- `references/framework-notes.md` — Framework index and authority routing
- `templates/output-template.md` — Deliverable shell for email system design
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/reveting-email-sequences.md` — Full sequence tables, timing benchmarks, and copy patterns

## Related Skills

- **linkedin-live-strategy**: Full Reveting content engine playbook (Jessie Lizak)
- **reveting-ghl-workflows**: GHL automation that sends these sequences
- **reveting-calendar-flows**: Calendar booking that triggers Sequence 2
- **cold-email-strategy**: Additional outreach patterns for guest outreach cold emails
- **mql-nurture**: Audience nurture patterns for converting viewers to pipeline
