# Framework Notes — Post Engager Play

## Trigify — Viral Engager Harvesting

Source: https://help.trigify.io/en/articles/8836198-draft-common-workflow-patterns

Trigify's Viral Engager Harvesting is one of four canonical agentic workflow
patterns in their public documentation. The pattern:

1. **Post Trigger** — detect a post above a configurable engagement threshold
   (likes + comments + shares)
2. **Fetch Engagers** — pull all people who reacted to the post (name, headline,
   LinkedIn URL, reaction type)
3. **Person Enrichment** — LinkedIn URL → firmographic data (title, company,
   company size, country, seniority level)
4. **ICP Filter** — Boolean condition on title + company size (applied before
   email enrichment to save credits)
5. **Email Enrichment** — verified work email lookup via LeadMagic or waterfall
6. **Deliverability Check** — verify email before push
7. **Route** — qualified + verified: CRM + sequencer; qualified no email: Slack
   alert for manual LinkedIn DM; not qualified: discard

Key design principle from Trigify documentation: the ICP filter step runs on
free platform data (title, company, country available from LinkedIn without
enrichment credits) before the paid enrichment step. This ordering reduces
enrichment spend by 40-60% on large post engagement lists.

Trigify-supported social sources for post monitoring: LinkedIn, X, Reddit.
Facebook support as of 2026: via Zapier webhook integration with Phantombuster
output.

---

## Phantombuster — Scraper Reference

### Facebook Post Likes/Comments Scraper
Source: https://phantombuster.com/automations/facebook/facebook-post-likes-comments-scraper

**Inputs:**
- Public Facebook post URL (must be publicly viewable without login, or session
  cookie must be connected)
- Facebook session cookie (connected via Phantombuster's Authentication system)
- Extraction limit (default: unlimited)

**Outputs:** CSV with columns:
- `profileName` — full name of the reactor/commenter
- `profileUrl` — Facebook profile URL
- `commentText` — comment text (empty for likes)
- `timestamp` — time of engagement

**Limitations:**
- Requires a valid Facebook session (Phantombuster cookie auth)
- Rate limited by Facebook's session policies; spread runs over time for large posts
- Private profiles may return partial data (name only, no profile URL)
- Comments from private-profile users will appear as limited entries

**Facebook-to-LinkedIn enrichment gap:** Facebook scraper output does not include
LinkedIn URLs or company data. The enrichment step must first attempt to identify
the person's LinkedIn profile via name + company search (Clay's LinkedIn Search
integration or LeadMagic `/find-contact`), then enrich from LinkedIn URL.

### LinkedIn Post Reactions Exporter
Source: https://phantombuster.com/automations/linkedin/linkedin-post-reactions-exporter

**Inputs:**
- LinkedIn post URL (desktop format: `linkedin.com/posts/[handle]_[postid]`)
- LinkedIn session cookie
- Extraction limit (default 2,500 per run)

**Outputs:** CSV with:
- `firstName`, `lastName`
- `headline` (job title)
- `company` (from headline)
- `profileUrl` (LinkedIn URL)
- `reactionType` (Like, Celebrate, Insightful, Love, Curious, Support)

**Enrichment advantage:** LinkedIn output already includes job title and company
from headline, enabling ICP filtering before full enrichment.

**Rate limits:** Phantombuster enforces slot-based execution. Running large exports
(1,000+ profiles) should be scheduled in off-peak hours to reduce LinkedIn session
risk.

---

## Pat Spielmann — Cold to Gold: Current-State Discovery

Source: Pat Spielmann Cold to Gold methodology — https://www.patspielmann.com

The Cold to Gold framework centers on discovery as the first-touch mechanism.
The Current-State question replaces the pitch in Touch 1.

**Why Current-State questions outperform pitches in cold outreach:**
- A pitch asks the prospect to evaluate your product with zero context
- A Current-State question asks the prospect to reflect on their own situation,
  which they know well and have opinions about
- Qualified prospects who have the problem reply to articulate their current
  state; non-qualified prospects opt out silently — self-selecting the list

**Current-State question formula:**
> "How are you currently [verb: handling / managing / thinking about / approaching]
> [the specific problem or category the post addressed]?"

**Applied to post-engager plays:** The post the prospect engaged with is the
bridge. Reference the post → name the topic → ask the Current-State question.
The reference makes the question specific rather than generic; the question
generates a reply that qualifies the prospect in one step.

**What NOT to ask in Touch 1:**
- "Would you be interested in..." — asks for commitment before context
- "Are you the right person to talk to about..." — wastes their time on
  internal routing
- "Can I show you how we..." — pitch disguised as question
- "Do you have 15 minutes for a call..." — asks for meeting before value exchange

---

## Jordan Crawford — Signal Relevance over Volume

Source: Jordan Crawford, Clay Agency published content — https://www.clay.com/blog

Crawford's published frameworks consistently apply the principle that a smaller
list with higher contextual relevance outperforms a larger list without it.

Quantified benchmark from Crawford's published work:
- Cold list with no signal context: 0.5-1.5% reply rate
- Signal-filtered list with generic opener: 2-4% reply rate
- Signal-filtered list with signal-anchored opener: 5-15% reply rate

The post-engager play achieves the third tier when:
1. The list is ICP-filtered (signal filtering)
2. The message opener references the specific post (signal-anchored opener)

Crawford's list size guidance for signal-based plays: 50-500 records per play is
the effective working range. Below 50 has insufficient statistical signal; above
500 requires automation that often degrades personalization quality.

---

## Signal Freshness Reference Table

Based on Trigify urgency windows and Spielmann's timing principles:

| Post Age at Time of Scrape | Outreach Send Timing | Expected Benefit |
|---|---|---|
| Same day (0-24 hrs) | Send within 24 hrs | Maximum — prospect still thinking about topic |
| 1-2 days | Send within 24-48 hrs | High — topic still recent in prospect's mind |
| 3-5 days | Send within 48 hrs | Medium — topic fading; reference more general |
| 5-7 days | Use only if no better signal | Low — treat as topic-based outreach, not post-based |
| 7+ days | Do not run post-engager play | Signal expired; run standard cold outreach |
