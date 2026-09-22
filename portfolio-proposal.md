# Developer portfolio

## Summary

Wan Zayd Abdullah is a Senior Technical Lead with five years of OutSystems
experience. This proposal describes a single-page website that presents his work to
hiring managers, to other technical leads, and to people who notice design. The site
carries three case studies, an account of how he works, and his career history. Wan
Zayd aims to keep it under 14 kilobytes compressed, so it loads quickly on a 3G
connection. Once the site exists, Wan Zayd owns a document that describes him in his
own voice.

## The problem

Wan Zayd passes CV screens and gets interviews. The document that represents him
belongs to AvePoint, his employer. AvePoint sends it to clients as a staffing
profile. It names four technologies, lists four employers, and describes his
responsibilities in the third person. It has no place for taste, voice or craft. He
wants to be known for front-end work and design judgment, and that document can show
neither.

A reader outside the low-code world cannot calibrate his experience. The word
"OutSystems" carries little meaning to that reader. They see five years and the
title Senior Technical Lead, and they cannot judge the distance between those two
facts. The AvePoint document gives them nothing else to work from.

The AvePoint document is also inaccurate in places. It compresses his employment
into year ranges, which makes his record look as though it has gaps. It names his
Maybank title differently from his LinkedIn profile. It omits an employer, Adam
Digital Assets, where he designed and built a Flutter application.

His public presence is thin. His LinkedIn profile holds 297 connections and 308
followers, and he has published no posts. In the seven days before this proposal,
LinkedIn recorded 40 profile views and 11 search appearances. His GitHub account
holds two repositories and no profile page. He wants a reputation as a developer,
and he owns no artifact that builds one.

## What this would do

The site makes one argument in two parts. The written work proves the engineering.
The site itself proves the taste, because Wan Zayd builds it and no image stands in
for it.

- A reader can follow how Wan Zayd designs a system, through three case studies that
  each state the problem, his decision and the trade-off.
- A reader who does not know OutSystems can judge his engineering from the decisions
  described, rather than from the platform name.
- A reader can learn how he makes architecture calls and how he runs a team.
- A reader can see the range of his work, through a short index of eight further
  projects.
- A reader can follow his career across five years and five employers, with no
  unexplained period.
- A reader can check his qualifications against three named certifications and two
  named degrees.
- A reader can reach him by email or on LinkedIn, and can download a CV that he
  wrote himself.
- A reader judges his front-end taste from the page in front of them, because the
  site carries no photograph and no screenshot.
- A reader on a slow connection receives a page small enough to load without
  waiting.

The three case studies are Digital Form, MyInsights and the iZone rebuild. Digital
Form has run through five MVP cycles. It connects four systems, which are GSAM,
HRIS, MStatus and MPowered, and it handles dynamic forms and SLA tracking. MyInsights
pushes millions of records through audit rules for Petronas. Wan Zayd refactored it
from one module into a decentralised system. The iZone rebuild is current work at
Sunway University. He owns the architecture there, which covers headless services,
integration libraries, single sign-on and a private gateway. He also designed the
database schema and the concurrency model for simultaneous student enrollment. He
leads three developers inside a project team of ten or more.

The short index names CAB-Q, Audit Log, Tokenizer, MPowered, RPSST, VIP Dashboard,
QR Asset Management and the Adam Digital Assets work. Each one gets its name and one
line. CAB-Q cut a daily approval process from 6 hours to 30 minutes, and that line
records it. The Adam Digital Assets line records an Islamic mosque signage
application, built in Flutter with a matching website.

The site names the technologies Wan Zayd will defend under questioning. These are
OutSystems in both O11 and ODC, SQL and Aurora PostgreSQL, REST APIs and integration
work, and architecture practice. Architecture practice covers C4 diagrams, technical
design documents and system design.

## What it leaves out

- Artistic direction: Wan Zayd will run a separate design session for it, and he
  plans to build a skill for that purpose. No colour, type or layout decision belongs
  in this document.
- Written pieces or a blog: writing is a continuing commitment rather than a build.
  He can add it later without rebuilding anything.
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
- CAB-Q as a full case study: he chose three case studies, so CAB-Q appears in the
  short index instead.
- Dated content of any kind: undated content cannot look abandoned.

## Constraints and risks

No date drives this work. Wan Zayd treats it as a continuing personal project, so
the build can run in stages.

The site must fit on one page. Wan Zayd aims to keep the whole page under 14
kilobytes compressed, and he treats that figure as a target rather than a limit. The
prose, the markup and the stylesheet together come to about 5 to 6 kilobytes
compressed, on my estimate. I have not validated that estimate against a built page.

Wan Zayd wants a mark for each organisation in his record. I measured the files he
sent, compressed with gzip. The compact marks are small. Petronas costs 474 bytes,
OutSystems 791 bytes, FPT Software 1,142 bytes, AvePoint 1,923 bytes and Maybank
1,937 bytes. Five compact marks together cost 6,267 bytes. Full wordmark versions
cost more. Maybank rises to 3,416 bytes and Petronas to 1,530 bytes.

Four organisations have no vector file. Sunway Education and Sunway Group exist only
as raster images. The smallest usable files cost 10,824 bytes and 3,899 bytes, and a
raster image does not compress further. Impact Business Solutions Sdn Bhd publishes
its own mark as a PNG file, and its website carries no vector version. Adam Digital
Assets has supplied nothing. Wan Zayd chose to use each organisation's own mark
where one exists.

The site runs on GitHub, which hosts it at no cost. Everything on the site is
public, and the traffic a personal portfolio receives places no meaningful load on
that hosting. If GitHub is slow or unavailable, the site is unreachable and no
fallback exists. Wan Zayd accepts that, because the alternative costs money and the
site carries nothing urgent. The site uses JavaScript only where CSS cannot do the
work. A reader whose connection drops during loading still sees readable content.

Wan Zayd decided to publish client detail from Maybank, Petronas, Sunway University
and Sarawak without restriction. I advised against this and he overruled me, so it
is recorded here as his decision. A separate point stands unresolved. Showing a
client logo is a trademark question rather than a confidentiality one, and a
displayed mark can imply that the client endorses him.

The site carries no dated content, which removes the main risk for a project with no
maintenance commitment. A reader cannot tell how old the site is, so it cannot look
abandoned.

## Assumptions

- I treat the LinkedIn profile as the accurate record where it contradicts the
  AvePoint CV. It carries exact months, and Wan Zayd confirmed its detail.
- I assume the career break from April 2022 to August 2022 appears on the timeline
  as his LinkedIn profile states it.
- I assume each case study runs to roughly 1,500 characters, which is the basis of
  the 5 to 6 kilobyte estimate above.
- I assume each organisation carries its own mark, in whatever format exists, now
  that 14 kilobytes is a target rather than a limit.
- I assume the downloadable CV is a separate file, so its size sits outside the 14
  kilobyte page budget.
- I assume Wan Zayd writes the words and directs every design decision, and that I
  implement.

## Open questions

- The Impact Business Solutions Sdn Bhd mark: the company publishes a PNG file and
  no vector version. Wan Zayd must send that file, because this environment cannot
  reach the company website.
- The Adam Digital Assets mark: no file exists yet, and the company may have no
  vector version.
- The raster marks: Wan Zayd first chose to set Sunway in type, because it exists
  only as a raster image. He then chose to use each organisation's own mark. Sunway
  and Impact Business Solutions Sdn Bhd both fall under that conflict, so he decides
  which choice stands.
- The page weight: I will build the page, measure it, and report the real figure
  against the 14 kilobyte target.
- His AvePoint title: the CV states Senior Technical Lead and his LinkedIn profile
  states Full Stack Developer and Technical Lead. He decides which the site uses.
- Flutter: he has under one year of experience and does not call himself
  knowledgeable. He decides whether it appears with that qualifier or not at all.
- What each case study contains beyond problem, decision and trade-off. This belongs
  to the next round of work.
- Whether he will publish a LinkedIn post for each case study. He named this as half
  his plan for reach, and he has published no post so far.
