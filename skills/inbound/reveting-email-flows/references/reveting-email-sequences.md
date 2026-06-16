# Reveting Email Sequences — Reference Tables

Reference tables for `SKILL.md`. Sources: Jessie Lizak (Reveting) public
show operations model, Outreach Sales Engagement Cadence Design benchmarks,
and HubSpot Academy CRM Automation lifecycle patterns.

**Public channels:** 🔗 [reveting.com](https://www.reveting.com) · 💼 [linkedin.com/in/jessie-lizak](https://www.linkedin.com/in/jessie-lizak/)

## Full sequence map

| # | Sequence | Audience | Trigger | Steps | Timing | GHL Workflow |
|---|---|---|---|---|---|---|
| 1 | Guest Outreach | Prospect guests | Manual | 3 | D1, D4, D9 | No (manual) |
| 2 | Booking Confirmation | Confirmed guests | Calendar booking | 1 | Immediate | Yes |
| 3 | Pre-Show Briefing | Confirmed guests | T-7 days from recording | 2 | T-7, T-3 | Yes |
| 4 | Show Promotion | Email subscribers | T-5 days before show | 2 | T-5, Show day T-2h | Yes |
| 5 | Post-Show | Guests + subscribers | Show recorded tag | 3 | T+24h, T+3d, T+4d | Yes |
| 6 | Ongoing Nurture | All subscribers | Weekly recurring | Ongoing | Weekly | Yes |

## Outreach cadence benchmarks applied to show operations

| Application | Outreach benchmark | Show adaptation |
|---|---|---|
| Guest outreach sequence | 3-5 touch, 9-12 day window | 3 touch, 9-day window |
| Pre-event reminder cadence | 1 week + 24h + 1h | T-7 + T-3 + T-24h + T-1h (split email/SMS) |
| Post-meeting follow-up | 24h thank-you | T+24h replay + T+4d clips |
| Re-engagement window | 60+ days inactive | 60 days no open → 3-touch re-engage |
| Suppression threshold | No response after 3 touches | Suppress from active list (not delete) |

## Subject line patterns — benchmarks by sequence type

| Sequence | Pattern | Example |
|---|---|---|
| Guest outreach T1 | `[Name], quick question about [topic]` | `Sarah, quick question about your RevOps framework` |
| Guest outreach T2 | `Re: [original subject]` | `Re: Sarah, quick question about your RevOps framework` |
| Guest outreach T3 | `Last note — [show name] guest spot` | `Last note — WinsDay guest spot` |
| Booking confirmation | `You're confirmed for [show] — here's what's next` | `You're confirmed for WinsDay — here's what's next` |
| Pre-show T-7 | `Pre-show briefing for your [show] episode` | `Pre-show briefing for your WinsDay episode` |
| Pre-show T-3 | `3 days to your [show] episode — quick read` | `3 days to your WinsDay episode — quick read` |
| Promotion T-5 | `[Show] this [Day] — [Guest] on [hook]` | `WinsDay this Wednesday — Sarah on scaling RevOps to $10M` |
| Promotion day-of | `We're live in 2 hours — [Guest] + [show]` | `We're live in 2 hours — Sarah + WinsDay` |
| Post-show T+24h guest | `[Show] is live — your episode + replay link` | `WinsDay is live — your episode + replay link` |
| Post-show clips | `Your 3 clips from [show] — ready to post` | `Your 3 clips from WinsDay — ready to post` |
| Post-show audience | `[Ep#] [Guest] on [topic] — replay + takeaways` | `Ep47 Sarah on RevOps — replay + takeaways` |
| Re-engagement T1 | `Still interested in [show]?` | `Still interested in WinsDay?` |
| Re-engagement T2 | `Our most-watched episode of the year` | `Our most-watched episode of the year` |
| Re-engagement T3 | `We'll miss you — unsubscribe anytime` | `We'll miss you — unsubscribe anytime` |

## Open rate benchmarks by email type

| Email type | Industry benchmark | Target for show |
|---|---|---|
| Guest outreach T1 | 30-40% (personalized cold) | >40% |
| Booking confirmation | 70-80% (transactional) | >80% |
| Pre-show briefing | 60-70% (relationship) | >65% |
| Show promotion (subscribers) | 25-35% (newsletter) | >30% |
| Post-show replay | 40-50% (post-event) | >45% |
| Clips delivery (guest) | 60-70% (relationship) | >65% |
| Weekly nurture | 20-30% (newsletter) | >25% |
| Re-engagement T1 | 15-25% | >20% |

Source: HubSpot Email Marketing Benchmarks Report (aggregate B2B data) and
Outreach Sales Engagement platform data.

## Post-show clip email — file delivery spec

| Clip | Format | Length | Hook type | Caption template |
|---|---|---|---|---|
| Clip 1 — best quote | MP4 vertical (9:16) | 60-75s | Guest insight or framework | "[Quote]. Full episode: [link]" |
| Clip 2 — tactical moment | MP4 vertical (9:16) | 60-90s | How-to or framework step | "Here's how [Guest] [did X]. Full replay: [link]" |
| Clip 3 — story or surprise | MP4 vertical (9:16) | 45-60s | Unexpected angle or emotion | "Nobody talks about this. [Guest] did. Watch: [link]" |

Guest clip email should include:
- Download links (Google Drive or Dropbox, not email attachment)
- Suggested caption for each clip
- Best posting day/time recommendation (van der Blom LinkedIn algorithm data)
- Tag: "@[Host LinkedIn handle] and @[Show LinkedIn page]"

## Re-engagement suppression logic

After 3-touch re-engagement sequence with no open or click:
1. Move contact to tag `show-inactive`
2. Remove from weekly episode list
3. Do NOT delete — they may re-engage from LinkedIn or word of mouth
4. Quarterly recheck: if they engage with LinkedIn content → remove `show-inactive`

GHL implementation: workflow with condition "Email not opened after touch 3" → add tag `show-inactive` → remove from episode announcement workflow.

## HubSpot CRM Automation principles applied

1. **Trigger on action, not time alone:** Confirmation email fires on booking
   event, not on a daily batch check.
2. **Unenrollment conditions:** Every sequence has explicit exit: "if rescheduled
   → unenroll from current sequence → enroll in reschedule sequence."
3. **A/B subject lines:** Weekly audience email runs 2-subject A/B; winning
   subject becomes default next month.
4. **Lifecycle gates:** Do not send audience nurture to contacts still in
   "Guest Prospect" stage — separate them to avoid cross-sequence confusion.

## Cross-references

| Topic | Skill / artifact |
|---|---|
| Full Reveting content engine | `linkedin-live-strategy` |
| GHL automation that sends these sequences | `reveting-ghl-workflows` |
| Calendar booking that triggers Sequence 2 | `reveting-calendar-flows` |
| StreamYard links referenced in emails | `reveting-streamyard-flows` |
| Cold email pattern for guest outreach | `cold-email-strategy`, `cold-email-copywriting` |
| MQL nurture for audience → pipeline | `mql-nurture` |
| LinkedIn algorithm for clip posting times | `linkedin-algorithm` |
