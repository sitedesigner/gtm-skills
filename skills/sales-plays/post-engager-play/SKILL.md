---
name: post-engager-play
description: >-
  Outbound play triggered by social post engagement — scrape likers, commenters,
  and sharers from a Facebook, LinkedIn, or X post that attracted your ICP, enrich
  and qualify the list, then reach out with a discovery-first message anchored to
  their engagement. Use when a relevant video, article, or discussion post has drawn
  your target buyers into a public conversation. Triggers on: "scrape post engagers",
  "active scrape outreach", "post commenters outreach", "Facebook post scrape",
  "LinkedIn post likers", "viral post prospecting", "social post play", "people who
  liked this post", "reach out to commenters", or any request to convert public social
  engagement into pipeline.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: sales-plays
  tags: [signals, social-scrape, post-engagement, outbound, discovery, phantombuster, clay, trigify]
  related_skills: [social-intent-monitoring, signal-scoring, lead-enrichment, cold-email-copywriting, multi-channel-outreach]
  frameworks:
    - "Trigify Workflow Patterns — Viral Engager Harvesting"
    - "Phantombuster — Facebook Post Likes/Comments Scraper"
    - "Pat Spielmann — Cold to Gold Current-State Discovery"
    - "Jordan Crawford — Signal Relevance over Volume (Clay Agency)"
---

# Post Engager Play

## Overview

When someone publicly likes, comments on, or shares a post about a topic your
product solves, they are telling you something about their current state. That
public act — especially on a video or discussion post — is a soft intent signal
with a 48-72 hour relevance window before the moment fades.

The play: identify the post, export the engagers, enrich and qualify them against
your ICP, find their work email, and reach out with a single discovery question
anchored to the post they engaged with. No pitch. No features. One question about
how they are currently handling the problem the post discussed.

This is "warm-ish" cold outreach — you have more context than a raw cold list, and
you use it. The signal is public and the reference is honest. The first message
reads like genuine curiosity, not a sequence.

Relevant for any post where your ICP congregated: a competitor's demo video, an
industry pain-point post, a product category discussion, an influencer's take on
a tool category, or a founder's question thread.

## When to Use

- "Scrape everyone who commented on this Facebook post and reach out"
- "Get a list of people who liked this LinkedIn video and send outreach"
- "Build an outbound play from people engaging with a viral industry post"
- "Find emails for commenters on this post and ask them about their current workflow"
- "Active scrape outreach from social post engagement"
- "People who engaged with this content are my ICP — how do I reach them?"
- "Convert post engagement into a prospecting list"

## Do NOT Use For

- Scraping private or members-only group posts without consent — only public content
- Mass-blasting all engagers with a pitch; this play requires ICP filtering first
- Evergreen list building; signals from posts older than 7 days lose timing relevance
- Replacing warm outreach on LinkedIn DM when a DM is the better channel (use
  `social-selling` for that)

## Authoritative Foundations

### Trigify — Viral Engager Harvesting Pattern

Trigify's public workflow documentation describes the Viral Engager Harvesting
pattern as a first-class agentic workflow:

**Post Engagement Trigger** → fetch all engagers from a post above a defined
engagement threshold → **Person Enrichment** (LinkedIn URL → name, title, company,
country, seniority) → **ICP Filter** (title + company size Boolean) → high-fit:
email enrichment → deliverability check → CRM push or email campaign enrollment;
lower-fit: CRM add with nurture tag.

The key design principle from Trigify's documentation: apply the ICP filter *before*
spending enrichment credits. Filtering on free platform data (country, headline,
connection count) reduces enrichment cost by 40-60% on large post lists.

Source: https://help.trigify.io/en/articles/8836198-draft-common-workflow-patterns

### Phantombuster — Social Post Scraper Tools

Phantombuster publishes specific scrapers for post engagement extraction:

**Facebook Post Likes/Comments Scraper**: Accepts a public Facebook post URL,
extracts a list of profiles that liked or commented on the post (name, profile URL,
comment text where available). Output: CSV with profile data for further enrichment.
Requires a Facebook session cookie via the Phantombuster connection system.

**LinkedIn Post Reactions Exporter**: Accepts a LinkedIn post URL and exports all
reactors (name, headline, profile URL, company, reaction type). Output: CSV for
Clay enrichment or direct LeadMagic waterfall. Rate limits apply; defaults to 2,500
profiles per run.

**X (Twitter) Post Engagers Scraper**: Extracts reply authors and retweeters from
a public X post. Output: profile handle list for enrichment.

Source: https://phantombuster.com/automations/facebook/facebook-post-likes-comments-scraper
Source: https://phantombuster.com/automations/linkedin/linkedin-post-reactions-exporter

### Pat Spielmann — Cold to Gold Current-State Discovery

Pat Spielmann's Cold to Gold framework (published via his newsletter and LinkedIn)
defines the discovery-first cold outreach structure where the first touch is always
a Current State question, not a pitch.

The Current State question format: "How are you currently [handling / solving /
thinking about] [the specific thing the post was about]?"

This accomplishes three things simultaneously:
1. It signals that the email is relevant (referenced their specific public action)
2. It positions the sender as curious rather than transactional
3. It generates a qualified response — only people who have an active relationship
   with the problem reply, self-selecting for pipeline fit

Spielmann's rule: the Current State question must be about their situation, not
about the product. "How are you currently handling X?" is correct. "Would you like
to see how we handle X?" is a pitch dressed as a question.

Source: Pat Spielmann — Cold to Gold methodology, https://www.patspielmann.com

### Jordan Crawford — Signal Relevance over Volume

Jordan Crawford (Clay Agency) articulates the core principle behind post-engager
plays in his published frameworks: relevance per message delivered beats volume.
A 100-person scraped list where every message references the exact post they
engaged with will outperform a 1,000-person cold list with no context 3-5x on
reply rate.

The practical implication for post-engager plays: do not scrape more than 500
engagers per post unless you have confirmed ICP density that warrants it. Smaller,
tightly filtered lists with genuine signal-anchored messages outperform large
scraped lists with generic openers.

Source: Jordan Crawford, Clay Agency published content — https://www.clay.com/blog

## Prerequisites

- Public social post URL (Facebook, LinkedIn, X, or YouTube comments)
- ICP criteria defined: job title keywords, company size range, industry or geo filters
- Scraping tool: Phantombuster (Facebook/LinkedIn/X) or Trigify (LinkedIn/X/Reddit)
- Enrichment provider: LeadMagic waterfall (company + email + phone), Clay table, or Apollo
- Email verification: LeadMagic `/email-verify` endpoint or NeverBounce before sequencer push
- Cold email sequencer: Smartlead, Instantly, Salesloft, Outreach, or HubSpot sequences
- CRM to record post-source attribution for tracking reply and meeting rates by post

## Step-by-Step Process

### Phase 1: Qualify the Post Before Scraping

Before running any scraper, assess whether the post has sufficient ICP density to
warrant the play.

**Post qualification checklist:**
- [ ] Post is public (no login required to view engagers)
- [ ] Post topic maps directly to a pain your product addresses
- [ ] Engagement count is sufficient (minimum 50 engagers for LinkedIn, 100 for Facebook)
- [ ] Post is recent (within 7 days; within 48 hours for maximum timing leverage)
- [ ] A sample of 10 engager profiles visible in the UI shows plausible ICP fit

If fewer than 20% of the visible engager sample fits your ICP criteria, the post
does not have enough ICP density. Move on; do not scrape.

**Post freshness windows:**

| Post Age | Outreach Timing | Message Tone |
|---|---|---|
| 0-48 hours | Send within 24 hrs of scrape | Direct reference to the post; high urgency |
| 2-7 days | Send within 48 hrs of scrape | Softer reference ("saw this circulating") |
| 7-14 days | Low priority — nurture only | No direct post reference; use topic instead |
| 14+ days | Do not run this play | Signal has expired; run standard outbound instead |

### Phase 2: Scrape the Post Engagers

**Facebook post:**
1. Copy the full post URL from the browser (not the mobile share link).
2. In Phantombuster, launch the **Facebook Post Likes/Comments Scraper**.
3. Paste the post URL, set extraction limit (default: all available).
4. Connect your Facebook session via Phantombuster's cookie integration.
5. Run the scraper. Output: CSV with name, profile URL, comment text (if applicable).

**LinkedIn post:**
1. Copy the LinkedIn post URL (desktop URL format: `linkedin.com/posts/...`).
2. In Phantombuster, launch **LinkedIn Post Reactions Exporter** or configure a
   Trigify signal watch on the post URL.
3. Set extraction limit. LinkedIn caps at ~2,500 per run via Phantombuster.
4. Output: CSV with name, headline, company, LinkedIn URL, reaction type.

**X (Twitter) post:**
1. Use Phantombuster's **X Post Engagers Scraper** with the tweet URL.
2. Output: handle list. Requires an additional enrichment step to get work emails.

**Clay (alternative for LinkedIn):**
1. Create a new Clay table with a LinkedIn Post URL column.
2. Use the "LinkedIn Post Reactions" integration to pull engager list directly.
3. Proceed to waterfall enrichment in the same table.

### Phase 3: Clean and ICP-Filter the List

Before enrichment, run a manual ICP filter to remove non-qualifying profiles and
avoid wasting enrichment credits.

**ICP filter steps:**
1. Open the CSV in Clay or a spreadsheet.
2. Add an ICP boolean column with criteria:
   - Title contains any of: `[your target title keywords]` AND
   - Company size between `[min]` and `[max]` employees (use LinkedIn headline
     or company data available in the scraper output)
   - Country/region matches target geo
3. Keep only rows where ICP = TRUE.
4. Remove duplicate profiles (same LinkedIn URL appearing from multiple reactions).
5. Remove anyone already in your CRM (export your CRM contacts for dedup).

Expected pass rate: 15-35% of raw engagers will pass ICP filter on a well-chosen
post. If pass rate is below 10%, reassess whether this post fits the play.

### Phase 4: Enrich the Filtered List

Run the filtered list through a multi-provider email waterfall to maximize coverage.

**Recommended waterfall order (LeadMagic-first):**
1. **LeadMagic Email Finder** — primary provider (highest hit rate for B2B contacts)
   - Input: first name, last name, company domain
   - Output: work email + verification status
2. **Apollo** — second-tier fallback for profiles LeadMagic does not find
3. **Hunter.io** — third-tier fallback for domain-pattern guessing with confidence score
4. **LinkedIn profile email** — manual spot-check for high-value targets with no hit

**For Facebook engagers** (no LinkedIn URL in raw data):
1. Use the name + comment text to identify the person on LinkedIn via Clay's
   LinkedIn Search integration or LeadMagic's `/find-contact` by name and company.
2. Enrich from LinkedIn URL once found.

**Email verification:** Run all found emails through LeadMagic `/email-verify`
or NeverBounce before pushing to the sequencer. Only push `valid` status emails.
Do not send to `catch-all` addresses at high volume without domain-level bounce
rate monitoring.

**Enrichment output schema per row:**

| Field | Source |
|---|---|
| First name | Scraper output |
| Last name | Scraper output |
| Work email | LeadMagic / waterfall |
| Email status | Verification endpoint |
| Job title | LinkedIn enrichment |
| Company name | LinkedIn / scraper |
| Company domain | Clay company enrichment |
| LinkedIn URL | Scraper output |
| Post engagement type | Scraper (like/comment/share) |
| Comment text | Scraper (if comment) |
| ICP tier | Your filter logic |

### Phase 5: Craft Discovery-First Outreach

Every message must reference the specific post or the topic it addressed. No
generic openers. The message structure follows Spielmann's Cold to Gold
Current-State pattern:

**Message architecture (3 lines, under 75 words):**

```
Line 1 (Context): Specific reference to the post or their engagement.
Line 2 (Bridge): Name the topic and why it's relevant to their role.
Line 3 (Question): One Current-State discovery question. No CTA, no meeting ask.
```

**Example — design technology discovery:**

> Hi [First name], saw you [liked/commented on] [author]'s post about [topic].
>
> Curious what your current setup looks like for [the specific problem/tool category
> the post was about] — specifically how [role-relevant pain point].
>
> How are you handling that today?

**Example — Facebook video post on design tools:**

> Hi [First name], noticed you engaged with [name]'s video on how design teams are
> rethinking their tool stack.
>
> We work with a lot of [title]-level folks at similar-sized companies on exactly
> that transition.
>
> How are you currently set up on the design technology side — still on [legacy
> tool], or already exploring alternatives?

**Message rules:**
- First line is traceable to the specific post or topic — never a generic opener
- Discovery question is about their current state, not your product
- Total message under 80 words
- No links, attachments, or calendly in the first touch
- Subject line references the post topic, not your product: "Design tech stack question"

**Variant by engagement type:**

| Engagement Type | Opening Approach |
|---|---|
| Liked the post | "Saw you liked [author]'s post on..." |
| Commented | "Saw your comment on [author]'s post — specifically [paraphrase their point]..." |
| Shared/Retweeted | "Noticed you shared [author]'s take on..." |
| Replied to thread | "Your reply to [author]'s thread caught my eye — [their specific point]..." |

If the person commented, use their comment text to open. This is the strongest
personalization signal available. Quote or closely paraphrase what they said.

### Phase 6: Sequence and Measure

**Recommended sequence structure:**

| Touch | Day | Channel | Content |
|---|---|---|---|
| Touch 1 | Day 1 | Email | Discovery question (post reference) |
| Touch 2 | Day 3 | LinkedIn DM | Short reference to the post + same question |
| Touch 3 | Day 6 | Email | Follow-up: share a relevant resource tied to the post topic |
| Touch 4 | Day 10 | Email | Breakup: "should I take you off this list?" |

Do not run more than 4 touches on a post-engager list. The signal window is short;
if they do not reply within 10 days, the timing has passed.

**Measurement:**

Track post-engager plays separately from standard outbound campaigns in your
sequencer and CRM. Tag source as `post-engager-play` + the post URL or topic.

| Metric | Target | Notes |
|---|---|---|
| Reply rate (Touch 1) | 8-15% | Higher than cold list due to signal relevance |
| Positive reply rate | 3-6% | Discovery questions generate more neutral replies than pitches |
| Meeting booked rate | 1.5-3% | |
| Enrichment hit rate | 55-70% | Facebook engagers harder to enrich than LinkedIn |
| ICP pass rate | 15-35% | Monitor to assess post quality for future plays |

Review signal quality after each post play. Posts where ICP pass rate was below
15% or reply rate was below 5% indicate the post content did not match your ICP
closely enough.

## Output Format

Post Engager Play documentation:

1. **Post qualification summary** — post URL, engagement count, ICP density
   sample assessment, freshness window, go/no-go decision
2. **Scrape output** — cleaned CSV with engagement type and comment text
3. **Filtered list** — ICP-qualified rows with enrichment schema populated
4. **Enrichment summary** — hit rate by provider, email verification status
   distribution, total contactable contacts
5. **Message variants** — 3-5 discovery-first message variants with subject
   lines, each under 80 words, tied to specific post reference
6. **Sequence spec** — 4-touch cadence with channel, day, and content for each
7. **Tracking setup** — source tag structure for CRM, reply rate by engagement
   type expected dashboard view

## Quality Check

- [ ] Post is public and within the 7-day freshness window
- [ ] ICP filter applied before enrichment (not after) to reduce credit waste
- [ ] Email verification run before sequencer push — only `valid` status enrolled
- [ ] All message Touch 1 variants reference the specific post or the commenter's
     own words — zero generic openers
- [ ] Discovery question asks about current state, not about the product
- [ ] Total message length under 80 words for Touch 1
- [ ] Sequence capped at 4 touches maximum (signal window is short)
- [ ] Source tag applied for post-engager tracking separate from cold list sends
- [ ] Dedup run against existing CRM contacts before enrichment

## Common Pitfalls

1. **Scraping without ICP filtering.** A post with 500 engagers likely has 350 who
   are not your buyer. Running all 500 through enrichment wastes credits and fills
   your CRM with noise. Filter first; enrich the qualified subset.

2. **Generic first lines.** "I saw you were interested in design technology" is not
   a signal-anchored opener — it could apply to anyone. Reference the specific post,
   the specific commenter's words if available, or the specific topic in a way that
   makes clear you saw the post they engaged with.

3. **Pitching in the first message.** The Spielmann Current-State question generates
   replies precisely because it does not pitch. Replacing the discovery question
   with a product claim destroys the warm-signal advantage and makes the email
   indistinguishable from cold outreach.

4. **Waiting too long after scraping.** A post from five days ago is not a fresh
   signal. Run the scraper the same day the post is identified and send Touch 1
   within 24 hours. Every day of delay cuts reply rate.

5. **Ignoring comment text as personalization.** When a person commented on the
   post, their comment is the most specific first-line material available. Not using
   it in favor of a generic opener is a wasted opportunity.

6. **No CRM dedup before sending.** Existing customers and active opportunities
   in your pipeline may have engaged with the same post. Send outreach to a current
   customer and you damage the relationship. Always dedup against CRM before
   enrichment begins.

7. **Sending to Facebook catch-all addresses.** Facebook engager lists often yield
   personal Gmail/Hotmail addresses when enriched, not work emails. Verify and skip
   non-work emails; personal-email cold outreach has significantly lower reply rates
   and higher spam placement risk.

## Execution Artifacts

- `references/framework-notes.md` — Trigify, Phantombuster, and Spielmann framework notes
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **social-intent-monitoring**: Continuously monitor social platforms for signals
  rather than targeting a single post; Trigify-based agentic setup
- **signal-scoring**: Layer post-engagement signals with hiring, funding, and
  tech-stack signals for prioritization
- **lead-enrichment**: Full enrichment schema and waterfall design for the filtered list
- **cold-email-copywriting**: Write the discovery-first message copy with proven
  subject line patterns
- **multi-channel-outreach**: Coordinate email + LinkedIn DM sequence after scrape
- **social-selling**: Build your own LinkedIn presence to attract ICP engagement
  on your own posts (inbound version of this play)
