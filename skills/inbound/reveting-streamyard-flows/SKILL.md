---
name: reveting-streamyard-flows
description: >-
  Set up and operate StreamYard for the Reveting/WinsDay livestream content
  engine — brand scenes, guest invite flows, multi-destination streaming to
  LinkedIn Live, live production run-of-show, recording download, and
  repurposing handoff. Triggers on: "StreamYard", "StreamYard setup", "live
  show production", "StreamYard guest invite", "WinsDay production", "Reveting
  StreamYard", "go live setup", "streaming tool for LinkedIn Live".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: inbound
  tags: [streamyard, livestream, linkedin-live, live-production, content-engine, b2b-marketing]
  related_skills: [linkedin-live-strategy, reveting-calendar-flows, reveting-email-flows, reveting-ghl-workflows, content-distribution]
  frameworks:
    - "Jessie Lizak (Reveting) — LinkedIn Live & livestream content engine"
    - "StreamYard — official platform documentation (streamyard.com)"
---

# Reveting StreamYard Flows

## Overview

StreamYard is the browser-based studio behind most Reveting-style LinkedIn Live
shows. No software install required for guests — they join by link. The host
manages scenes, overlays, and guest cameras from a browser dashboard, streams
to LinkedIn Live (and optionally YouTube, Facebook, or a custom RTMP), and
downloads the recording for podcast and clip production.

This skill covers the full StreamYard operating model for a weekly WinsDay-style
show: brand setup, scene library, guest invite workflow, live run-of-show, and
the recording handoff that feeds the repurposing engine in `linkedin-live-strategy`.

## When to Use

- "How do I set up StreamYard for LinkedIn Live?"
- "Build scenes and overlays for a weekly B2B show"
- "What does a guest invite flow look like in StreamYard?"
- "How do I stream to LinkedIn Live from StreamYard?"
- "Run-of-show template for a 45-minute interview show"
- "Download StreamYard recording for podcast and clips"

## Authoritative Foundations

**Jessie Lizak (Reveting) — livestream content engine.** Reveting runs 10+
B2B livestream podcasts using StreamYard as the production layer. Public best
practices: brand consistency across every scene, low-friction guest onboarding
(browser link, no app), and clean chapter breaks every 8-12 minutes for
clipping. Full repurposing model → `references/streamyard-platform-reference.md`
and `linkedin-live-strategy`.

**StreamYard — official platform documentation.** StreamYard publishes
setup guides, destination integration docs, and billing tiers at
streamyard.com. The free tier allows one destination and 720p; the Basic
($49/mo) tier adds brand kit, custom overlays, multiple destinations, and
1080p. Professional ($99/mo) adds 8 guests, 8 destinations, and HD recording.
Capability matrix → `references/streamyard-platform-reference.md`.

## Prerequisites

- StreamYard account (Basic or Professional tier for brand kit + multi-destination)
- LinkedIn Creator mode enabled with LinkedIn Live access (request at linkedin.com/help/linkedin/answer/100225)
- Brand assets: logo (PNG transparent), show colors (hex), lower-third template
- Guest list with email addresses for invite links
- Recording storage: local drive, Google Drive, or Dropbox for handoff

## Step-by-Step Process

### Phase 1: Account and Brand Kit Setup

1. **Create StreamYard account** at streamyard.com; select Basic or Professional tier.
2. **Upload brand assets** under Brand → Brand Kit:
   - Logo (PNG with transparent background, minimum 400×400px)
   - Primary and accent colors (hex values)
   - Background image or color for full-screen scenes
3. **Add social profiles** under Destinations:
   - LinkedIn: connect via LinkedIn OAuth; authorize page or profile streaming
   - YouTube (optional): connect via Google OAuth for simulcast
   - Custom RTMP (optional): for website or podcast platform embeds
4. **Test connection**: create a private broadcast to verify all destinations receive stream.

### Phase 2: Scene Library Design

Build a scene library before the first live. Minimum 6 scenes for a WinsDay-style show:

| Scene | Purpose | Layout |
|---|---|---|
| **Holding / Countdown** | Pre-show buffer while attendees join | Full-screen graphic + ticker |
| **Host Solo** | Intro, segue, and close | Single camera fullscreen or offset |
| **Host + Guest** | Main interview segments | Side-by-side or 60/40 split |
| **Screen Share** | Demo, chart, or slide reference | Screen left, cameras right |
| **Quote / Highlight** | Pull-quote overlays during conversation | Background + text overlay |
| **End Card** | CTA and next episode date | Static graphic + social handles |

Naming convention: `[ShowName]-[SceneName]-v[n]` (e.g., `WinsDay-HostGuest-v2`).

### Phase 3: Overlay and Lower-Third Templates

1. **Lower thirds:** Guest name, title, and company. Use brand colors. Set display
   duration to 8 seconds (long enough to read, short enough not to distract).
2. **Show logo bug:** Persistent logo overlay in corner at 30–40% opacity.
3. **Ticker / scroll:** Optional bottom-of-frame text for episode topic or CTA.
4. **Banner overlays:** Episode number, sponsored by (if applicable), and hashtag.
5. Save all overlays to the Brand Kit for instant recall during live.

### Phase 4: Guest Invite Workflow

StreamYard guests join via a unique browser link — no app required.

1. **Create or open the broadcast** for the episode.
2. Click **Invite** → copy guest link.
3. Send link to guest via email (see `reveting-email-flows` pre-show briefing template).
4. **Pre-show tech check (15 min before go-live):**
   - Guest opens link in Chrome or Firefox
   - Confirm camera, microphone, and internet connection
   - Verify guest name display (edit in StreamYard if needed)
   - Brief guest on scene transitions and chapter marks
5. **Backup plan:** Have guest phone number for audio-only dial-in if link fails.
6. **Bring on screen:** Click guest tile → "Add to broadcast" when show starts.

### Phase 5: Multi-Destination Streaming Setup

1. In the broadcast, click **Go Live** → select all active destinations.
2. LinkedIn stream settings:
   - Title: Episode name with ICP keyword (e.g., "WinsDay Ep. 47 | How [Guest] Scaled RevOps to $10M ARR")
   - Description: 3-5 sentence episode summary + guest name + LinkedIn handle
   - Visibility: Public
3. If simulcasting to YouTube: set stream as Public or Unlisted for replay.
4. Click **Go Live** — StreamYard confirms all destinations are receiving.

### Phase 6: Live Production Run-of-Show

Standard run-of-show for a 45-minute WinsDay-style interview:

| Time | Action | Scene |
|---|---|---|
| T-5 min | Holding screen live; host welcomes early arrivals in comments | Holding |
| T-0 | Host intro, episode context, guest intro | Host Solo → Host + Guest |
| T+3 | Guest bio, origin story | Host + Guest |
| T+12 | Chapter 1: guest topic deep-dive | Host + Guest |
| T+24 | Chapter 2: tactical framework or case study | Host + Guest or Screen Share |
| T+36 | Chapter 3: audience Q&A + rapid-fire | Host + Guest |
| T+44 | Close: guest CTA, next episode date | Host Solo |
| T+45 | End card 60 seconds | End Card |
| Post | Click **End Broadcast** → confirm recording saved | — |

Production notes:
- **Pin a welcome comment** within 60 seconds of going live.
- **Read commenter names aloud** during transitions to reward engagement.
- **Verbal chapter marks** ("Let's shift to...") help editors find clip cut points.
- **Avoid screen share when guest is talking** — face-to-face builds trust.

### Phase 7: Recording Download and Handoff

1. After broadcast ends, navigate to **Recordings** in StreamYard dashboard.
2. Download MP4 (original quality, not compressed thumbnail).
3. **Handoff package** for repurposing (see `linkedin-live-strategy` Phase 5):
   - Full MP4 for podcast audio extraction
   - Timestamp log: chapter start/end times for clip extraction
   - Guest headshot and bio (collected during booking — see `reveting-calendar-flows`)
   - Show notes draft from StreamYard broadcast description

## Output Format

StreamYard production kit: brand scene library (6 scenes), overlay templates
(lower thirds, logo bug, end card), guest invite SOP, pre-show tech check
checklist, live run-of-show (45-minute template), recording download and handoff
workflow, and naming conventions for broadcast archive.

## Quality Check

- [ ] Brand kit uploaded: logo, colors, background
- [ ] All 6 scenes built and named per convention
- [ ] LinkedIn Live destination connected and stream-tested (private broadcast)
- [ ] Guest invite flow tested with a teammate before first real guest
- [ ] Run-of-show includes verbal chapter marks at 8-12 minute intervals
- [ ] End card includes CTA and next episode date
- [ ] Recording download confirmed before ending first broadcast
- [ ] Repurposing handoff package defined and delivered within 24 hours post-show

## Common Pitfalls

1. **LinkedIn Live access not enabled.** Request Creator Mode + Live access before
   scheduling the first show — approval can take 24-48 hours.

2. **Guest joins wrong browser.** StreamYard requires Chrome or Firefox; Safari
   blocks some audio/video APIs. Include browser instructions in every guest invite.

3. **No pre-show tech check.** Audio issues discovered live cost engagement — 15
   minutes of setup prevents 45 minutes of friction.

4. **Scenes not prepared before going live.** Switching scenes mid-show while
   talking breaks the conversation. Pre-load all scenes and overlays.

5. **Forgetting to download the recording.** StreamYard stores recordings for 15
   days (Basic) or 30 days (Professional) — download immediately after the show.

6. **Single destination only.** Not simulcasting to YouTube means no replay SEO or
   podcast RSS fallback. Connect both destinations from episode 1.

7. **Generic broadcast title.** Keyword-rich titles rank in LinkedIn search and
   notify the algorithm this is a Live event — not a video upload.

## Execution Artifacts

- `references/framework-notes.md` — Framework index and authority routing
- `templates/output-template.md` — Deliverable shell for StreamYard production kit
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/streamyard-platform-reference.md` — Scene library, tier matrix, and production tables

## Related Skills

- **linkedin-live-strategy**: Full Reveting content engine playbook (Jessie Lizak)
- **reveting-calendar-flows**: Guest booking and pre-show scheduling
- **reveting-email-flows**: Guest invite and pre-show briefing email sequences
- **reveting-ghl-workflows**: GHL automation for show operations
- **content-distribution**: Extending recordings beyond LinkedIn
