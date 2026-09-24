"""Round 7: option PS kept. Humbler first-person copy (plain words, team credited), Worked with as a
right-to-left strip of fixed height, a sideways poster shelf on phones with one set of notes, and the history
bar stacking into full-width rows on phones. Reuses blocks from make_spec6.py (and, through it, rounds 1-5)."""
import json, sys, os

ARGS7 = sys.argv[:]
src6 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_spec6.py'), encoding='utf-8').read()
sys.argv = [sys.argv[0], '/dev/null']
exec(src6[:src6.index('\n# ---------- options ----------')])
OUT = ARGS7[1]

D.update({
    'humble': '"Once the site exists, Wan Zayd owns a document that describes him in his own voice." (details); '
              '"Change them to something bit more humble less slop" (your feedback, round 6)',
    'marquee_kc': '"the worked with should be a animated carousel like where by it goes from right to left showcaing all the companies i worked with '
                  'so on mobile it is also the fixed height" (your feedback, round 6); WCAG 2.2.2 Pause, Stop, Hide: moving content that '
                  'starts on its own and lasts over 5 seconds needs a way to pause it',
    'shelf_m': '"for mobile the project section is weird" (your feedback, round 6); RESP-06 "List–detail shows two panes when wide and one at a time when narrow"',
    'hist_m': '"for mobile the history needs work.." (your feedback, round 6); "Sep 2024 - Jan 2026 · 1 yr 5 mos" (LinkedIn)',
})

# ---------- hero: the iZone decision in his own words, team credited ----------
block('F0h', 'Home · title card: the iZone decision in his own words, then years and title',
      '<div style="position:relative">'
      '<div style="position:absolute;inset:0;border:2px dashed #aaaaaa;background:repeating-linear-gradient(120deg,#ececec 0 18px,#f6f6f6 18px 36px)"></div>'
      '<div style="position:relative;padding:12px">'
      '<h1 style="font-size:clamp(22px,3vw,44px);line-height:1.15;margin:0;padding-top:clamp(4px,3vw,48px);max-width:26ch">'
      'Enrolment crashed at every peak, so my team and I rebuilt it around row locking.</h1>'
      '<p style="margin:14px 0 0;font-size:clamp(16px,1.5vw,20px)">A university portal, load-tested with 40,000 enrolments over 20 minutes.</p>'
      '<p style="margin:clamp(16px,3vw,40px) 0 0;font-size:15px;font-weight:700">5 years · since Apr 2021</p>'
      '<p style="margin:4px 0 clamp(24px,2vw,40px);font-size:20px;font-weight:600">OutSystems Technical Lead</p>'
      + fun('light rays behind this card follow the pointer · off on touch and reduced motion') + LIVE + '</div></div>',
      ['HIER-01', 'HIER-04', 'SCAN-03', 'PRIO-02', 'PRIO-01'], 'humble')

block('GLh', 'Home · At a glance, plain counts',
      f'<h2 style="{LABEL};margin-bottom:8px">At a glance</h2><ul style="list-style:none;margin:0;padding:0;display:grid;gap:6px">'
      + ''.join(f'<li><strong style="font-size:20px">{a}</strong> <span style="color:#444444">{b}</span></li>'
                for a, b in (('5', 'employers'), ('11', 'projects, 3 in detail'), ('5', 'qualifications'))) + '</ul>',
      ['SCAN-01', 'CPLX-03', 'GRP-02', 'CPLX-01'], 'humble')

# ---------- Worked with: one fixed-height strip drifting right to left ----------
KC_SET = (bigmark('AvePoint') + bigmark('Sunway University', True) + bigmark('Maybank') + bigmark('Adam Digital Assets', True)
          + bigmark('FPT Software') + bigmark('PETRONAS') + bigmark('Impact Business Solutions', True))
block('KCm', 'Home · Worked with, a fixed-height strip drifting right to left, with Pause',
      '<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:6px">'
      f'<h2 style="{LABEL}">Worked with</h2>'
      f'<button type="button" aria-pressed="false" style="{TAP};border:1px solid #666666;background:#ffffff;font:inherit;font-size:14px">Pause</button></div>'
      '<div style="height:88px;overflow-x:auto;scrollbar-width:none;display:flex;align-items:center;border-block:1px solid #bbbbbb;'
      'mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent)">'
      f'<div style="display:flex;align-items:center;gap:32px;width:max-content;padding:0 24px">{KC_SET}'
      f'<span aria-hidden="true" style="display:contents">{KC_SET}</span></div></div>'
      + '<p style="margin:8px 0 0">' + fun('drifts right to left in a loop · same 88 px height on phone and desktop · pauses on hover, focus or Pause · '
                                            'the second set is a copy for the loop, hidden from screen readers · under reduced motion it stands still and swipes') + '</p>',
      ['GRP-01', 'A11Y-04', 'INT-15', 'RESP-04', 'SCAN-10'], 'marquee_kc')

block('P0h', 'Project case study · heading with one plain line on what each project covers',
      B['P0']['html'] + f'<p style="margin:0 0 8px;{SMALL}">Three projects, each with what was wrong, what we chose and what it cost.</p>'
      + fun('each project rises in as it enters view · text visible from first paint'),
      ['HIER-02', 'SCAN-03', 'SCAN-05'], 'humble')

# ---------- Main Projects: poster shelf, sideways on phones, one set of notes below ----------
TITLE7 = {1: 'Row locking for enrolment', 2: 'Question types added one MVP at a time', 3: 'A fixed set of roles, each with its own rules'}
CRED7 = {1: 'I led a team of three', 2: 'Just me: lead, product owner and developer', 3: 'One of four developers'}
def poster7(n):
    name, anchor, org, dec, dec2 = DEC[n]
    sel = n == 1
    return (f'<a href="#notes-{anchor}"{CUR if sel else ""} style="scroll-snap-align:start;display:flex;flex-direction:column;aspect-ratio:2/3;'
            f'border:{"3px solid #1f1f1f" if sel else "1px solid #999999"};background:#ffffff;color:#1f1f1f;text-decoration:none;padding:14px;gap:8px">'
            f'<span style="font-size:40px;font-weight:800;line-height:1;color:#888888">0{n}</span>'
            f'<span style="flex:1 1 auto;min-height:72px;border:2px dashed #888888;{STRIPE};display:flex;align-items:flex-end;padding:6px;font-size:11px;color:#333333">'
            f'[PLACEHOLDER: poster art · {FIGSHORT[n]} · drawn in code]</span>'
            f'<span style="font-size:clamp(19px,1.6vw,24px);font-weight:800;line-height:1.15">{TITLE7[n]}</span>'
            f'<span style="font-weight:600">{name}</span>'
            f'<span style="font-size:13px;color:#444444">{CRED7[n]} · {SHORT[n][4]}</span></a>')
block('PS7', 'Project case study · the three Main Projects as a poster shelf; sideways on a phone, the next poster peeking in',
      fun('posters lift on hover or tap; the chosen one stays raised')
      + tag('PHONE', 'the shelf scrolls sideways and snaps; the next poster peeks in')
      + '<div role="region" aria-label="Projects" tabindex="0" style="display:grid;grid-template-columns:repeat(3,minmax(220px,1fr));gap:16px;'
        'overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:8px">' + ''.join(poster7(n) for n in (1, 2, 3)) + '</div>',
      ['SCAN-10', 'SCAN-02', 'CPLX-03', 'HIER-01', 'RESP-04', 'Asked Q4', 'Asked Q5'], 'shelf_m')

TOOLS7 = {n: dict(REST[n])['Tools'] for n in (1, 2, 3)}
NOTES7 = {
    1: [('The problem', 'The old portal crashed at every enrolment peak. It counted submissions before they were committed, which breaks when many people '
                        'submit at once. The interface was old too, and the client wanted it modernised.'),
        ('The choice', 'Row locking (SELECT FOR UPDATE on Aurora PostgreSQL) for enrolment. I also kept the old database structure as a local replica.'),
        ('What it cost', 'The replica wasn\'t well optimised. The team was small, so I wrote code as well as leading, and that stretched me.'),
        ('What happened', 'It\'s live, but not in use yet. It was load-tested with 40,000 enrolments over 20 minutes.'),
        ('My part', 'Senior Technical Lead. I owned the architecture and worked with two developers, one junior and one mid-level.'),
        ('Tools', TOOLS7[1])],
    2: [('The problem', 'Maybank had no internal form platform. A vendor built the forms, and nothing confidential could go in them.'),
        ('The choice', 'Question types built to be extended, so each MVP added new types and features and made the platform more stable.'),
        ('What it cost', 'Each new question type added complexity.'),
        ('What happened', 'Used across Maybank. By the fifth MVP it had over 80 forms, with thousands of submissions and users.'),
        ('My part', 'I was the only developer, and also the Technical Lead and Product Owner.'),
        ('Tools', TOOLS7[2])],
    3: [('The problem', 'Auditors checked exceptions by hand, on files and paper.'),
        ('The choice', 'A fixed set of roles, each tied to its own business rules.'),
        ('What it cost', 'Not much, as far as I could see.'),
        ('What happened', 'Auditors moved audit exceptions into one place and worked through them in the system, not on files and paper.'),
        ('My part', 'One of four developers; I wasn\'t the lead. I built user management, permissions and front-end screens, '
                    'and parts of the audit rules and the data sync.'),
        ('Tools', TOOLS7[3])],
}
for n in (1, 2, 3):
    name, anchor, org, dec, dec2 = DEC[n]
    block(f'PSD7_{n}', f'Project case study · {name} notes, opened under the shelf',
          f'<div id="notes-{anchor}"><p style="{LABEL}">0{n} / 03</p><h3 id="{anchor}" style="margin:4px 0 0;font-size:24px">{name}</h3>'
          f'<p style="margin:4px 0 12px;{SMALL}">{org}</p>' + dl(NOTES7[n], ';max-width:48ch') + '</div>',
          ['A11Y-01', 'PRIO-04', 'RESP-06', 'TYPE-01', 'Asked Q5'], 'humble')
block('PSX7', 'Project case study · where the other notes open, at every width',
      f'<p style="margin:0;{SMALL}">Picking 02 or 03 swaps these notes for that project, on phone and desktop alike (CSS :target, no script).</p>',
      ['PRIO-04', 'RESP-06', 'A11Y-01'], 'shelf_m')

# ---------- History: one bar on desktop, full-width rows on a phone ----------
DUR = {'h-avepoint': '9 mos', 'h-maybank': '1 yr 5 mos', 'h-fpt': '2 yrs 1 mo', 'h-break': '5 mos', 'h-impact': '1 yr 2 mos'}
SEG7 = [  # anchor, months, mark html, name, period, role, client
    ('h-avepoint', 9, mark('AvePoint'), 'AvePoint', 'Jan 2026 – present', 'Full-stack developer', 'Sunway University'),
    ('h-maybank', 17, mark('Maybank'), 'Maybank', 'Sep 2024 – Jan 2026', 'Senior OutSystems Engineer', ''),
    ('h-fpt', 25, mark('FPT Software'), 'FPT Software Malaysia', 'Sep 2022 – Sep 2024', 'Software Consultant', mark('PETRONAS') + 'PETRONAS Digital'),
    ('h-break', 5, '', 'Career break', 'Apr 2022 – Aug 2022', 'Time for personal goals', ''),
    ('h-impact', 14, '', 'Impact Business Solutions', 'Apr 2021 – May 2022', 'Software Consultant', ''),
]
def seg7(i, s):
    a, m, mk, name, period, role, client = s
    sel = i == 0
    bg, fg = ('#333333', '#ffffff') if sel else ('#dddddd', '#1f1f1f')
    chip = ''
    if a == 'h-fpt':
        chip = (f'<a href="#h-adam" style="display:flex;align-items:center;min-height:44px;margin-top:2px;padding:0 12px;'
                f'border:1px dashed #555555;background:#ffffff;color:#1f1f1f;font-size:13px">+ Adam Digital Assets · May – Jul 2024 · 3 mos · part-time</a>')
    return (f'<li style="flex:{m} 1 0;min-width:min(100%,150px);display:flex;flex-direction:column">'
            f'<a href="#{a}"{CUR if sel else ""} style="flex:1 1 auto;display:block;min-height:44px;padding:10px 12px;background:{bg};color:{fg};text-decoration:none">'
            f'<span style="display:block;font-size:12px;font-weight:600">{period} · {DUR[a]}</span>'
            f'<span style="display:block;font-weight:700;margin-top:2px">{mk}{name}</span>'
            f'<span style="display:block;font-size:13px;margin-top:2px">{role}</span>'
            + (f'<span style="display:block;font-size:13px;margin-top:2px">↳ {client}</span>' if client else '')
            + f'<span aria-hidden="true" style="display:block;margin-top:8px;height:clamp(0px,calc((400px - 100cqw) * 999),4px);width:{m * 9}px;max-width:100%;'
              f'background:currentColor;border-radius:0 2px 2px 0"></span></a>{chip}</li>')
block('HB7', 'History · one bar on desktop (segments sized by months); on a phone the segments stack as rows, each with a length bar',
      f'<h2 id="history" style="{H2}">History</h2>'
      f'<p style="margin:0 0 10px;{SMALL}">Pick a period to see more.</p>'
      '<ol style="list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:2px;container-type:inline-size">'
      + ''.join(seg7(i, s) for i, s in enumerate(SEG7)) + '</ol>'
      + '<p style="margin:8px 0 0">' + tag('PHONE', 'rows stack newest first; the bar in each row is its length, 9 px a month')
      + tag('LIVE', 'AvePoint\'s months grow with "present"; periods and months come from LinkedIn') + '</p>',
      ['SCAN-10', 'GRP-03', 'INT-12', 'RESP-03', 'RESP-05', 'Asked Q2', 'Asked Q4'], 'hist_m')

block('HP7', 'History · the chosen period, opened under the bar (AvePoint by default)',
      f'<div id="h-avepoint" style="border-top:2px solid #333333;padding-top:12px">'
      f'<div style="display:flex;gap:16px;justify-content:space-between;align-items:flex-start;flex-wrap:wrap">'
      f'<div><p style="{LABEL}">Jan 2026 – present · full-time</p><h3 style="margin:4px 0 0;font-size:22px">AvePoint · Full-stack developer</h3></div>'
      f'{bigmark("AvePoint")}</div>'
      f'<p style="margin:10px 0 0">↳ Sunway University, client · Apr 2026 – present · Senior Technical Lead</p>'
      f'<p style="margin:6px 0 0">Project in this period: <a href="#izone" style="{TAP};padding:0">iZone rebuild ↑</a></p>'
      f'<p style="margin:0;{SMALL}">Tools: ' + mark('OutSystems') + 'OutSystems ODC, Aurora PostgreSQL, Microsoft single sign-on, private gateway</p>'
      f'<a href="#history" style="{TAP};padding:0;margin-top:6px">↑ All periods</a></div>'
      f'<p style="margin:12px 0 0;font-size:13px;color:#555555">Maybank, FPT Software (with PETRONAS Digital), Adam Digital Assets, the career break and Impact '
      f'each have a panel here, shown only when picked (CSS :target, no script). On a phone, picking a row scrolls to its panel.</p>',
      ['A11Y-01', 'A11Y-04', 'GRP-05', 'PRIO-04', 'RESP-06', 'Asked Q2'], 'hist_m')

block('C1h', 'Contact · one plain line, email copies on click',
      B['C1']['html'].replace('</h2>', '</h2>' + '<p style="margin:0 0 10px">Happy to talk about any of this.</p>', 1)
      + '<p style="margin:8px 0 0">' + fun('click Email to copy it · "Copied" appears next to it') + '</p>',
      B['C1']['rules'] + ['INT-12', 'A11Y-04'], 'humble')

# ---------- options ----------
HDR = lambda: {'landmark': 'header', 'rows': [[cell(12, [P('H1', 'top bar', ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]}
FTR = lambda cells: {'landmark': 'footer', 'rows': [cells]}
def pl(ids, where, add=()):
    return [P(b, where, B[b]['rules'] + list(add)) for b in ids]

answered = ('Answered: Q1 one page, 5 sections · Q2 LinkedIn dates, CV roles · Q3 fold 765 / 568 · Q4 44×44 · '
            'Q5 iZone, Digital Form, MyInsights · Q6 timeline, then Minor. Round 7 feedback: keep PS; humbler, less sloppy copy; '
            'Worked with as a right-to-left strip, fixed height on phones; fix the phone Projects and History.')
task = ('Dominant task (SCAN-14): judge his engineering from the decisions, then decide to interview or contact '
        '(hiring manager, tech lead; desktop). Recruiter scans title, tools, tenure; designer peer browses on a phone.\n')
TOP = ['F0h', 'GLh', 'KCm', 'H4', 'H5', 'P0h']
MAIN = ['PS7', 'PSD7_1', 'PSX7']
END = ['X1', 'HB7', 'HP7', 'MB2', 'FM']
rows1440 = ([[cell(8, pl(['F0h'], 'hero, 8 columns', ['HIER-01'])), cell(4, pl(['GLh'], 'beside the hero, after it in reading order'))],
             [cell(12, pl(['KCm'], 'Worked with strip, full width'))],
             [cell(6, pl(['H4'], 'left half')), cell(6, pl(['H5'], 'right half'))],
             [cell(12, pl(['P0h'], 'full-width heading'))],
             [cell(12, pl(['PS7'], 'full-width shelf'))],
             [gap(2), cell(8, pl(['PSD7_1', 'PSX7'], 'notes, under the shelf')), gap(2)],
             [gap(2), cell(8, pl(['X1'], 'cols 3–10')), gap(2)],
             [cell(12, pl(['HB7'], 'full-width history bar'))],
             [gap(2), cell(8, pl(['HP7'], 'the chosen period, directly under the bar'))],
             [cell(12, pl(['MB2'], 'full-width bento'))],
             [cell(12, pl(['FM'], 'closing band'))]])
note = ('Option PS, round 7. Copy is first person and plain: the team gets credit, and the labels say what was wrong, the choice, '
        'what it cost, what happened, and his part. All facts are unchanged from the CV, LinkedIn and the details doc; only the wording is new, '
        'so every sentence is a draft for Wan Zayd to approve. Worked with drifts right to left in one 88 px strip at every width, with a Pause button. '
        'On a phone the poster shelf scrolls sideways and one set of notes sits under it; the history bar stacks into full-width rows, '
        'each with a length bar, and the picked period opens below.')
options = [{'id': 'PS', 'name': 'R3 · poster shelf, humbler copy', 'axis': 'Round-6 PS with first-person copy and the three phone fixes',
            'note': task + note + '\n' + answered,
            'artboards': [compact(TOP + MAIN + END, footer='C1h'),
                          {'width': 1440, 'margin': 80, 'rows': [HDR(), {'landmark': 'main', 'rows': rows1440},
                                                                 FTR([gap(2), cell(8, pl(['C1h'], 'footer, cols 3–10')), gap(2)])]}]}]

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
FAIL = json.load(open(ARGS7[2])) if len(ARGS7) > 2 and os.path.exists(ARGS7[2]) else {}
spec = {'title': 'Portfolio block-out · round 7', 'fold': {'320': 568, '1440': 765}, 'blocks': blocks,
        'options': options, 'failures': FAIL}
json.dump(spec, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('blocks', len(blocks), 'options', len(options))
