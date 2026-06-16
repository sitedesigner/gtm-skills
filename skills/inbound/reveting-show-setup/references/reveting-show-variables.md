# Reveting Show Variables — Full Reference

Complete variable definitions, email trigger map, and calendar description
templates. Source: Jessie Lizak (Reveting) production SOP and Go High Level
platform documentation.

**Production system:** app.reveting.com · Calendar: ww@reveting.com · Questions: WhatsApp Jessie

---

## TIER 1 — SHOW CONSTANTS

*Set once at show launch. Stored in show's Google Drive root folder.*

### Show Identity

| Variable | Definition | Example |
|---|---|---|
| `[SHOW_NAME]` | Full public show name | WinsDay |
| `[SHOW_EMAIL]` | Production team inbox | ea@reveting.com |
| `[CALENDAR_ACCOUNT]` | Google Calendar used as source of truth | ww@reveting.com |
| `[SHOW_TIMEZONE]` | Broadcast timezone for all calendar events | Eastern Time (USA) |
| `[SHOW_DAY_OF_WEEK]` | Recurring show day | Wednesday |
| `[SHOW_RECURRING_TIME_ET]` | Recurring go-live time in ET | 12:00 PM ET |
| `[PRESHOW_DURATION_MIN]` | Minutes before go-live for tech check | 15 |
| `[SHOW_DURATION_MIN]` | Max reserved time for show | 60 |

### Team

| Variable | Definition | Example |
|---|---|---|
| `[HOST_NAME]` | On-camera host name | Alanna Smith |
| `[HOST_LINKEDIN_URL]` | Host LinkedIn profile URL | linkedin.com/in/... |
| `[PRODUCER_NAME]` | Behind-the-scenes producer | Jessie Lizak |
| `[PRODUCTION_ASSISTANT_NAME]` | PA who sends emails + manages calendar | |
| `[SIGNATURE_BLOCK]` | Full email signature block (name, title, links) | |

### Channel Stack

*Pull from Total Deliverables Document every time. Never guess.*

| Variable | Value (Yes/No) |
|---|---|
| `[STREAM_TO_LINKEDIN]` | |
| `[STREAM_TO_YOUTUBE]` | |
| `[STREAM_TO_FACEBOOK]` | |
| `[STREAM_TO_TWITCH]` | |
| `[STREAM_TO_INSTAGRAM]` | Note: events cannot be pre-posted on IG — link to channel only |
| `[LINKEDIN_PAGE_OR_PROFILE]` | Page or Personal Profile |
| `[LINKEDIN_CHANNEL_OWNER]` | Name of person/page the LinkedIn Live streams from |

### Podcast & Replay Links

| Variable | Definition |
|---|---|
| `[SPOTIFY_SHOW_LINK]` | Spotify show page (not individual episode) |
| `[APPLE_PODCASTS_SHOW_LINK]` | Apple Podcasts show page |
| `[YOUTUBE_CHANNEL_LINK]` | YouTube channel for this show |
| `[SHOW_WEBSITE_LINK]` | Show website or landing page |
| `[PAST_EPISODES_LINK]` | Best link for guests to hear past episodes before their appearance |

### Booking & Docs

| Variable | Definition |
|---|---|
| `[BOOKING_FORM_LINK]` | Public-facing guest booking calendar link |
| `[TOTAL_DELIVERABLES_DOC]` | Master Sheet — channel stack, outline links, show structure |
| `[CLIENT_OUTLINE_LINK]` | Show-specific episode outline Google Doc |
| `[GOOGLE_DRIVE_ROOT_FOLDER]` | Root Google Drive folder for all show assets |
| `[STREAMYARD_ACCOUNT_URL]` | StreamYard account base URL for this show |
| `[LINKEDIN_INVITE_WALKTHROUGH_URL]` | Video walkthrough for how guests send LinkedIn event invites |

### Guest Qualification Rules

| Variable | Value |
|---|---|
| `[MIN_LINKEDIN_FOLLOWERS]` | 5,000+ preferred. 1,000–4,999: confirm with Production + Marketing Lead. Below 1,000: no-go unless no other option. |
| `[SHOW_CONTENT_PILLARS]` | Comma-separated topic categories that align with client messaging |
| `[ESCALATION_CONTACT]` | Jessie via WhatsApp |
| `[FALLBACK_SHOW_LINKS]` | Up to 3 other client shows to redirect "not a fit" guests |

---

## TIER 2 — EPISODE VARIABLES

*Set per episode. Complete before any email is sent.*

### Guest Info

| Variable | Source |
|---|---|
| `[GUEST_FIRST_NAME]` | Booking form |
| `[GUEST_LAST_NAME]` | Booking form |
| `[GUEST_TITLE]` | Booking form → "What job title and company name should we use on promotional materials?" |
| `[GUEST_COMPANY]` | Booking form |
| `[GUEST_EMAIL]` | Booking form |
| `[GUEST_PHONE]` | Booking form |
| `[GUEST_LINKEDIN_URL]` | Booking form |
| `[GUEST_LINKEDIN_FOLLOWERS]` | Manual LinkedIn check — used for fit gate |
| `[GUEST_PR_CONTACT_NAME]` | Booking form (if submitted) |
| `[GUEST_PR_CONTACT_EMAIL]` | Booking form (if submitted) |
| `[GUEST_TIMEZONE]` | Booking form → selectedTimezone field |

### Episode Details

| Variable | Source / Rule |
|---|---|
| `[EPISODE_NUMBER]` | Assigned by Production + Marketing Lead |
| `[EPISODE_DATE]` | e.g. Wednesday, June 18, 2026 |
| `[EPISODE_TITLE]` | **Created by production team — NEVER raw guest submission** |
| `[TOPIC_1]` | Edited by production team. 3–7 words. Aligned to show strategy. |
| `[TOPIC_2]` | Edited by production team. 3–7 words. |
| `[TOPIC_3]` | Edited by production team. 3–7 words. |
| `[TOPIC_4]` | Edited by production team. 3–7 words. (optional) |
| `[GURU_OF_THE_WEEK]` | LinkedIn URL submitted by guest |
| `[SEGMENT_TITLE]` | For podcast platform metadata |

### Show Timing (all three time zones, every episode)

| Variable | Calculation |
|---|---|
| `[PRESHOW_TIME_ET]` | Go-live time minus 15 min, Eastern |
| `[PRESHOW_TIME_CT]` | Go-live time minus 15 min, Central |
| `[PRESHOW_TIME_PT]` | Go-live time minus 15 min, Pacific |
| `[GOLIVE_TIME_ET]` | Confirmed from calendar — Eastern |
| `[GOLIVE_TIME_CT]` | Confirmed from calendar — Central |
| `[GOLIVE_TIME_PT]` | Confirmed from calendar — Pacific |

### Episode Links

| Variable | When available |
|---|---|
| `[STREAMYARD_GUEST_LINK]` | Generated fresh per episode |
| `[LINKEDIN_EVENT_URL]` | After event is published |
| `[YOUTUBE_EVENT_URL]` | After event is published |
| `[FACEBOOK_EVENT_URL]` | After event is published |
| `[TWITCH_EVENT_URL]` | After event is published |
| `[INSTAGRAM_CHANNEL_URL]` | IG channel link (events can't be pre-posted) |
| `[EPISODE_DRIVE_FOLDER]` | Google Drive subfolder for this episode |
| `[EPISODE_SCRIPT_LINK]` | Episode-specific outline in Google Drive |

### Post-Production Assets

| Variable | SLA |
|---|---|
| `[AI_CLIPS_DRIVE_LINK]` | Within 1 hour of show end (Email 5) |
| `[FULL_RECORDING_LINK]` | Within 1 hour of show end (Email 5) |
| `[TRANSCRIPT_LINK]` | Within 1 hour of show end (Email 5) |
| `[HUMAN_EDITED_CLIPS_LINK]` | Within 24 hours of show end, max 36h (Email 6) |
| `[SPOTIFY_EPISODE_LINK]` | After podcast upload (Email 6) |
| `[APPLE_EPISODE_LINK]` | After podcast upload (Email 6) |

---

## EMAIL TRIGGER CHECKLIST

| Email | Trigger | Required Tier 1 variables | Required Tier 2 variables |
|---|---|---|---|
| **Not a Fit** | Guest fails fit check | `[SHOW_NAME]`, `[SIGNATURE_BLOCK]`, `[FALLBACK_SHOW_LINKS]` | `[GUEST_FIRST_NAME]` |
| **T-14 Activation** | 14 days before show (or immediate if booking within 14 days) | `[SIGNATURE_BLOCK]` | `[GUEST_FIRST_NAME]` |
| **Email 1** | Event published on all platforms | `[SHOW_NAME]`, `[SIGNATURE_BLOCK]`, `[LINKEDIN_INVITE_WALKTHROUGH_URL]` | `[GUEST_FIRST_NAME]`, `[EPISODE_DATE]`, `[EPISODE_TITLE]`, `[TOPIC_1–4]`, `[PRESHOW_TIME_PT/CT/ET]`, `[GOLIVE_TIME_PT/CT/ET]`, `[STREAMYARD_GUEST_LINK]`, `[LINKEDIN_EVENT_URL]`, `[YOUTUBE_EVENT_URL]`, `[FACEBOOK_EVENT_URL]`, `[TWITCH_EVENT_URL]`, `[INSTAGRAM_CHANNEL_URL]` |
| **Email 2** | T-7 days | `[SHOW_NAME]`, `[SIGNATURE_BLOCK]`, `[LINKEDIN_INVITE_WALKTHROUGH_URL]` | `[GUEST_FIRST_NAME]`, `[EPISODE_DATE]`, `[PRESHOW_TIME_ET]`, `[GOLIVE_TIME_ET]`, `[LINKEDIN_EVENT_URL]` |
| **Email 3** | T-1 day | `[SHOW_NAME]`, `[HOST_NAME]`, `[PRODUCER_NAME]`, `[SIGNATURE_BLOCK]`, `[PAST_EPISODES_LINK]`, `[LINKEDIN_INVITE_WALKTHROUGH_URL]` | `[GUEST_FIRST_NAME]`, `[PRESHOW_TIME_PT/CT/ET]`, `[GOLIVE_TIME_PT/CT/ET]`, `[STREAMYARD_GUEST_LINK]`, `[LINKEDIN_EVENT_URL]` |
| **Email 4** | Morning of show (2–4 hrs before pre-show) | `[SHOW_NAME]`, `[SIGNATURE_BLOCK]` | `[GUEST_FIRST_NAME]`, `[STREAMYARD_GUEST_LINK]`, `[PRESHOW_TIME_PT/CT/ET]`, `[GOLIVE_TIME_PT/CT/ET]` |
| **Email 5** | Within 1 hour of show end | `[SIGNATURE_BLOCK]` | `[GUEST_FIRST_NAME]`, `[AI_CLIPS_DRIVE_LINK]`, `[FULL_RECORDING_LINK]`, `[TRANSCRIPT_LINK]` |
| **Email 6** | 24–36 hours after show (hard max 36h) | `[SHOW_NAME]`, `[SIGNATURE_BLOCK]` | `[GUEST_FIRST_NAME]`, `[EPISODE_TITLE]`, `[SEGMENT_TITLE]`, `[SPOTIFY_EPISODE_LINK]`, `[APPLE_EPISODE_LINK]`, `[HUMAN_EDITED_CLIPS_LINK]`, `[LINKEDIN_EVENT_URL]`, `[YOUTUBE_EVENT_URL]` |

---

## CALENDAR DESCRIPTION TEMPLATES

### Stage 1: New Booking (immediate on booking)

```
Event Name: [SHOW_NAME] with [GUEST_FIRST_NAME] [GUEST_LAST_NAME]
Location: StreamYard URL TBD

Thank you for submitting your topics. We will format them to fit the show
and then we will email them and update this calendar description. Please
stay tuned as we welcome your feedback on topics.

Promote the Event: We will share a LinkedIn event URL with you and ask you
and your team to invite their LinkedIn connections to the event.

We will ask you to accept a speaker role on LinkedIn too. Please connect
with [LINKEDIN_CHANNEL_OWNER] on LinkedIn so they can make you the guest
speaker.

We will also be livestreaming [CHANNEL_STACK_LIST]. Once posted, we will
share those links as well.

Logistics: Please plan to login to StreamYard 15 minutes early at
[PRESHOW_TIME_ET] / [PRESHOW_TIME_CT] / [PRESHOW_TIME_PT].
We will go live at [GOLIVE_TIME_ET] / [GOLIVE_TIME_CT] / [GOLIVE_TIME_PT].

Short video clips will be shared post production. Full discussions will be
immediately available on [CHANNEL_STACK_LIST]. They will be made available
on podcast channels post production as well.

If you have any questions, email [SHOW_EMAIL].

Looking forward to the conversation. We're excited to talk to you!

_____Original Submission from the Guest_______
[Paste raw booking form submission from app.reveting.com here — preserve always]
```

### Stage 2: Event Published (after Production + Marketing Lead posts event)

```
Event Name: [SHOW_NAME] with [GUEST_FIRST_NAME] [GUEST_LAST_NAME]

📅 [SHOW_NAME] with [GUEST_FIRST_NAME] [GUEST_LAST_NAME]
🗓 [EPISODE_DATE]
🕚 [PRESHOW_TIME_ET] Pre-Show
🕛 [GOLIVE_TIME_ET] Livestream

Login (recording studio): [STREAMYARD_GUEST_LINK]

Guest: [GUEST_FIRST_NAME] [GUEST_LAST_NAME]: [GUEST_LINKEDIN_URL]

Episode title: [EPISODE_TITLE]

Topics:
1. [TOPIC_1]
2. [TOPIC_2]
3. [TOPIC_3]
4. [TOPIC_4]

Script: [EPISODE_SCRIPT_LINK]

Promo Link:
LinkedIn: [LINKEDIN_EVENT_URL]

IMPORTANT. We highly suggest inviting your audience. Your network would
love to see you live, and the best way to get them involved is by
personally inviting them to the event. Reposting is great, but direct
invitations drive real engagement!

Here's a quick walkthrough of how to invite your LinkedIn connections:
[LINKEDIN_INVITE_WALKTHROUGH_URL]

LinkedIn gives you 1,000 invites per week, so you still have time! You
can filter by industry, location, company, or school to send targeted
invites in just a few clicks.

Event Link:
LinkedIn: [LINKEDIN_EVENT_URL]
Facebook: [FACEBOOK_EVENT_URL]
Twitch: [TWITCH_EVENT_URL]
YouTube: [YOUTUBE_EVENT_URL]

We always plan for a 15-minute pre-show and reserve one hour for the
livestream, though the full time isn't always needed.

Stream to Your Audience:
During pre-show we will check your camera, mic, lighting and show you how
to stream this to your audience on StreamYard. Bring your social media
credentials to the pre-show so you can plug in your channels and stream
this to your audience too.

We highly suggest livestreaming this to your LinkedIn.

Let us know if you have any questions in the meantime.

The Reveting Team

_____Original Submission from the Guest_______
[Preserve original booking form submission — never remove]
```

---

## HOW TO FIND BOOKINGS IN app.reveting.com

Option A (Appointment view):
1. Calendars → Appointment List View → Sort by newest

Option B (Contact activity):
1. Contacts → Sort by "Last Activity"

**Triple check:** Before sending any calendar invite, verify date and time
are set in Eastern Time (USA). This is the most common error.
