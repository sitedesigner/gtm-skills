# Go High Level — Workflow Reference for Reveting Show Operations

Reference tables for `SKILL.md`. Source: Go High Level official documentation
(help.gohighlevel.com) and Jessie Lizak (Reveting) public show operations model.

**Public channels:** 🔗 [gohighlevel.com](https://www.gohighlevel.com) · 📚 [help.gohighlevel.com](https://help.gohighlevel.com)

## GHL Workflow trigger types used in show operations

| Trigger | Use case |
|---|---|
| Pipeline Stage Change | Fire confirmation sequence when guest moves to "Confirmed" |
| Appointment Status | Fire reminders when calendar booking is confirmed or cancelled |
| Tag Added | Fire post-show sequence when `show-recorded-ep[N]` tag is applied |
| Form Submitted | Fire audience capture workflow on show page form fill |
| Inbound Webhook | Receive LinkedIn comment data from third-party tools |
| Contact Created | Optional: welcome sequence for cold outreach responses |

## GHL Workflow action types used in show operations

| Action | Use case |
|---|---|
| Send Email | Confirmation, briefing, thank-you, clip delivery |
| Send SMS | Show-day reminders (with opt-in consent) |
| Add/Remove Tag | Track stage transitions without pipeline dependency |
| Move Pipeline Stage | Automated stage advance on trigger |
| Create Task | Human-in-the-loop for headshot collection, clip editing |
| Send Internal Notification | Email or Slack webhook to host/ops team |
| Add to Workflow | Chain into post-show workflow from show-day workflow |
| Remove from Workflow | Unenroll on reschedule or cancel |
| Wait (time-based) | Day-of reminders relative to appointment time |

## Guest pipeline — detailed stage spec

| Stage | Entry trigger | Required fields | Exit trigger |
|---|---|---|---|
| Prospect | Manual or LinkedIn DM response | Name, LinkedIn URL | Outreach sent |
| Outreach Sent | Workflow: first email sent | Episode Topic interest | Positive reply → Shortlisted |
| Shortlisted | Manual move after reply | Bio (short), Headshot URL | Calendar booking confirmed |
| Confirmed | Calendar booking confirmed | Episode Number, Recording Date | Show day |
| Recorded | Manual tag `show-recorded-ep[N]` | Replay URL | Clip delivery sent |
| Past Guest | Post-show workflow step 5 | Clip URLs | 30-day re-engage task |

## GHL Calendar configuration for show bookings

| Setting | Value |
|---|---|
| Calendar type | Round Robin or Personal (host-owned) |
| Slot duration | 60 min (show) + 15 min buffer |
| Availability | Day of show only (recurring slot) |
| Confirmation | Immediate email + ICS file |
| Reminder | 24h and 1h before (built into GHL Calendar settings) |
| Cancellation policy | Auto-move to Shortlisted; trigger reschedule workflow |
| Form fields | Topic, Bio, Headshot URL, LinkedIn URL, SMS consent checkbox |

## SMS consent requirements (GHL / TCPA)

GHL SMS sending is subject to TCPA (US) or equivalent regulations. For show
operations:

1. Guest application form must include: "I consent to receive SMS reminders
   about my episode from [Company Name]."
2. Store consent field on contact record.
3. Condition all SMS steps in workflows on `sms_consent = true`.
4. Honor STOP requests — GHL handles opt-out automatically if LC Phone is used.

## Webhook integration patterns

For LinkedIn comment capture (third-party tools like Zapier, Make, or n8n):

```
Webhook payload → GHL Inbound Webhook Trigger
  → Create/Update Contact (email or LinkedIn ID)
  → Add Tag: show-viewer
  → Enroll in Audience Capture Workflow
```

Tools that can send LinkedIn comment data to GHL via webhook:
- Zapier (LinkedIn Lead Gen Forms → GHL)
- Make (Phantombuster LinkedIn monitor → GHL)
- n8n (LinkedIn scraper → GHL webhook)

## Reporting dashboard widgets — GHL configuration

| Widget | Type | Data source | Filter |
|---|---|---|---|
| Guest Pipeline Funnel | Funnel | Guest Pipeline | All stages |
| New Show Subscribers | Number | Contacts | Tag: show-viewer, Last 30 days |
| Confirmation Rate | Percentage | Workflow stats | Confirmation sequence |
| Task Backlog | Number | Tasks | Open tasks, Assignee: ops team |
| Email Opens | Percentage | Email reporting | Campaign: show sequences |
| CSQL Conversions | Number | Audience Pipeline | Stage: CSQL, Last 30 days |

## Cross-references

| Topic | Skill / artifact |
|---|---|
| Full Reveting content engine | `linkedin-live-strategy` |
| StreamYard production | `reveting-streamyard-flows` |
| Guest booking calendar | `reveting-calendar-flows` |
| Email copy for GHL sequences | `reveting-email-flows` |
| Alternative CRM | `hubspot-setup`, `crm-integration` |
