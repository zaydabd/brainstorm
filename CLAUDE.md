# CLAUDE.md

Domain vocabulary and document conventions for this project.

## Scope of this file

These rules govern the artefacts under `brainstorm/`: the proposal, the specs and the
handoff. The plugin's own skill files, hooks and scripts are instructions and code, not
artefacts, so they are not bound by the glossary.

The subject of Phase 1 is not chosen yet. This glossary therefore holds the workflow
vocabulary only. Stage 1 adds the product's domain terms once the proposal names them.

## Glossary

One term, one definition, one spelling.

| Term | Definition |
|------|------------|
| artefact | A document this workflow produces and gates: the proposal, a spec, or the handoff. |
| brainstorm | Phase 1 of delivery. An idea becomes approved documents. |
| business rule | A constraint on behaviour, carrying the ID `R-###`, defined in a spec. |
| change delta | A record of a change to an approved artefact, held in `brainstorm/changes/<name>/delta.md`. |
| checker | `scripts/check.py`, and the PostToolUse hook that runs it after every write to an artefact. |
| decision log | `brainstorm/decisions.md`. Append only. Holds every HUMAN and AUTO decision. |
| design phase | Phase 2. It happens outside this workflow and reads only the handoff. |
| gate | A condition an artefact must meet before its stage completes. |
| goal | A measurable outcome, carrying the ID `G-###`, defined in the proposal. |
| handoff | `brainstorm/HANDOFF.md`. The single document the design phase consumes. |
| non-functional requirement | A quality constraint, carrying the ID `NFR-###`, defined in the proposal. |
| operator | The person who runs the workflow and makes decisions D1 to D4. |
| proposal | `brainstorm/proposal.md`. The scope document every later stage reads. |
| scenario | An observable example of a rule, carrying the ID `SC-###`, written as GIVEN, WHEN, THEN. |
| spec | `brainstorm/specs/US-###.md`. The behaviour contract for one story. |
| stage | One numbered step of the workflow, 0 to 3. |
| status | `brainstorm/status.json`. The source of truth for what runs next. |
| story | A unit of user-visible value, carrying the ID `US-###`, listed in the proposal. |
| unit | The one piece of work a single `/brainstorm:next` invocation completes. |

## Roles

| Role | Does |
|------|------|
| operator | Runs `/brainstorm:next`. Decides D1 to D4. Answers every question a stage raises. |

## Conventions

- **Spelling: British.** `behaviour`, `prioritise`, `initialise`, `artefact`, `recognise`.
- **One exception**, because it is a file path the hook configuration resolves:
  `hooks/validate-artifact`. The file name keeps its American spelling. Its prose does not.
- **Dates**: `YYYY-MM-DD`.
- **IDs**: as `skills/using-brainstorm/references/conventions.md` defines them. Unique
  across the project, never renumbered.
- **The handoff** obeys the ASD-STE100 subset in
  `skills/using-brainstorm/references/handoff-language.md`. Its reader is a Claude design
  session starting cold, with no context beyond the handoff itself. Every term the handoff
  uses is defined here or in the handoff.
- Code spans, quoted values, IDs and product names are never rewritten by a language pass.

## Forbidden terms

| Do not write | Write |
|--------------|-------|
| artifact | artefact |
| initializing | initialising |
| behavior | behaviour |
| prioritize | prioritise |
| acceptance criteria | scenario |
| the human | operator |

## brainstorm

This project runs Phase 1 of the brainstorm workflow: idea to approved documents.
Follow the `brainstorm:using-brainstorm` skill. Artefacts live in `brainstorm/`.
A change to an approved artefact goes in `brainstorm/changes/<name>/delta.md`.
Design and UI happen in a separate phase that consumes `brainstorm/HANDOFF.md`.
