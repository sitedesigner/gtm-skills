#!/usr/bin/env python3
"""
check-output.py — Post Engager Play deliverable validator.

Validates that agent output for the post-engager-play skill meets minimum
quality requirements before delivery. Run against the agent's markdown output.

Usage:
    python3 check-output.py <output_file.md>
    python3 check-output.py --text "..."
"""

import sys
import re


REQUIRED_SECTIONS = [
    "post qualification",
    "scrape",
    "filter",
    "enrichment",
    "message variant",
    "sequence",
]

MAX_TOUCH1_WORDS = 80

POST_REFERENCE_PATTERNS = [
    r"saw you (liked|commented|shared)",
    r"noticed you (liked|commented|engaged|shared)",
    r"your comment on",
    r"saw your (comment|reply|post)",
    r"saw some discussion",
    r"post (on|about|regarding)",
]

PITCH_PATTERNS = [
    r"would you be interested",
    r"can i show you",
    r"do you have (15|30|[0-9]+) minutes",
    r"i'd love to (schedule|set up|book)",
    r"check out our",
    r"our product",
    r"our platform",
    r"our solution",
    r"click here",
    r"book a (call|demo|meeting)",
]

CURRENT_STATE_PATTERNS = [
    r"how are you (currently|today)",
    r"how (do|are) you (handle|managing|approaching|thinking)",
    r"what('s| is) your current",
    r"what does your (current|existing)",
    r"curious (how|what|about)",
]


def check_output(text: str) -> list[dict]:
    findings = []
    text_lower = text.lower()

    # Check required sections
    missing = [s for s in REQUIRED_SECTIONS if s not in text_lower]
    if missing:
        findings.append({
            "level": "ERROR",
            "check": "Required sections",
            "detail": f"Missing sections: {', '.join(missing)}",
        })
    else:
        findings.append({
            "level": "PASS",
            "check": "Required sections",
            "detail": "All required sections present",
        })

    # Check post reference in message variants
    variant_block = re.search(
        r"(variant|message|touch 1|subject:).{0,2000}",
        text_lower,
        re.DOTALL,
    )
    if variant_block:
        variant_text = variant_block.group(0)
        has_reference = any(
            re.search(p, variant_text) for p in POST_REFERENCE_PATTERNS
        )
        if has_reference:
            findings.append({
                "level": "PASS",
                "check": "Post reference in message",
                "detail": "Touch 1 opener references the post or engagement",
            })
        else:
            findings.append({
                "level": "ERROR",
                "check": "Post reference in message",
                "detail": (
                    "No detectable post reference in message variant. "
                    "Touch 1 must reference the specific post or commenter's words."
                ),
            })

    # Check for pitch patterns in Touch 1
    if variant_block:
        variant_text = variant_block.group(0)
        pitch_hits = [p for p in PITCH_PATTERNS if re.search(p, variant_text)]
        if pitch_hits:
            findings.append({
                "level": "WARN",
                "check": "No pitch in Touch 1",
                "detail": (
                    f"Possible pitch language detected: {pitch_hits}. "
                    "Touch 1 should be a discovery question, not a pitch."
                ),
            })
        else:
            findings.append({
                "level": "PASS",
                "check": "No pitch in Touch 1",
                "detail": "No pitch language detected in message variants",
            })

    # Check for Current-State question
    if variant_block:
        variant_text = variant_block.group(0)
        has_cs_q = any(
            re.search(p, variant_text) for p in CURRENT_STATE_PATTERNS
        )
        if has_cs_q:
            findings.append({
                "level": "PASS",
                "check": "Current-State question",
                "detail": "Discovery question detected in message variant",
            })
        else:
            findings.append({
                "level": "WARN",
                "check": "Current-State question",
                "detail": (
                    "No Current-State question pattern detected. "
                    "Touch 1 should end with 'How are you currently...' or similar."
                ),
            })

    # Check touch count (should be 4 max)
    touch_mentions = re.findall(r"\btouch\s*[1-9]\b", text_lower)
    max_touch = 0
    for t in touch_mentions:
        n = re.search(r"[1-9]", t)
        if n:
            max_touch = max(max_touch, int(n.group()))
    if max_touch > 4:
        findings.append({
            "level": "WARN",
            "check": "Touch count",
            "detail": (
                f"Sequence references Touch {max_touch}. "
                "Post-engager plays should cap at 4 touches (short signal window)."
            ),
        })
    elif max_touch > 0:
        findings.append({
            "level": "PASS",
            "check": "Touch count",
            "detail": f"Sequence uses {max_touch} touches (within 4-touch cap)",
        })

    # Check ICP filter mention
    if re.search(r"icp.{0,20}filter|filter.{0,20}icp", text_lower):
        findings.append({
            "level": "PASS",
            "check": "ICP filter step",
            "detail": "ICP filter step present in output",
        })
    else:
        findings.append({
            "level": "ERROR",
            "check": "ICP filter step",
            "detail": "ICP filter step not found. Filter must run before enrichment.",
        })

    # Check email verification mention
    if re.search(r"(email.{0,20}verif|verif.{0,20}email|neverb|valid status)", text_lower):
        findings.append({
            "level": "PASS",
            "check": "Email verification",
            "detail": "Email verification step referenced",
        })
    else:
        findings.append({
            "level": "WARN",
            "check": "Email verification",
            "detail": "No email verification step detected. Verify emails before sequencer push.",
        })

    # Check source tag / CRM tracking
    if re.search(r"(source.{0,20}tag|post.engager|crm.{0,20}track)", text_lower):
        findings.append({
            "level": "PASS",
            "check": "CRM source tracking",
            "detail": "Source tracking / CRM tag referenced",
        })
    else:
        findings.append({
            "level": "WARN",
            "check": "CRM source tracking",
            "detail": "No source tag or CRM tracking setup found.",
        })

    return findings


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check-output.py <output_file.md>")
        sys.exit(1)

    flag = sys.argv[1]
    if flag == "--text" and len(sys.argv) >= 3:
        text = sys.argv[2]
    else:
        with open(sys.argv[1], "r") as f:
            text = f.read()

    findings = check_output(text)

    errors = [f for f in findings if f["level"] == "ERROR"]
    warnings = [f for f in findings if f["level"] == "WARN"]
    passes = [f for f in findings if f["level"] == "PASS"]

    print(f"\nPost Engager Play — Output Quality Check")
    print(f"{'=' * 48}")
    print(f"  PASS   : {len(passes)}")
    print(f"  WARN   : {len(warnings)}")
    print(f"  ERROR  : {len(errors)}")
    print()

    for f in findings:
        icon = {"PASS": "✓", "WARN": "⚠", "ERROR": "✗"}.get(f["level"], "?")
        print(f"  {icon} [{f['level']}] {f['check']}")
        if f["level"] != "PASS":
            print(f"         {f['detail']}")

    print()
    if errors:
        print("Result: FAIL — fix errors before delivering to user.")
        sys.exit(1)
    elif warnings:
        print("Result: PASS WITH WARNINGS — review warnings before delivery.")
    else:
        print("Result: PASS — output meets post-engager-play quality bar.")


if __name__ == "__main__":
    main()
