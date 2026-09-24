"""Round 2: 8 radically different options (F-M) of the single-page portfolio, at 320 and 1440.
Reuses the shared blocks and helpers from make_spec.py."""
import json, sys, os

ARGS = sys.argv[:]
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_spec.py'), encoding='utf-8').read()
sys.argv = [sys.argv[0], '/dev/null']
exec(src[:src.index('answered = (')])          # blocks B, docs D, helpers cell/gap/P/compact, MINORS, TL, QUALS
OUT = ARGS[1]

# ---------- extra doc lines ----------
D.update({
    'card': '"work shown in a \\"01 / 04\\" carousel with tools on each project" (references, K2 Sousali)',
    'table_main': '"| Project | For | His role | Key decision | Outcome |" (proposal, The engineering)',
    'table_tl': '"| Period | Employer (client) | Role | Type |" (proposal, timeline table)',
    'table_minor': '"| Project | Employer | Tools | One line |" (proposal, Around the Main Projects)',
    'listdetail': '"Pages: Home, Projects list, Project case study, About/Experience, Contact" (your request)',
    'onescreen': '"One screen, no scroll. A dotted-leader contents list" (moodboard, Interactive and fun · Lynn Fisher)',
    'credits': '"Steady progression, banks and big clients." (journey, Hiring manager stage 4); "artistic layouts … showcase logos" (your message)',
    'spine': '"Work history 2013 to present with a logo beside each company" (references, #69 Alasdair Monk); "a mark appears wherever an employer or client with a vector file is named" (details, Rule 8)',
    'wall': '"album art, minimalist movie posters, bento layouts" (next-session brief); "An organisation with no vector file appears in type." (details, Rule 8)',
})

def bigmark(org, typeonly=False):
    if typeonly:
        return (f'<span style="display:inline-flex;align-items:center;justify-content:center;min-width:clamp(72px,9vw,128px);'
                f'height:clamp(40px,4.5vw,64px);padding:0 8px;border:1px solid #bbbbbb;background:#ffffff;font-weight:700;'
                f'font-size:13px;color:#333333;text-align:center">{org}<br>(in type)</span>')
    return (f'<span style="display:inline-flex;align-items:center;justify-content:center;width:clamp(72px,9vw,128px);'
            f'height:clamp(40px,4.5vw,64px);border:1px dashed #777777;background:#d6d6d6;font-size:12px;color:#333333;'
            f'text-align:center">Mark · {org}</span>')

DEC = {
    1: ('iZone rebuild', 'izone', 'Sunway University · via ' + mark('AvePoint') + 'AvePoint',
        'Row locking with SELECT FOR UPDATE on Aurora PostgreSQL for enrolment.',
        'He kept the legacy database structure as a local replica.'),
    2: ('Digital Form', 'digital-form', mark('Maybank') + 'Maybank',
        'Extensible question types, so each MVP cycle added types and features and stabilised the platform.', ''),
    3: ('MyInsights', 'myinsights', mark('PETRONAS') + 'PETRONAS · via ' + mark('FPT Software') + 'FPT Software',
        'A fixed set of roles, each tied to its business rules.', ''),
}
REST = {
    1: [('Problem', 'The legacy portal did not scale and crashed at every enrolment peak. The interface was old, and the client wanted it modernised. The old system counted submissions before commit, which fails under concurrency.'),
        ('Trade-off', 'The replica was not well optimised. With a thin team, he developed as well as led, and he was stretched hard.'),
        ('Role and team', 'Senior Technical Lead and architecture owner, of three developers, himself included.'),
        ('Outcome', 'Deployed to live, not yet in use. Load-tested at 40,000 enrolments over a sustained 20-minute window.'),
        ('Tools', mark('OutSystems') + 'OutSystems ODC · Aurora PostgreSQL · Microsoft single sign-on · private gateway')],
    2: [('Problem', 'No internal form platform existed. A vendor built forms, but no confidential item was allowed in them.'),
        ('Trade-off', 'Each new question type added complexity.'),
        ('Role and team', 'Technical Lead, Product Owner and sole developer.'),
        ('Outcome', 'Used across Maybank. Over 80 forms by the fifth MVP, with thousands of submissions and users.'),
        ('Tools', mark('OutSystems') + 'OutSystems O11')],
    3: [('Problem', 'Auditors checked exceptions manually, on files and paper.'),
        ('Trade-off', 'Low cost, in his account.'),
        ('Role and team', 'OutSystems developer in a team of four; not the lead. Built user management, permissions, front-end screens, part of the audit rule logic and part of the data sync.'),
        ('Outcome', 'Auditors centralised audit exceptions and processed them in the system, not on files and paper.'),
        ('Tools', mark('OutSystems') + 'OutSystems O11')],
}
SHORT = {  # the proposal's summary table
    1: ('Row locking for enrolment', 'Load-tested at 40,000 enrolments over a sustained 20-minute window; deployed to live',
        'Sunway University, via AvePoint', 'Senior Technical Lead of three developers, himself included',
        mark('OutSystems') + 'OutSystems ODC, Aurora PostgreSQL'),
    2: ('Extensible question types', 'Over 80 forms and thousands of users by the fifth MVP', mark('Maybank') + 'Maybank',
        'Technical Lead, Product Owner, sole developer', mark('OutSystems') + 'OutSystems O11'),
    3: ('Fixed roles tied to business rules', 'Audit exceptions moved from paper into the system',
        mark('PETRONAS') + 'PETRONAS, via ' + mark('FPT Software') + 'FPT Software', 'Developer in a team of four',
        mark('OutSystems') + 'OutSystems O11'),
}
def dl(fields, extra=''):
    return f'<dl style="margin:0;display:grid;gap:10px{extra}">' + ''.join(field(k, v) for k, v in fields) + '</dl>'

# ---------- F · title cards ----------
block('F0', 'Home · title card (decision, then title)',
      '<h1 style="font-size:clamp(34px,6vw,76px);line-height:1.05;margin:0;padding-top:clamp(8px,5vw,80px)">Row locking under enrolment load</h1>'
      '<p style="margin:16px 0 0;font-size:clamp(17px,1.6vw,22px)">Load-tested at 40,000 enrolments over a sustained 20-minute window.</p>'
      '<p style="margin:clamp(16px,3vw,40px) 0 clamp(32px,2vw,40px);font-size:20px;font-weight:600">OutSystems Technical Lead</p>',
      ['HIER-01', 'SCAN-03', 'CPLX-01', 'CPLX-02', 'PRIO-01'], 'decision')
for n in (1, 2, 3):
    name, anchor, org, dec, dec2 = DEC[n]
    block(f'FP{n}c', f'Project case study · {name} title card (decision as headline)',
          f'<p style="{LABEL}">0{n} / 03 · {name} · {org}</p>'
          f'<h3 id="{anchor}" style="font-size:clamp(24px,3.4vw,46px);line-height:1.1;margin:8px 0 0">{dec}</h3>'
          + (f'<p style="margin:8px 0 0;font-size:18px">{dec2}</p>' if dec2 else '')
          + '<div style="height:clamp(8px,3vw,40px)"></div>',
          ['HIER-02', 'SCAN-04', 'SCAN-03', 'CPLX-01', 'Asked Q5'], 'card')
    block(f'FP{n}r', f'Project case study · {name} fields', dl(REST[n]),
          ['GRP-02', 'A11Y-04', 'TYPE-01', 'Asked Q5'], ['izone', 'df', 'mi'][n - 1])

# ---------- G · contents sheet ----------
block('GI', 'Home · contents of the three Main Projects (decision, outcome, tools)',
      f'<h2 id="work" style="{H2}">Projects <span style="color:#555555">(3)</span></h2><ol style="list-style:none;margin:0;padding:0">'
      + ''.join(f'<li style="border-top:1px solid #cccccc;padding:8px 0"><a href="#{DEC[n][1]}" style="font-weight:700">{DEC[n][0]}</a>'
                f'<span style="color:#777777"> ······ </span>{SHORT[n][0]}'
                f'<p style="margin:2px 0 0;{SMALL}">{SHORT[n][1]} · {SHORT[n][2]} · {SHORT[n][4]}</p></li>' for n in (1, 2, 3))
      + '</ol>',
      ['PRIO-02', 'SCAN-10', 'SCAN-04', 'TYPE-03', 'Asked Q5'], 'table_main')

# ---------- H · data tables ----------
TH = 'text-align:left;vertical-align:top;padding:8px;border-bottom:1px solid #999999;font-size:14px'
TD = 'vertical-align:top;padding:8px;border-bottom:1px solid #cccccc;font-size:14px'
rows = [('Decision', {n: DEC[n][3] + (' ' + DEC[n][4] if DEC[n][4] else '') for n in (1, 2, 3)})] + \
       [(lab, {n: dict(REST[n])[lab] for n in (1, 2, 3)}) for lab in ('Problem', 'Trade-off', 'Role and team', 'Outcome', 'Tools')]
block('HT1', 'Project case study · the three Main Projects as one comparison table',
      '<div style="overflow-x:auto"><table style="border-collapse:collapse;min-width:860px;width:100%">'
      f'<thead><tr><th style="{TH};position:sticky;top:0;background:#f2f2f2;width:12%">Field</th>'
      + ''.join(f'<th id="{DEC[n][1]}" style="{TH};position:sticky;top:0;background:#f2f2f2">{DEC[n][0]}<br><span style="font-weight:400;{SMALL}">{DEC[n][2]}</span></th>' for n in (1, 2, 3))
      + '</tr></thead><tbody>'
      + ''.join(f'<tr><th scope="row" style="{TH}">{lab}</th>' + ''.join(f'<td style="{TD}">{vals[n]}</td>' for n in (1, 2, 3)) + '</tr>' for lab, vals in rows)
      + '</tbody></table></div><p style="margin:6px 0 0;font-size:13px;color:#555555">Scrolls sideways inside the table on a phone.</p>',
      ['SCAN-13', 'RESP-04', 'GRP-02', 'Asked Q5'], 'table_main')
tl_rows = [
    ('Jan 2026 – present', mark('AvePoint') + 'AvePoint', 'Full-stack developer', 'full-time', mark('OutSystems') + 'OutSystems ODC, Aurora PostgreSQL, Microsoft single sign-on, private gateway'),
    ('Apr 2026 – present', '↳ Sunway University', 'Senior Technical Lead', '—', ''),
    ('Sep 2024 – Jan 2026', mark('Maybank') + 'Maybank', 'Senior OS Engineer', 'full-time', mark('OutSystems') + 'OutSystems O11'),
    ('May 2024 – Jul 2024', 'Adam Digital Assets', 'Flutter Developer', 'part-time', ''),
    ('Sep 2022 – Sep 2024', mark('FPT Software') + 'FPT Software Malaysia', 'Software Consultant', 'contract', mark('OutSystems') + 'OutSystems O11'),
    ('Sep 2022 – Sep 2024', '↳ ' + mark('PETRONAS') + 'PETRONAS Digital', 'OutSystems Developer', '—', ''),
    ('Apr 2022 – Aug 2022', 'Career break', 'Personal goal pursuit', '—', ''),
    ('Apr 2021 – May 2022', 'Impact Business Solutions', 'Software Consultant', 'contract', 'Power BI, QGIS, Firebase'),
]
block('HT2', 'About/Experience · timeline as a table',
      f'<h2 id="history" style="{H2}">History</h2><div style="overflow-x:auto"><table style="border-collapse:collapse;min-width:760px;width:100%">'
      '<thead><tr>' + ''.join(f'<th style="{TH}">{h}</th>' for h in ('Period', 'Employer (client)', 'Role', 'Type', 'Tools')) + '</tr></thead><tbody>'
      + ''.join('<tr>' + ''.join(f'<td style="{TD}">{c}</td>' for c in r) + '</tr>' for r in tl_rows) + '</tbody></table></div>',
      ['SCAN-13', 'RESP-04', 'SCAN-10', 'GRP-05', 'Asked Q2', 'Asked Q6'], 'table_tl')
block('HT3', 'Projects list · Minor Projects as a table',
      f'<h2 style="{H2};font-size:18px">Minor Projects <span style="color:#555555">(8)</span></h2><div style="overflow-x:auto"><table style="border-collapse:collapse;min-width:760px;width:100%">'
      '<thead><tr>' + ''.join(f'<th style="{TH}">{h}</th>' for h in ('Project', 'One line', 'Employer', 'Tools')) + '</tr></thead><tbody>'
      + ''.join(f'<tr><th scope="row" style="{TH}">{a}</th><td style="{TD}">{b}</td><td style="{TD}">{c}</td><td style="{TD}">{d}</td></tr>' for a, b, c, d in MINORS)
      + '</tbody></table></div>',
      ['SCAN-13', 'RESP-04', 'SCAN-04', 'Asked Q6'], 'table_minor')

# ---------- I · list + detail ----------
CUR = ' aria-current="true"'
block('IL', 'Projects list · list pane (Main Projects, then Minor)',
      f'<h2 id="work" style="{H2}">Projects list <span style="color:#555555">(3 + 8)</span></h2><ol style="list-style:none;margin:0;padding:0">'
      + ''.join(f'<li style="border-top:1px solid #cccccc;padding:8px 0{";background:#e2e2e2" if n == 1 else ""}">'
                f'<a href="#{DEC[n][1]}" style="font-weight:700;{TAP};padding:0"{CUR if n == 1 else ""}>0{n} · {DEC[n][0]}</a>'
                f'<p style="margin:0;{SMALL}">{SHORT[n][0]}{" · reading now" if n == 1 else ""}</p></li>' for n in (1, 2, 3))
      + '</ol><ul style="list-style:none;margin:12px 0 0;padding:0">'
      + ''.join(f'<li style="border-top:1px solid #dddddd;padding:6px 0;font-size:14px"><b>{a}</b> — {b}<br><span style="color:#555555">{c} · {d}</span></li>' for a, b, c, d in MINORS)
      + '</ul>',
      ['RESP-06', 'SCAN-10', 'SCAN-04', 'Asked Q4', 'Asked Q5'], 'listdetail')
for n in (1, 2, 3):
    name, anchor, org, dec, dec2 = DEC[n]
    block(f'IP{n}', f'Project case study · {name} detail pane',
          f'<a href="#work" style="{TAP};padding:0;font-size:14px">← Projects list</a>'
          f'<div style="max-width:66ch"><h3 id="{anchor}" style="margin:4px 0 0;font-size:24px">{name}</h3><p style="margin:4px 0 12px;{SMALL}">{org}</p>'
          + dl([('Decision', dec + (' ' + dec2 if dec2 else ''))] + REST[n]) + '</div>',
          ['RESP-06', 'INT-10', 'GRP-02', 'A11Y-04', 'TYPE-01', 'Asked Q5'], 'listdetail')
block('IPX', 'Project case study · where Digital Form and MyInsights appear at 1440',
      f'<p style="margin:0;{SMALL}">Digital Form (IP2) and MyInsights (IP3) sit here in the same pane, hidden until chosen in the list (CSS :target, no script).</p>',
      ['RESP-06', 'PRIO-04'], 'listdetail')

# ---------- J · one-screen poster ----------
SUM = 'padding:11px 0;font-size:16px;font-weight:600'
for n in (1, 2, 3):
    name, anchor, org, dec, dec2 = DEC[n]
    block(f'JP{n}', f'Project case study · {name} (opens in place)',
          f'<details{" open" if n == 1 else ""} id="{anchor}"><summary style="{SUM}">{name} — {SHORT[n][0]}</summary>'
          f'<p style="margin:0 0 10px;{SMALL}">{org}</p>' + dl([('Decision', dec + (' ' + dec2 if dec2 else ''))] + REST[n]) + '</details>',
          ['PRIO-04', 'PRIO-C1', 'A11Y-01', 'SCAN-10', 'Asked Q4', 'Asked Q5'], 'onescreen')
block('JX1', 'About/Experience · How I work (opens in place)',
      f'<details><summary style="{SUM}">How I work</summary><p style="margin:0 0 10px">{ph("one short paragraph, in his words")}</p></details>',
      ['PRIO-04', 'A11Y-01', 'Asked Q4'], 'onescreen')
block('JX2', 'About/Experience · History (opens in place)',
      f'<details><summary style="{SUM}">History · Apr 2021 – present · five employers</summary>'
      '<ol style="list-style:none;padding:0;margin:0 0 10px;display:grid;gap:8px">' + ''.join(tl_item(*t) for t in TL) + '</ol></details>',
      ['PRIO-04', 'A11Y-01', 'SCAN-10', 'Asked Q2', 'Asked Q4', 'Asked Q6'], 'onescreen')
block('JM', 'Projects list · Minor Projects (opens in place)',
      f'<details><summary style="{SUM}">Minor Projects (8)</summary>' + minor_list(MINORS) + '</details>',
      ['PRIO-04', 'A11Y-01', 'Asked Q4', 'Asked Q6'], 'onescreen')

# ---------- K · credits strip ----------
block('KC', 'Home · credits strip of marks (newest first)',
      f'<p style="{LABEL};margin-bottom:8px">Worked with</p><div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center">'
      + bigmark('AvePoint') + bigmark('Sunway University', True) + bigmark('Maybank') + bigmark('Adam Digital Assets', True)
      + bigmark('FPT Software') + bigmark('PETRONAS') + bigmark('Impact Business Solutions', True) + '</div>',
      ['HIER-03', 'SCAN-12', 'SCAN-02', 'CPLX-01', 'SCAN-10'], 'credits')

# ---------- L · mark spine (marks on the trailing edge of every employer row) ----------
def spine_row(inner, marks):
    return (f'<div style="display:flex;gap:16px;justify-content:space-between;align-items:flex-start">'
            f'<div style="flex:1 1 auto;min-width:0">{inner}</div><div style="flex:0 0 auto;display:grid;gap:6px;justify-items:end">{marks}</div></div>')
LMK = {1: bigmark('AvePoint') + bigmark('Sunway University', True), 2: bigmark('Maybank'), 3: bigmark('PETRONAS') + bigmark('FPT Software')}
for n in (1, 2, 3):
    name, anchor, org, dec, dec2 = DEC[n]
    block(f'LP{n}', f'Project case study · {name} with its marks trailing',
          spine_row(f'<h3 id="{anchor}" style="margin:0;font-size:22px">{name}</h3><p style="margin:4px 0 0;{SMALL}">{org.replace(mark("AvePoint"), "").replace(mark("Maybank"), "").replace(mark("PETRONAS"), "").replace(mark("FPT Software"), "")}</p>', LMK[n])
          + '<div style="margin-top:12px">' + dl([('Decision', dec + (' ' + dec2 if dec2 else ''))] + REST[n]) + '</div>',
          ['SCAN-12', 'HIER-02', 'GRP-02', 'A11Y-04', 'Asked Q5'], 'spine')
TLM = [bigmark('AvePoint'), bigmark('Maybank'), bigmark('Adam Digital Assets', True), bigmark('FPT Software') + bigmark('PETRONAS'), '', bigmark('Impact Business Solutions', True)]
block('LX2', 'About/Experience · timeline with marks trailing each entry',
      f'<h2 id="history" style="{H2}">History</h2><ol style="list-style:none;padding:0;margin:0;display:grid;gap:10px">'
      + ''.join(f'<li style="border-top:1px solid #cccccc;padding-top:8px">' + spine_row(tl_item(*t)[len('<li style="border-top:1px solid #cccccc;padding-top:8px">'):-5], m) + '</li>'
                for t, m in zip(TL, TLM)) + '</ol>',
      ['SCAN-12', 'HIER-02', 'SCAN-10', 'GRP-05', 'Asked Q2', 'Asked Q6'], 'spine')

# ---------- M · employer wall (tiles) ----------
WALL = [
    (bigmark('AvePoint'), 'Jan 2026 – present', 'AvePoint · Full-stack developer · full-time', '↳ Sunway University · Apr 2026 – present · Senior Technical Lead', mark('OutSystems') + 'OutSystems ODC, Aurora PostgreSQL, Microsoft single sign-on, private gateway'),
    (bigmark('Maybank'), 'Sep 2024 – Jan 2026', 'Maybank · Senior OS Engineer · full-time', '', mark('OutSystems') + 'OutSystems O11'),
    (bigmark('Adam Digital Assets', True), 'May 2024 – Jul 2024', 'Adam Digital Assets · Flutter Developer · part-time', '', ''),
    (bigmark('FPT Software'), 'Sep 2022 – Sep 2024', 'FPT Software Malaysia · Software Consultant · contract', '↳ ' + mark('PETRONAS') + 'PETRONAS Digital · Sep 2022 – Sep 2024 · OutSystems Developer', mark('OutSystems') + 'OutSystems O11'),
    ('', 'Apr 2022 – Aug 2022', 'Career break · Personal goal pursuit', '', ''),
    (bigmark('Impact Business Solutions', True), 'Apr 2021 – May 2022', 'Impact Business Solutions · Software Consultant · contract', '', 'Power BI, QGIS, Firebase'),
]
block('MT0', 'About/Experience · History heading (wall)', f'<h2 id="history" style="{H2}">History</h2><p style="margin:0;{SMALL}">Newest first, one tile per employer</p>',
      ['HIER-02', 'SCAN-10'], 'wall')
for i, (mk, period, org, client, tools) in enumerate(WALL, 1):
    block(f'MT{i}', f'History · employer tile {i}',
          (f'<div style="margin-bottom:10px">{mk}</div>' if mk else '')
          + f'<p style="{LABEL}">{period}</p><p style="margin:2px 0 0;font-weight:600">{org}</p>'
          + (f'<p style="margin:6px 0 0 16px;{SMALL}">{client}</p>' if client else '')
          + (f'<p style="margin:6px 0 0;{SMALL}">Tools: {tools}</p>' if tools else ''),
          ['GRP-01', 'GRID-01', 'SCAN-10', 'GRP-05', 'Asked Q2'], 'wall')

# ---------- options ----------
HDR = lambda where='top bar': {'landmark': 'header', 'rows': [[cell(12, [P('H1', where, ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]}
FTR = lambda cells: {'landmark': 'footer', 'rows': [cells]}
def pl(ids, where, add=()):
    return [P(b, where, B[b]['rules'] + list(add)) for b in ids]

answered = ('Answered: Q1 one page, your 5 pages = sections · Q2 LinkedIn dates, CV roles · Q3 fold 765 / 568 · '
            'Q4 44×44 key controls · Q5 iZone, Digital Form, MyInsights · Q6 timeline, then Minor. '
            'Round 2 asks: radically different layouts; K–M showcase marks. Icons are not named in the docs, so none are drawn.')
task = ('Dominant task (SCAN-14): judge his engineering from the decisions, then decide to interview or contact '
        '(hiring manager, tech lead; desktop). Recruiter scans title, tools, tenure; designer peer browses on a phone. '
        'Goal-directed, so SCAN-01, -03, -07, -08 strict.\n')
def opt(i, name, axis, note, order, rows1440, margin=80):
    return {'id': i, 'name': name, 'axis': axis, 'note': task + note + '\n' + answered,
            'artboards': [compact(order), {'width': 1440, 'margin': margin, 'rows': rows1440}]}

options = []
F_ORDER = ['F0', 'H4', 'H5', 'FP1c', 'FP1r', 'FP2c', 'FP2r', 'FP3c', 'FP3r', 'X1', 'X2', 'M1']
options.append(opt('F', 'Title cards', 'CPLX-01: one idea per screen, fewest blocks · moodboard "Title-card entrance", Art of the Title',
    'Option F: every Main Project opens on its own title card whose headline IS the decision (SCAN-04), numbered 01 / 03. Home is one card: decision, then title. Type scales with width.',
    F_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(10, pl(['F0'], 'title card, cols 1–10', ['HIER-01'])), gap(2)],
          [gap(2), cell(6, pl(['H4', 'H5'], 'quiet column, cols 3–8', ['TYPE-01'])), gap(4)]]
        + [r for n in (1, 2, 3) for r in (
            [cell(10, pl([f'FP{n}c'], 'title card, cols 1–10')), gap(2)],
            [gap(2), cell(6, pl([f'FP{n}r'], 'fields under the card, cols 3–8')), gap(4)])]
        + [[gap(2), cell(6, pl(['X1', 'X2', 'M1'], 'cols 3–8', ['TYPE-01'])), gap(4)]]},
      FTR([cell(10, pl(['C1'], 'closing card'))])]))

G_ORDER = ['H2', 'H3', 'H4', 'H5', 'GI', 'X1', 'X2', 'M1', 'P0', 'P1', 'P2', 'P3']
options.append(opt('G', 'Contents sheet', 'PRIO-02: every entry point in viewport 1 · TYPE-03 columns for scannable lists · moodboard Paco, Practical Typography contents',
    'Option G: the top of the page is a dense contents sheet (the whole CV in 3 columns); the full Main Project write-ups follow as "the reading". Each contents row leads with the decision, then outcome, then tools.',
    G_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(5, pl(['H2', 'H3'], 'sheet, column 1: decision, then title')), cell(4, pl(['H4'], 'sheet, column 2')), cell(3, pl(['H5'], 'sheet, column 3', ['TYPE-03']))],
          [cell(4, pl(['GI'], 'sheet, column 1', ['TYPE-03'])), cell(4, pl(['X1', 'X2'], 'sheet, column 2', ['TYPE-03'])), cell(4, pl(['M1'], 'sheet, column 3', ['TYPE-03']))],
          [gap(2), cell(6, pl(['P0', 'P1', 'P2', 'P3'], 'the reading, cols 3–8', ['TYPE-01'])), gap(4)]]},
      FTR([gap(2), cell(6, pl(['C1'], 'footer, cols 3–8')), gap(4)])]))

H_ORDER = ['H2', 'H3', 'H4', 'H5', 'P0', 'HT1', 'X1', 'HT2', 'HT3']
options.append(opt('H', 'Data sheet', 'SCAN-13: fields as rows, projects as columns, labels far left · RESP-04: tables scroll inside themselves on a phone',
    'Option H: the proposal already sets the content as tables, so the page does too: one comparison table for the 3 Main Projects (sticky project header), a timeline table and a Minor Projects table.',
    H_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(6, pl(['H2', 'H3'], 'left half: decision, then title')), cell(3, pl(['H4'], 'middle')), cell(3, pl(['H5'], 'right'))],
          [cell(12, pl(['P0', 'HT1'], 'full width'))],
          [cell(6, pl(['X1'], 'left half', ['TYPE-01'])), gap(6)],
          [cell(12, pl(['HT2', 'HT3'], 'full width'))]]},
      FTR([cell(12, pl(['C1'], 'footer'))])]))

I_ORDER = ['H2', 'H3', 'H4', 'H5', 'IL', 'IP1', 'IP2', 'IP3', 'X1', 'X2']
options.append(opt('I', 'List + detail reader', 'RESP-06: list and detail side by side at 1440, one at a time at 320 · your "Projects list" and "Project case study"',
    'Option I: the Projects list pins on the left at 1440 and the chosen Main Project fills the right pane (iZone shown). At 320 the list comes first and each detail has a back link to it (INT-10). No medium artboard: at medium RESP-06 keeps one pane, as at 320.',
    I_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(6, pl(['H2', 'H3'], 'left half: decision, then title')), cell(3, pl(['H4'], 'middle')), cell(3, pl(['H5'], 'right'))],
          [cell(4, pl(['IL'], 'list pane, pinned'), sticky=True), cell(8, pl(['IP1', 'IPX'], 'detail pane'))],
          [cell(6, pl(['X1'], 'left half')), cell(6, pl(['X2'], 'right half'))]]},
      FTR([cell(12, pl(['C1'], 'footer'))])]))

J_ORDER = ['H2', 'H3', 'H4', 'H5', 'JP1', 'JP2', 'JP3', 'JX1', 'JX2', 'JM']
options.append(opt('J', 'One-screen poster', 'PRIO-04 / PRIO-C1: occasional readers get everything closed, opened in place · moodboard Lynn Fisher "One screen, no scroll"',
    'Option J: with every section closed the whole site fits about one screen; each Main Project, History, Minor Projects and How I work opens in place on tap (native details, no hover). iZone is drawn open.',
    J_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(7, pl(['H2', 'H3'], 'poster, left: decision, then title')), cell(5, pl(['H4', 'H5'], 'poster, right'))],
          [cell(7, pl(['JP1', 'JP2', 'JP3'], 'projects, left', ['TYPE-01'])), cell(5, pl(['JX1', 'JX2', 'JM'], 'the rest, right'))]]},
      FTR([cell(12, pl(['C1'], 'footer'))])]))

K_ORDER = ['F0', 'KC', 'H4', 'H5', 'P0', 'P1', 'P2', 'P3', 'X1', 'X2', 'M1']
options.append(opt('K', 'Credits poster (marks)', 'HIER-03: the salient marks sit after the decision, never above it · SCAN-12: one strip, one side · film-poster billing block',
    'Option K: a title card (decision, then title) and, under it, a credits strip of every employer and client, newest first: vector marks where they exist, names in type where not (Rule 8). The strip is the last thing in viewport 1. OutSystems stays with its employers, not in the strip (Rule 8).',
    K_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(10, pl(['F0'], 'title card, cols 1–10', ['HIER-01'])), gap(2)],
          [cell(12, pl(['KC'], 'credits strip, full width'))],
          [gap(2), cell(6, pl(['H4', 'H5', 'P0', 'P1', 'P2', 'P3', 'X1', 'X2', 'M1'], 'one column, cols 3–8', ['TYPE-01'])), gap(4)]]},
      FTR([gap(2), cell(6, pl(['C1'], 'footer, cols 3–8')), gap(4)])]))

L_ORDER = ['H2', 'H3', 'H4', 'H5', 'P0', 'LP1', 'LP2', 'LP3', 'X1', 'LX2', 'M1']
options.append(opt('L', 'Mark spine (marks)', 'SCAN-12: marks always on the trailing edge, text first (HIER-02) · references #69 "a logo beside each company"',
    'Option L: every row that names an employer or client carries its marks, large, on the trailing edge, so the marks form a vertical spine down the right of the column. Orgs with no vector file sit in type in the same slot. Moodboard idea: marks grey until touched, then their own colours.',
    L_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [[gap(2), cell(7, pl(L_ORDER, 'one column with a mark spine, cols 3–9', ['TYPE-01'])), gap(3)]]},
      FTR([gap(2), cell(7, pl(['C1'], 'footer, cols 3–9')), gap(3)])]))

M_ORDER = ['H2', 'H3', 'H4', 'H5', 'P0', 'P1', 'P2', 'P3', 'X1', 'MT0'] + [f'MT{i}' for i in range(1, 7)] + ['M1']
options.append(opt('M', 'Employer wall (marks)', 'GRP-01: one bounded tile per employer, clients nested inside (GRP-05) · brief "bento layouts"',
    'Option M: History becomes a wall of employer tiles, newest first, read row by row: mark (or name in type), period, role, nested client, tools. The rest reads as one column.',
    M_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [gap(2), cell(6, pl(['H2', 'H3', 'H4', 'H5', 'P0', 'P1', 'P2', 'P3', 'X1'], 'one column, cols 3–8', ['TYPE-01'])), gap(4)],
          [cell(12, pl(['MT0'], 'wall heading'))],
          [cell(4, pl(['MT1'], 'wall row 1')), cell(4, pl(['MT2'], 'wall row 1')), cell(4, pl(['MT3'], 'wall row 1'))],
          [cell(4, pl(['MT4'], 'wall row 2')), cell(4, pl(['MT5'], 'wall row 2')), cell(4, pl(['MT6'], 'wall row 2'))],
          [gap(2), cell(6, pl(['M1'], 'cols 3–8')), gap(4)]]},
      FTR([gap(2), cell(6, pl(['C1'], 'footer, cols 3–8')), gap(4)])]))

# drop blocks this canvas does not place
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

FAIL = json.load(open(ARGS[2])) if len(ARGS) > 2 and os.path.exists(ARGS[2]) else {}
spec = {'title': 'Portfolio block-out · round 2', 'fold': {'320': 568, '1440': 765}, 'blocks': blocks,
        'options': options, 'failures': FAIL}
json.dump(spec, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('blocks', len(blocks), 'options', len(options))
