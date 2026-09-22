# Developer portfolio proposal

A single-page site, under 14 kilobytes compressed, where the written work proves
the engineering and the site itself proves the taste.

## Summary

Wan Zayd Abdullah is an OutSystems Technical Lead with five years of experience.
This proposal describes a single-page website that presents his work to hiring
managers, to other technical leads, and to people who notice design. The site
carries three projects, an account of how he works, and his career history. Wan
Zayd aims to keep it under 14 kilobytes compressed, so it loads quickly on a 3G
connection. Once the site exists, Wan Zayd owns a document that describes him in
his own voice.

## The problem

Wan Zayd owns no document of his own that shows his work. The document that
represents him today belongs to AvePoint, his employer. AvePoint sends it to
clients as a staffing profile, and it describes his responsibilities in the
third person. It has no place for taste, voice or craft. He wants to be known
for front-end work and design judgment, and that document can show neither.

A reader outside the low-code world cannot calibrate his experience. The word
"OutSystems" carries little meaning to that reader. They see five years and the
title OutSystems Technical Lead, and they cannot judge the distance between
those two facts. The AvePoint document gives them nothing else to work from.

## What this would do

The site makes one argument in two parts. The written work proves the
engineering. The site itself proves the taste, because Wan Zayd builds it and no
image stands in for it.

- A reader can follow how Wan Zayd designs a system, through three projects that
  each explain the problem, his decision and the trade-off.
- A reader who does not know OutSystems can judge his engineering from the decisions
  described, rather than from the platform name.
- A reader can learn how he makes architecture calls and how he runs a team.
- A reader can see the range of his work, through a short index of eight further
  projects.
- A reader can follow his career across five years and five employers.
- A reader can check his qualifications against three named certifications and two
  named degrees.
- A reader can reach him by email or on LinkedIn, and can download a CV that he
  wrote himself.
- A reader judges his front-end taste from the page in front of them, because the
  site carries no photograph and no screenshot.
- A reader on a slow connection receives a page small enough to load without
  waiting.

The three main projects are Digital Form, MyInsights and the iZone rebuild. Each
one gets a semi-detailed explanation rather than a formal case study. Digital
Form has run through five MVP cycles. It connects four systems, which are GSAM,
HRIS, MStatus and MPowered, and it handles dynamic forms and SLA tracking.
MyInsights pushes millions of records through audit rules for Petronas. The
iZone rebuild remakes a legacy student portal at Sunway University, where he
holds the title Senior Technical Lead. Wan Zayd owns the architecture there,
which covers headless services, integration libraries, single sign-on and a
private gateway. The database schema comes from the legacy application, and he
designed the concurrency model for simultaneous student enrollment. He leads
three developers inside a project team of ten or more.

The short index names CAB-Q, Audit Log, Tokenizer, MPowered, RPSST, VIP
Dashboard, QR Asset Management and the Adam Digital Assets work. Each one gets
its name and one line. CAB-Q cut a daily approval process from 6 hours to 30
minutes, and that line records it. The Adam Digital Assets line records an
Islamic mosque signage application, built in Flutter with a matching website.

The site names the technologies Wan Zayd will defend under questioning. These
are OutSystems in both O11 and ODC, SQL and Aurora PostgreSQL, REST APIs and
integration work, and architecture practice. Architecture practice covers C4
diagrams, technical design documents and system design.

## What it leaves out

- Artistic direction: Wan Zayd will run a separate design session for it, and he
  plans to build a skill for that purpose. No colour, type or layout decision belongs
  in this document.
- Audience building and social reach: Wan Zayd wants a portfolio, not a presence on
  social media. The site does not exist to grow a following.
- Written pieces or a blog: he does not want one. Writing is a continuing commitment
  rather than a build, and he can add it later without rebuilding anything.
- A custom domain: GitHub hosting costs nothing, and he chose to spend nothing.
  Without a domain his name is harder to find in a search engine.
- Any server, form or database: an email address and a LinkedIn link do the same
  job. Nothing can break, and nothing costs money to run.
- Music and session work: he chose to keep the site strictly professional.
- The Maybank design-ownership account: his LinkedIn profile describes how he raised
  the design baseline for a team with no designer. I recommended it as evidence of
  design judgment, and he chose to leave it out.
- Claims about React, AWS and .NET/C#: these appear on his LinkedIn profile, and he
  will not defend them in an interview.
- Web fonts and photographs: each one costs more than the page can afford. Wan Zayd
  keeps them out as a discipline, so the typography carries the design.
- CAB-Q as a main project: he chose three, so CAB-Q appears in the short index
  instead.
- Dated content of any kind: undated content cannot look abandoned.

## Constraints and risks

No date drives this work. Wan Zayd treats it as a continuing personal project,
so the build can run in stages.

The site must fit on one page. Wan Zayd aims to keep the whole page under 14
kilobytes compressed, and he treats that figure as a target rather than a limit.
The prose, the markup and the stylesheet together come to about 5 to 6 kilobytes
compressed, on my estimate. I have not validated that estimate against a built
page.

Wan Zayd wants a mark for each organisation in his record. I measured the files
he sent, compressed with gzip.

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

Five compact marks together cost 6,267 bytes. A raster image does not compress
further. Wan Zayd decided that a mark is optional. The site carries the five
vector marks, and the four organisations with no vector file appear in type. I
noted that a reader can see which companies carry a mark, and he accepted that.

The site runs on GitHub, which hosts it at no cost. Everything on the site is
public, and the traffic a personal portfolio receives places no meaningful load
on that hosting. If GitHub is slow or unavailable, the site is unreachable and
no fallback exists. Wan Zayd accepts that, because the alternative costs money
and the site carries nothing urgent. The site uses JavaScript only where CSS
cannot do the work. A reader whose connection drops during loading still sees
readable content.

Wan Zayd decided to publish client detail from Maybank, Petronas, Sunway
University and Sarawak without restriction. I advised against this and he
overruled me, so it is recorded here as his decision. A separate point stands
unresolved. Showing a client logo is a trademark question rather than a
confidentiality one, and a displayed mark can imply that the client endorses
him.

The site carries no dated content, which removes the main risk for a project
with no maintenance commitment. A reader cannot tell how old the site is, so it
cannot look abandoned.

## Assumptions

- I assume the career break from April 2022 to August 2022 appears on the timeline
  as his LinkedIn profile states it.
- I assume each project explanation runs to roughly 1,500 characters, which is the
  basis of the 5 to 6 kilobyte estimate above.
- I assume the five vector marks appear at their compact size rather than as full
  wordmarks. The compact files cost less than half as much.
- I assume the downloadable CV is a separate file, so its size sits outside the 14
  kilobyte page budget.
- I assume Wan Zayd writes the words and directs every design decision, and that I
  implement.

## Open questions

- What MyInsights actually was. Wan Zayd marked the decentralisation claim as wrong,
  so that sentence is removed. Only he can describe what the work really involved.
- The page weight: I will build the page, measure it, and report the real figure
  against the 14 kilobyte target.
- Flutter: he has under one year of experience and does not call himself
  knowledgeable. He decides whether it appears with that qualifier or not at all.
- What each project explanation contains beyond problem, decision and trade-off.
  This belongs to the next round of work.
