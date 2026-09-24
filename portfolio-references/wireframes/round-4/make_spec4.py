"""Round 4: synthesis of the user's feedback on rounds 1-3.
Q = I reader (lighter list, artistic history), R = K hero + credits with lighter E-style cards,
S = B with ambient art in the third, T = C chapters with ambient art. All gain an At a glance strip,
captioned visuals and bento Minor Projects. Reuses blocks from make_spec3.py (and, through it, 2 and 1)."""
import json, sys, os

ARGS4 = sys.argv[:]
src3 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_spec3.py'), encoding='utf-8').read()
sys.argv = [sys.argv[0], '/dev/null']
exec(src3[:src3.index('\n# ---------- options ----------')])
OUT = ARGS4[1]

D.update({
    'glance': '"5 years, no gaps, dates clear." (journey, Recruiter stage 3); "add 5 yrs … at a single glance" (your feedback)',
    'fig_iz': '"Designing architecture (headless services, integration libs, SSO, private gateway). C4 diagrams" (LinkedIn); "make sure the place holder have some context" (your feedback)',
    'fig_df': '"connecting with GSAM, HRIS, MStatus, and MPowered" (CV); "make sure the place holder have some context" (your feedback)',
    'fig_mi': '"Auditors centralised audit exceptions and processed them in the system, not on files and paper." (details); "add some context" (your feedback)',
    'lightlist': '"The projects list could be less dense somehow" (your feedback, round 3 I)',
    'cards': '"E - is great because it was different but it is just too dense." (your feedback, round 1)',
    'mbento': '"the minor projects sections with the bentos is creative" (your feedback, round 3 M)',
    'timebar': '"The history seciton could be somewhat more artistic" (your feedback, round 3 I)',
    'ambient': '"allows me to add more animated backgrounds to fill the white space" (your feedback, round 1 B); "All three are pure CSS: two gradients, a blur and a mask, roughly 0.6 KB." (moodboard, Night light)',
    'keepk': '"keep the worked with seciont and hero section" (your feedback, round 2 K)',
})

def tag(kind, label):
    return (f'<span style="display:inline-block;border:1px dotted #333333;background:#ffffff;color:#333333;font-size:11px;'
            f'line-height:16px;padding:1px 6px;margin:0 4px 6px 0;font-weight:600">{kind} · {label}</span>')

STRIPE = 'background:repeating-linear-gradient(45deg,#e6e6e6 0 10px,#f3f3f3 10px 20px)'
def figure(caption, ratio='16/9'):
    return (f'<figure style="margin:12px 0"><div style="aspect-ratio:{ratio};border:2px dashed #888888;{STRIPE}"></div>'
            f'<figcaption style="font-size:13px;color:#333333;margin-top:6px">[PLACEHOLDER: visual · {caption} · drawn in code, never a photo or screenshot]</figcaption></figure>')

FIG = {1: 'suggested: the iZone architecture as a C4-style diagram: headless services, integration libraries, single sign-on, private gateway',
       2: 'suggested: the four systems Digital Form connects: GSAM, HRIS, MStatus and MPowered',
       3: 'suggested: audit exceptions moving from files and paper into the system'}
FIGSHORT = {1: 'architecture sketch', 2: 'the four systems it connects', 3: 'paper → system'}
FIGDOC = {1: 'fig_iz', 2: 'fig_df', 3: 'fig_mi'}

# ---------- At a glance ----------
def stat(num, label, sub=''):
    return (f'<li style="min-width:120px"><strong style="display:block;font-size:32px;font-weight:800;line-height:1.1">{num}</strong>'
            f'<span style="{LABEL}">{label}</span>' + (f'<span style="display:block;font-size:12px;color:#555555">{sub}</span>' if sub else '') + '</li>')
block('GL', 'Home · At a glance: years, employers, projects, qualifications',
      f'<h2 style="{LABEL};margin-bottom:8px">At a glance</h2>'
      '<ul style="list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:16px 32px">'
      + stat('5', 'employers', 'since Apr 2021') + stat('3 + 8', 'main and minor projects') + stat('5', 'qualifications') + stat('40,000', 'enrolments load-tested', 'over 20 minutes')
      + '</ul>',
      ['SCAN-01', 'PRIO-02', 'CPLX-03', 'GRP-02', 'SCAN-04'], 'glance')


D['years'] = '"They see five years and the title OutSystems Technical Lead" (proposal); "add 5 yrs … at a single glance" (your feedback)'
YEARS_LINE = (f'<p style="margin:0;font-size:15px;font-weight:700">5 years · since Apr 2021</p>')
LIVE = tag('LIVE', 'years counted from Apr 2021 when the page loads; without script it reads "since Apr 2021"')
block('H3y', 'Home · years, then title', YEARS_LINE + B['H3']['html'] + LIVE,
      ['SCAN-01', 'PRIO-02', 'GRP-02', 'SCAN-04'], 'years')
block('F0ry', 'Home · title card with rays, years before the title',
      B['F0r']['html'].replace('<p style="margin:clamp(16px,3vw,40px) 0 clamp(32px,2vw,40px);font-size:20px;font-weight:600">OutSystems Technical Lead</p>',
                               '<p style="margin:clamp(16px,3vw,40px) 0 0;font-size:15px;font-weight:700">5 years · since Apr 2021</p>'
                               '<p style="margin:4px 0 clamp(32px,2vw,40px);font-size:20px;font-weight:600">OutSystems Technical Lead</p>') .replace(
                               'off on touch and reduced motion</span>', 'off on touch and reduced motion</span>' + LIVE),
      ['HIER-01', 'HIER-04', 'SCAN-03', 'PRIO-02', 'PRIO-01'], 'years')
assert '5 years · since Apr 2021' in B['F0ry']['html']

# ---------- Main Projects with a captioned figure after the decision ----------
def project_with_figure(n, back=False):
    name, anchor, org, dec, dec2 = DEC[n]
    head = (f'<a href="#work" style="{TAP};padding:0;font-size:14px">← Projects list</a>' if back else '')
    return (head + f'<div style="max-width:66ch"><h3 id="{anchor}" style="margin:4px 0 0;font-size:24px">{name}</h3>'
            f'<p style="margin:4px 0 12px;{SMALL}">{org}</p>'
            + dl([('Decision', dec + (' ' + dec2 if dec2 else ''))]) + figure(FIG[n]) + dl(REST[n]) + '</div>')
for n in (1, 2, 3):
    block(f'PF{n}', f'Project case study · {DEC[n][0]}, figure right after its decision', project_with_figure(n),
          ['SCAN-10', 'SCAN-03', 'HIER-02', 'GRP-02', 'A11Y-04', 'TYPE-01', 'Asked Q5'], FIGDOC[n])
    block(f'IPF{n}', f'Project case study · {DEC[n][0]} detail pane, figure after its decision', project_with_figure(n, back=True),
          ['RESP-06', 'INT-10', 'HIER-02', 'GRP-02', 'A11Y-04', 'TYPE-01', 'Asked Q5'], FIGDOC[n])

# ---------- lighter Projects list (Main only; Minor moves to the bento) ----------
block('ILl', 'Projects list · the three Main Projects only, with a captioned thumb each',
      f'<h2 id="work" style="{H2}">Projects <span style="color:#555555">(3)</span></h2><ol style="list-style:none;margin:0;padding:0">'
      + ''.join(f'<li style="border-top:1px solid #cccccc;padding:16px 0;display:flex;gap:16px;align-items:flex-start{";background:#e2e2e2" if n == 1 else ""}">'
                f'<div style="flex:1 1 auto;min-width:0"><a href="#{DEC[n][1]}" style="font-weight:700;{TAP};padding:0"{CUR if n == 1 else ""}>0{n} · {DEC[n][0]}</a>'
                f'<p style="margin:0;{SMALL}">{SHORT[n][0]}</p></div>'
                f'<div style="flex:0 0 96px"><div style="height:64px;border:2px dashed #888888;{STRIPE}"></div>'
                f'<p style="margin:4px 0 0;font-size:11px;color:#444444">{FIGSHORT[n]}</p></div></li>' for n in (1, 2, 3))
      + '</ol><p style="margin:8px 0 0;font-size:13px;color:#555555">Choosing a project swaps the pane beside it (no script).</p>',
      ['RESP-06', 'SCAN-10', 'SCAN-12', 'CPLX-01', 'Asked Q4', 'Asked Q5'], 'lightlist')

# ---------- lighter E-style cards ----------
for n in (1, 2, 3):
    name, anchor, org, dec, dec2 = DEC[n]
    block(f'RC{n}', f'Project case study · {name} card (decision, outcome, tools, captioned visual)',
          f'<p style="{LABEL}">0{n} / 03</p><h3 style="margin:4px 0 0;font-size:22px">{name}</h3><p style="margin:4px 0 10px;{SMALL}">{org}</p>'
          f'<p style="margin:0"><b>Decision</b> · {SHORT[n][0]}</p><p style="margin:6px 0 0"><b>Outcome</b> · {SHORT[n][1]}</p>'
          f'<p style="margin:6px 0 0;{SMALL}">{SHORT[n][4]}</p>' + figure(FIG[n])
          + f'<a href="#{anchor}" style="{TAP};padding:0">Read the full write-up ↓</a>',
          ['SCAN-10', 'CPLX-03', 'HIER-02', 'PRIO-04', 'Asked Q4', 'Asked Q5'], 'cards')

# ---------- Minor Projects as a bento ----------
def mtile(name, line, emp, tools, big=''):
    return (f'<div style="border:1px solid #999999;background:#ffffff;padding:12px;display:flex;flex-direction:column;gap:6px">'
            + (f'<p style="margin:0;font-size:28px;font-weight:800;line-height:1.1">{big}</p>' if big else '')
            + f'<p style="margin:0;font-weight:700">{name}</p><p style="margin:0;font-size:14px">{line}</p>'
            f'<p style="margin:auto 0 0;font-size:13px;color:#555555">{emp} · {tools}</p></div>')
block('MB', 'Projects list · Minor Projects as bento tiles',
      f'<h2 style="{H2};font-size:18px">Minor Projects <span style="color:#555555">(8)</span></h2>'
      + tag('FUN', 'marks grey until touched · tile lifts on hover or tap')
      + '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px">'
      + mtile(*MINORS[0], big='6 h → 30 min') + ''.join(mtile(*m) for m in MINORS[1:]) + '</div>',
      ['GRP-01', 'GRID-01', 'CPLX-04', 'SCAN-04', 'Asked Q6'], 'mbento')

# ---------- artistic history: the five years as one bar ----------
block('TB', 'History · the five years as one bar (captioned visual)',
      figure('suggested: Apr 2021 → present as one bar, a segment per employer sized by its months: Impact, career break, FPT (PETRONAS), Adam (overlaps FPT), Maybank, AvePoint (Sunway)', '5/1'),
      ['SCAN-10', 'GRP-03', 'HIER-03', 'Asked Q2'], 'timebar')


block('TBh', 'History · heading, then the five years as one bar (captioned visual)',
      f'<h2 id="history" style="{H2}">History</h2>' + B['TB']['html'],
      ['HIER-02', 'SCAN-10', 'GRP-03', 'HIER-03', 'Asked Q2'], 'timebar')
_lx = B['LX2']['html']
block('LX2n', 'History · timeline entries with marks trailing (under the bar)',
      _lx[_lx.index('</h2>') + 5:], B['LX2']['rules'], 'spine')

# ---------- ambient art slots (fill white space; hidden content-free decoration) ----------
def amb(i, where):
    block(f'AMB{i}', f'Ambient · animated background in the white space {where}',
          f'<div style="min-height:260px;border:2px dashed #aaaaaa;background:repeating-linear-gradient(120deg,#ececec 0 18px,#f6f6f6 18px 36px);'
          f'display:flex;align-items:center;justify-content:center;text-align:center;padding:12px;font-size:13px;color:#333333">'
          f'AMBIENT · animated background {where} · e.g. light rays through haze, CSS only · still under reduced motion · no content in it</div>',
          ['GRID-03', 'HIER-03', 'HIER-04'], 'ambient')
for i, w in ((0, 'beside the opening'), (1, 'beside iZone'), (2, 'beside Digital Form'), (3, 'beside MyInsights'), (4, 'beside the Maybank chapter'), (5, 'beside the FPT chapter')):
    amb(i, w)

# ---------- chapter spines with large marks ----------
SPINE = [('Jan 2026 – present', bigmark('AvePoint'), 'AvePoint'), ('Sep 2024 – Jan 2026', bigmark('Maybank'), 'Maybank'),
         ('May 2024 – Jul 2024', bigmark('Adam Digital Assets', True), 'Adam Digital Assets'),
         ('Sep 2022 – Sep 2024', bigmark('FPT Software'), 'FPT Software Malaysia'), ('Apr 2022 – Aug 2022', '', 'Career break'),
         ('Apr 2021 – May 2022', bigmark('Impact Business Solutions', True), 'Impact Business Solutions')]
for i, (period, mk, org) in enumerate(SPINE, 1):
    block(f'TS{i}', f'History · chapter {i} spine with its mark',
          (tag('FUN', 'marks grey until touched') if i == 1 else '') + (f'<div style="margin-bottom:8px">{mk}</div>' if mk else '')
          + f'<p style="{LABEL}">{period}</p><p style="margin:2px 0 0;font-weight:700">{org}</p>',
          ['GRP-05', 'SCAN-10', 'GRID-01', 'A11Y-04', 'SCAN-12'], 'spine')

# ---------- options ----------
HDR = lambda: {'landmark': 'header', 'rows': [[cell(12, [P('H1', 'top bar', ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]}
FTR = lambda cells: {'landmark': 'footer', 'rows': [cells]}
def pl(ids, where, add=()):
    return [P(b, where, B[b]['rules'] + list(add)) for b in ids]

answered = ('Answered: Q1 one page, 5 sections · Q2 LinkedIn dates, CV roles · Q3 fold 765 / 568 · Q4 44×44 · '
            'Q5 iZone, Digital Form, MyInsights · Q6 timeline, then Minor. Round 4 feedback: add years at a glance; '
            'keep B/C white space for animated backgrounds; E less dense; keep I; keep K hero and Worked with; '
            'visuals need context; history more artistic; Minor Projects as bento.')
task = ('Dominant task (SCAN-14): judge his engineering from the decisions, then decide to interview or contact '
        '(hiring manager, tech lead; desktop). Recruiter scans title, tools, tenure; designer peer browses on a phone.\n')
def opt(i, name, axis, note, order, rows1440, margin=80):
    return {'id': i, 'name': name, 'axis': axis, 'note': task + note + '\n' + answered,
            'artboards': [compact(order, footer='C1f'), {'width': 1440, 'margin': margin, 'rows': rows1440}]}
options = []

Q_ORDER = ['H2', 'H3y', 'H4', 'GL', 'H5', 'ILl', 'IPF1', 'IPF2', 'IPF3', 'X1', 'TBh', 'LX2n', 'MB']
options.append(opt('Q', 'Reader, lighter', 'RESP-06 list + detail (from round 2/3 I) · list holds the 3 Main Projects only; Minor Projects move to a bento after the timeline (fixes Q6)',
    'Option Q: the reader you liked. The list now holds just the three Main Projects with a captioned thumb each; the pane beside it swaps when you choose one. History is the five years as one bar, then the timeline with marks on the trailing edge. Minor Projects close as bento tiles.',
    Q_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(6, pl(['H2', 'H3y'], 'left half: decision, years, title')), cell(3, pl(['H4', 'GL'], 'middle: About, then At a glance')), cell(3, pl(['H5'], 'right'))],
          [cell(4, pl(['ILl'], 'list pane, pinned'), sticky=True), cell(8, pl(['IPF1', 'IPX'], 'detail pane'))],
          [cell(6, pl(['X1'], 'left half')), gap(6)],
          [cell(12, pl(['TBh'], 'History heading, then the full-width bar'))],
          [gap(2), cell(7, pl(['LX2n'], 'timeline, marks trailing, cols 3–9', ['TYPE-01'])), gap(3)],
          [cell(12, pl(['MB'], 'full-width bento'))]]},
      FTR([cell(12, pl(['C1f'], 'footer'))])]))

R_ORDER = ['F0ry', 'GL', 'KCf', 'H4', 'H5', 'P0f', 'RC1', 'RC2', 'RC3', 'IPF1', 'IPF2', 'IPF3', 'X1', 'MT0f'] + [f'MT{i}' for i in range(1, 7)] + ['MB', 'FM']
options.append(opt('R', 'Credits hero + cards', 'Keeps round-2 K hero and Worked with · below it, three light cards side by side (round-1 E, less dense) with the full write-up opening under them',
    'Option R: the hero and the Worked with strip stay as you liked them, with At a glance beside the hero. Below, three light cards (decision, outcome, tools, a captioned visual); "Read the full write-up" opens the chosen project under the cards. History is the employer wall; Minor Projects are bento tiles.',
    R_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(8, pl(['F0ry'], 'hero, 8 columns', ['HIER-01'])), cell(4, pl(['GL'], 'beside the hero, after it in reading order'))],
          [cell(12, pl(['KCf'], 'Worked with strip, full width'))],
          [cell(6, pl(['H4'], 'left half')), cell(6, pl(['H5'], 'right half'))],
          [cell(12, pl(['P0f'], 'full-width heading'))],
          [cell(4, pl(['RC1'], 'card 1 of 3')), cell(4, pl(['RC2'], 'card 2 of 3')), cell(4, pl(['RC3'], 'card 3 of 3'))],
          [gap(2), cell(8, pl(['IPF1', 'IPX'], 'the chosen write-up, under the cards')), gap(2)],
          [gap(2), cell(8, pl(['X1'], 'cols 3–10')), gap(2)],
          [cell(12, pl(['MT0f'], 'wall heading'))],
          [cell(4, pl(['MT1'], 'wall row 1')), cell(4, pl(['MT2'], 'wall row 1')), cell(4, pl(['MT3'], 'wall row 1'))],
          [cell(4, pl(['MT4'], 'wall row 2')), cell(4, pl(['MT5'], 'wall row 2')), cell(4, pl(['MT6'], 'wall row 2'))],
          [cell(12, pl(['MB'], 'full-width bento'))],
          [cell(12, pl(['FM'], 'closing band'))]]},
      FTR([gap(2), cell(8, pl(['C1f'], 'footer, cols 3–10')), gap(2)])]))

S_ORDER = ['H2', 'H3y', 'GL', 'H4', 'H5', 'P0f', 'PF1', 'PF2', 'PF3', 'X1', 'X2f', 'M1f']
options.append(opt('S', 'Two-thirds + ambient third', 'GRID-02 (round-1 B) · the empty third beside the projects now holds ambient animated art (GRID-03: evens the density)',
    'Option S: round-1 B kept simple. Beside each Main Project, the trailing third is an ambient slot for an animated background or artistic detail, content-free, so nothing essential sits in the rail (SCAN-08). Each project carries a captioned figure right after its decision. Ambient slots are dropped at 320: decoration only, nothing lost (RESP-C2).',
    S_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(8, pl(['H2', 'H3y', 'GL', 'H4'], 'leading two-thirds', ['GRID-02'])), cell(4, pl(['H5'], 'trailing third, beside About', ['GRID-02']))],
          [cell(8, pl(['P0f'], 'leading two-thirds')), gap(4)]]
        + [[cell(8, pl([f'PF{n}'], 'leading two-thirds', ['GRID-02'])), cell(4, pl([f'AMB{n}'], 'trailing third, ambient', ['GRID-02', 'SCAN-08']), sticky=True)] for n in (1, 2, 3)]
        + [[cell(8, pl(['X1', 'X2f'], 'leading two-thirds', ['GRID-02'])), cell(4, pl(['M1f'], 'trailing third, beside the timeline', ['GRID-02', 'SCAN-08']), sticky=True)]]},
      FTR([cell(8, pl(['C1f'], 'footer, leading two-thirds'))])], margin=210))

T_ORDER = ['H2', 'H3y', 'GL', 'H4', 'H5', 'P0f', 'PF1', 'PF2', 'PF3', 'X1', 'CH0', 'TB'] + [x for i in range(1, 7) for x in (f'TS{i}', f'CH{i}c')]
T_ROWS = [
    [gap(3), cell(6, pl(['H2', 'H3y', 'GL', 'H4', 'H5'], 'content column, cols 4–9', ['GRID-01', 'TYPE-01'])), cell(3, pl(['AMB0'], 'trailing white space, ambient'))],
    [cell(3, pl(['P0f'], 'spine, beside the projects', ['GRID-01']), sticky=True), cell(6, pl(['PF1'], 'content column', ['GRID-01'])), cell(3, pl(['AMB1'], 'ambient'))],
    [gap(3), cell(6, pl(['PF2'], 'content column', ['GRID-01'])), cell(3, pl(['AMB2'], 'ambient'))],
    [gap(3), cell(6, pl(['PF3'], 'content column', ['GRID-01'])), cell(3, pl(['AMB3'], 'ambient'))],
    [gap(3), cell(6, pl(['X1'], 'content column')), gap(3)],
    [cell(3, pl(['CH0'], 'spine heading')), cell(6, pl(['TB'], 'the five years as one bar')), gap(3)],
] + [[cell(3, pl([f'TS{i}'], 'spine: mark, period, employer'), sticky=True), cell(6, pl([f'CH{i}c'], 'chapter body')),
      (cell(3, pl([{2: 'AMB4', 4: 'AMB5'}[i]], 'ambient beside the chapter')) if i in (2, 4) else gap(3))] for i in range(1, 7)]
options.append(opt('T', 'Chapters + ambient', 'GRP-05 employer chapters (round-1 C), structured · marks move into the spine; white space on the trailing side holds ambient art',
    'Option T: round-1 C, structured. A leading spine carries section labels and, in History, each employer\'s mark and period; the trailing white space holds ambient slots. Projects carry captioned figures; History opens with the five years as one bar. Ambient slots are dropped at 320.',
    T_ORDER, [HDR(), {'landmark': 'main', 'rows': T_ROWS},
      FTR([gap(3), cell(6, pl(['C1f'], 'footer, content column')), gap(3)])]))

used = set()
def walk(rows):
    for r in rows:
        if isinstance(r, dict) and 'rows' in r:
            walk(r['rows']); continue
        for c in (r['cells'] if isinstance(r, dict) else r):
            for it in c['blocks']:
                used.add(it if isinstance(it, str) else it['id'])
for o in options:
    for ab in o['artboards']:
        walk(ab['rows'])
blocks = {k: v for k, v in B.items() if k in used}
FAIL = json.load(open(ARGS4[2])) if len(ARGS4) > 2 and os.path.exists(ARGS4[2]) else {}
spec = {'title': 'Portfolio block-out · round 4', 'fold': {'320': 568, '1440': 765}, 'blocks': blocks,
        'options': options, 'failures': FAIL}
json.dump(spec, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('blocks', len(blocks), 'options', len(options))
