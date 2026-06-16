# StreamYard — Platform Reference for Reveting Production

Reference tables for `SKILL.md`. Source: StreamYard official documentation
(streamyard.com) and Jessie Lizak (Reveting) public production practices.

**Public channels:** 🔗 [streamyard.com](https://streamyard.com) · 📚 [streamyard.com/blog](https://streamyard.com/blog)

## Tier comparison for show operators

| Feature | Free | Basic ($49/mo) | Professional ($99/mo) |
|---|---|---|---|
| Destinations | 1 | 5 | 8 |
| Max guests | 3 | 5 | 8 |
| Resolution | 720p | 1080p | 1080p |
| Brand kit | No | Yes | Yes |
| Custom overlays | No | Yes | Yes |
| Recording storage | 15 days | 15 days | 30 days |
| Recording download | Yes | Yes | Yes |
| Watermark removal | No | Yes | Yes |

**Recommendation for Reveting-style shows:** Basic tier minimum (brand kit, 1080p, 5 guests). Professional if running panels (4+ guests) or 5+ simulcast destinations.

## Supported streaming destinations

| Destination | Auth method | Notes |
|---|---|---|
| LinkedIn Live | OAuth (profile or page) | Requires Creator Mode + Live access |
| YouTube Live | Google OAuth | Supports scheduled and on-demand |
| Facebook Live | Facebook OAuth | Personal profile or page |
| Twitter/X Live | OAuth | Limited algorithm reach for B2B |
| Custom RTMP | Endpoint + stream key | Restream.io, Castr, website embeds |

**B2B default:** LinkedIn Live primary + YouTube as replay archive. Facebook optional if audience is active there.

## Scene layout specifications

StreamYard scene editor uses percentage-based positioning. Reference layouts:

| Layout | Guest tiles | Host position | Best for |
|---|---|---|---|
| Side by side | 2 equal | Left | Standard interview |
| 60/40 split | Host 60%, guest 40% | Left | Host-led segments |
| Guest spotlight | Guest full | Host PiP (small) | Guest story moment |
| Screen share | Screen 70% | Cameras right 30% | Demo or slide |
| Full screen | None | Full frame | Host intro/close |

## Brand kit assets — technical specs

| Asset | Format | Size | Notes |
|---|---|---|---|
| Logo | PNG (transparent) | Min 400×400px | Used in overlays and end card |
| Show background | PNG or JPG | 1920×1080px | Full-screen scenes |
| Lower third | PNG (transparent) | 1920×200px approx | Name + title strip |
| Ticker text | Text input in UI | N/A | Scroll speed adjustable |
| Overlay color | Hex code | N/A | Matches brand kit |

## Recording specs and handoff

| Spec | Value |
|---|---|
| Container | MP4 |
| Resolution | 720p (Free), 1080p (Basic/Pro) |
| Audio | AAC stereo |
| Download window | 15 days (Free/Basic), 30 days (Pro) |
| Max broadcast length | 12 hours (Basic/Pro) |

**Handoff checklist after each show:**
- [ ] MP4 downloaded to shared drive within 2 hours of broadcast end
- [ ] Timestamp log created (chapter start/end times in minutes)
- [ ] Guest headshot and bio confirmed for lower-third accuracy
- [ ] Broadcast title and description saved for show notes draft
- [ ] Clips extracted within 48 hours for LinkedIn repurposing

## Guest tech requirements

StreamYard is browser-based. Guest requirements:
- Chrome (v90+) or Firefox (v90+) — Safari not fully supported
- Stable internet: minimum 5 Mbps upload recommended
- Webcam: 720p minimum; 1080p preferred
- Headset or wired earbuds (prevents echo)
- Quiet background or virtual background (StreamYard supports blur + custom)

**Pre-show tech check script (host to guest):**
1. "Can you open the link in Chrome?"
2. "Click Allow on camera and microphone permission."
3. "How does your audio sound to you? Can you hear an echo?"
4. "Your name shows as [X] — correct?"
5. "We'll start in about 10 minutes. Any questions before we go live?"

## Chapter mark verbal cues (Reveting style)

Use these in-show to signal clip cut points to the editor:

| Cue | Use case |
|---|---|
| "Let's zoom in on that…" | Transition to tactical depth |
| "Before we move on…" | Pause before chapter shift |
| "Here's the part I want everyone to remember…" | Pull-quote moment |
| "Let's shift gears…" | New chapter start |
| "What's your one takeaway for the audience?" | Close of chapter / clip endpoint |

## Cross-references

| Topic | Skill / artifact |
|---|---|
| Full Reveting content engine | `linkedin-live-strategy` |
| Guest booking and scheduling | `reveting-calendar-flows` |
| Guest invite and briefing emails | `reveting-email-flows` |
| GHL post-show automation | `reveting-ghl-workflows` |
| Repurposing clips to LinkedIn feed | `linkedin-algorithm` |
