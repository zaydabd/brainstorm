# References - Developer portfolio (round 1, sorted by Zayd)

## Brief
- Feel: cinematic but calm; restraint; type carries the page
- Audience / platform: hiring managers, tech leads, recruiters (desktop); designer peers (phone). Single static page, GitHub Pages, under a 14 KB target
- Type: system fonts only. Didone display serif, system sans body, mono labels
- Theme: light and dark, following the system setting (prefers-color-scheme)
- Colour: open. Round 1 shows a range
- Density: mixed. Main Projects airy; Minor Projects and timeline dense
- Motion: subtle and cinematic, CSS only (scroll-driven reveals, a title-card entrance)
- Avoid: photos, screenshots, web fonts, default Material/Tailwind/Bootstrap looks, AI tropes, rounded cards with shadows

> Where the "Take from it" note says *(opened)*, I read the page. Everything else comes from the search listing or what I already knew about the site. Check those when you open them.

## Kept (user picks)

### What I like (look and feel)
| Ref | Reference | Notes |
|-----|-----------|-------|
| #15 | [Butterick's Practical Typography](https://practicaltypography.com/) | Also in Minimal |
| #3 | [Rauno Freiberg 2023](https://2023.rauno.me/) | |
| #2 | [Rauno Freiberg](https://rauno.me/) | |
| K1 | [Megha Sharma (Wall of Portfolios)](https://www.wallofportfolios.in/portfolios/megha-sharma/) | *(opened)* A directory entry for a creative designer. Her real site is [meghasharmafolio.framer.website](https://meghasharmafolio.framer.website/), which I haven't opened |
| K2 | [Ayoub Sousali](https://www.sousali.com/) | *(opened)* A dark single page with a deep purple accent (`#150734`, from its metadata). Hero line, work shown in a "01 / 04" carousel with tools on each project, arrow links ("View work →") |

### Minimal
| Ref | Reference | Notes |
|-----|-----------|-------|
| #1 | [Paco Coursey](https://paco.me/) | Labelled text lists, no images |
| #15 | [Butterick's Practical Typography](https://practicaltypography.com/) | |

### Token and component theory (how to build it)
| Ref | Reference | Use for |
|-----|-----------|---------|
| #19 | [Utopia type calculator](https://utopia.fyi/type/calculator/) | Fluid type scale |
| #18 | [Modern Font Stacks](https://modernfontstacks.com/) | System font stacks |
| K3 | [Coolors palette](https://coolors.co/palette/ffffff-e9f6f6-82909d-373f47-cfd6c9-334444-262032) | Colour candidate. These hex codes come from the link: `#ffffff` `#e9f6f6` `#82909d` `#373f47` `#cfd6c9` `#334444` `#262032` |
| #27 | [MDN: `<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details) | Qualification detail that opens on tap |
| #29 | [Scott O'Hara: details and summary](https://www.scottohara.me/blog/2018/09/03/details-and-summary.html) | Disclosure accessibility |
| #28 | [Adrian Roselli: Disclosure widgets](https://adrianroselli.com/2020/05/disclosure-widgets.html) | Disclosure accessibility |
| #38 | [Art of the Title: Top 10 of 2021](https://www.artofthetitle.com/feature/top-10-title-sequences-of-2021/) | Title-card and hero composition |
| #36 | [Josh W. Comeau: scroll-driven animations](https://www.joshwcomeau.com/animation/scroll-driven-animations/) | CSS-only motion |

### Round 2 picks
| Ref | Reference | Notes |
|-----|-----------|-------|
| #84 | [Melvin Winkeler](https://www.melvinwinkeler.com/) | *(opened)* Neutral black, white and grey. Large bold headings, a "Scroll" cue, smooth scrolling with content revealed in stages |
| #82 | [Porsche Motorsport](https://racing.porsche.com/) | *(opened)* Heritage timeline year by year (1941 → 2014) revealed as you scroll. Short fragment headlines ("Built to brake late") |
| #72 | [Shu Ding](https://shud.in/) | *(opened)* `#fcfcfc` background, the name as the only heading, a bio paragraph, no images |

The library is closed (Zayd: "we do have enough"). Everything else in round 2 was "fine but meh".

### Ideas noted (suggestions only, not decided)
- **Whole page as a timeline**, inspired by Megha Sharma's scroll (her scroll is your observation; I couldn't see scroll behaviour through a fetch). Proposed reading:
  - Newest first, iZone (your strongest Main Project) comes first anyway
  - Each employer becomes a chapter that holds its projects: AvePoint → iZone; Maybank → Digital Form plus 5 Minor Projects; FPT → MyInsights; Impact → 2 Minor; Adam → 1 Minor
  - Main and Minor Projects then sit in context, not in separate lists
  - Risk: the journey's hiring manager scans Main Projects first, so Main Projects must still stand out inside each chapter

## Digest of your picks

**Common threads (observed on the pages I opened)**
- Text first, no images: Paco, Rauno (current), Practical Typography
- Craft shown through small interactions, not media: Rauno's click-to-copy email with a "Copied" confirmation, and his stacked one-line principles
- Rauno 2023 and Megha use video and thumbnails. Take their pacing and structure, not the media (rule 10)
- Tools named on each project: Sousali (backs up rule 6)
- A dark theme with a purple-black accent: Sousali `#150734`, and `#262032` in your palette

**Your palette, measured** (WCAG contrast ratios, computed from the hex codes)
- Light to dark: `#ffffff` → `#e9f6f6` icy white → `#cfd6c9` sage grey → `#82909d` **blue-grey (the icy middle)** → `#373f47` slate → `#334444` teal slate → `#262032` purple-black
- `#82909d` measures 3.3:1 on white and 4.8:1 on `#262032`. On the light theme it's for large text only (24px and up, which suits the Didone headings), rules and marks. On the dark theme it passes AA even for body text
- `#373f47` against `#334444` measures 1.0:1, so they read as the same colour. Keep one
- `#cfd6c9` leans warm green and may soften the icy look. It's the one to question

**Green removed (Zayd's call).** Hues are measured in HSL degrees; blue is roughly 200–215°.
| Original | Hue | Change | New hue | Contrast on `#262032` |
|----------|-----|--------|---------|-----------------------|
| `#cfd6c9` sage | 92° (green) | → `#c9d3de` ice grey (same lightness) | 211° | 10.4:1 (was 10.6:1) |
| `#e9f6f6` icy white | 180° (cyan, reads slightly green) | → `#eaf2f8` blue-white | 206° | 13.9:1 (was 14.2:1) |
| `#334444` teal slate | 180° (cyan) | → dropped, it duplicates `#373f47` | — | — |
| `#ffffff`, `#82909d`, `#373f47`, `#262032` | 209–210° or neutral | kept | — | — |

**Icy palette v2, light to dark:** `#ffffff` · `#eaf2f8` · `#c9d3de` · `#82909d` · `#373f47` · `#262032`

**Palette v4: black and white lead, clay only as accent** (Zayd's direction). The roles are my proposal; the contrast ratios are measured.

*Main colours, used for almost everything:*
| Swatch | Name | On `#ffffff` | On `#262032` | Role |
|--------|------|--------------|--------------|------|
| `#ffffff` | Snow | — | 15.7:1 | Light background |
| `#262032` | Night | 15.7:1 | — | Ink on light; dark background |

*Ice neutrals, which support the main pair and never compete with it:*
| Swatch | Name | On `#ffffff` | On `#262032` | Role |
|--------|------|--------------|--------------|------|
| `#eaf2f8` | Frost | 1.1:1 | 13.9:1 | Ink on dark; a subtle light band |
| `#c9d3de` | Ice | 1.5:1 | 10.4:1 | Muted text on dark; hairline rules on light |
| `#82909d` | Ice grey | 3.3:1 | 4.8:1 | Metadata and labels (large on light) |
| `#373f47` | Slate | 10.7:1 | 1.5:1 | Muted text on light; rules on dark |

*Clay accents, the full range kept but used sparingly:*
| Swatch | Name | HSL | On `#ffffff` | On `#262032` | Accent use |
|--------|------|-----|--------------|--------------|------------|
| `#e3d3d0` | Frosted clay | 9° 25% 85% | 1.4:1 | 10.9:1 | Accent on dark: text selection, focus ring |
| `#b88478` | Red rock | 11° 31% 60% | 3.2:1 | **5.0:1** | **Main accent on dark**: links, active state, marks |
| `#8e5a4f` | Cold clay | 10° 29% 43% | **5.6:1** | 2.8:1 | **Main accent on light**: links, active state, marks |
| `#4a2e2e` | Oxblood | 0° 23% 24% | 12.2:1 | 1.3:1 | Accent on light: one display word or a numeral |

- The rule: black and white carry the page; ice supports; clay appears only where the eye should land (links, the current item, one highlighted figure such as "40,000")
- The clay stays cold because it's red (9–11°) but dusty (23–31% saturation)
- Parked, not used: sand `#e8dccb`, driftwood `#b8997a`, wood `#8a6a4f`, walnut `#5c4332`, and the v2 roles table

### Not picked in round 1
- #4, #5, #6, #7, #8–14, #16, #17, #20–26, #30–35, #37, #39–42. They stay listed below for reference.

## 1. Type-only personal sites
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 1 | [Paco Coursey](https://paco.me/) | Real site | *(opened)* Name, a one-line tagline, then short labelled text lists (Building, Projects, Writing). No images | The closest match to "type carries the page" |
| 2 | [Rauno Freiberg](https://rauno.me/) | Real site | Design-engineer craft shown in small interaction details | Taste proven by the page itself |
| 3 | [Rauno Freiberg 2023](https://2023.rauno.me/) | Real site (archived version) | Compare against the current version to see how the idea changed | Same person, different expression |
| 4 | [Frank Chimero](https://frankchimero.com/) | Real site | Writing-first personal site with an editorial voice | Type-led; the words do the work |
| 5 | [Tom MacWright](https://macwright.com/) | Real site | *(opened)* A header menu with an **Auto / Light / Dark** toggle, and a home page of sections that each end with a "⇢" link to more. Ignore its photo sections | Pattern for dual themes and an index |
| 6 | [Siteinspire: minimal / portfolio / typography](https://www.siteinspire.com/websites/categories/minimal/portfolio/typography) | Siteinspire | Gallery to browse. I couldn't open it | Filtered to exactly this style |
| 7 | [Minimal Gallery: portfolio](https://minimal.gallery/tag/portfolio/) | Minimal Gallery | Gallery to browse | Minimal portfolios only |

## 2. Engineer portfolios (experience and tools)
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 8 | [Brittany Chiang](https://brittanychiang.com/) | Real site | *(opened)* Experience listed newest first, each with dates, title, company, a short description and **tool tags**. Dark navy theme, Inter. Ignore its project images | Direct pattern for Timeline Entry plus Tools (rules 6 and 7) |
| 9 | [Brittany Chiang v4](https://v4.brittanychiang.com/) | Real site (older version) | Older layout, widely copied | Shows how common this look is, so you can avoid it |
| 10 | [Ramit Krishnan](https://www.ramitkrishnan.com/) | Via SiteBuilderReport | Listed as "minimal yet elegant, projects presented clearly for technical depth" | Technical depth without visual noise |
| 11 | [Constantine Venizelos](https://www.venizelos.net/) | Via SiteBuilderReport | Listed as "minimal, academic style" | An academic, restrained tone |
| 12 | [Lee Robinson: Personal Software](https://leerob.com/personal-software) | Real site | A minimal engineer site; look at its prose layout | Writing that reads like a decision record |
| 13 | [designengineer.fyi](https://designengineer.fyi/) | Directory | A directory of design-engineer sites to mine for round 2 | Your target peer group |

## 3. Serif / Didone editorial type
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 14 | [Stripe Press](https://www.siteinspire.com/website/10454-stripe-press) | Siteinspire | A classic serif, book-like site | Cinematic but calm, serif-led |
| 15 | [Butterick's Practical Typography](https://practicaltypography.com/) | Real site | Text set with care: measure, leading, hierarchy | Body-text discipline |
| 16 | [Craig Mod: Essays](https://craigmod.com/essays/) | Real site | A calm, long-form reading layout | Editorial calm |
| 17 | [Craig Mod: A Simpler Page](https://craigmod.com/essays/a_simpler_page/) | Essay | The thinking behind stripped-back pages | The case for your restraint |
| 18 | [Modern Font Stacks](https://modernfontstacks.com/) | Tool | System font stacks by classification, including Didone | Checks your system-only Didone stack |
| 19 | [Utopia type calculator](https://utopia.fyi/type/calculator/) | Tool | Your `step-*` scale is built on this | Tune the fluid scale |

## 4. Colour range
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 20 | [Nord: colours and palettes](https://www.nordtheme.com/docs/colors-and-palettes) | Nord | A documented arctic, north-bluish palette with dark and light groups | Arctic-cool candidate |
| 21 | [Coolors: Arctic palettes](https://coolors.co/palettes/popular/arctic) | Coolors | Palette browsing | Arctic-cool range |
| 22 | [Coolors: Icy palettes](https://coolors.co/palettes/popular/icy) | Coolors | Palette browsing | Arctic-cool range |
| 23 | [14 monochromatic websites](https://blog.hubspot.com/website/monochromatic-websites) | HubSpot | A roundup of single-hue sites | Warm-mono and strict-mono candidates |
| 24 | [Gallereee: dark mode](https://www.gallereee.com/style/dark-mode) | Gallereee | A dark portfolio gallery | Dark, cinematic candidates |
| 25 | [Wall of Portfolios: dark theme](https://www.wallofportfolios.in/dark-theme) | Gallery | Dark portfolios | Dark, cinematic candidates |

## 5. Timeline, index and disclosure patterns
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 26 | [swiss-minimal-cv](https://github.com/obk/swiss-minimal-cv) | GitHub | A typography-focused CV template inspired by Swiss design | Dense timeline and Minor list |
| 27 | [MDN: `<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details) | MDN | Native disclosure that opens on tap without JS | Solves qualification detail on touch screens |
| 28 | [Adrian Roselli: Disclosure widgets](http://adrianroselli.com/2020/05/disclosure-widgets.html) | Blog | Accessible disclosure patterns | Same, done properly |
| 29 | [Scott O'Hara: details and summary](https://www.scottohara.me/blog/2018/09/03/details-and-summary.html) | Blog | The accessibility caveats of details and summary | Same |

## 6. Tiny, fast sites
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 30 | [512KB Club](https://512kb.club/) | Showcase | A list of lightweight sites to browse, sorted by size | Peers in your budget spirit |
| 31 | [minimal-14kb-website](https://github.com/jaetask/minimal-14kb-website) | GitHub | "A modern website in ≤ 14 KB" | Proof the budget can hold a modern look |
| 32 | [Portfolio under 14 KB](https://dev.to/moonshadowrev/how-i-finally-built-my-portfolio-site-under-14kb-a-chill-journey-inspired-by-a-random-youtube-5f73) | DEV | A write-up of the same goal | Directly comparable |
| 33 | [KISS for pages below 14 KB](https://aohorodnyk.com/post/2025-09-19-pages-below-14kb/) | Blog | Techniques | Budget tactics |
| 34 | [The 14kB website myth](https://angusjf.com/14kb/) | Blog | The counter-argument | Tests your target honestly |

## 7. Motion (subtle, CSS only)
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 35 | [Chrome: scroll-driven animations](https://developer.chrome.com/docs/css-ui/scroll-driven-animations) | Chrome docs | `scroll()` and `view()` timelines, no JS | Cinematic reveals within budget |
| 36 | [Josh W. Comeau: scroll-driven animations](https://www.joshwcomeau.com/animation/scroll-driven-animations/) | Blog | Interactive explainer | Restrained examples |
| 37 | [Smashing: intro to scroll-driven animations](https://www.smashingmagazine.com/2024/12/introduction-css-scroll-driven-animations/) | Smashing | Scroll and view progress timelines | Reference |

## 8. Wildcard: film titles and the Swiss grid
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 38 | [Art of the Title: Top 10 of 2021](https://www.artofthetitle.com/feature/top-10-title-sequences-of-2021/) | Art of the Title | Title-card composition and type on black | Where "cinematic" comes from |
| 39 | [MUBI identity](https://fontsinuse.com/uses/51030/mubi-identity) | Fonts In Use | A film brand with a strict type system | Cinematic but calm |
| 40 | [MUBI by Spin](https://spin.co.uk/projects/mubi) | Spin | The studio's case study | Same, from the designers |
| 41 | [Müller-Brockmann](https://www.thegraphicdesignschool.com/design-history/joseph-mueller-brockmann/) | TGDS | Grid systems and Tonhalle posters | The Swiss grid discipline in your principles |
| 42 | [The Swiss Grid (Poster House)](https://posterhouse.org/wp-content/uploads/2019/10/PH_Exh_Swiss_Archive_interactive_Final.pdf) | Poster House | Exhibition catalogue PDF | Grid and type-only posters |

# Round 2: cinematic, icy colour

## 9. Cold film palettes and colour references
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 43 | [Arrival (2016): movie palette](https://moviepalette.com/products/arrival-2016) | Movie Palette | Palette pulled from the film | Fog, grey-blue, near-black: very close to your palette |
| 44 | [Arrival: cinematography analysis](https://colorculture.org/cinematography-analysis-of-arrival-in-depth/) | Color Culture | How the muted grey-blue was built | Calm, cinematic and cold |
| 45 | [Arrival: Bradford Young interview](https://nofilmschool.com/2016/11/arrival-cinematographer-bradford-young-interview) | No Film School | The DP's own reasoning | Restraint as intent |
| 46 | [The Revenant: cinematography analysis](https://colorculture.org/cinematography-analysis-of-the-revenant-in-depth/) | Color Culture | Natural cold light, snow whites, blue shadows | Icy white to deep ink |
| 47 | [Blade Runner 2049: Deakins on colour](https://filmmakermagazine.com/103272-the-color-of-the-future/) | Filmmaker Magazine | Colour used by scene | A cinematic accent against a cold base |
| 48 | [Fincher's desaturated palette](http://www.slate.com/blogs/browbeat/2015/06/23/david_fincher_s_color_palette_supercut_shows_how_the_director_uses_desaturated.html) | Slate | Desaturated blue and yellow | How to keep colour quiet |
| 49 | [BLUE: movie colour palettes](https://www.filmmakersacademy.com/blog-movie-color-palettes-blue/) | Filmmakers Academy | Blue-led film stills with palettes | Round-up of icy looks |
| 50 | [CYAN: movie colour palettes](https://www.filmmakersacademy.com/blog-cyan-movie-color-palettes/) | Filmmakers Academy | Cyan and teal stills | Your `#334444` direction |
| 51 | [@cinema.palettes](https://zenaoconnor.com/instagram-cinema-palettes/) | Zena O'Connor | Film stills with extracted swatches | Browse for icy stills |
| 52 | [Movies in Color](https://moviesincolor.com/) | Archive | Swatches taken from film stills | Same, as an archive |
| 53 | [StudioBinder: 50+ movie palettes](https://www.studiobinder.com/blog/how-to-use-color-in-film-50-examples-of-movie-color-palettes/) | StudioBinder | A broad set of examples | Range check |
| 54 | [Coolors: Cinematic](https://coolors.co/palettes/popular/cinematic) | Coolors | Browse. The fetch returned no hex codes | More palettes like your pick |
| 55 | [Radix Colors](https://www.radix-ui.com/colors) | Radix | 12-step scales with matching light and dark versions (Slate, Mauve). Not opened | A way to extend your palette into steps for both themes |

## 10. Snow in the desert (icy plus woody)
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 56 | [Sahara painted white with snow](https://www.npr.org/sections/thetwo-way/2018/01/09/576747323/photos-the-sahara-desert-painted-white-with-snow) | NPR | Photos of snow on red-orange dunes | The literal mood |
| 57 | [Rare snow on the Sahara dunes](https://www.foxweather.com/extreme-weather/ain-sefra-sahara-snow) | Fox Weather | More photos of the same event | Same |
| 58 | [A Dusting of White in the Sahara](https://www.earthobservatory.nasa.gov/images/91556/a-dusting-of-white-in-the-sahara) | NASA Earth Observatory | Satellite view: white over ochre | An abstract, poster-like version |
| 59 | [Dune: Part Two cinematography](https://colorculture.org/cinematography-analysis-of-dune-part-two-in-depth/) | Color Culture | Desert sand set against cold, pale light | Cinematic desert |
| 60 | [Creating the colours of Dune](https://www.digitalcinemareport.com/article/creating-colors-dune) | Digital Cinema Report | How the desert palette was graded | Same |
| 61 | [Nordic Woods palette](https://www.color-hex.com/color-palette/27739) | color-hex | Wood and snow swatches. Not opened | Woody side |
| 62 | [Scandinavian palette](https://phototones.com/palettes/scandinavian) | PhotoTones | Nordic neutrals with hex codes. Not opened | Snow and wood neutrals |

## 11. Red rock and clay, snowfall in Arabia
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 63 | [Jabal Al-Lawz covered in snow](https://www.arabnews.com/node/2222481/amp) | Arab News | Snow on the Tabuk mountains | Snow in Arabia, literally |
| 64 | [Jabal Al-Lawz: historic snowfall](https://gulfnews.com/world/gulf/saudi/saudi-arabias-jabal-al-lawz-transforms-into-winter-wonderland-with-historic-snowfall-1.1703934125252) | Gulf News | More photos | Same |
| 65 | [Snow blankets Al-Lawz](https://saudigazette.com.sa/article/657496/SAUDI-ARABIA/Snow-blankets-Al-Lawz-Mountains-in-Tabuk) | Saudi Gazette | More photos | Same |
| 66 | [Wadi Disah, Tabuk](https://houseofsaud.com/travel/tabuk-wadi-disah/) | House of Saud | Red sandstone canyon | Red rock tones |
| 67 | [Wadi Rum guide](https://www.nationalgeographic.com/travel/world-heritage/article/wadi-rum-jordan) | National Geographic | Red desert and rock | Red rock and clay |
| 68 | [Petra guide](https://www.nationalgeographic.com/travel/world-heritage/article/petra-jordan) | National Geographic | The rose-red carved city | Olden Arabia in cold rose stone |

# Round 2: around your picks

## 12. Design-engineer sites (like Rauno and Paco)
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 69 | [Alasdair Monk](https://www.alasdairmonk.com/) | Real site | *(opened)* Single column. Work history 2013 to present with a **logo beside each company**, then projects and archived projects | **Closest match to your marks on the timeline (rule 8)** |
| 70 | [Emil Kowalski](https://emilkowal.ski/) | Real site | *(opened)* Text-first, no images. Bio, 4 projects, then writing | Main-vs-list hierarchy without media |
| 71 | [Emil Kowalski: Great animations](https://emilkowal.ski/ui/great-animations) | Article | Principles for restrained motion | Guide for the subtle cinematic motion |
| 72 | [Shu Ding](https://shud.in/) | Real site | *(opened)* `#fcfcfc` background, a name heading, a bio paragraph, no images | Near-white main colour, done quietly |
| 73 | [Amelie Schlüter](https://www.amelieschlueter.com/) | Real site | *(opened)* Experience listed newest first with MM/YYYY – Present dates. Projects use cover images (ignore them) | Timeline date format, same as rule 2 |
| 74 | [Brian Lovin](https://brianlovin.com/) | Real site | A design-engineer home page | Same peer group |
| 75 | [Brian Lovin: personal-websites list](https://github.com/stars/brianlovin/lists/personal-websites) | GitHub | *(opened)* 22 personal-site repos (Paco, Dan Eden, Timo Lins, Rauch…) | A source for round 3 |
| 76 | [Daniel Eden](https://daneden.me/) | Real site | Designer's site, from the list above | Same peer group |
| 77 | [Timo Lins on One Page Love](https://onepagelove.com/authors/timolins) | One Page Love | One-page sites by Timo Lins | Single-page craft |
| 78 | [Web of Devs](https://webofdevs.com/) | Directory | A directory of developer websites | A source for round 3 |

## 13. Book-like typography (like Practical Typography)
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 79 | [Web Typography by Richard Rutter](https://book.webtypography.net/) | Real site | *(opened)* Centred single column, a table of contents you can show or hide, high-contrast text | The collapsible contents is a pattern for qualification detail |
| 80 | [Better Web Type](https://betterwebtype.com/web-typography-book/) | Real site | A typography book and course site | Rhythm and scale for developers |
| 81 | [Web Style Guide: Typography](https://webstyleguide.com/9-typography.html) | Reference | A classic chapter on type in web layout | Theory to back the fundamentals |

## 14. Scroll as timeline (like Megha)
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 82 | [Porsche Motorsport](https://racing.porsche.com/) | Via scrollytelling.ai | Listed as a scroll-triggered heritage timeline across seven decades. Its 3D hero is out of budget | A career timeline told through scrolling |
| 83 | [YesNo](https://yesnowww.com/) | Via scrollytelling.ai | Listed as "scroll-driven bold typographic transitions and stark visual shifts" | Type-only scroll drama, black and white |
| 84 | [Melvin Winkeler](https://melvinwinkeler.com/) | Via scrollytelling.ai | Listed as elastic transitions through a project selection | Portfolio-scale scroll |
| 85 | [Best scrollytelling examples](https://scrollytelling.ai/examples/) | Roundup | *(opened)* 27 reviewed examples. Most are 3D or WebGL, so take the pacing only | Idea bank |

## 15. Black and white with one accent colour
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 86 | [Pixlspace](https://pixlspace.io/) | Via Wix roundup | Listed as charcoal and ivory with "occasional red accent pops" | **Exactly your v4 rule**: black and white main, red-clay accent |
| 87 | [Bodaghee Consulting](https://bodagheeconsulting.com/) | Via Wix roundup | Listed as using a crimson accent on calls to action | An accent kept for action points only |
| 88 | [Diego Aguiar](https://diegoaguiar.work/) | Via Wix roundup | Listed as a black canvas, white details, section dividers, text animations | Dark-theme reference |
| 89 | [Violet Henderson](https://violet-henderson.com/) | Via Wix roundup | Listed as a writing portfolio that puts the words first | A written portfolio like yours |
| 90 | [Les Marteau](https://lesmarteau.com/) | Via Wix roundup | Listed as alternating black and white sections | Chapter changes in the timeline |
| 91 | [17 black and white websites](https://www.wix.com/studio/blog/black-and-white-websites) | Wix | *(opened)* The source roundup | More to browse |

## 16. Title-card heroes
| # | Reference | Source | Take from it | Why it fits |
|---|-----------|--------|--------------|-------------|
| 92 | [Typographic hero examples](https://htmlburger.com/blog/typographic-hero-image-examples/) | HTMLBurger | Type-only heroes | Hero with no image |
| 93 | [Hero typography trends](https://qodeinteractive.com/magazine/innovative-typography-hero-trends/) | Qode | Large-type hero treatments | Same |
| 94 | [Anzo Studio](https://anzo.studio/) | Via Wix roundup | Listed as "cinematic typography" with entrance animations. Its videos are out of budget | The title-card entrance |

## Dropped
- Robin Rendle's site: *(opened)* it is now mainly a photo gallery, which clashes with rule 10
- SiteBuilderReport engineer list (Katie Heinemann and others): image-heavy
