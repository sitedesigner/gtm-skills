# Post Engager Play — Output Template

Replace all `[BRACKETED]` values with actual content before delivering to the user.

---

## 1. Post Qualification Summary

**Post URL:** [URL of the Facebook / LinkedIn / X post]
**Platform:** [Facebook / LinkedIn / X]
**Post Author:** [Name or handle]
**Post Topic:** [One sentence: what problem or topic does this post address?]
**Post Date:** [Date posted]
**Days Since Posted:** [Number] — [Within window / Borderline / Expired]
**Total Engagements:** [Likes + comments + shares count]
**ICP Density Assessment:** Reviewed [N] visible engager profiles; [N] appear ICP-fit ([%] pass rate)
**Go / No-Go Decision:** [GO — proceed / NO-GO — reason]

---

## 2. Scrape Configuration

**Tool Used:** [Phantombuster / Trigify / Clay / Other]
**Scrape Type:** [Likers / Commenters / Both / All Reactions]
**Extraction Limit:** [Number or "All available"]
**Output File:** [Filename or location]
**Raw Engager Count:** [Total rows in scrape output]

---

## 3. Filtered List Summary

**ICP Filter Criteria Applied:**
- Job title includes: [keywords]
- Company size: [min] – [max] employees
- Geography: [regions/countries]
- Excluded: [any exclusion criteria]

**Filter Results:**
- Raw engagers: [N]
- Passed ICP filter: [N] ([%])
- Deduped against CRM: removed [N] existing contacts
- **Final enrichment-ready list:** [N] contacts

---

## 4. Enrichment Summary

**Waterfall order used:** [LeadMagic → Apollo → Hunter / other sequence]

| Provider | Hits | % of Attempted |
|---|---|---|
| [Provider 1] | [N] | [%] |
| [Provider 2] | [N] | [%] |
| [Provider 3] | [N] | [%] |
| **Total** | **[N]** | **[%]** |

**Email verification results:**
- Valid: [N] ([%])
- Catch-all: [N] ([%])
- Invalid / Bounce: [N] ([%])
- **Contactable (valid only):** [N] contacts

---

## 5. Message Variants

### Variant A — Liker (no comment available)

**Subject:** [Subject line — reference the post topic, not your product]

> Hi [First name],
>
> [Line 1: Reference to the post — "Saw you liked [Author]'s post on [topic]."]
>
> [Line 2: Bridge to their role — "A lot of [title]-level folks we talk to are navigating [the same topic]."]
>
> [Line 3: Current-State discovery question — "How are you currently [handling/approaching] [the problem]?"]

---

### Variant B — Commenter (comment text available)

**Subject:** [Subject line]

> Hi [First name],
>
> [Line 1: Reference their comment — "Saw your comment on [Author]'s post — specifically your point about [paraphrase their comment]."]
>
> [Line 2: Bridge — "That [specific point] is something [title]-level folks at [company size] orgs deal with a lot."]
>
> [Line 3: Current-State question — "How are you handling [the specific thing they mentioned] today?"]

---

### Variant C — Topic-Based (post 5-7 days old, softer reference)

**Subject:** [Subject line]

> Hi [First name],
>
> [Line 1: Topic reference — "Saw some discussion recently on [topic the post covered]."]
>
> [Line 2: Bridge — "We work with a lot of [titles] on exactly that — [one-line description of the problem space]."]
>
> [Line 3: Current-State question — "Curious how you're currently set up on the [topic] side?"]

---

## 6. Sequence Spec

**Sequence Name:** Post Engager — [Post Topic] — [Date]
**Source Tag:** `post-engager-[platform]-[YYYY-MM-DD]`

| Touch | Day | Channel | Content | Notes |
|---|---|---|---|---|
| 1 | Day 1 | Email | Variant A or B (matched to engagement type) | Personalize with engagement type |
| 2 | Day 3 | LinkedIn DM | Short reference to same post + same discovery question | Only send if connected; otherwise skip |
| 3 | Day 6 | Email | Follow-up: share resource relevant to the post topic | Resource must be genuinely useful, no product pitch |
| 4 | Day 10 | Email | Breakup: "Should I stop reaching out?" | 2-sentence maximum |

**Sequencer:** [Smartlead / Instantly / Salesloft / HubSpot / Other]
**Sending domain:** [Domain used for outreach — not primary domain]
**Sending volume:** [Max contacts per day from this campaign]

---

## 7. CRM Tracking Setup

**Source field value:** `post-engager-play`
**Campaign tag:** `[Post topic] — [Platform] — [Date]`
**Custom properties to record:**
- `post_url`: [URL]
- `post_engagement_type`: [like / comment / share]
- `comment_text`: [if applicable]

**Reporting view:** Filter CRM contacts by `source = post-engager-play` to
track reply rate, meeting rate, and pipeline by campaign separately from cold lists.

---

## 8. Quality Checklist (Complete Before Launch)

- [ ] Post is public and within 7-day freshness window
- [ ] ICP filter applied before enrichment — not after
- [ ] Email verification run; only `valid` status pushed to sequencer
- [ ] All Touch 1 variants reference the specific post or commenter's own words
- [ ] Discovery question asks about current state — not about the product
- [ ] Total Touch 1 message length under 80 words
- [ ] Sequence is 4 touches maximum
- [ ] Source tag configured in sequencer and CRM
- [ ] Dedup against existing CRM contacts confirmed
