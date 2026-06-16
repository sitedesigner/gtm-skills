#!/usr/bin/env python3
"""Build Reveting Show Flow PowerPoint."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# Brand colors
NAVY     = RGBColor(0x0D, 0x1B, 0x3E)   # dark navy background
GOLD     = RGBColor(0xF5, 0xA6, 0x23)   # Reveting gold/amber
WHITE    = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT    = RGBColor(0xF0, 0xF4, 0xFF)   # very light blue-white
GREEN    = RGBColor(0x1E, 0xA5, 0x6B)   # success green
RED      = RGBColor(0xD9, 0x3B, 0x3B)   # rejection red
MIDBLUE  = RGBColor(0x1A, 0x4B, 0x9F)   # mid blue
GREY     = RGBColor(0x8A, 0x9B, 0xB5)

SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H

blank = prs.slide_layouts[6]   # completely blank layout


def add_slide():
    return prs.slides.add_slide(blank)


def rect(slide, x, y, w, h, fill=None, line=None, line_w=Pt(0)):
    from pptx.util import Emu
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        Inches(x), Inches(y), Inches(w), Inches(h)
    )
    shape.line.fill.background()
    if fill:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill
    else:
        shape.fill.background()
    if line:
        shape.line.color.rgb = line
        shape.line.width = line_w
    else:
        shape.line.fill.background()
    return shape


def text_box(slide, x, y, w, h, text, size=Pt(12), bold=False,
             color=WHITE, align=PP_ALIGN.LEFT, wrap=True):
    txBox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    txBox.word_wrap = wrap
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = size
    run.font.bold = bold
    run.font.color.rgb = color
    return txBox


def add_para(tf, text, size=Pt(11), bold=False, color=WHITE,
             align=PP_ALIGN.LEFT, space_before=Pt(2)):
    p = tf.add_paragraph()
    p.alignment = align
    p.space_before = space_before
    run = p.add_run()
    run.text = text
    run.font.size = size
    run.font.bold = bold
    run.font.color.rgb = color
    return p


def bg(slide, color=NAVY):
    r = rect(slide, 0, 0, 13.33, 7.5, fill=color)
    return r


def header_bar(slide, title, subtitle=None):
    rect(slide, 0, 0, 13.33, 1.2, fill=MIDBLUE)
    rect(slide, 0, 1.2, 13.33, 0.05, fill=GOLD)
    text_box(slide, 0.3, 0.1, 9, 0.6, title, size=Pt(28), bold=True,
             color=WHITE)
    if subtitle:
        text_box(slide, 0.3, 0.7, 10, 0.45, subtitle, size=Pt(13),
                 color=GOLD)


def step_box(slide, x, y, w, h, number, title, lines, fill=MIDBLUE,
             num_color=GOLD):
    rect(slide, x, y, w, h, fill=fill, line=GOLD, line_w=Pt(1))
    # number circle
    circle = slide.shapes.add_shape(
        9,   # oval
        Inches(x + 0.1), Inches(y + 0.08),
        Inches(0.42), Inches(0.42)
    )
    circle.fill.solid()
    circle.fill.fore_color.rgb = GOLD
    circle.line.fill.background()
    ctf = circle.text_frame
    ctf.word_wrap = False
    cp = ctf.paragraphs[0]
    cp.alignment = PP_ALIGN.CENTER
    crun = cp.add_run()
    crun.text = str(number)
    crun.font.size = Pt(13)
    crun.font.bold = True
    crun.font.color.rgb = NAVY
    # title
    text_box(slide, x + 0.58, y + 0.1, w - 0.65, 0.35,
             title, size=Pt(12), bold=True, color=WHITE)
    # body lines
    ty = y + 0.48
    for line in lines:
        text_box(slide, x + 0.15, ty, w - 0.25, 0.28,
                 line, size=Pt(9.5), color=LIGHT)
        ty += 0.26


def arrow_right(slide, x, y, length=0.35, thickness=0.18):
    """Draw a right-pointing arrow."""
    shape = slide.shapes.add_shape(
        13,  # right arrow
        Inches(x), Inches(y - thickness / 2),
        Inches(length), Inches(thickness)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = GOLD
    shape.line.fill.background()
    return shape


def arrow_down(slide, x, y, length=0.3):
    shape = slide.shapes.add_shape(
        14,  # down arrow
        Inches(x - 0.09), Inches(y),
        Inches(0.18), Inches(length)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = GOLD
    shape.line.fill.background()
    return shape


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 1 — TITLE
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
# top accent
rect(s, 0, 0, 13.33, 0.12, fill=GOLD)
rect(s, 0, 7.38, 13.33, 0.12, fill=GOLD)

text_box(s, 1.5, 1.4, 10, 1.0,
         "REVETING SHOW OPERATIONS",
         size=Pt(14), bold=True, color=GOLD, align=PP_ALIGN.CENTER)
text_box(s, 0.5, 2.3, 12.33, 1.4,
         "End-to-End Production Flow",
         size=Pt(46), bold=True, color=WHITE, align=PP_ALIGN.CENTER)
text_box(s, 1.0, 3.75, 11.33, 0.6,
         "From New Show Setup → Guest Booking → Email Sequence → Live Show → Post-Production",
         size=Pt(15), color=LIGHT, align=PP_ALIGN.CENTER)

# 5 pillars row
pillars = [
    ("SHOW\nSETUP", MIDBLUE),
    ("GUEST\nBOOKING", MIDBLUE),
    ("EMAIL\nSEQUENCE", MIDBLUE),
    ("LIVE\nSHOW", MIDBLUE),
    ("POST-\nPROD", MIDBLUE),
]
px = 0.8
for label, col in pillars:
    rect(s, px, 4.65, 2.2, 1.3, fill=col, line=GOLD, line_w=Pt(1.5))
    text_box(s, px, 4.65, 2.2, 1.3, label,
             size=Pt(15), bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    px += 2.35

text_box(s, 0.5, 6.25, 12.33, 0.4,
         "Based on Jessie Lizak (Reveting) LinkedIn Live & Livestream Content Engine SOP",
         size=Pt(10), color=GREY, align=PP_ALIGN.CENTER)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 2 — OVERVIEW FLOW MAP
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Complete Show Flow — Overview",
           "The end-to-end Reveting production lifecycle")

# 4-column lanes
lanes = [
    ("TIER 1\nSHOW SETUP", MIDBLUE, [
        "Show Identity",
        "Team Roster",
        "Channel Stack",
        "Podcast Links",
        "Booking Docs",
        "Guest Rules",
    ]),
    ("EPISODE\nPREP", RGBColor(0x1A, 0x5C, 0x4A), [
        "Guest Booking",
        "Fit Gate",
        "Tier 2 Variables",
        "Topic Editing",
        "Calendar Stage 1",
        "T-14 Activation",
    ]),
    ("PRE-SHOW\nEMAILS", RGBColor(0x4A, 0x1A, 0x5C), [
        "Email 1 — Event Published",
        "Email 2 — T-7 Days",
        "Email 3 — Day Before",
        "Email 4 — Day Of",
        "Calendar Stage 2",
        "StreamYard Guest Link",
    ]),
    ("LIVE &\nPOST-SHOW", RGBColor(0x5C, 0x2A, 0x1A), [
        "Pre-show Tech Check",
        "Go Live (60 min)",
        "Email 5 — Within 1h",
        "Clips Delivered",
        "Email 6 — 24–36h",
        "Podcast Upload",
    ]),
]

lx = 0.2
for title, col, items in lanes:
    rect(s, lx, 1.35, 3.1, 5.9, fill=col)
    r, g, b = col[0], col[1], col[2]
    rect(s, lx, 1.35, 3.1, 0.65, fill=RGBColor(
        min(r + 30, 255),
        min(g + 30, 255),
        min(b + 30, 255)
    ))
    text_box(s, lx, 1.35, 3.1, 0.65, title,
             size=Pt(13), bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    iy = 2.1
    for item in items:
        rect(s, lx + 0.1, iy, 2.9, 0.7,
             fill=RGBColor(
                 min(col[0] + 15, 255),
                 min(col[1] + 15, 255),
                 min(col[2] + 15, 255)
             ),
             line=GOLD, line_w=Pt(0.5))
        text_box(s, lx + 0.15, iy + 0.12, 2.8, 0.5, item,
                 size=Pt(10), color=WHITE)
        iy += 0.78
    lx += 3.3


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 3 — TIER 1 SHOW SETUP
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Phase 1 — New Show Setup (Tier 1 Constants)",
           "Complete once at show launch. Store in Google Drive root folder. Share with all team members.")

# 3×2 grid of variable groups
groups = [
    ("Show Identity", MIDBLUE, [
        "[SHOW_NAME]  ·  [SHOW_EMAIL]",
        "[SHOW_TIMEZONE] → Eastern Time (USA)",
        "[SHOW_DAY_OF_WEEK]  ·  [SHOW_RECURRING_TIME_ET]",
        "[PRESHOW_DURATION_MIN] = 15  ·  [SHOW_DURATION_MIN] = 60",
    ]),
    ("Team", MIDBLUE, [
        "[HOST_NAME]  ·  [HOST_LINKEDIN_URL]",
        "[PRODUCER_NAME]  ·  [PRODUCTION_ASSISTANT_NAME]",
        "[SIGNATURE_BLOCK] — full email sign-off",
        "[CALENDAR_ACCOUNT] = ww@reveting.com",
    ]),
    ("Channel Stack", RGBColor(0x1A, 0x5C, 0x4A), [
        "[STREAM_TO_LINKEDIN]  ·  [STREAM_TO_YOUTUBE]",
        "[STREAM_TO_FACEBOOK]  ·  [STREAM_TO_TWITCH]",
        "[STREAM_TO_INSTAGRAM]",
        "⚠ Confirm against Total Deliverables Doc — NEVER guess",
    ]),
    ("Podcast & Replay Links", RGBColor(0x1A, 0x5C, 0x4A), [
        "[SPOTIFY_SHOW_LINK]  ·  [APPLE_PODCASTS_SHOW_LINK]",
        "[YOUTUBE_CHANNEL_LINK]  ·  [SHOW_WEBSITE_LINK]",
        "[PAST_EPISODES_LINK]",
        "",
    ]),
    ("Booking & Docs", RGBColor(0x4A, 0x1A, 0x5C), [
        "[BOOKING_FORM_LINK]",
        "[TOTAL_DELIVERABLES_DOC]",
        "[STREAMYARD_ACCOUNT_URL]  ·  [CLIENT_OUTLINE_LINK]",
        "[GOOGLE_DRIVE_ROOT_FOLDER]  ·  [LINKEDIN_INVITE_WALKTHROUGH_URL]",
    ]),
    ("Guest Qualification Rules", RGBColor(0x4A, 0x1A, 0x5C), [
        "[MIN_LINKEDIN_FOLLOWERS]: 5,000+ preferred",
        "1,000–4,999: confirm with Prod + Marketing Lead",
        "Below 1,000: NO-GO unless no other option",
        "[SHOW_CONTENT_PILLARS]  ·  Escalation → WhatsApp Jessie",
    ]),
]

gx, gy = 0.2, 1.45
col_w, row_h = 4.3, 2.7
for i, (title, col, lines) in enumerate(groups):
    cx = gx + (i % 3) * (col_w + 0.1)
    cy = gy + (i // 3) * (row_h + 0.1)
    rect(s, cx, cy, col_w, row_h, fill=col, line=GOLD, line_w=Pt(1))
    rect(s, cx, cy, col_w, 0.45, fill=RGBColor(
        min(col[0] + 25, 255),
        min(col[1] + 25, 255),
        min(col[2] + 25, 255)
    ))
    text_box(s, cx + 0.1, cy + 0.06, col_w - 0.2, 0.38,
             title, size=Pt(11.5), bold=True, color=GOLD)
    ly = cy + 0.52
    for line in lines:
        text_box(s, cx + 0.12, ly, col_w - 0.22, 0.42,
                 line, size=Pt(9), color=LIGHT)
        ly += 0.5


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 4 — GUEST BOOKING + FIT GATE
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Phase 2 — Guest Booking & Fit Gate",
           "New booking appears in app.reveting.com → complete Tier 2 → make fit decision")

# Left: booking flow steps
rect(s, 0.2, 1.4, 5.8, 5.7, fill=MIDBLUE)
text_box(s, 0.3, 1.45, 5.5, 0.4, "BOOKING INTAKE STEPS",
         size=Pt(12), bold=True, color=GOLD)

steps = [
    ("1", "Find the Booking", "Calendars → Appointment List View → newest"),
    ("2", "Pull Form Submission", "Click guest → 3 dots → View Details → Form Submission"),
    ("3", "Complete Tier 2 Guest Info", "[GUEST_FIRST_NAME], [GUEST_EMAIL], [GUEST_LINKEDIN_URL], etc."),
    ("4", "Check LinkedIn Followers", "Manual LinkedIn lookup → compare to [MIN_LINKEDIN_FOLLOWERS]"),
    ("5", "Edit Topics", "Format raw submissions to 3–7 words · aligned to show strategy"),
    ("6", "Set Episode Details", "[EPISODE_NUMBER], [EPISODE_DATE], [EPISODE_TITLE], [TOPIC_1–4]"),
    ("7", "Calendar Description Stage 1", "Set immediately · include placeholder timing text"),
]

sy = 1.95
for num, title, desc in steps:
    rect(s, 0.3, sy, 5.6, 0.62, fill=RGBColor(0x1F, 0x3B, 0x7A), line=GOLD, line_w=Pt(0.5))
    text_box(s, 0.32, sy + 0.02, 0.32, 0.32, num,
             size=Pt(13), bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(s, 0.68, sy + 0.02, 4.5, 0.26, title,
             size=Pt(10), bold=True, color=WHITE)
    text_box(s, 0.68, sy + 0.28, 5.1, 0.3, desc,
             size=Pt(8.5), color=LIGHT)
    sy += 0.7

# Right: Fit Gate decision tree
rect(s, 6.3, 1.4, 6.8, 5.7, fill=RGBColor(0x1A, 0x3A, 0x2A))
text_box(s, 6.4, 1.45, 6.5, 0.4, "FIT GATE DECISION",
         size=Pt(12), bold=True, color=GOLD)

# Decision diamond (use rectangle rotated look via text)
rect(s, 8.1, 2.1, 3.2, 1.0, fill=RGBColor(0x1A, 0x5C, 0x4A), line=GOLD, line_w=Pt(1.5))
text_box(s, 8.1, 2.1, 3.2, 1.0,
         "LinkedIn followers\n≥ 5,000?",
         size=Pt(12), bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# YES branch
rect(s, 6.4, 3.4, 2.6, 0.75, fill=GREEN, line=WHITE, line_w=Pt(1))
text_box(s, 6.4, 3.4, 2.6, 0.75,
         "✓  FIT\nProceed with booking",
         size=Pt(10), bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# 1000-4999 branch
rect(s, 9.35, 3.4, 3.5, 0.75, fill=RGBColor(0xB8, 0x76, 0x10), line=WHITE, line_w=Pt(1))
text_box(s, 9.35, 3.4, 3.5, 0.75,
         "⚠  1,000–4,999\nConfirm with Prod + Mktg Lead",
         size=Pt(9.5), bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# below 1000
rect(s, 8.1, 4.6, 3.2, 0.75, fill=RED, line=WHITE, line_w=Pt(1))
text_box(s, 8.1, 4.6, 3.2, 0.75,
         "✗  NOT A FIT\n< 1,000 followers",
         size=Pt(10), bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# Not a Fit path
rect(s, 6.5, 5.6, 6.4, 1.1, fill=RGBColor(0x5C, 0x1A, 0x1A), line=RED, line_w=Pt(1))
text_box(s, 6.6, 5.65, 6.2, 0.95,
         'Send "Not a Fit" Email\n[SHOW_NAME] · [SIGNATURE_BLOCK] · [GUEST_FIRST_NAME] · [FALLBACK_SHOW_LINKS]\n→ STOP. Do not continue to booking.',
         size=Pt(9.5), color=WHITE)

# Labels YES/NO
text_box(s, 7.0, 3.1, 0.8, 0.3, "YES ↙", size=Pt(9), bold=True, color=GREEN)
text_box(s, 10.5, 3.1, 0.8, 0.3, "⚠ ↘", size=Pt(9), bold=True, color=GOLD)
text_box(s, 9.5, 3.9, 0.4, 0.6, "↓", size=Pt(18), bold=True, color=RED)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 5 — T-14 ACTIVATION + CALENDAR STAGE 1
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Phase 3 — T-14 Activation & Calendar Stage 1",
           "Guest is a fit → send T-14 activation immediately if booking is within 14 days")

# T-14 Email box
rect(s, 0.2, 1.4, 6.0, 5.7, fill=RGBColor(0x2A, 0x1A, 0x4A), line=GOLD, line_w=Pt(1.5))
text_box(s, 0.3, 1.45, 5.7, 0.5,
         "T-14 ACTIVATION EMAIL",
         size=Pt(14), bold=True, color=GOLD)
text_box(s, 0.3, 1.92, 5.7, 0.35,
         "Trigger: 14 days before show (or immediately if < 14 days away)",
         size=Pt(10), color=LIGHT)

t14_content = [
    ("Required Tier 1", "[SIGNATURE_BLOCK]"),
    ("Required Tier 2", "[GUEST_FIRST_NAME]"),
    ("Subject", "Confirming your appearance on [SHOW_NAME]"),
    ("", ""),
    ("Email opens", "Hi [GUEST_FIRST_NAME],"),
    ("", "We're excited to have you on [SHOW_NAME]!"),
    ("", ""),
    ("Includes", "• Confirm show date + time"),
    ("", "• Request LinkedIn connection with [LINKEDIN_CHANNEL_OWNER]"),
    ("", "• Link to past episodes for reference"),
    ("", "• Explain topic editing process"),
    ("", "• Note: topics will be formatted & emailed soon"),
    ("", ""),
    ("Sign-off", "[SIGNATURE_BLOCK]"),
]

ty = 2.35
for label, val in t14_content:
    if label:
        text_box(s, 0.3, ty, 1.4, 0.28, label + ":", size=Pt(9), bold=True, color=GOLD)
        text_box(s, 1.72, ty, 4.3, 0.28, val, size=Pt(9), color=WHITE)
    else:
        text_box(s, 0.3, ty, 5.7, 0.28, val, size=Pt(9), color=LIGHT)
    ty += 0.3

# Calendar Stage 1 box
rect(s, 6.5, 1.4, 6.6, 5.7, fill=RGBColor(0x1A, 0x3A, 0x5A), line=GOLD, line_w=Pt(1.5))
text_box(s, 6.6, 1.45, 6.3, 0.5,
         "CALENDAR DESCRIPTION — STAGE 1",
         size=Pt(14), bold=True, color=GOLD)
text_box(s, 6.6, 1.92, 6.3, 0.35,
         "Set immediately when booking is created in ww@reveting.com",
         size=Pt(10), color=LIGHT)

cal1_lines = [
    "Event Name: [SHOW_NAME] with [GUEST_FIRST_NAME] [GUEST_LAST_NAME]",
    "Location: StreamYard URL TBD",
    "",
    "Thank you for submitting your topics. We will format",
    "them to fit the show and email them shortly.",
    "",
    "Promote the Event: We will share a LinkedIn event URL",
    "and ask you and your team to invite their connections.",
    "",
    "Please connect with [LINKEDIN_CHANNEL_OWNER] on LinkedIn",
    "so they can make you the guest speaker.",
    "",
    "Logistics: Login to StreamYard 15 min early at",
    "[PRESHOW_TIME_ET] / [PRESHOW_TIME_CT] / [PRESHOW_TIME_PT]",
    "Go live: [GOLIVE_TIME_ET] / [GOLIVE_TIME_CT] / [GOLIVE_TIME_PT]",
    "",
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
    "⚠ Preserve original booking form submission at bottom",
    "   — NEVER remove this block",
]

ty = 2.35
for line in cal1_lines:
    color = GOLD if line.startswith("⚠") else (GREY if line.startswith("━") else LIGHT)
    sz = Pt(8.5)
    text_box(s, 6.62, ty, 6.25, 0.26, line, size=sz, color=color)
    ty += 0.26


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 6 — EMAIL 1 (Event Published)
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Phase 4 — Email 1: Appearance Details (Event Published)",
           "Trigger: Production + Marketing Lead has published the event on all platforms")

rect(s, 0.2, 1.4, 12.9, 0.65, fill=MIDBLUE)
text_box(s, 0.3, 1.45, 12.5, 0.55,
         "This is the MOST VARIABLE-HEAVY email. All Tier 2 episode details + links must be complete before sending.",
         size=Pt(11), color=GOLD)

# Two columns: variables needed | content summary
rect(s, 0.2, 2.15, 6.2, 5.0, fill=RGBColor(0x12, 0x2A, 0x5C), line=GOLD, line_w=Pt(1))
text_box(s, 0.3, 2.2, 5.9, 0.4, "REQUIRED VARIABLES", size=Pt(12), bold=True, color=GOLD)

vars_e1 = [
    ("Tier 1", "[SHOW_NAME]  ·  [SIGNATURE_BLOCK]  ·  [LINKEDIN_INVITE_WALKTHROUGH_URL]"),
    ("Guest", "[GUEST_FIRST_NAME]"),
    ("Episode", "[EPISODE_DATE]  ·  [EPISODE_TITLE]  ·  [TOPIC_1]  ·  [TOPIC_2]  ·  [TOPIC_3]  ·  [TOPIC_4]"),
    ("Timing", "[PRESHOW_TIME_PT/CT/ET]  ·  [GOLIVE_TIME_PT/CT/ET]"),
    ("Links", "[STREAMYARD_GUEST_LINK]  (fresh — never reused!)"),
    ("Events", "[LINKEDIN_EVENT_URL]  ·  [YOUTUBE_EVENT_URL]"),
    ("Events", "[FACEBOOK_EVENT_URL]  ·  [TWITCH_EVENT_URL]  ·  [INSTAGRAM_CHANNEL_URL]"),
]

vy = 2.68
for label, val in vars_e1:
    rect(s, 0.3, vy, 6.0, 0.6, fill=RGBColor(0x1A, 0x38, 0x6A), line=RGBColor(0x2A, 0x5A, 0xA0), line_w=Pt(0.5))
    text_box(s, 0.35, vy + 0.03, 1.0, 0.24, label, size=Pt(8.5), bold=True, color=GOLD)
    text_box(s, 1.38, vy + 0.03, 4.8, 0.54, val, size=Pt(8.5), color=LIGHT)
    vy += 0.65

rect(s, 6.6, 2.15, 6.6, 5.0, fill=RGBColor(0x2A, 0x1A, 0x4A), line=GOLD, line_w=Pt(1))
text_box(s, 6.7, 2.2, 6.3, 0.4, "EMAIL CONTENT SUMMARY", size=Pt(12), bold=True, color=GOLD)

e1_content = [
    "Subject: You're confirmed for [SHOW_NAME]! Here are your details.",
    "",
    "Hi [GUEST_FIRST_NAME],",
    "",
    "Your episode details:",
    "• Date: [EPISODE_DATE]",
    "• Title: [EPISODE_TITLE]",
    "• Topics: [TOPIC_1], [TOPIC_2], [TOPIC_3], [TOPIC_4]",
    "• Pre-show: [PRESHOW_TIME_PT] / [PRESHOW_TIME_CT] / [PRESHOW_TIME_ET]",
    "• Go live: [GOLIVE_TIME_PT] / [GOLIVE_TIME_CT] / [GOLIVE_TIME_ET]",
    "• StreamYard (recording studio): [STREAMYARD_GUEST_LINK]",
    "",
    "Promo links (share with your audience!):",
    "• LinkedIn: [LINKEDIN_EVENT_URL]",
    "• YouTube: [YOUTUBE_EVENT_URL]",
    "• Facebook: [FACEBOOK_EVENT_URL]",
    "",
    "LinkedIn invite walkthrough: [LINKEDIN_INVITE_WALKTHROUGH_URL]",
    "",
    "[SIGNATURE_BLOCK]",
]

cy = 2.68
for line in e1_content:
    color = GOLD if line.startswith("Subject") else LIGHT
    text_box(s, 6.7, cy, 6.35, 0.28, line, size=Pt(8.5), color=color)
    cy += 0.24


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 7 — EMAILS 2, 3, 4 (Pre-show cadence)
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Phase 4 (cont.) — Pre-Show Email Cadence",
           "Email 2 at T-7 · Email 3 day before · Email 4 morning of show")

email_cols = [
    {
        "title": "Email 2 — One Week Out",
        "trigger": "T-7 days before show",
        "t1": "[SHOW_NAME]  ·  [SIGNATURE_BLOCK]\n[LINKEDIN_INVITE_WALKTHROUGH_URL]",
        "t2": "[GUEST_FIRST_NAME]  ·  [EPISODE_DATE]\n[PRESHOW_TIME_ET]  ·  [GOLIVE_TIME_ET]\n[LINKEDIN_EVENT_URL]",
        "key": "Remind guest to invite LinkedIn connections to the event",
        "color": RGBColor(0x1A, 0x3A, 0x6A),
    },
    {
        "title": "Email 3 — Day Before",
        "trigger": "T-1 day before show",
        "t1": "[SHOW_NAME]  ·  [HOST_NAME]  ·  [PRODUCER_NAME]\n[SIGNATURE_BLOCK]  ·  [PAST_EPISODES_LINK]\n[LINKEDIN_INVITE_WALKTHROUGH_URL]",
        "t2": "[GUEST_FIRST_NAME]\n[PRESHOW_TIME_PT/CT/ET]\n[GOLIVE_TIME_PT/CT/ET]\n[STREAMYARD_GUEST_LINK]\n[LINKEDIN_EVENT_URL]",
        "key": "Send StreamYard link again · Time zones all 3 · Hype episode",
        "color": RGBColor(0x2A, 0x1A, 0x5A),
    },
    {
        "title": "Email 4 — Day Of Show",
        "trigger": "Morning of show (2–4 hrs before pre-show)",
        "t1": "[SHOW_NAME]  ·  [SIGNATURE_BLOCK]",
        "t2": "[GUEST_FIRST_NAME]\n[STREAMYARD_GUEST_LINK]\n[PRESHOW_TIME_PT/CT/ET]\n[GOLIVE_TIME_PT/CT/ET]",
        "key": "Final reminder with StreamYard link · All 3 time zones",
        "color": RGBColor(0x1A, 0x3A, 0x2A),
    },
]

ex = 0.2
for ec in email_cols:
    rect(s, ex, 1.4, 4.2, 5.85, fill=ec["color"], line=GOLD, line_w=Pt(1.5))
    rect(s, ex, 1.4, 4.2, 0.55, fill=RGBColor(
        min(ec["color"][0] + 30, 255),
        min(ec["color"][1] + 30, 255),
        min(ec["color"][2] + 30, 255)
    ))
    text_box(s, ex + 0.1, 1.42, 4.0, 0.5, ec["title"],
             size=Pt(12), bold=True, color=GOLD)

    text_box(s, ex + 0.1, 2.0, 4.0, 0.3,
             "Trigger: " + ec["trigger"], size=Pt(9), color=LIGHT)

    text_box(s, ex + 0.1, 2.38, 4.0, 0.3, "Required Tier 1:",
             size=Pt(9), bold=True, color=GOLD)
    text_box(s, ex + 0.1, 2.65, 4.0, 0.65, ec["t1"], size=Pt(8.5), color=LIGHT)

    text_box(s, ex + 0.1, 3.38, 4.0, 0.3, "Required Tier 2:",
             size=Pt(9), bold=True, color=GOLD)
    text_box(s, ex + 0.1, 3.65, 4.0, 1.0, ec["t2"], size=Pt(8.5), color=LIGHT)

    text_box(s, ex + 0.1, 4.75, 4.0, 0.3, "Key Purpose:",
             size=Pt(9), bold=True, color=GOLD)
    text_box(s, ex + 0.1, 5.0, 4.0, 1.1, ec["key"], size=Pt(9), color=WHITE)

    ex += 4.37


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 8 — CALENDAR STAGE 2 + STREAMYARD SETUP
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Phase 4 (cont.) — Calendar Stage 2 & StreamYard Prep",
           "After Production + Marketing Lead publishes the event — update calendar + generate fresh StreamYard link")

# Calendar Stage 2
rect(s, 0.2, 1.4, 6.5, 5.8, fill=RGBColor(0x12, 0x2A, 0x5C), line=GOLD, line_w=Pt(1.5))
text_box(s, 0.3, 1.45, 6.2, 0.45, "CALENDAR DESCRIPTION — STAGE 2",
         size=Pt(13), bold=True, color=GOLD)
text_box(s, 0.3, 1.87, 6.2, 0.3,
         "Replace Stage 1 placeholder text. Preserve original booking submission at bottom.",
         size=Pt(9), color=LIGHT)

cal2_items = [
    "Event Name: [SHOW_NAME] with [GUEST_FIRST_NAME] [GUEST_LAST_NAME]",
    "📅 [SHOW_NAME] with [GUEST_FIRST_NAME] [GUEST_LAST_NAME]",
    "🗓 [EPISODE_DATE]",
    "🕚 [PRESHOW_TIME_ET] Pre-Show",
    "🕛 [GOLIVE_TIME_ET] Livestream",
    "",
    "Login (recording studio): [STREAMYARD_GUEST_LINK]",
    "Guest: [GUEST_FIRST_NAME] [GUEST_LAST_NAME]: [GUEST_LINKEDIN_URL]",
    "Episode title: [EPISODE_TITLE]",
    "",
    "Topics:",
    "1. [TOPIC_1]   2. [TOPIC_2]",
    "3. [TOPIC_3]   4. [TOPIC_4]",
    "",
    "Script: [EPISODE_SCRIPT_LINK]",
    "LinkedIn: [LINKEDIN_EVENT_URL]",
    "YouTube: [YOUTUBE_EVENT_URL]",
    "Facebook: [FACEBOOK_EVENT_URL]",
    "",
    "⚠ NEVER remove original guest booking submission from bottom",
]

cy2 = 2.22
for line in cal2_items:
    color = RED if line.startswith("⚠") else (GREY if not line else LIGHT)
    text_box(s, 0.3, cy2, 6.3, 0.26, line, size=Pt(8.5), color=color)
    cy2 += 0.25

# StreamYard setup
rect(s, 7.0, 1.4, 6.1, 5.8, fill=RGBColor(0x1A, 0x3A, 0x2A), line=GOLD, line_w=Pt(1.5))
text_box(s, 7.1, 1.45, 5.8, 0.45, "STREAMYARD PRE-SHOW SETUP",
         size=Pt(13), bold=True, color=GOLD)

sy_items = [
    ("Generate Guest Link", "Fresh per episode — never reuse\nSet in StreamYard → Invite → Guest Link\nPaste into [STREAMYARD_GUEST_LINK]"),
    ("Scene Library", "6 scenes: Pre-show · Full Screen Guest\nSplit Screen · Lower Third · Break\nEnd Card"),
    ("Brand Kit Active", "Logo · Background · Colors loaded\nOverlay confirmed on all scenes"),
    ("Destinations", "LinkedIn Live · YouTube Live\nFacebook Live · Twitch · Instagram\n(confirm against channel stack)"),
    ("Pre-Show Checklist", "Guest camera check · mic levels\nLighting · show guest how to stream\nto their own LinkedIn/social"),
    ("Run-of-Show", "15 min pre-show → Go Live at [GOLIVE_TIME_ET]\nHost opens · intro guest · 3 topics\nCTA → outro → record auto-saves"),
]

sy2 = 1.95
for title, body in sy_items:
    rect(s, 7.1, sy2, 5.8, 0.82,
         fill=RGBColor(0x12, 0x30, 0x20), line=GOLD, line_w=Pt(0.5))
    text_box(s, 7.15, sy2 + 0.04, 5.6, 0.25, title,
             size=Pt(10), bold=True, color=GOLD)
    text_box(s, 7.15, sy2 + 0.3, 5.6, 0.48, body, size=Pt(8.5), color=LIGHT)
    sy2 += 0.9


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 9 — LIVE SHOW + POST-SHOW (Emails 5 & 6)
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Phase 5 & 6 — Live Show, Email 5 (1h SLA) & Email 6 (36h SLA)",
           "Hard SLAs: Email 5 within 1 hour of show end · Email 6 max 36 hours after show")

# Live Show column
rect(s, 0.2, 1.4, 3.8, 5.85, fill=MIDBLUE, line=GOLD, line_w=Pt(1.5))
text_box(s, 0.3, 1.45, 3.5, 0.45, "LIVE SHOW", size=Pt(14), bold=True, color=GOLD)

live_items = [
    "Pre-Show (T-15 min)",
    "→ Tech check: cam / mic / lighting",
    "→ Show guest how to stream to their LinkedIn",
    "→ Confirm all social destinations live",
    "",
    "Go Live at [GOLIVE_TIME_ET]",
    "→ Host opens (1–2 min)",
    "→ Guest intro (2–3 min)",
    "→ Topic 1 · Topic 2 · Topic 3",
    "→ Optional Topic 4",
    "→ Guru of the Week mention",
    "→ CTA → Outro",
    "",
    "Show Ends",
    "→ StreamYard auto-saves recording",
    "→ Clock starts on Email 5 SLA",
    "→ Video editors notified (24h SLA)",
]

ly = 1.98
for line in live_items:
    color = GOLD if (line.endswith(")") or line in ("Go Live at [GOLIVE_TIME_ET]", "Show Ends", "Pre-Show (T-15 min)")) else LIGHT
    text_box(s, 0.3, ly, 3.6, 0.28, line, size=Pt(9), bold=(color == GOLD), color=color)
    ly += 0.3

# Email 5 column
rect(s, 4.2, 1.4, 4.3, 5.85, fill=RGBColor(0x1A, 0x5C, 0x2A), line=GOLD, line_w=Pt(1.5))
text_box(s, 4.3, 1.45, 4.1, 0.45,
         "EMAIL 5 — IMMEDIATE POST-SHOW",
         size=Pt(12), bold=True, color=GOLD)
rect(s, 4.2, 1.85, 4.3, 0.38, fill=GREEN)
text_box(s, 4.25, 1.88, 4.2, 0.32,
         "⏱ SLA: Within 1 HOUR of show end",
         size=Pt(10.5), bold=True, color=WHITE, align=PP_ALIGN.CENTER)

e5_vars = [
    ("Tier 1", "[SIGNATURE_BLOCK]"),
    ("Tier 2", "[GUEST_FIRST_NAME]"),
    ("Links", "[AI_CLIPS_DRIVE_LINK]"),
    ("", "[FULL_RECORDING_LINK]"),
    ("", "[TRANSCRIPT_LINK]"),
]
v5y = 2.35
for label, val in e5_vars:
    if label:
        text_box(s, 4.3, v5y, 0.9, 0.28, label + ":", size=Pt(8.5), bold=True, color=GOLD)
    text_box(s, 5.22, v5y, 3.15, 0.28, val, size=Pt(8.5), color=LIGHT)
    v5y += 0.3

text_box(s, 4.3, 3.55, 4.1, 0.32, "Content:", size=Pt(9), bold=True, color=GOLD)
e5_body = [
    "Hi [GUEST_FIRST_NAME],",
    "",
    "Thank you for joining us! Here are your assets:",
    "• AI clips (drive): [AI_CLIPS_DRIVE_LINK]",
    "• Full recording: [FULL_RECORDING_LINK]",
    "• Transcript: [TRANSCRIPT_LINK]",
    "",
    "Human-edited clips + podcast links coming soon.",
    "",
    "[SIGNATURE_BLOCK]",
]
e5y = 3.88
for line in e5_body:
    text_box(s, 4.3, e5y, 4.1, 0.27, line, size=Pt(8.5), color=LIGHT)
    e5y += 0.25

# Email 6 column
rect(s, 8.7, 1.4, 4.4, 5.85, fill=RGBColor(0x3A, 0x1A, 0x5A), line=GOLD, line_w=Pt(1.5))
text_box(s, 8.8, 1.45, 4.2, 0.45,
         "EMAIL 6 — ASSETS 24–36h",
         size=Pt(12), bold=True, color=GOLD)
rect(s, 8.7, 1.85, 4.4, 0.38, fill=RGBColor(0x9B, 0x59, 0xB6))
text_box(s, 8.75, 1.88, 4.3, 0.32,
         "⏱ SLA: 24–36h MAX after show",
         size=Pt(10.5), bold=True, color=WHITE, align=PP_ALIGN.CENTER)

e6_vars = [
    ("Tier 1", "[SHOW_NAME]  ·  [SIGNATURE_BLOCK]"),
    ("Tier 2", "[GUEST_FIRST_NAME]  ·  [EPISODE_TITLE]"),
    ("", "[SEGMENT_TITLE]"),
    ("Links", "[SPOTIFY_EPISODE_LINK]"),
    ("", "[APPLE_EPISODE_LINK]"),
    ("", "[HUMAN_EDITED_CLIPS_LINK]"),
    ("", "[LINKEDIN_EVENT_URL]"),
    ("", "[YOUTUBE_EVENT_URL]"),
]
v6y = 2.35
for label, val in e6_vars:
    if label:
        text_box(s, 8.8, v6y, 0.9, 0.28, label + ":", size=Pt(8.5), bold=True, color=GOLD)
    text_box(s, 9.72, v6y, 3.25, 0.28, val, size=Pt(8.5), color=LIGHT)
    v6y += 0.3

text_box(s, 8.8, 4.65, 4.2, 0.32, "Content:", size=Pt(9), bold=True, color=GOLD)
e6_body = [
    "Hi [GUEST_FIRST_NAME],",
    "",
    "Your edited assets are ready!",
    "• Human clips: [HUMAN_EDITED_CLIPS_LINK]",
    "• Spotify: [SPOTIFY_EPISODE_LINK]",
    "• Apple Podcasts: [APPLE_EPISODE_LINK]",
    "• LinkedIn replay: [LINKEDIN_EVENT_URL]",
    "• YouTube replay: [YOUTUBE_EVENT_URL]",
    "",
    "[SIGNATURE_BLOCK]",
]
e6y = 4.97
for line in e6_body:
    text_box(s, 8.8, e6y, 4.2, 0.27, line, size=Pt(8.5), color=LIGHT)
    e6y += 0.25


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 10 — GHL PIPELINE & AUTOMATION
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Go High Level — Guest Pipeline & Automation Workflows",
           "app.reveting.com · All guests tracked through 6-stage pipeline · 4 automation workflows")

# Pipeline stages
stages = [
    ("New Booking", MIDBLUE, "Booking arrives in GHL\nCheck daily"),
    ("Fit Check\nPending", RGBColor(0x7A, 0x5A, 0x0A), "LinkedIn check\nWaiting for decision"),
    ("Tier 2\nComplete", RGBColor(0x1A, 0x5C, 0x2A), "All variables filled\nTopics edited"),
    ("Event\nPublished", RGBColor(0x2A, 0x1A, 0x5C), "Calendar Stage 2\nEmail 1 sent"),
    ("Show\nComplete", RGBColor(0x5C, 0x2A, 0x1A), "Emails 5 & 6 sent\nAssets delivered"),
    ("Archived", RGBColor(0x2A, 0x2A, 0x2A), "All done\nRecord preserved"),
]

sx = 0.25
for title, col, desc in stages:
    rect(s, sx, 1.45, 2.05, 1.2, fill=col, line=GOLD, line_w=Pt(1))
    text_box(s, sx + 0.08, 1.5, 1.9, 0.52, title,
             size=Pt(10), bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    text_box(s, sx + 0.08, 2.0, 1.9, 0.6, desc,
             size=Pt(8), color=LIGHT, align=PP_ALIGN.CENTER)
    if sx < 12.0:
        text_box(s, sx + 2.06, 1.85, 0.15, 0.4, "→", size=Pt(16), bold=True, color=GOLD)
    sx += 2.2

# 4 Workflows
text_box(s, 0.2, 2.85, 13.0, 0.4, "AUTOMATION WORKFLOWS",
         size=Pt(13), bold=True, color=GOLD)

workflows = [
    ("Workflow 1\nGuest Confirmation", RGBColor(0x12, 0x2A, 0x5C), [
        "Trigger: Booking form submitted",
        "Action: Move to 'New Booking' stage",
        "Action: Send T-14 Activation email",
        "Action: Add 'new-booking' tag",
        "Action: Assign PA task: complete Tier 2",
    ]),
    ("Workflow 2\nShow-Day Reminders", RGBColor(0x1A, 0x3A, 0x5A), [
        "Trigger: Appointment date − 1 day",
        "Action: Send Email 3 (Day Before)",
        "Trigger: Appointment date − 4h",
        "Action: Send Email 4 (Day Of)",
        "Action: PA notification — pre-show prep",
    ]),
    ("Workflow 3\nPost-Show Delivery", RGBColor(0x1A, 0x5C, 0x2A), [
        "Trigger: Appointment completed",
        "Action: Move to 'Show Complete'",
        "Action: PA task — send Email 5 within 1h",
        "Action: Wait 24h",
        "Action: PA task — send Email 6 (max 36h)",
    ]),
    ("Workflow 4\nAudience Capture", RGBColor(0x4A, 0x1A, 0x5C), [
        "Trigger: LinkedIn Live comment / reaction",
        "Action: Add to Audience pipeline",
        "Action: Tag with show + episode number",
        "Action: Enroll in nurture if opted in",
        "Action: Log engagement source",
    ]),
]

wx = 0.2
for title, col, items in workflows:
    rect(s, wx, 3.3, 3.15, 3.95, fill=col, line=GOLD, line_w=Pt(1))
    rect(s, wx, 3.3, 3.15, 0.52, fill=RGBColor(
        min(col[0] + 25, 255),
        min(col[1] + 25, 255),
        min(col[2] + 25, 255)
    ))
    text_box(s, wx + 0.1, 3.33, 2.9, 0.48, title,
             size=Pt(10), bold=True, color=GOLD)
    iy = 3.88
    for item in items:
        text_box(s, wx + 0.1, iy, 2.95, 0.56, item, size=Pt(8.5), color=LIGHT)
        iy += 0.6
    wx += 3.3


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 11 — MASTER EMAIL SEQUENCE TIMELINE
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Master Email Sequence — Complete Timeline",
           "From booking to 36 hours post-show · 8 possible emails per guest")

# Timeline bar
rect(s, 0.3, 1.42, 12.73, 0.18, fill=GOLD)

emails = [
    ("NOT A\nFIT", "If fails\nfit gate", RED, 0.3),
    ("T-14\nACTIV.", "Day of\nbooking\n(or T-14)", RGBColor(0x7A, 0x5A, 0x0A), 1.65),
    ("EMAIL\n1", "Event\npublished", MIDBLUE, 3.3),
    ("EMAIL\n2", "T-7\ndays", RGBColor(0x1A, 0x5C, 0x2A), 5.1),
    ("EMAIL\n3", "Day\nbefore", RGBColor(0x2A, 0x1A, 0x5C), 6.8),
    ("EMAIL\n4", "Morning\nof show", RGBColor(0x5C, 0x2A, 0x1A), 8.4),
    ("EMAIL\n5", "Within\n1 hour", GREEN, 10.0),
    ("EMAIL\n6", "24–36h\nafter", RGBColor(0x4A, 0x1A, 0x5C), 11.7),
]

for label, timing, col, tx in emails:
    # dot on timeline
    circle = s.shapes.add_shape(
        9, Inches(tx + 0.55), Inches(1.33),
        Inches(0.22), Inches(0.22)
    )
    circle.fill.solid()
    circle.fill.fore_color.rgb = col
    circle.line.fill.background()

    rect(s, tx, 1.65, 1.25, 1.3, fill=col, line=WHITE, line_w=Pt(0.5))
    text_box(s, tx + 0.05, 1.7, 1.15, 0.7, label,
             size=Pt(10), bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    text_box(s, tx + 0.05, 2.38, 1.15, 0.5, timing,
             size=Pt(7.5), color=LIGHT, align=PP_ALIGN.CENTER)

# Content checklist below
text_box(s, 0.2, 3.15, 13.0, 0.38, "WHAT EACH EMAIL DELIVERS",
         size=Pt(12), bold=True, color=GOLD)

content_rows = [
    ("Not a Fit", "Polite decline · [SHOW_NAME] · [FALLBACK_SHOW_LINKS]", RED),
    ("T-14 Activation", "Booking confirmed · Connect on LinkedIn · Explain topic editing process", RGBColor(0xA0, 0x78, 0x20)),
    ("Email 1 — Appearance Details", "All episode details · Timing all 3 TZs · StreamYard link · All event URLs · LinkedIn invite walkthrough", MIDBLUE),
    ("Email 2 — One Week Out", "One-week reminder · LinkedIn event link · Invite connections walkthrough", RGBColor(0x1A, 0x5C, 0x2A)),
    ("Email 3 — Day Before", "Final prep · StreamYard link again · All timing · Past episodes link", RGBColor(0x2A, 0x1A, 0x5C)),
    ("Email 4 — Day Of", "Morning reminder · StreamYard link · Timing in all 3 TZs", RGBColor(0x5C, 0x2A, 0x1A)),
    ("Email 5 — Immediate Post-Show", "AI clips · Full recording · Transcript — within 1 HOUR of show end", GREEN),
    ("Email 6 — Assets 24–36h", "Human-edited clips · Podcast links · Replay URLs — max 36h SLA", RGBColor(0x4A, 0x1A, 0x5C)),
]

ry = 3.6
for name, desc, col in content_rows:
    rect(s, 0.2, ry, 13.1, 0.46, fill=RGBColor(
        min(col[0] + 20, 255) // 4 + col[0] // 2,
        min(col[1] + 20, 255) // 4 + col[1] // 2,
        min(col[2] + 20, 255) // 4 + col[2] // 2,
    ), line=col, line_w=Pt(0.5))
    text_box(s, 0.28, ry + 0.06, 2.4, 0.34, name,
             size=Pt(9), bold=True, color=GOLD)
    text_box(s, 2.75, ry + 0.06, 10.4, 0.34, desc,
             size=Pt(9), color=WHITE)
    ry += 0.5


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 12 — QUICK REFERENCE + COMMON PITFALLS
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Quick Reference — Rules, SLAs & Common Pitfalls",
           "Print and post. These are the non-negotiables.")

# SLAs
rect(s, 0.2, 1.4, 5.8, 5.85, fill=RGBColor(0x12, 0x2A, 0x5C), line=GOLD, line_w=Pt(1.5))
text_box(s, 0.3, 1.45, 5.5, 0.45, "HARD SLAs & RULES", size=Pt(13), bold=True, color=GOLD)

rules = [
    (GREEN, "✓", "Email 5: Within 1 HOUR of show end"),
    (GREEN, "✓", "Email 6: Max 36 HOURS after show"),
    (GREEN, "✓", "Calendar always set in Eastern Time (USA)"),
    (GREEN, "✓", "Topics edited BEFORE appearing in any email"),
    (GREEN, "✓", "Tier 2 complete BEFORE any email is sent"),
    (GREEN, "✓", "StreamYard link is FRESH per episode (never reuse)"),
    (GREEN, "✓", "Original booking submission preserved at bottom of calendar"),
    (GREEN, "✓", "Channel stack confirmed from Total Deliverables Doc"),
    (GREEN, "✓", "Check app.reveting.com DAILY — automations are unreliable"),
    (GOLD, "→", "5,000+ followers = proceed"),
    (GOLD, "→", "1,000–4,999 = confirm with Prod + Marketing Lead"),
    (RED, "✗", "Below 1,000 = NO-GO unless no other option"),
    (RED, "✗", "Never set calendar in guest's local timezone"),
    (RED, "✗", "Never send raw topics from booking form to guest"),
    (RED, "✗", "Never reuse StreamYard link from a prior episode"),
]

ry = 1.95
for col, sym, text in rules:
    text_box(s, 0.3, ry, 0.35, 0.3, sym, size=Pt(11), bold=True, color=col)
    text_box(s, 0.65, ry, 5.2, 0.32, text, size=Pt(9), color=WHITE)
    ry += 0.35

# Common Pitfalls
rect(s, 6.2, 1.4, 6.9, 5.85, fill=RGBColor(0x3A, 0x10, 0x10), line=RED, line_w=Pt(1.5))
text_box(s, 6.3, 1.45, 6.6, 0.45, "COMMON PITFALLS", size=Pt(13), bold=True, color=RED)

pitfalls = [
    ("Reusing the StreamYard guest link",
     "Each guest needs a fresh link. Reused links can break or admit the wrong person."),
    ("Calendar time in guest's local timezone",
     "All events MUST be in Eastern Time (USA). Most common error."),
    ("Skipping Tier 1 and winging it per episode",
     "Without locked show constants, variable errors compound. Do Tier 1 once, correctly."),
    ("Raw topics in Email 1",
     "Topics from booking form are self-promotional and misaligned. Always edit to fit show strategy."),
    ("Missing the Email 5 one-hour SLA",
     "Immediate post-show is peak engagement. Delay kills clip sharing momentum."),
    ("Removing original booking from calendar description",
     "The original submission is the audit trail. Keep it at the bottom — always."),
    ("Not checking app.reveting.com daily",
     "Automations fail silently. Manual daily check in Calendars → Appointment List View."),
]

py = 1.95
for title, body in pitfalls:
    rect(s, 6.3, py, 6.7, 0.76, fill=RGBColor(0x4A, 0x10, 0x10), line=RED, line_w=Pt(0.5))
    text_box(s, 6.38, py + 0.04, 6.5, 0.26, "✗  " + title,
             size=Pt(9.5), bold=True, color=RED)
    text_box(s, 6.38, py + 0.3, 6.5, 0.42, body, size=Pt(8.5), color=LIGHT)
    py += 0.82


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 13 — SKILL SYSTEM MAP
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide()
bg(s)
header_bar(s, "Reveting Skill System — Complete Map",
           "5 interconnected skills in the gtm-skills repository power the full Reveting production engine")

center_x, center_y = 6.67, 4.3
center_w, center_h = 2.4, 0.9

# Central hub
rect(s, center_x - center_w/2, center_y - center_h/2, center_w, center_h,
     fill=GOLD, line=WHITE, line_w=Pt(2))
text_box(s, center_x - center_w/2, center_y - 0.3, center_w, 0.6,
         "reveting-show-setup\n(MASTER VARIABLES)",
         size=Pt(9.5), bold=True, color=NAVY, align=PP_ALIGN.CENTER)

satellite_skills = [
    ("reveting-email-flows", "T-14 Activation\nEmails 1–6\nNot a Fit\n7 email templates",
     MIDBLUE, 1.8, 2.0),
    ("reveting-calendar-flows", "Show slot architecture\nGuest booking page\n6-touch reminder seq.\nNo-show recovery",
     RGBColor(0x1A, 0x5C, 0x2A), 9.8, 2.0),
    ("reveting-ghl-workflows", "Guest pipeline\n6-stage CRM\n4 automation workflows\nGHL custom fields",
     RGBColor(0x4A, 0x1A, 0x5C), 1.8, 6.1),
    ("reveting-streamyard-flows", "Brand scene library\nGuest invite flows\nMulti-destination live\nRecording handoff",
     RGBColor(0x5C, 0x2A, 0x1A), 9.8, 6.1),
]

skill_w, skill_h = 2.7, 1.6

for skill_name, desc, col, sx, sy in satellite_skills:
    rect(s, sx - skill_w/2, sy - skill_h/2, skill_w, skill_h,
         fill=col, line=GOLD, line_w=Pt(1.5))
    text_box(s, sx - skill_w/2 + 0.1, sy - skill_h/2 + 0.08, skill_w - 0.2, 0.38,
             skill_name, size=Pt(9.5), bold=True, color=GOLD)
    text_box(s, sx - skill_w/2 + 0.1, sy - skill_h/2 + 0.48, skill_w - 0.2, 1.0,
             desc, size=Pt(8.5), color=LIGHT)

text_box(s, 1.5, 7.05, 10.0, 0.38,
         "All 5 skills are in /skills/inbound/ in the gtm-skills repository · Load reveting-show-setup first to establish Tier 1 variables",
         size=Pt(9.5), color=GREY, align=PP_ALIGN.CENTER)


# ─────────────────────────────────────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────────────────────────────────────
out = "/home/user/gtm-skills/Reveting-Show-Flow.pptx"
prs.save(out)
print(f"Saved: {out}")
print(f"Slides: {len(prs.slides)}")
