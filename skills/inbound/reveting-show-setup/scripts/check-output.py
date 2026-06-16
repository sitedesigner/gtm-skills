#!/usr/bin/env python3
"""Validate Reveting show setup intake deliverables."""

import sys
from pathlib import Path

TIER1_TERMS = ['show_name', 'show_email', 'channel', 'signature', 'booking']
TIER2_TERMS = ['guest_first_name', 'episode_number', 'episode_title', 'golive_time', 'streamyard']
EMAIL_LOG = ['email send log', 'calendar description log']


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.exists():
        print("Usage: check-output.py path/to/deliverable.md")
        return 2

    text = path.read_text(encoding="utf-8", errors="replace").lower()
    if len(text.strip()) < 300:
        print("FAIL — deliverable too short (<300 chars)")
        return 1

    missing_t1 = [t for t in TIER1_TERMS if t not in text]
    if missing_t1:
        print("FAIL — missing Tier 1 variables:", ", ".join(missing_t1))
        return 1

    missing_t2 = [t for t in TIER2_TERMS if t not in text]
    if missing_t2:
        print("FAIL — missing Tier 2 variables:", ", ".join(missing_t2))
        return 1

    missing_log = [t for t in EMAIL_LOG if t not in text]
    if missing_log:
        print("FAIL — missing tracking section:", ", ".join(missing_log))
        return 1

    print("PASS — Reveting show setup intake meets minimum checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
