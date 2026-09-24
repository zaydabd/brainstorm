# Next session: project substance interview

Hand this to a fresh session. It carries everything the interview needs, because the
source uploads (CV, LinkedIn exports, logo archives) do not survive a new session.

**Task for the next session:** run a round-based grilling interview on the substance
of Wan Zayd's three main projects, then write those three project explanations.
Do not re-open the scope decisions below — they are settled.

- Proposal: `portfolio-proposal.md` in this repo
- Live doc: https://claude.ai/code/artifact/2dd92bf4-ee62-42cb-9b40-d88826dcf1c9
- Interview method: the `ihaveanidea` skill's round format. Ask the whole frontier
  in one round, number each question, give a recommended answer, then wait.
- Use plain markdown questions, not multiple choice. Content answers need prose.

---

## Settled — do not re-litigate

| Decision | Settled as |
|---|---|
| What it is | One page, under 14 KB compressed, hosted free on GitHub |
| Purpose | Wan Zayd owns no document of his own showing his work |
| Not the purpose | Job-seeking, audience building, social media presence |
| The claim | The work proves the engineering; the site itself proves the taste |
| Audience | Hiring managers, other technical leads, people who notice design |
| Title | "OutSystems Technical Lead" throughout; "Senior Technical Lead" on iZone only |
| Three main projects | Digital Form, MyInsights, iZone rebuild |
| Format | "Semi-detailed explanation of the project", NOT a formal case study |
| Short index | 8 items, name + one line each |
| Also on the site | About, how I work, timeline, certifications, contact, CV download |
| Excluded | Blog, custom domain, backend, music/session work, artistic direction |
| Excluded claims | React, AWS, .NET/C# — he will not defend these |
| Confidentiality | He publishes client detail freely. His call, against advice. Do not raise again. |
| 14 KB | A target, not a hard limit |
| Logos | Five vector marks only; organisations without one appear in type |
| Staleness | No dated content anywhere |
| Artistic direction | Out of scope. He is building a separate design skill for it. |

Design references he mentioned for that later session: album art, minimalist movie
posters, bento layouts.

---

## Verified facts

### Career timeline (from LinkedIn — authoritative over the CV)

| Period | Organisation | Role |
|---|---|---|
| Jan 2026 – present | AvePoint, full-time, KL | Full Stack Developer / Technical Lead |
| Apr 2026 – present | └ Sunway University (client) | Senior Technical Lead, iZone rebuild |
| Sep 2024 – Jan 2026 | Maybank | Senior OutSystems Engineer (his preferred wording) |
| May 2024 – Jul 2024 | Adam Digital Assets, part-time, remote | Flutter Developer |
| Sep 2022 – Sep 2024 | FPT Software Malaysia, contract | incl. PETRONAS Digital placement |
| Apr 2022 – Aug 2022 | Career break | "Personal goal pursuit" |
| Apr 2021 – May 2022 | Impact Business Solutions Sdn Bhd, contract | |

No gaps. The CV's vague year ranges made it look otherwise; that was wrong.

### Stack he will defend under questioning

OutSystems (O11 and ODC) · SQL / Aurora PostgreSQL · REST APIs and integration ·
architecture practice (C4 diagrams, technical design documents, system design).

Flutter: under one year, he does not call himself knowledgeable. Open question
whether it appears with that qualifier or not at all.

### Qualifications

OutSystems Associate Developer Specialist (O11) · OutSystems Associate Technical
Lead (O11) · Professional Scrum Developer · BSc Information Systems (Intelligent
Systems Engineering), UiTM, 2019–2021 · Diploma Computer Science, UiTM, 2015–2019.

### Logo assets, measured with gzip -9

| Organisation | Compact mark | Full wordmark |
|---|---|---|
| Petronas | 474 B | 1,530 B |
| OutSystems | 791 B | 3,107 B |
| FPT Software | 1,142 B | not supplied |
| AvePoint | 1,923 B | not supplied |
| Maybank | 1,937 B | 3,416 B |
| Sunway Education / Group | no vector file | 10,824 B / 3,899 B raster |
| Impact Business Solutions Sdn Bhd | no vector file | PNG only |
| Adam Digital Assets | nothing supplied | nothing supplied |

Five compact marks total 6,267 B. Prose, markup and stylesheet estimated at
5–6 KB compressed, unvalidated.

---

## What is known about each project, and what is missing

### 1. iZone rebuild — AvePoint, at Sunway University (current)

**Known.** Remake of a legacy student portal on OutSystems ODC. He owns the
architecture: headless services, integration libraries, single sign-on, a private
gateway. The database schema comes from the legacy application. He designed the
concurrency model for simultaneous student enrollment. Integrations with the iZone
API and cloud storage, including batch synchronisation with audit logging.
Responsive front-end and progressive web app work. C4 diagrams and technical design
documents. Delivery managed on Jira, feature scoping with the business analyst team,
load testing planned. He leads three developers inside a project team of ten or more.

**Missing — these questions were asked and never answered:**
1. What was actually wrong with the old iZone? Why rebuild rather than improve?
   What did students and staff experience?
2. The concurrency problem in detail. How many students at once, over what window?
   What broke or would have broken? What did he actually do — row locking, queueing,
   optimistic concurrency? What did he try that failed?
3. The on-premise integration and SSO. What must stay on-premise and why? What did
   the private gateway solve that a direct connection could not? What was rejected?
4. The hardest call he made and what it cost. What went wrong on this project?
5. What "leading three developers in a 10+ team" means day to day. Who are the
   others? Which decisions are his, and which must he win from someone else?

### 2. MyInsights — FPT Software, for PETRONAS

**Known, and it is thin.** Automated detection of exceptions and anomalies for the
auditors department, across digitalised departmental data (Finance, Assets,
Maintenance, Procurement). Pushes millions of records through audit rules. Built a
user management system where each module carries different business rules per user.
Built front-end screens for the auditing module, implementing designs from Figma
with UI/UX designers. Business rule logic to client requirements.

**Critical:** the CV claimed he "turned it from a monolithic module into a
decentralized system." **Wan Zayd marked this as wrong.** That claim is removed and
he has not yet said what is correct. This project currently has the least substance
of the three and needs the most interview time.

### 3. Digital Form — Maybank

**Known.** A standalone form builder platform integrated with Maybank applications.
He was Technical Lead and Product Owner, defining the roadmap, integration strategy
and requirements. A core component of the Dynamic Workflow Builder. Connects GSAM,
HRIS, MStatus and MPowered. Handles dynamic forms and SLA tracking. Has run through
five MVP cycles and is on its fifth iteration.

**Missing.** What existed before it. Why five cycles — what changed each time, and
what did cycle one get wrong. Who uses it and how many forms exist. The hardest
integration. What he would design differently.

### Short index — 8 items, one line each

| Item | What is known |
|---|---|
| CAB-Q | Maybank deployment approval tool. Cut a daily process from 6 hours to 30 minutes. His only quantified outcome. |
| Audit Log | Maybank. Standardised audit logging adopted across every OutSystems application. |
| Tokenizer | Maybank. Tokenisation for public display strings, with an encrypted database. |
| MPowered | Maybank internal agile project management platform. Stability and defect work. |
| RPSST | Maybank. Prototype to modernise legacy RBS transaction processes. |
| VIP Dashboard | Impact. Power BI and QGIS visualisations of Sarawak data for VIP presentation. |
| QR Asset Management | Impact. QR-based asset tracking, Flutter with a Firebase backend. |
| Adam Digital Assets | Islamic mosque signage app in Flutter, plus a website twin. Two developers; he shared requirements, design and build. |

---

## Remaining open questions

1. **MyInsights** — what the work actually was. Blocking.
2. **Flutter** — appears with an honest "under one year" qualifier, or not at all.
3. **Page weight** — build it, measure it, report against the 14 KB target.
4. **Project write-up contents** — beyond problem, decision, trade-off. This is
   what the next session's interview settles.

## Environment notes

This sandbox's network proxy blocks general web domains, including github.io,
linkedin.com and impact-multimedia.com. Package registries and GitHub API access
work. Anything from the open web must be uploaded by Wan Zayd.
