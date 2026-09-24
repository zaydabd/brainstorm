"""Writes spec.json for build_canvas.py: 5 options x (320, 1440) of the single-page portfolio."""
import json, sys

OUT = sys.argv[1]

# ---------- shared bits (neutral greys, system font only) ----------
def mark(org):
    return (f'<span style="display:inline-block;border:1px dashed #777777;background:#dddddd;'
            f'font-size:11px;line-height:16px;padding:1px 4px;margin-right:4px;color:#333333">Mark · {org}</span>')

def ph(what):
    return f'<span style="background:#e6e6e6;border:1px dashed #888888;padding:0 4px">[PLACEHOLDER: {what}]</span>'

LABEL = 'font-size:13px;color:#555555;font-weight:600;margin:0'
H2 = 'margin:0 0 8px;font-size:22px;line-height:1.2'
TAP = 'display:inline-flex;align-items:center;min-height:44px;min-width:44px;padding:0 8px'
SMALL = 'font-size:14px;color:#444444'

def field(label, value):
    return f'<div><dt style="{LABEL}">{label}</dt><dd style="margin:2px 0 0">{value}</dd></div>'

def main_project(anchor, name, org, decision, problem, tradeoff, role, outcome, tools):
    return (f'<h3 id="{anchor}" style="margin:0;font-size:22px;line-height:1.2">{name}</h3>'
            f'<p style="margin:4px 0 12px;{SMALL}">{org}</p>'
            f'<dl style="margin:0;display:grid;gap:10px">'
            + field('Decision', decision) + field('Problem', problem) + field('Trade-off', tradeoff)
            + field('Role and team', role) + field('Outcome', outcome) + field('Tools', tools)
            + '</dl>')

def minor_row(name, line, employer, tools):
    return (f'<li style="break-inside:avoid;padding:6px 0;border-top:1px solid #cccccc;font-size:14px">'
            f'<b>{name}</b> — {line}<br><span style="color:#555555">{employer} · {tools}</span></li>')

MINORS = [
    ('CAB-Q', 'Deployment approval tool. Cut a daily process from 6 hours to 30 minutes.', mark('Maybank') + 'Maybank', mark('OutSystems') + 'OutSystems O11'),
    ('Audit Log', 'Standardised audit logging, adopted across every OutSystems application.', mark('Maybank') + 'Maybank', mark('OutSystems') + 'OutSystems O11'),
    ('Tokenizer', 'Tokenisation for public display strings, with an encrypted database.', mark('Maybank') + 'Maybank', mark('OutSystems') + 'OutSystems O11'),
    ('MPowered', 'Internal agile project management platform. Stability and defect work.', mark('Maybank') + 'Maybank', mark('OutSystems') + 'OutSystems O11'),
    ('RPSST', 'Prototype to modernise legacy RBS transaction processes.', mark('Maybank') + 'Maybank', mark('OutSystems') + 'OutSystems O11'),
    ('VIP Dashboard', 'Visualisations of Sarawak data for a VIP presentation.', 'Impact Business Solutions', 'Power BI, QGIS'),
    ('QR Asset Management', 'QR-based asset tracking.', 'Impact Business Solutions', 'Flutter, Firebase'),
    ('Adam Digital Assets', 'Islamic mosque signage app, plus a website twin. Two developers shared requirements, design and build.', 'Adam Digital Assets', 'Flutter'),
]

def minor_list(rows):
    return ('<ul style="list-style:none;margin:0;padding:0;columns:240px;column-gap:24px">'
            + ''.join(minor_row(*r) for r in rows) + '</ul>')

def chapter_minor(rows):
    return (f'<p style="{LABEL};margin-top:8px">Minor Projects</p>'
            '<ul style="list-style:none;margin:0;padding:0">'
            + ''.join(f'<li style="padding:6px 0;border-top:1px solid #cccccc;font-size:14px"><b>{n}</b> — {l}'
                      f'<br><span style="color:#555555">{t}</span></li>' for n, l, _, t in rows) + '</ul>')

# ---------- doc lines (quoted from the inputs) ----------
D = {
    'nav': '"Italic-serif side nav … work … history … contact" (moodboard, Patterns); name "Wan Zayd Abdullah" (LinkedIn)',
    'decision': '"So the site describes his decisions first, such as row locking under enrolment load, and names the platform second." (proposal, intro)',
    'title': '"The site uses \'OutSystems Technical Lead\' throughout." (details, Rule 4); recruiter drop-off "Arrive, if the title is not obvious" (journey, Key moments)',
    'about': '"The hiring manager reads the About text and the title \'OutSystems Technical Lead\'." (journey, Hiring manager stage 2)',
    'quals': '"shows the five qualifications as minor items near the About text. It gives the detail of each one on demand." (details, Specs)',
    'projects': '"Counter beside the heading · Projects (3)" (moodboard, Patterns); "Three projects carry the engineering argument." (proposal)',
    'izone': '"Each gets a semi-detailed explanation: problem, decision, trade-off, role and team, outcome and tools." (proposal); Asked Q5 order',
    'df': '"Each gets a semi-detailed explanation: problem, decision, trade-off, role and team, outcome and tools." (proposal); Asked Q5 order',
    'mi': '"The technical lead notes that he was not the lead on MyInsights." (journey, Technical lead stage 2); Asked Q5 order',
    'how': '"How I work: one short paragraph, in his words, on architecture calls and running a team." (proposal)',
    'timeline': '"The timeline covers five years across five employers, newest first, with clients nested under their employer. Periods show month and year only" (proposal)',
    'minor': '"Eight Minor Projects sit in a less highlighted list. Each has a name, one line, its employer and its tools." (proposal)',
    'contact': '"Contact: email and LinkedIn. No CV download." (proposal)',
    'chapter': '"Page as timeline · Newest first. Each employer is a chapter holding its projects" (moodboard, Patterns)',
}

B = {}
def block(bid, name, html, rules, doc):
    B[bid] = {'name': name, 'html': html, 'rules': rules, 'doc': D[doc]}

block('H1', 'Header · skip link, identity, nav',
      '<a href="#main" style="font-size:13px;color:#555555">Skip to content (shows on focus)</a>'
      '<div style="display:flex;flex-wrap:wrap;align-items:center;gap:4px 16px;margin-top:4px">'
      f'<a href="#top" style="font-weight:700;font-size:18px;{TAP};padding:0">Wan Zayd Abdullah</a>'
      f'<nav aria-label="Sections" style="display:flex;flex-wrap:wrap;gap:4px">'
      f'<a href="#work" style="{TAP}">work</a><a href="#history" style="{TAP}">history</a><a href="#contact" style="{TAP}">contact</a></nav></div>',
      ['CONV-01', 'INT-16', 'CONV-04', 'A11Y-02', 'Asked Q4'], 'nav')

block('H2', 'Home · decision first',
      '<h1 style="font-size:32px;line-height:1.15;margin:0">Row locking under enrolment load</h1>'
      '<p style="margin:8px 0 0;font-size:18px">Load-tested at 40,000 enrolments over a sustained 20-minute window.</p>',
      ['SCAN-03', 'HIER-01', 'SCAN-01', 'PRIO-01'], 'decision')

block('H3', 'Home · title',
      '<p style="margin:0;font-size:20px;font-weight:600">OutSystems Technical Lead</p>',
      ['SCAN-01', 'PRIO-02', 'GRP-02'], 'title')

block('H4', 'Home · About',
      f'<h2 style="{LABEL}">About</h2><p style="margin:4px 0 0">{ph("About text, written by Wan Zayd; a decision comes before the platform name")}</p>',
      ['SCAN-03', 'PRIO-01'], 'about')

QUALS = [
    ('OutSystems Associate Developer Specialist (O11)', 'Issuer: OutSystems · Year: ' + ph('year')),
    ('OutSystems Associate Technical Lead (O11)', 'Issuer: OutSystems · Year: ' + ph('year')),
    ('Professional Scrum Developer', 'Issuer: ' + ph('issuer') + ' · Year: ' + ph('year')),
    ('Bachelor of Information System, Intelligent Systems Engineering', 'Universiti Teknologi MARA · 2019 – 2021'),
    ('Diploma in Computer Science', 'Universiti Teknologi MARA · 2015 – 2019'),
]
block('H5', 'Home · Qualifications (detail on tap)',
      f'<h2 style="{LABEL}">Qualifications (5)</h2>'
      + ''.join(f'<details{" open" if i == 0 else ""} style="border-top:1px solid #cccccc">'
                f'<summary style="padding:11px 0;font-size:15px">{n}</summary>'
                f'<p style="margin:0 0 10px 16px;{SMALL}">{d}</p></details>' for i, (n, d) in enumerate(QUALS)),
      ['PRIO-04', 'A11Y-01', 'GRP-02', 'Asked Q4'], 'quals')

block('P0', 'Project case study · section heading',
      f'<h2 id="work" style="{H2};font-size:26px">Projects <span style="color:#555555">(3)</span></h2>',
      ['HIER-02', 'SCAN-05'], 'projects')

block('P1', 'Project case study · iZone rebuild',
      main_project('izone', 'iZone rebuild', 'Sunway University · via ' + mark('AvePoint') + 'AvePoint',
                   'Row locking with SELECT FOR UPDATE on Aurora PostgreSQL for enrolment. He kept the legacy database structure as a local replica.',
                   'The legacy portal did not scale and crashed at every enrolment peak. The interface was old, and the client wanted it modernised. The old system counted submissions before commit, which fails under concurrency.',
                   'The replica was not well optimised. With a thin team, he developed as well as led, and he was stretched hard.',
                   'Senior Technical Lead and architecture owner, of three developers, himself included.',
                   'Deployed to live, not yet in use. Load-tested at 40,000 enrolments over a sustained 20-minute window.',
                   mark('OutSystems') + 'OutSystems ODC · Aurora PostgreSQL · Microsoft single sign-on · private gateway'),
      ['SCAN-10', 'SCAN-03', 'HIER-02', 'GRP-02', 'A11Y-04', 'Asked Q5'], 'izone')

block('P2', 'Project case study · Digital Form',
      main_project('digital-form', 'Digital Form', mark('Maybank') + 'Maybank',
                   'Extensible question types, so each MVP cycle added types and features and stabilised the platform.',
                   'No internal form platform existed. A vendor built forms, but no confidential item was allowed in them.',
                   'Each new question type added complexity.',
                   'Technical Lead, Product Owner and sole developer.',
                   'Used across Maybank. Over 80 forms by the fifth MVP, with thousands of submissions and users.',
                   mark('OutSystems') + 'OutSystems O11'),
      ['SCAN-10', 'SCAN-03', 'GRP-02', 'A11Y-04', 'Asked Q5'], 'df')

block('P3', 'Project case study · MyInsights',
      main_project('myinsights', 'MyInsights', mark('PETRONAS') + 'PETRONAS · via ' + mark('FPT Software') + 'FPT Software',
                   'A fixed set of roles, each tied to its business rules.',
                   'Auditors checked exceptions manually, on files and paper.',
                   'Low cost, in his account.',
                   'OutSystems developer in a team of four; not the lead. Built user management, permissions, front-end screens, part of the audit rule logic and part of the data sync.',
                   'Auditors centralised audit exceptions and processed them in the system, not on files and paper.',
                   mark('OutSystems') + 'OutSystems O11'),
      ['SCAN-10', 'SCAN-03', 'GRP-02', 'A11Y-04', 'Asked Q5'], 'mi')

block('X1', 'About/Experience · How I work',
      f'<h2 style="{H2}">How I work</h2><p style="margin:0">{ph("one short paragraph, in his words, on architecture calls and running a team")}</p>',
      ['PRIO-01', 'SCAN-05'], 'how')

TL = [
    ('Jan 2026 – present', mark('AvePoint') + '<b>AvePoint</b> · Full-stack developer · full-time',
     'Tools: ' + mark('OutSystems') + 'OutSystems ODC, Aurora PostgreSQL, Microsoft single sign-on, private gateway',
     'Apr 2026 – present · Sunway University · Senior Technical Lead'),
    ('Sep 2024 – Jan 2026', mark('Maybank') + '<b>Maybank</b> · Senior OS Engineer · full-time',
     'Tools: ' + mark('OutSystems') + 'OutSystems O11', None),
    ('May 2024 – Jul 2024', '<b>Adam Digital Assets</b> · Flutter Developer · part-time', None, None),
    ('Sep 2022 – Sep 2024', mark('FPT Software') + '<b>FPT Software Malaysia</b> · Software Consultant · contract',
     'Tools: ' + mark('OutSystems') + 'OutSystems O11',
     'Sep 2022 – Sep 2024 · ' + mark('PETRONAS') + 'PETRONAS Digital · OutSystems Developer'),
    ('Apr 2022 – Aug 2022', '<b>Career break</b> · Personal goal pursuit', None, None),
    ('Apr 2021 – May 2022', '<b>Impact Business Solutions</b> · Software Consultant · contract', 'Tools: Power BI, QGIS, Firebase', None),
]
def tl_item(period, org, tools, client):
    s = f'<li style="border-top:1px solid #cccccc;padding-top:8px"><p style="{LABEL}">{period}</p><p style="margin:2px 0 0">{org}</p>'
    if tools:
        s += f'<p style="margin:2px 0 0;{SMALL}">{tools}</p>'
    if client:
        s += f'<ol style="list-style:none;margin:6px 0 0 20px;padding:0"><li style="{SMALL}">↳ {client}</li></ol>'
    return s + '</li>'
block('X2', 'About/Experience · Timeline',
      f'<h2 id="history" style="{H2}">History</h2><ol style="list-style:none;padding:0;margin:0;display:grid;gap:10px">'
      + ''.join(tl_item(*t) for t in TL) + '</ol>',
      ['SCAN-10', 'GRP-05', 'GRP-02', 'A11Y-04', 'Asked Q2', 'Asked Q6'], 'timeline')

block('M1', 'Projects list · Minor Projects (less highlighted)',
      f'<h2 style="{H2};font-size:18px">Minor Projects <span style="color:#555555">(8)</span></h2>' + minor_list(MINORS),
      ['PRIO-01', 'SCAN-04', 'CPLX-04', 'GRP-02', 'TYPE-03', 'Asked Q6'], 'minor')

block('C1', 'Contact · email and LinkedIn (no form, no CV)',
      f'<h2 id="contact" style="{H2}">Contact</h2><p style="margin:0;display:flex;flex-wrap:wrap;gap:12px">'
      f'<a href="mailto:" style="{TAP};padding:0 12px;border:1px solid #666666;overflow-wrap:anywhere">Email · {ph("email address")}</a>'
      f'<a href="https://www.linkedin.com/in/wan-zayd-abdullah-690033230/" style="{TAP};padding:0 12px;border:1px solid #666666;overflow-wrap:anywhere">'
      f'LinkedIn · linkedin.com/in/wan-zayd-abdullah-690033230</a></p>',
      ['CONV-05', 'INT-11', 'A11Y-05', 'Asked Q4'], 'contact')

# ---------- option C: employer chapters ----------
block('CH0', 'About/Experience · History heading (chapters)',
      f'<h2 id="history" style="{H2}">History</h2><p style="margin:0;{SMALL}">Newest first · each employer holds its projects</p>',
      ['HIER-02', 'SCAN-10'], 'chapter')
CHAPTERS = [
    ('Jan 2026 – present', mark('AvePoint') + 'AvePoint',
     'Full-stack developer · full-time'
     f'<ol style="list-style:none;margin:6px 0 0 20px;padding:0"><li style="{SMALL}">↳ Apr 2026 – present · Sunway University · Senior Technical Lead</li></ol>'
     f'<p style="margin:8px 0 0">Main Project: <a href="#izone">iZone rebuild ↑</a></p>'
     f'<p style="margin:4px 0 0;{SMALL}">Tools: ' + mark('OutSystems') + 'OutSystems ODC, Aurora PostgreSQL, Microsoft single sign-on, private gateway</p>'),
    ('Sep 2024 – Jan 2026', mark('Maybank') + 'Maybank',
     'Senior OS Engineer · full-time'
     f'<p style="margin:8px 0 0">Main Project: <a href="#digital-form">Digital Form ↑</a></p>'
     + chapter_minor(MINORS[:5])
     + f'<p style="margin:8px 0 0;{SMALL}">Tools: ' + mark('OutSystems') + 'OutSystems O11</p>'),
    ('May 2024 – Jul 2024', 'Adam Digital Assets',
     'Flutter Developer · part-time' + chapter_minor(MINORS[7:8])),
    ('Sep 2022 – Sep 2024', mark('FPT Software') + 'FPT Software Malaysia',
     'Software Consultant · contract'
     f'<ol style="list-style:none;margin:6px 0 0 20px;padding:0"><li style="{SMALL}">↳ Sep 2022 – Sep 2024 · ' + mark('PETRONAS') + 'PETRONAS Digital · OutSystems Developer</li></ol>'
     f'<p style="margin:8px 0 0">Main Project: <a href="#myinsights">MyInsights ↑</a></p>'
     f'<p style="margin:4px 0 0;{SMALL}">Tools: ' + mark('OutSystems') + 'OutSystems O11</p>'),
    ('Apr 2022 – Aug 2022', 'Career break', 'Personal goal pursuit'),
    ('Apr 2021 – May 2022', 'Impact Business Solutions',
     'Software Consultant · contract' + chapter_minor(MINORS[5:7])),
]
for i, (period, org, body) in enumerate(CHAPTERS, 1):
    block(f'CH{i}s', f'History · chapter {i} spine (period, employer, mark)',
          f'<p style="{LABEL}">{period}</p><p style="margin:2px 0 0;font-weight:700">{org}</p>',
          ['GRP-05', 'SCAN-10', 'GRID-01', 'A11Y-04'], 'chapter')
    block(f'CH{i}c', f'History · chapter {i} role, clients, projects',
          f'<div style="margin:0">{body}</div>',
          ['GRP-05', 'GRP-02', 'PRIO-01', 'Asked Q2', 'Asked Q6'], 'chapter')

# ---------- layout helpers ----------
def cell(span, ids, **kw):
    c = {'span': span, 'blocks': ids}
    c.update(kw)
    return c
def gap(span):
    return {'span': span, 'blocks': []}
def P(bid, where, rules=None):
    p = {'id': bid, 'where': where}
    if rules:
        p['rules'] = rules
    return p

MASTER = ['H2', 'H3', 'H4', 'H5', 'P0', 'P1', 'P2', 'P3', 'X1', 'X2', 'M1']

def compact(order, header='H1', footer='C1'):
    return {'width': 320, 'margin': 16, 'rows': [
        {'landmark': 'header', 'rows': [[cell(12, [P(header, 'top, full width', ['CONV-01', 'INT-16', 'RESP-02', 'A11Y-02', 'Asked Q4'])])]]},
        {'landmark': 'main', 'rows': [[cell(12, [P(b, 'single column, master order', B[b]['rules'] + ['RESP-01']) for b in order])]]},
        {'landmark': 'footer', 'rows': [[cell(12, [P(footer, 'last, footer', B[footer]['rules'] + ['RESP-02'])])]]},
    ]}

answered = ('Answered: Q1 one page, your 5 pages = sections, 5 options · Q2 LinkedIn dates, CV roles · '
            'Q3 fold 765 / 568 · Q4 44×44 key controls · Q5 iZone, Digital Form, MyInsights · Q6 timeline, then Minor.')
task = ('Dominant task (SCAN-14): judge his engineering from the decisions, then decide to interview or contact '
        '(hiring manager, tech lead; desktop). Recruiter scans title, tools, tenure; designer peer browses on a phone. '
        'Goal-directed, so SCAN-01, -03, -07, -08 strict.\n'
        'Your 5 pages → sections: Home = H2–H5 · Project case study = P0–P3 · About/Experience = X1–X2 · '
        'Projects list = M1 · Contact = C1.\n')

options = []

# A · one reading column
options.append({'id': 'A', 'name': 'One reading column',
    'axis': 'TYPE-03: one column is read faster · moodboard Paco / Shu Ding',
    'note': task + 'Option A: every section in one capped column (cols 3–8 at 1440, TYPE-01 measure); header full width; '
            'Minor Projects flow into 2 text columns (Paco index).\n' + answered,
    'artboards': [compact(MASTER), {'width': 1440, 'margin': 80, 'rows': [
        {'landmark': 'header', 'rows': [[cell(12, [P('H1', 'top bar, identity leading, nav after it', ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]},
        {'landmark': 'main', 'rows': [[gap(2), cell(6, [P(b, 'one column, cols 3–8', B[b]['rules'] + ['TYPE-03', 'TYPE-01']) for b in MASTER]), gap(4)]]},
        {'landmark': 'footer', 'rows': [[gap(2), cell(6, [P('C1', 'footer, cols 3–8', B['C1']['rules'] + ['TYPE-03'])]), gap(4)]]},
    ]}]})

# B · two-thirds + one-third (minor items in the third)
options.append({'id': 'B', 'name': 'Two-thirds + a third for minor items',
    'axis': 'GRID-02 over TYPE-03 · the third holds Qualifications and Minor Projects',
    'note': task + 'Option B: primary content leads in cols 1–8; the trailing third holds only the minor items the docs call minor: '
            'Qualifications beside About, Minor Projects beside the timeline (SCAN-08: nothing essential in the rail). Page capped at 1020 px (GRID-01, GOV.UK max width) so the two-thirds keeps the TYPE-01 measure.\n' + answered,
    'artboards': [compact(MASTER), {'width': 1440, 'margin': 210, 'rows': [
        {'landmark': 'header', 'rows': [[cell(12, [P('H1', 'top bar', ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]},
        {'landmark': 'main', 'rows': [
            [cell(8, [P(b, 'leading two-thirds', B[b]['rules'] + ['GRID-02', 'HIER-01']) for b in ['H2', 'H3', 'H4']]),
             cell(4, [P('H5', 'trailing third, beside About', B['H5']['rules'] + ['GRID-02', 'SCAN-07'])])],
            [cell(8, [P(b, 'leading two-thirds', B[b]['rules'] + ['GRID-02', 'TYPE-01']) for b in ['P0', 'P1', 'P2', 'P3']]), gap(4)],
            [cell(8, [P(b, 'leading two-thirds', B[b]['rules'] + ['GRID-02']) for b in ['X1', 'X2']]),
             cell(4, [P('M1', 'trailing third, beside the timeline', B['M1']['rules'] + ['GRID-02', 'SCAN-08'])], sticky=True)],
        ]},
        {'landmark': 'footer', 'rows': [[cell(8, [P('C1', 'footer, leading two-thirds', B['C1']['rules'] + ['GRID-02'])]), gap(4)]]},
    ]}]})

# C · employer chapters
C_ORDER = ['H2', 'H3', 'H4', 'H5', 'P0', 'P1', 'P2', 'P3', 'X1', 'CH0'] + [f'CH{i}{s}' for i in range(1, 7) for s in 'sc']
C_ROWS_1440 = [
    [gap(3), cell(6, [P(b, 'content column, cols 4–9', B[b]['rules'] + ['GRID-01', 'TYPE-01']) for b in ['H2', 'H3', 'H4', 'H5']]), gap(3)],
    [cell(3, [P('P0', 'spine column, beside the projects', B['P0']['rules'] + ['GRID-01', 'GRP-02'])], sticky=True),
     cell(6, [P(b, 'content column', B[b]['rules'] + ['GRID-01', 'TYPE-01']) for b in ['P1', 'P2', 'P3']]), gap(3)],
    [gap(3), cell(6, [P('X1', 'content column', B['X1']['rules'] + ['GRID-01'])]), gap(3)],
    [cell(3, [P('CH0', 'spine column heading', B['CH0']['rules'] + ['GRID-01'])]), gap(9)],
] + [[cell(3, [P(f'CH{i}s', 'spine: period, employer, mark', None)], sticky=True),
      cell(6, [P(f'CH{i}c', 'chapter body beside its spine', None)]), gap(3)] for i in range(1, 7)]
options.append({'id': 'C', 'name': 'Employer chapters',
    'axis': 'GRP-05 nesting: Minor Projects sit inside their employer in the timeline (moodboard "Page as timeline")',
    'note': task + 'Option C: content in cols 4–9 (TYPE-01). Main Projects stay first (Q5); the timeline becomes chapters, newest first, each holding its Minor Projects '
            'and a link back to its Main Project. A leading spine column carries periods (moodboard scroll-ruler idea). '
            'Flutter now shows only on Minor Projects (rule 3).\n' + answered,
    'artboards': [compact(C_ORDER), {'width': 1440, 'margin': 80, 'rows': [
        {'landmark': 'header', 'rows': [[cell(12, [P('H1', 'top bar', ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]},
        {'landmark': 'main', 'rows': C_ROWS_1440},
        {'landmark': 'footer', 'rows': [[gap(3), cell(6, [P('C1', 'footer, content column', B['C1']['rules'] + ['GRID-01'])]), gap(3)]]},
    ]}]})

# D · pinned leading rail
options.append({'id': 'D', 'name': 'Pinned rail',
    'axis': 'CONV-04: leading rail instead of a top bar · moodboard "Pinned name beside a scrolling list"',
    'note': task + 'Option D: at 1440 the header (name + nav) pins in a leading rail, cols 1–3, while one capped column scrolls in cols 4–9. '
            'The rail never carries the title, so the decision still comes before the platform name. At 320 it is a top bar (RESP-02, INT-16).\n' + answered,
    'artboards': [compact(MASTER), {'width': 1440, 'margin': 80, 'rows': [
        [cell(3, [P('H1', 'leading rail, pinned', ['CONV-04', 'CONV-01', 'INT-16', 'A11Y-02', 'A11Y-03', 'Asked Q4'])], sticky=True, landmark='header'),
         cell(6, [P(b, 'scrolling column, cols 4–9', B[b]['rules'] + ['TYPE-01', 'TYPE-03']) for b in MASTER], landmark='main'), gap(3)],
        [gap(3), cell(6, [P('C1', 'footer, under the column', B['C1']['rules'] + ['TYPE-03'])], landmark='footer'), gap(3)],
    ]}]})

# E · side-by-side tiles
options.append({'id': 'E', 'name': 'Side-by-side tiles',
    'axis': 'PRIO-C1 "show everything" side by side vs TYPE-03 one column (multi-column is preferred, not faster)',
    'note': task + 'Option E: at 1440 sections sit side by side: Home in two columns, the three Main Projects as three columns '
            '(all three Main Projects start in viewport 1), How I work beside the timeline, Minor Projects as a 5-column index. '
            'Reads column by column (A11Y-01). For the expert reader (tech lead), PRIO-C1 favours the dense combined view.\n' + answered,
    'artboards': [compact(MASTER), {'width': 1440, 'margin': 80, 'rows': [
        {'landmark': 'header', 'rows': [[cell(12, [P('H1', 'top bar', ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]},
        {'landmark': 'main', 'rows': [
            [cell(6, [P(b, 'left half', B[b]['rules'] + ['A11Y-01']) for b in ['H2', 'H3']]),
             cell(6, [P(b, 'right half, read after the left', B[b]['rules'] + ['A11Y-01']) for b in ['H4', 'H5']])],
            [cell(12, [P('P0', 'full width heading', B['P0']['rules'])])],
            [cell(4, [P('P1', 'column 1 of 3', B['P1']['rules'] + ['PRIO-01', 'CPLX-03', 'A11Y-01'])]),
             cell(4, [P('P2', 'column 2 of 3', B['P2']['rules'] + ['CPLX-03', 'A11Y-01'])]),
             cell(4, [P('P3', 'column 3 of 3', B['P3']['rules'] + ['CPLX-03', 'A11Y-01'])])],
            [cell(6, [P('X1', 'left half', B['X1']['rules'] + ['A11Y-01'])]),
             cell(6, [P('X2', 'right half, read after How I work', B['X2']['rules'] + ['A11Y-01'])])],
            [cell(12, [P('M1', 'full width, multi-column index', B['M1']['rules'] + ['TYPE-03'])])],
        ]},
        {'landmark': 'footer', 'rows': [[cell(12, [P('C1', 'footer, full width', B['C1']['rules'])])]]},
    ]}]})


TOOLS = ('Journey, Recruiter stage 1 "Title and tools, right there": the title is in viewport 1, the first Tools field is not '
         '(P1 Tools at {y} px). Details forbid a separate stack list, so this is an open question, not a placement fix.')
PHONE = ('SCAN-01 / PRIO-02: at 320 only the decision headline and title fit above the fold (568). About starts at 602, '
         'the first Main Project decision at 1392 (viewport 3).')
FAIL = {
    'A-320': [PHONE, TOOLS.format(y=2101)],
    'B-320': [PHONE, TOOLS.format(y=2101)],
    'C-320': [PHONE, TOOLS.format(y=2101),
              'Asked Q6 met per chapter only: Minor Projects sit inside the timeline chapters, so a reader checking tenure passes 8 Minor rows.'],
    'D-320': [PHONE, TOOLS.format(y=2101)],
    'E-320': [PHONE, TOOLS.format(y=2101)],
    'A-1440': ['SCAN-01 / PRIO-02: the first Main Project decision starts at 1056 px, in viewport 2 (fold 765). Qualifications sit above it because the spec puts them "near the About text".',
               TOOLS.format(y=1477)],
    'B-1440': [TOOLS.format(y=1167),
               'GRID-03: the trailing third is empty beside the Main Projects and dense beside the timeline.'],
    'C-1440': ['SCAN-01 / PRIO-02: the first Main Project decision starts at 962 px, in viewport 2 (fold 765).',
               TOOLS.format(y=1384),
               'Asked Q6 met per chapter only: Minor Projects sit inside the timeline chapters, so a reader checking tenure passes 8 Minor rows.'],
    'D-1440': ['SCAN-01 / PRIO-02: the first Main Project decision starts at 930 px, in viewport 2 (fold 765).',
               TOOLS.format(y=1351)],
    'E-1440': ['TYPE-01: the three project columns measure about 42 characters per line, under the ~55 cpl comprehension figure.',
               'CPLX-01: 9 blocks start in viewport 1, the most of any option.',
               'SCAN-01: the three Main Projects start in viewport 1, but their Decision fields start at 782 px, just under the fold (765).',
               TOOLS.format(y=1324)],
}

spec = {'title': 'Portfolio block-out', 'fold': {'320': 568, '1440': 765}, 'blocks': B,
        'options': options, 'failures': FAIL}
json.dump(spec, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('blocks', len(B), 'options', len(options))
