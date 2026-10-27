---
name: convercus-offer-builder
description: Prepare, review, and publish Convercus economic offers from MEDDICC, scope, and validated pricing outputs; use Compactor only as an isolated trial reference.
---

# Convercus Offer Builder

Use this skill when the user asks to prepare, revise, update, convert, or publish a Convercus economic offer or commercial proposal.

Start by locating the opportunity sources. Distinguish confirmed facts, assumptions, and open items before drafting or converting anything. If the request involves Compactor, treat it as that account only; never carry its prices, volumes, scope, technologies, or conditions into another account.

## Operating Boundaries

- Do not invent amounts, discounts, capacities, deadlines, scope, legal terms, assumptions, or commercial conditions.
- For pre-contractual effort, produce evidence-linked analyst estimates in hours; distinguish them from validated commercial prices and never derive hours from prices or historical customer figures.
- Use only final pricing or ROI outputs that the user identifies as validated for the current opportunity.
- Keep three decisions separate: Word generation succeeded, documentary review passed, and commercial approval was granted.
- Do not modify original client/reference documents. Work on copies inside the workspace or another user-approved output folder.
- Do not copy or fork the Markdown-to-DOCX converter. Use the existing converter configured in `assets/convercus_offer_builder.yaml`.
- Exclude internal costs, markup, negotiation strategy, and unresolved assumptions from client-ready outputs.
- Mark internal drafts as `INTERNAL` when they include internal commentary, unapproved economics, or pending controls.

## Workflow

1. Read `assets/convercus_offer_builder.yaml` and confirm paths exist.
2. For offer preparation, read `references/source-control.md` and build a source inventory with owner, date, status, and what each source can prove.
3. If the scope includes implementation, configuration, migration, or integrations, read `references/functional-effort-estimation.md` and prepare its internal effort estimate before pricing inputs. Keep the estimate separate from the client-facing proposal unless the user asks otherwise.
4. For economic content, read `references/commercial-review.md`. Stop or ask for missing validated pricing outputs instead of filling gaps; technical uncertainty may be recorded as a conditional risk without inventing a reserve.
5. For Word generation, read `references/word-publication.md`, then use the configured converter root and the `commercial_proposal` profile unless the user explicitly authorizes another profile. Prefer passing account resource paths at invocation time or via copied working files rather than relying on account-specific profiles.
6. For Compactor trial work, read `references/compactor-trial.md`. Use the trial documents only to inspect behavior and structure.
7. Before reporting completion, state separately: generation result, documentary review status, commercial approval status, checks run, and unresolved blockers.

## Language

- Use `fidelización` for processes and `lealtad` for the resulting condition.
- Use `vinculación` in Spanish.
- Distinguish accumulated points from monetary credits.
- Use `ganar` and `canjear`.
- Keep MEDDICC internal terminology in English.
- Draft in the client's language.

## Helper Script

Run `scripts/check_setup.py` from the skill directory when validating local setup. It checks the configured converter, profiles, templates, trial document names, and local skill structure without modifying source documents.
