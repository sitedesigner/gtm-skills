# Calendar and Booking Reference — Reveting Show Operations

Reference tables for `SKILL.md`. Sources: Calendly official documentation
(calendly.com), Cal.com documentation (cal.com/docs), GHL Calendar
(help.gohighlevel.com), and Outreach Sales Engagement Cadence Design.

## Platform comparison — show guest booking

| Feature | Calendly Pro ($12/mo) | Cal.com (Free/Teams) | GHL Calendar (included) |
|---|---|---|---|
| Custom intake forms | Yes (routing forms) | Yes | Yes |
| Multi-host round robin | Yes | Yes | Yes |
| CRM webhook | Yes (native HubSpot/SF, Zapier for GHL) | Yes (webhooks) | Native GHL |
| SMS reminders | No (email only) | No | Yes (with LC Phone) |
| Custom redirect after booking | Yes | Yes | Yes |
| Routing logic (pre-qualify) | Yes (routing forms, Pro+) | Partial | No |
| Branding | Yes | Limited (free), Full (Teams) | Full (GHL branding) |
| Best for | Teams already using HubSpot/SF | Tech-savvy / self-hosted | Teams already in GHL |

**Recommendation for Reveting-style shows:**
- GHL-first teams: GHL Calendar (native SMS, pipeline sync)
- HubSpot teams: Calendly Pro (native HubSpot sync)
- Budget-conscious / open source: Cal.com + n8n for CRM sync

## Guest booking page — intake form spec

| Field | Required | Format | Used for |
|---|---|---|---|
| First / Last Name | Yes | Text | Contact record, lower thirds |
| Company | Yes | Text | Show notes, graphic |
| Title | Yes | Text | Lower thirds |
| Short Bio | Yes | Text (50 words max) | Show notes, audience preview |
| Episode Topic | Yes | Text (2-3 sentences) | Talking points prep |
| LinkedIn Profile URL | Yes | URL | Show promotion, tagging |
| Headshot | Yes | File upload or Drive link | Graphics, thumbnail |
| SMS Consent | Yes | Checkbox | SMS reminder opt-in |
| How did you hear about us? | Optional | Dropdown | Referral tracking |
| Previous guest referral | Optional | Text | Referral attribution |

## Reminder cadence — Outreach pattern applied to show bookings

Outreach Sales Engagement Cadence Design recommends a minimum 3-touch pre-meeting
cadence for high no-show prevention. For show guest bookings, extend to 6 touches:

| Touch | Timing | Channel | Key message |
|---|---|---|---|
| 1 — Confirmation | Immediately after booking | Email | Confirmed, prep checklist, StreamYard test |
| 2 — Briefing invite | T-7 days | Email | 15-min pre-show call invitation |
| 3 — Episode reminder | T-3 days | Email | Topic review, what to prepare |
| 4 — Day before | T-24 hours | Email + SMS | Tomorrow at [time], link: [url] |
| 5 — Show day | T-1 hour | SMS | In 1 hour. READY or RESCHEDULE? |
| 6 — Tech check | T-15 min | SMS | "Open StreamYard now and test camera" |

**Target no-show rate with this sequence:** <5% (vs. industry average of 20-30%
for single-email confirmation only).

## Calendar slot architecture — weekly show

| Block | Day | Time | Duration | Purpose |
|---|---|---|---|---|
| Prep block | Day before show | 2 hours | 2h | Finalize talking points, check guest status |
| Buffer block | Show morning | 1 hour | 1h | Final tech setup, StreamYard scene check |
| Show recording | Show day | Recurring | 75 min | 60 min show + 15 min buffer |
| Handoff block | Day after show | 1 hour | 1h | Download recording, send to repurposing |
| Blackout | Show day (all other) | All day | — | No other calls or meetings |

## No-show rates by reminder method

| Reminder setup | Estimated no-show rate |
|---|---|
| Confirmation email only | 20-30% |
| Confirmation + 24h email | 15-20% |
| Confirmation + 24h email + SMS | 8-12% |
| 6-touch sequence (as above) | 3-5% |

Source: Outreach Sales Engagement Cadence Design benchmark data (aggregate customer analysis).

## Calendly routing form — pre-qualification logic

For shows that receive many guest requests and need to filter:

1. Create routing form with question: "What is your episode topic?"
2. Add rule: if topic matches ICP keyword list → route to booking page
3. If topic does not match → route to "Not a fit right now" page with alternative CTA
4. Calendly Pro required for routing forms ($12/seat/month)

## Cal.com + n8n CRM sync pattern

For teams using Cal.com as booking tool with GHL as CRM:

```
Cal.com booking confirmed
  → Cal.com webhook (POST to n8n webhook URL)
    → n8n: parse booking payload
      → GHL API: create/update contact
      → GHL API: move to "Shortlisted" pipeline stage
      → GHL API: enroll in Confirmation Sequence workflow
```

n8n node sequence: Webhook → Set (map fields) → HTTP Request (GHL API) → HTTP Request (GHL pipeline).

## Cross-references

| Topic | Skill / artifact |
|---|---|
| Full Reveting content engine | `linkedin-live-strategy` |
| GHL automation on booking | `reveting-ghl-workflows` |
| Email copy for reminders | `reveting-email-flows` |
| StreamYard tech check linked from confirmation | `reveting-streamyard-flows` |
| n8n webhook integration | `n8n-automation`, `n8n-toolkit` |
