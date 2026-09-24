# Developer portfolio: details

Sep 23, 2026 · @Someone

Source: Developer portfolio proposal and next-session-brief.md. Details from: an interview with Wan Zayd Abdullah on 23 September 2026, and the verified facts in the brief.

## Summary

Wan Zayd Abdullah is an OutSystems Technical Lead with five years of experience. This proposal describes a single-page website that presents his work to hiring managers, to other technical leads, and to people who notice design. The site carries three projects, an account of how he works, and his career history. Wan Zayd aims to keep it under 14 kilobytes compressed, so it loads quickly on a 3G connection. Once the site exists, Wan Zayd owns a document that describes him in his own voice.

## The problem

Wan Zayd owns no document of his own that shows his work. The document that represents him today belongs to AvePoint, his employer. AvePoint sends it to clients as a staffing profile, and it describes his responsibilities in the third person. It has no place for taste, voice or craft. He wants to be known for front-end work and design judgment, and that document can show neither.

A reader outside the low-code world cannot calibrate his experience. The word "OutSystems" carries little meaning to that reader. They see five years and the title OutSystems Technical Lead, and they cannot judge the distance between those two facts. The AvePoint document gives them nothing else to work from.

## What this would do

The site makes one argument in two parts. The written work proves the engineering. The site itself proves the taste, because Wan Zayd builds it and no image stands in for it.

- A reader can follow how Wan Zayd designs a system, through three Main Projects. Each one explains the problem, his decision, the trade-off, his role and team, the outcome and the tools.
- A reader who does not know OutSystems can judge his engineering from the decisions described, rather than from the platform name.
- A reader can learn how he makes architecture calls and how he runs a team.
- A reader can see the range of his work, through a less highlighted list of eight Minor Projects.
- A reader can follow his career across five years and five employers.
- A reader can check his qualifications against three named certifications and two named degrees.
- A reader can reach him by email or on LinkedIn, and can download a CV that he wrote himself.
- A reader judges his front-end taste from the page in front of them, because the site carries no photograph and no screenshot.
- A reader on a slow connection receives a page small enough to load without waiting.

The three Main Projects are Digital Form, MyInsights and the iZone rebuild. Each one gets a semi-detailed explanation rather than a formal case study. Digital Form has run through five MVP cycles. It connects four systems, which are GSAM, HRIS, MStatus and MPowered, and it handles dynamic forms and SLA tracking. MyInsights pushes millions of records through audit rules for Petronas. The iZone rebuild remakes a legacy student portal at Sunway University, where he holds the title Senior Technical Lead.

Wan Zayd owns the iZone architecture, which covers headless services, integration libraries, single sign-on and a private gateway. The database schema comes from the legacy application. He designed the concurrency model for simultaneous student enrollment. He leads three developers inside a project team of ten or more.

The Minor Projects are CAB-Q, Audit Log, Tokenizer, MPowered, RPSST, VIP Dashboard, QR Asset Management and the Adam Digital Assets work. Each one gets its name, one line, its employer and its tools. CAB-Q cut a daily approval process from 6 hours to 30 minutes, and that line records it. The Adam Digital Assets line records an Islamic mosque signage application, built in Flutter with a matching website.

Each project names its tools, and each timeline entry shows the tools of its projects. Together they name the technologies Wan Zayd will defend under questioning. These are OutSystems in both O11 and ODC, SQL and Aurora PostgreSQL, REST APIs and integration work, and architecture practice. Architecture practice covers C4 diagrams, technical design documents and system design.

## What it leaves out

- Artistic direction: Wan Zayd will run a separate design session for it, and he plans to build a skill for that purpose. No colour, type or layout decision belongs in this document.
- Audience building and social reach: Wan Zayd wants a portfolio, not a presence on social media. The site does not exist to grow a following.
- Written pieces or a blog: he does not want one. Writing is a continuing commitment rather than a build, and he can add it later without rebuilding anything.
- A custom domain: GitHub hosting costs nothing, and he chose to spend nothing. Without a domain his name is harder to find in a search engine.
- Any server, form or database: an email address and a LinkedIn link do the same job. Nothing can break, and nothing costs money to run.
- Music and session work: he chose to keep the site strictly professional.
- The Maybank design-ownership account: his LinkedIn profile describes how he raised the design baseline for a team with no designer. I recommended it as evidence of design judgment, and he chose to leave it out.
- Claims about React, AWS and .NET/C#: these appear on his LinkedIn profile, and he will not defend them in an interview.
- A separate stack list: the tools appear on each project and each timeline entry instead.
- Flutter as a claimed skill: Flutter appears only as a tool of a Minor Project.
- Web fonts and photographs: each one costs more than the page can afford. Wan Zayd keeps them out as a discipline, so the typography carries the design.
- CAB-Q as a Main Project: he chose three, so CAB-Q appears in the list of Minor Projects instead.
- Relative time words and "last updated" stamps: undated content cannot look abandoned.

## Constraints and risks

No date drives this work. Wan Zayd treats it as a continuing personal project, so the build can run in stages.

The site must fit on one page. Wan Zayd aims to keep the whole page under 14 kilobytes compressed, and he treats that figure as a target rather than a limit. The prose, the markup and the stylesheet together come to about 5 to 6 kilobytes compressed, on my estimate. I have not validated that estimate against a built page.

Wan Zayd wants a mark for each organisation in his record. I measured the files he sent, compressed with gzip.

| Organisation | Compact mark | Full wordmark |
| --- | --- | --- |
| Petronas | 474 B | 1,530 B |
| OutSystems | 791 B | 3,107 B |
| FPT Software | 1,142 B | not supplied |
| AvePoint | 1,923 B | not supplied |
| Maybank | 1,937 B | 3,416 B |
| Sunway Education | no vector file | 10,824 B raster |
| Sunway Group | no vector file | 3,899 B raster |
| Impact Business Solutions Sdn Bhd | no vector file | PNG only |
| Adam Digital Assets | nothing supplied | nothing supplied |

Five compact marks together cost 6,267 bytes. A raster image does not compress further. Wan Zayd decided that a mark is optional. The site carries the five vector marks, and the four organisations with no vector file appear in type. A reader can see which companies carry a mark, and he accepted that.

The site runs on GitHub, which hosts it at no cost. Everything on the site is public, and the traffic a personal portfolio receives places no meaningful load on that hosting. If GitHub is slow or unavailable, the site is unreachable and no fallback exists. Wan Zayd accepts that, because the alternative costs money and the site carries nothing urgent. The site uses JavaScript only where CSS cannot do the work. A reader whose connection drops during loading still sees readable content.

Wan Zayd decided to publish client detail from Maybank, Petronas, Sunway University and Sarawak without restriction. I advised against this and he overruled me, so it is recorded here as his decision.

Wan Zayd decided that marks appear with employers and clients, including Petronas. A displayed client mark can imply that the client endorses him. That risk stays recorded here, and it is his call.

The site carries no relative time words, which removes the main risk for a project with no maintenance commitment. Timeline periods carry month and year, and the latest one reads "present". If he changes employer and does not update the page, that entry becomes wrong.

## Assumptions

- I assume each Main Project explanation runs to roughly 1,500 characters, which is the basis of the 5 to 6 kilobyte estimate above.
- I assume the five vector marks appear at their compact size rather than as full wordmarks. The compact files cost less than half as much.
- I assume the downloadable CV is a separate file, so its size sits outside the 14 kilobyte page budget.
- I assume Wan Zayd writes the words and directs every design decision, and that I implement.

## Changes from the proposal

- Main Project contents: the proposal named problem, decision and trade-off. Each Main Project now also carries role and team, outcome and tools. This settles the proposal's open question on contents.
- Short index: the proposal called it an index of eight items. It is now a less highlighted list of Minor Projects. Wan Zayd rejected a special name for either list.
- Minor Project contents: the proposal gave name and one line. Each Minor Project now also carries its employer and its tools, and tools are required.
- Stack: the proposal named the technologies once. Tools now appear on each project, and each timeline entry derives its tools from its projects. No separate stack list exists.
- Flutter: the proposal left it open. Flutter appears only as a tool of a Minor Project, never as a claimed skill.
- Dated content: the proposal banned it everywhere. Timeline periods now carry month and year, and the current entry reads "present". The ban covers relative time words and "last updated" stamps.
- Career break: the proposal assumed it appears. Wan Zayd confirmed it as its own timeline entry, so the assumption moved into the details.
- Marks: the proposal carried five marks with the trademark point unresolved. Marks now appear wherever an employer or client is named, and a tool mark sits with its employer. Wan Zayd decided this.
- About and How I work: Wan Zayd writes both himself. How I work is one short paragraph.

## Glossary

**Main Project**: One of the three projects the site explains in detail: Digital Form, MyInsights and the iZone rebuild. *Avoid*: case study, feature, project explanation

**Minor Project**: One of eight projects in a less highlighted list, each with a name and one line. *Avoid*: index entry, short index

**Timeline Entry**: One period in Wan Zayd's career: an employer, a client nested under it, or the career break. *Avoid*: engagement, project

**Employer**: The organisation that employed or contracted Wan Zayd, for example AvePoint or FPT Software.

**Client**: The organisation an employer placed Wan Zayd at, for example Sunway University or PETRONAS Digital.

**Tools**: The technologies used on a project, or at an employer through its projects. *Avoid*: stack

**Outcome**: What changed after a Main Project, stated without time words.

**Mark**: The compact vector logo of an employer, a client or a tool. *Avoid*: logo, trademark

**Qualification**: A certification or a degree. *Avoid*: award

## Items

This is a solo project, so no item has an owner line. Wan Zayd supplies every value.

### Main Project

A project the site explains in detail. Three exist.

| Field | Meaning | Format | Required | Allowed values | Example | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Name | The project name | text | yes | any | iZone rebuild | Wan Zayd |
| Employer | The employer he did the work for | text | yes | an employer on the timeline | AvePoint | timeline |
| Client | The client the work was for | text | no | a client on the timeline | Sunway University | timeline |
| Role and team | His title, what he owned, and the team size | text | yes | any; title follows rule 4 | Technical Lead, Product Owner and sole developer | Wan Zayd |
| Problem | What was wrong before the project | text | yes | any | The old portal crashed at every enrolment peak | Wan Zayd |
| Decision | His key design choice | text | yes | any | Row locking with SELECT FOR UPDATE | Wan Zayd |
| Trade-off | What the decision cost | text | yes | any | More complexity with each new question type | Wan Zayd |
| Outcome | What changed afterwards | text | yes | no time words (rule 9) | Deployed to live, not yet in use | Wan Zayd |
| Tools | Technologies used on the project | list | yes | defensible only (rule 3) | OutSystems O11 | Wan Zayd |

**Content from the interview**:

| Field | Digital Form | MyInsights | iZone rebuild |
| --- | --- | --- | --- |
| Employer | Maybank | FPT Software | AvePoint |
| Client | none | PETRONAS | Sunway University |
| Role and team | Technical Lead, Product Owner and sole developer | OutSystems developer in a team of four; not the lead. Built user management, permissions, front-end screens, part of the audit rule logic and part of the data sync. Worked on almost every area except email. | Senior Technical Lead and architecture owner. Two OutSystems developers of junior and mid level, so he also develops. |
| Problem | No internal form platform existed. A vendor built forms, but no confidential item was allowed in them. | Auditors checked exceptions manually, on files and paper. | The legacy portal did not scale and crashed at every enrolment peak. The interface was old, and the client wanted it modernised. The old system counted submissions before commit, which fails under concurrency. |
| Decision | Extensible question types, so each MVP cycle added types and features and stabilised the platform. | A fixed set of roles, each tied to its business rules. | Row locking with SELECT FOR UPDATE on Aurora PostgreSQL for enrolment. He kept the legacy database structure as a local replica. |
| Trade-off | Each new question type added complexity. | Low cost, in his account. | The replica was not well optimised. With a thin team, he developed as well as led, and he was stretched hard. |
| Outcome | Used across Maybank. Over 80 forms by the fifth MVP, with thousands of submissions and users. | Auditors centralised audit exceptions and processed them in the system, not on files and paper. | Deployed to live, not yet in use. Load-tested at 40,000 enrolments over a sustained 20-minute window. |
| Tools | OutSystems O11 | OutSystems O11 | OutSystems ODC, Aurora PostgreSQL, Microsoft single sign-on, private gateway |

**States**: No states.

**Rules**: 1, 3, 4, 5, 6, 9, 11

### Minor Project

A project in the less highlighted list. Eight exist.

| Field | Meaning | Format | Required | Allowed values | Example | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Name | The project name | text | yes | any | CAB-Q | Wan Zayd |
| One line | What it is or what it achieved | text | yes | one sentence | Cut a daily process from 6 hours to 30 minutes | brief |
| Employer | The employer he did the work for | text | yes | an employer on the timeline | Maybank | brief |
| Tools | Technologies used | list | yes | defensible only (rule 3) | Flutter, Firebase | Wan Zayd |

**Content from the interview and the brief**:

| Name | One line | Employer | Tools |
| --- | --- | --- | --- |
| CAB-Q | Deployment approval tool. Cut a daily process from 6 hours to 30 minutes. | Maybank | OutSystems O11 |
| Audit Log | Standardised audit logging, adopted across every OutSystems application. | Maybank | OutSystems O11 |
| Tokenizer | Tokenisation for public display strings, with an encrypted database. | Maybank | OutSystems O11 |
| MPowered | Internal agile project management platform. Stability and defect work. | Maybank | OutSystems O11 |
| RPSST | Prototype to modernise legacy RBS transaction processes. | Maybank | OutSystems O11 |
| VIP Dashboard | Visualisations of Sarawak data for a VIP presentation. | Impact Business Solutions Sdn Bhd | Power BI, QGIS |
| QR Asset Management | QR-based asset tracking. | Impact Business Solutions Sdn Bhd | Flutter, Firebase |
| Adam Digital Assets | Islamic mosque signage app, plus a website twin. Two developers shared requirements, design and build. | Adam Digital Assets | Flutter |

**States**: No states.

**Rules**: 1, 3, 5, 6

### Timeline Entry

One period in Wan Zayd's career.

| Field | Meaning | Format | Required | Allowed values | Example | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Kind | What the period is | list | yes | employer, client, career break | client | LinkedIn |
| Organisation | The employer or client | text | yes, except career break | any | Maybank | LinkedIn |
| Parent employer | The employer a client sits under | text | only for a client | an employer entry | AvePoint | LinkedIn |
| Role | His title in that period | text | no | title follows rule 4 | Senior OutSystems Engineer | Wan Zayd |
| Employment type | The terms of the employment | list | no | full-time, contract, part-time | contract | LinkedIn |
| Start | First month | month and year | yes | a past month | Sep 2024 | LinkedIn |
| End | Last month | month and year, or "present" | yes | rule 2 | Jan 2026 | LinkedIn |
| Tools | Technologies used there | list | no | derived (rule 7) | OutSystems O11 | its projects |
| Mark | The organisation's mark, and marks of its tools | file | no | rule 8 | Maybank + OutSystems | Wan Zayd's files |

**Content from the brief**:

| Kind | Organisation | Role | Type | Start | End |
| --- | --- | --- | --- | --- | --- |
| employer | AvePoint | Full Stack Developer / Technical Lead | full-time | Jan 2026 | present |
| client | Sunway University (under AvePoint) | Senior Technical Lead | not given | Apr 2026 | present |
| employer | Maybank | Senior OutSystems Engineer | not given | Sep 2024 | Jan 2026 |
| employer | Adam Digital Assets | Flutter Developer | part-time | May 2024 | Jul 2024 |
| employer | FPT Software Malaysia | not given | contract | Sep 2022 | Sep 2024 |
| client | PETRONAS Digital (under FPT Software) | not given | not given | not given | not given |
| career break | none | Personal goal pursuit | none | Apr 2022 | Aug 2022 |
| employer | Impact Business Solutions Sdn Bhd | not given | contract | Apr 2021 | May 2022 |

**States**: No states. Wan Zayd edits "present" when an entry ends.

**Rules**: 2, 4, 7, 8

### Qualification

A certification or a degree, shown as a minor item near the About text, with detail on demand.

| Field | Meaning | Format | Required | Allowed values | Example | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Name | The qualification name | text | yes | any | OutSystems Associate Technical Lead (O11) | brief |
| Issuer | Who awarded it | text | yes | any | UiTM | brief |
| Period | Years of study, or year awarded | year or year range | no | rule 2 | 2019–2021 | brief |
| Detail | The extra information a reader asks for | text | no | any | not given | Wan Zayd |

**Content from the brief**:

| Name | Issuer | Period |
| --- | --- | --- |
| OutSystems Associate Developer Specialist (O11) | OutSystems | not given |
| OutSystems Associate Technical Lead (O11) | OutSystems | not given |
| Professional Scrum Developer | not given | not given |
| BSc Information Systems (Intelligent Systems Engineering) | UiTM | 2019–2021 |
| Diploma Computer Science | UiTM | 2015–2019 |

**States**: No states.

**Rules**: 2, 8

### Mark

A compact vector logo. Five exist: Petronas, OutSystems, FPT Software, AvePoint and Maybank. Their sizes stand in Constraints and risks.

| Field | Meaning | Format | Required | Allowed values | Example | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Organisation | Whose mark it is | text | yes | an employer, client or tool | Maybank | Wan Zayd's files |
| File | The vector file | file | yes | compact vector only | not given | Wan Zayd's files |
| Compressed size | Size after gzip -9 | number, bytes | yes | any | 1,937 B | measured |

**States**: No states.

**Rules**: 8

### About

A short account of who Wan Zayd is. He writes it himself.

| Field | Meaning | Format | Required | Allowed values | Example | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Text | The about text | text | yes | any | not given | Wan Zayd |

Suggestions from Claude, not content (medium confidence): one line on what he is, in the settled title. One line that lets a reader outside low-code calibrate OutSystems, through a decision rather than the platform name. One line on the front-end and design interest the page itself shows.

**States**: No states.

**Rules**: 1, 4

### How I work

One short paragraph on how Wan Zayd makes architecture calls and runs a team. He writes it himself.

| Field | Meaning | Format | Required | Allowed values | Example | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Text | The paragraph | text | yes | one short paragraph | not given | Wan Zayd |

Suggestions from Claude, not content (medium confidence): how he makes an architecture call, for example with C4 diagrams, technical design documents and scoping with business analysts. How he runs a team, for example leading while he also develops when the team is thin. What he is willing to trade off.

**States**: No states.

**Rules**: 1

### Contact

The ways a reader reaches Wan Zayd.

| Field | Meaning | Format | Required | Allowed values | Example | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Email | His email address | text | yes | one address | not given | Wan Zayd, at build |
| LinkedIn | His LinkedIn profile address | text | yes | one address | not given | Wan Zayd, at build |
| CV | The CV he wrote himself | file, PDF | yes | one file | not given | Wan Zayd, at build |

**States**: No states.

**Rules**: 5

## Business rules

The site is static, so no system enforces these rules. Wan Zayd must check each one before he publishes.

1. **No relative time**: no text says how recent something is. "Currently", "this year", "recently" and "last updated" are out. Reason: the site has no maintenance commitment, and undated content cannot look abandoned. When broken: Wan Zayd rewrites the sentence before he publishes.
2. **Dates in periods only**: a timeline period carries month and year, and the current entry ends with "present". A qualification can carry a year or a year range. Reason: a reader can see tenure length. When broken: a date outside a period is removed.
3. **Defensible tools only**: the Tools field names only technologies Wan Zayd will defend under questioning. React, AWS and .NET/C# never appear. Flutter appears only on a Minor Project. Reason: an interviewer can question any tool the site names.
4. **Title use**: the site uses "OutSystems Technical Lead" throughout. "Senior Technical Lead" appears on the iZone rebuild only. Reason: settled by Wan Zayd in the proposal.
5. **Real figures only**: every figure is measured or stated by Wan Zayd. For example, 40,000 enrolments over 20 minutes comes from a load test. Reason: the site is evidence, and an invented figure breaks it. When broken: the figure is removed, and the sentence stands without it.
6. **Tools required**: every Main Project and every Minor Project names its tools. Reason: Wan Zayd decided tools belong on every entry.
7. **Derived employer tools**: the tools on a timeline entry are the tools of that employer's projects. Reason: one source of tools, so the two places cannot disagree.
8. **Mark placement**: a mark appears wherever an employer or client with a vector file is named. A tool mark, for example OutSystems, sits with the employer whose projects used it. An organisation with no vector file appears in type. Reason: Wan Zayd's decision; exact placement belongs to the design session.
9. **Undated outcome**: every Main Project has an outcome, stated without time words. Reason: an outcome with a date goes stale.
10. **No photographs or screenshots**: the page carries no image of Wan Zayd or of his work. Reason: the page itself proves the taste, and images cost more than the budget allows.
11. **Client detail published**: client detail from Maybank, Petronas, Sunway University and Sarawak appears without restriction. Reason: Wan Zayd's decision, against Claude's advice.

## Specs

Every spec has the same trigger: a reader opens the page. The page is static, so the only error case is a failed load.

### Follow how he designs a system

- **Trigger**: a reader opens the page.
- **The system**: shows the three Main Projects, each with all its fields. Rules 1, 3, 4, 5, 6, 9 and 11 apply.
- **Result**: the reader knows the problem, decision, trade-off, role and team, outcome and tools of each Main Project.
- **Errors**: None found.

### Judge his engineering without knowing OutSystems

- **Trigger**: a reader opens the page.
- **The system**: states each decision in general terms, for example row locking, before it names the platform.
- **Result**: a reader outside low-code can judge the decisions.
- **Errors**: None found.

### Learn how he makes architecture calls and runs a team

- **Trigger**: a reader opens the page.
- **The system**: shows the How I work paragraph and the role and team of each Main Project.
- **Result**: the reader knows how he decides and how he leads.
- **Errors**: None found.

### See the range of his work

- **Trigger**: a reader opens the page.
- **The system**: shows the eight Minor Projects, less highlighted than the Main Projects, each with its employer and tools.
- **Result**: the reader sees work beyond the three Main Projects.
- **Errors**: None found.

### Follow his career

- **Trigger**: a reader opens the page.
- **The system**: shows each timeline entry, newest first, with clients nested under employers. Rules 2, 7 and 8 apply.
- **Result**: the reader sees five years and five employers with no gap.
- **Errors**: None found.

### Check his qualifications

- **Trigger**: a reader opens the page.
- **The system**: shows the five qualifications as minor items near the About text. It gives the detail of each one on demand.
- **Result**: the reader can check each qualification by name and issuer.
- **Errors**: None found.

### Reach him and download his CV

- **Trigger**: a reader wants to contact Wan Zayd.
- **The system**: gives his email address, his LinkedIn address and the CV file.
- **Result**: the reader can write to him, open his profile or save his CV.
- **Errors**: if LinkedIn is unavailable, the email address still works.

### Judge his front-end taste

- **Trigger**: a reader opens the page.
- **The system**: shows the page with no photograph and no screenshot. Rule 10 applies.
- **Result**: the reader judges taste from the page itself.
- **Errors**: None found.

### Load on a slow connection

- **Trigger**: a reader opens the page on a 3G connection.
- **The system**: sends one page, with a target under 14 kilobytes compressed.
- **Result**: the page loads without waiting.
- **Errors**: if the connection drops during loading, the reader still sees readable content.

## Integrations

- **GitHub hosting**: serves the page and the CV file, on every visit, owned by GitHub. When it is unavailable: the site is unreachable, and no fallback exists.
- **LinkedIn**: an outgoing link to his profile, on demand, owned by LinkedIn. When it is unavailable: the reader uses the email address instead.
- **Email**: an outgoing address, on demand, owned by Wan Zayd's mail provider. When it is unavailable: the reader uses LinkedIn instead.

## Open questions

- iZone team size: the proposal says he leads three developers in a team of ten or more. The interview says two OutSystems developers, and he develops too. Wan Zayd must say which is correct.
- MStatus: what the system is, for the Digital Form integration list. Wan Zayd, or a Maybank colleague.
- Missing timeline facts: his role at FPT Software and at Impact, and the period of the PETRONAS Digital placement. Wan Zayd.
- Missing qualification facts: the issuer of Professional Scrum Developer, and the year of each certification. Wan Zayd.
- Contact values: email address, LinkedIn address and the CV file. Wan Zayd supplies them at build.
- About and How I work text: Wan Zayd writes both.
- Page weight: Claude builds the page, measures it, and reports the real figure against the 14 kilobyte target.
- Input for the design session: how Main Projects stand out from Minor Projects, where marks sit, and how qualification detail appears on demand. Hover alone does not work on a touch screen.
