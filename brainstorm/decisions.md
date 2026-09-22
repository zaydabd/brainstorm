# Decision log

Format: `ID | WHO | TYPE | DATE | DECISION | Reason: ... | Affects: ...`

- DEC-001 | HUMAN | -- | 2026-09-22 | Adopted brainstorm Phase 1 | Reason: documents need staged gates | Affects: all stages
- DEC-002 | HUMAN | -- | 2026-09-22 | British spelling throughout; initializing-project renamed to initialising-project, artifact to artefact | Reason: operator chose all-British over keeping the two American exceptions | Affects: CLAUDE.md, all artefacts, skills/initialising-project
- DEC-003 | HUMAN | -- | 2026-09-22 | The handoff reader is a Claude design session starting cold | Reason: operator selection at stage 0 | Affects: HANDOFF.md, handoff language rules
- DEC-004 | HUMAN | -- | 2026-09-22 | The operator is the only role the glossary defines | Reason: operator deselected Claude, design phase and checker as roles | Affects: CLAUDE.md roles table
- DEC-005 | HUMAN | -- | 2026-09-22 | Phase 1 subject deferred; stage 1 will name it | Reason: operator said the handover subject is not needed now | Affects: proposal.md, glossary domain terms
- DEC-006 | AUTO  | --  | 2026-09-22 | hooks/validate-artifact keeps its American file name | Reason: the name is a path resolved by hooks.json, and CLAUDE.md exempts code identifiers | Affects: hooks/hooks.json
- DEC-007 | AUTO  | --  | 2026-09-22 | The glossary binds artefacts under brainstorm/, not the plugin's own skill and hook files | Reason: those files are instructions and code, so "the human" stays in them | Affects: all stages
- DEC-008 | AUTO  | --  | 2026-09-22 | Design phase and checker are defined as glossary terms though not as roles | Reason: a cold handoff reader needs both nouns defined | Affects: CLAUDE.md glossary
