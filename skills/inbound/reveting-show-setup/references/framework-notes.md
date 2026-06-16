# Reveting Show Setup — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations — not as decoration.

## Primary Frameworks

- **Jessie Lizak (Reveting) — LinkedIn Live & livestream content engine**
- **Go High Level — official automation documentation (help.gohighlevel.com)**

## Deep-dive references

| File | Authority | Use when |
|---|---|---|
| `references/reveting-show-variables.md` | Reveting SOP + GHL platform docs | Full variable definitions, email trigger map, calendar description templates |

## Templates

- `templates/output-template.md` — Master intake form (Tier 1 + Tier 2 + checklists)

## Agent routing

| Question | Action |
|---|---|
| New show launch | Complete Tier 1 in `templates/output-template.md` |
| New episode | Complete Tier 2 in `templates/output-template.md` |
| Which variables does Email 3 need? | Load `references/reveting-show-variables.md` → Email Trigger Checklist |
| Calendar description content | Load `references/reveting-show-variables.md` → Calendar Description section |
| Validate completed intake | Run `scripts/check-output.py` |
| Full email copy | Load `reveting-email-flows` |
| GHL field mapping | Load `reveting-ghl-workflows` |

Before final output, cite which framework shaped the recommendation.
