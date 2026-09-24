"""Round 6: R3 kept; the history becomes a clickable segmented bar with one panel below;
Main Projects get three artistic treatments (storyboard, annotated diagram, poster shelf).
Reuses blocks from make_spec5.py (and, through it, rounds 1-4)."""
import json, sys, os

ARGS6 = sys.argv[:]
src5 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_spec5.py'), encoding='utf-8').read()
sys.argv = [sys.argv[0], '/dev/null']
exec(src5[:src5.index('\n# ---------- options ----------')])
OUT = ARGS6[1]

D.update({
    'histbar': '"if i click that segment then it shows that history at the bottom instead of showing all . the history bar should have enough info per segment" (your feedback, round 5); "Sep 2024 - Jan 2026 · 1 yr 5 mos" (LinkedIn)',
    'storyboard': '"a filmstrip of grayscale slices; the hovered slice turns to colour while its neighbours stay grey" (moodboard, Aristide Benoist); "Feel: cinematic but calm" (references, Brief)',
    'posters': '"album art, minimalist movie posters, bento layouts" (next-session brief); "anything else artistic?" (your feedback, round 5)',
})

# ---------- history: segmented bar (newest first, sized by months) + one panel below ----------
SEG = [  # anchor, months, mark html, name, period, role
    ('h-avepoint', 9, mark('AvePoint'), 'AvePoint', 'Jan 2026 – present', 'Full-stack developer · ↳ Sunway University'),
    ('h-maybank', 17, mark('Maybank'), 'Maybank', 'Sep 2024 – Jan 2026', 'Senior OS Engineer'),
    ('h-fpt', 25, mark('FPT Software'), 'FPT Software Malaysia', 'Sep 2022 – Sep 2024', 'Software Consultant · ↳ ' + mark('PETRONAS') + 'PETRONAS Digital'),
    ('h-break', 5, '', 'Career break', 'Apr 2022 – Aug 2022', 'Personal goal pursuit'),
    ('h-impact', 14, '', 'Impact Business Solutions', 'Apr 2021 – May 2022', 'Software Consultant'),
]
def seg(i, s):
    a, m, mk, name, period, role = s
    sel = i == 0
    bg, fg = ('#333333', '#ffffff') if sel else ('#dddddd', '#1f1f1f')
    chip = ''
    if a == 'h-fpt':
        chip = (f'<a href="#h-adam" style="display:inline-flex;align-items:center;min-height:44px;margin-top:6px;padding:0 8px;'
                f'border:1px dashed #555555;background:#ffffff;color:#1f1f1f;font-size:12px">+ Adam Digital Assets · May – Jul 2024 · part-time</a>')
    return (f'<li style="flex:{m} 1 0;min-width:110px;display:flex;flex-direction:column">'
            f'<a href="#{a}"{CUR if sel else ""} style="flex:1 1 auto;display:block;min-height:44px;padding:10px;background:{bg};color:{fg};text-decoration:none">'
            f'<span style="display:block;font-size:12px;font-weight:600">{period}</span>'
            f'<span style="display:block;font-weight:700;margin-top:2px">{mk}{name}</span>'
            f'<span style="display:block;font-size:13px;margin-top:2px">{role}</span></a>{chip}</li>')
block('HB', 'History · the five years as a bar you can click: one segment per employer, sized by its months, newest first',
      f'<h2 id="history" style="{H2}">History</h2>'
      f'<p style="margin:0 0 10px;{SMALL}">Choose a period to open it below.</p>'
      '<ol style="list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:2px">' + ''.join(seg(i, s) for i, s in enumerate(SEG)) + '</ol>'
      + tag('LIVE', 'the AvePoint segment grows with "present"; widths come from the LinkedIn periods'),
      ['SCAN-10', 'GRP-03', 'INT-12', 'PRIO-04', 'RESP-03', 'Asked Q2', 'Asked Q4'], 'histbar')

block('HP', 'History · the chosen period, opened under the bar (AvePoint by default)',
      f'<div id="h-avepoint" style="border-top:2px solid #333333;padding-top:12px">'
      f'<div style="display:flex;gap:16px;justify-content:space-between;align-items:flex-start;flex-wrap:wrap">'
      f'<div><p style="{LABEL}">Jan 2026 – present · full-time</p><h3 style="margin:4px 0 0;font-size:22px">AvePoint · Full-stack developer</h3></div>'
      f'{bigmark("AvePoint")}</div>'
      f'<ol style="list-style:none;margin:10px 0 0 20px;padding:0"><li>↳ Sunway University · Apr 2026 – present · Senior Technical Lead</li></ol>'
      f'<p style="margin:10px 0 0">Main Project: <a href="#izone">iZone rebuild ↑</a></p>'
      f'<p style="margin:6px 0 0;{SMALL}">Tools: ' + mark('OutSystems') + 'OutSystems ODC, Aurora PostgreSQL, Microsoft single sign-on, private gateway</p></div>'
      f'<p style="margin:12px 0 0;font-size:13px;color:#555555">Maybank, FPT Software (with PETRONAS Digital), Adam Digital Assets, the career break and Impact '
      f'each have a panel here, shown only when their segment is chosen (CSS :target, no script).</p>',
      ['A11Y-01', 'A11Y-04', 'GRP-05', 'PRIO-04', 'Asked Q2'], 'histbar')

# ---------- Main Projects A: storyboard ----------
SKETCH = {
    1: ['the old portal falling over at an enrolment peak', 'one row locked while the others wait their turn',
        'the local replica standing beside the new platform', '40,000 enrolments across a 20-minute window'],
    2: ['forms built by a vendor, confidential items kept out', 'question types snapping in like parts',
        'complexity growing with each new type', 'over 80 forms by the fifth MVP'],
    3: ['exceptions checked on files and paper', 'fixed roles, each carrying its own rules',
        'low cost, in his account', 'exceptions moved from paper into the system'],
}
def panel(k, label, text, sketch):
    return (f'<li style="border:1px solid #999999;background:#ffffff;padding:10px;display:flex;flex-direction:column;gap:8px">'
            f'<p style="{LABEL}">{k} · {label}</p>'
            f'<figure style="margin:0"><div style="aspect-ratio:4/3;border:2px dashed #888888;{STRIPE}"></div>'
            f'<figcaption style="font-size:11px;color:#333333;margin-top:4px">[PLACEHOLDER: sketch · {sketch} · drawn in code]</figcaption></figure>'
            f'<p style="margin:0;font-size:15px">{text}</p></li>')
for n in (1, 2, 3):
    name, anchor, org, dec, dec2 = DEC[n]
    fields = [('Problem', PROB[n]), ('Decision', dec + (' ' + dec2 if dec2 else '')), ('Trade-off', TRADE[n]), ('Outcome', OUTC[n])]
    block(f'SB{n}', f'Project case study · {name} as a four-panel storyboard',
          f'<p style="{LABEL}">0{n} / 03</p><h3 id="{anchor}" style="margin:4px 0 0;font-size:24px">{name} — {SHORT[n][0]}</h3>'
          f'<p style="margin:4px 0 12px;{SMALL}">{org}</p>' + tag('FUN', 'panels grey until touched, then come into focus')
          + '<ol style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">'
          + ''.join(panel(i + 1, l, t, SKETCH[n][i]) for i, (l, t) in enumerate(fields)) + '</ol>'
          + f'<p style="margin:12px 0 0;text-align:center;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:#333333">'
            f'Role · {ROLE[n]} &nbsp;·&nbsp; Tools · {TOOLS[n]}</p>',
          ['HIER-02', 'GRP-01', 'SCAN-12', 'A11Y-01', 'Asked Q5'], 'storyboard')

# ---------- Main Projects B: annotated diagram ----------
PINS = [(14, 22), (46, 58), (70, 26), (86, 70)]
def pin(i, x, y):
    return (f'<span aria-hidden="true" style="position:absolute;left:{x}%;top:{y}%;width:32px;height:32px;border-radius:50%;background:#333333;'
            f'color:#ffffff;display:flex;align-items:center;justify-content:center;font-weight:700">{i}</span>')
for n in (1, 2, 3):
    name, anchor, org, dec, dec2 = DEC[n]
    fields = [('Problem', PROB[n]), ('Decision', dec + (' ' + dec2 if dec2 else '')), ('Trade-off', TRADE[n]), ('Outcome', OUTC[n])]
    block(f'AD{n}', f'Project case study · {name} as one annotated diagram with numbered notes',
          f'<p style="{LABEL}">0{n} / 03</p><h3 id="{anchor}" style="margin:4px 0 0;font-size:24px">{name} — {SHORT[n][0]}</h3>'
          f'<p style="margin:4px 0 12px;{SMALL}">{org}</p>'
          f'<figure style="margin:0"><div style="position:relative;aspect-ratio:21/9;border:2px dashed #888888;{STRIPE}">'
          + ''.join(pin(i + 1, x, y) for i, (x, y) in enumerate(PINS)) + '</div>'
          f'<figcaption style="font-size:12px;color:#333333;margin-top:6px">[PLACEHOLDER: diagram · {FIG[n]} · numbered pins mark where each note below happens · drawn in code]</figcaption></figure>'
          '<ol style="list-style:none;margin:12px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(420px,100%),1fr));gap:16px 32px">'
          + ''.join(f'<li style="display:flex;gap:10px"><span style="flex:0 0 28px;height:28px;border-radius:50%;background:#333333;color:#ffffff;'
                    f'display:flex;align-items:center;justify-content:center;font-weight:700">{i + 1}</span>'
                    f'<div><p style="{LABEL}">{l}</p><p style="margin:2px 0 0">{t}</p></div></li>' for i, (l, t) in enumerate(fields))
          + '</ol>'
          + f'<p style="margin:12px 0 0;{SMALL}"><b>Role and team</b> · {ROLE[n]}</p><p style="margin:4px 0 0;{SMALL}"><b>Tools</b> · {TOOLS[n]}</p>',
          ['A11Y-04', 'GRP-02', 'HIER-02', 'SCAN-10', 'Asked Q5'], FIGDOC[n])

# ---------- Main Projects C: poster shelf + liner notes ----------
BILL = {1: 'Senior Technical Lead · three developers', 2: 'Technical Lead · Product Owner · sole developer', 3: 'Developer · team of four'}
def poster(n):
    name, anchor, org, dec, dec2 = DEC[n]
    sel = n == 1
    return (f'<a href="#notes-{anchor}"{CUR if sel else ""} style="display:flex;flex-direction:column;aspect-ratio:2/3;min-height:44px;'
            f'border:{"3px solid #1f1f1f" if sel else "1px solid #999999"};background:#ffffff;color:#1f1f1f;text-decoration:none;padding:14px;gap:8px">'
            f'<span style="font-size:48px;font-weight:800;line-height:1;color:#888888">0{n}</span>'
            f'<span style="flex:1 1 auto;border:2px dashed #888888;{STRIPE};display:flex;align-items:flex-end;padding:6px;font-size:11px;color:#333333">'
            f'[PLACEHOLDER: poster art · {FIGSHORT[n]} · drawn in code]</span>'
            f'<span style="font-size:22px;font-weight:800;line-height:1.1">{SHORT[n][0]}</span>'
            f'<span style="font-weight:600">{name}</span>'
            f'<span style="font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:#444444">{BILL[n]} · {SHORT[n][4]}</span></a>')
block('PS', 'Project case study · the three Main Projects as a poster shelf (choose one)',
      tag('FUN', 'posters lift on hover or tap; the chosen one stays raised')
      + '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px">' + ''.join(poster(n) for n in (1, 2, 3)) + '</div>',
      ['SCAN-10', 'CPLX-03', 'HIER-01', 'Asked Q4', 'Asked Q5'], 'posters')
for n in (1, 2, 3):
    name, anchor, org, dec, dec2 = DEC[n]
    block(f'PSD{n}', f'Project case study · {name} liner notes, opened under the shelf',
          f'<div id="notes-{anchor}"><p style="{LABEL}">Liner notes · 0{n} / 03</p><h3 id="{anchor}" style="margin:4px 0 0;font-size:24px">{name}</h3>'
          f'<p style="margin:4px 0 12px;{SMALL}">{org}</p>' + dl([('Decision', dec + (' ' + dec2 if dec2 else ''))] + REST[n], ';max-width:66ch') + '</div>',
          ['A11Y-01', 'PRIO-04', 'INT-12', 'TYPE-01', 'Asked Q5'], 'posters')
block('PSX', 'Project case study · where the other liner notes open at 1440',
      f'<p style="margin:0;{SMALL}">Digital Form and MyInsights notes open in this same place when their poster is chosen (CSS :target, no script).</p>',
      ['PRIO-04', 'A11Y-01'], 'posters')

# ---------- options ----------
HDR = lambda: {'landmark': 'header', 'rows': [[cell(12, [P('H1', 'top bar', ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]}
FTR = lambda cells: {'landmark': 'footer', 'rows': [cells]}
def pl(ids, where, add=()):
    return [P(b, where, B[b]['rules'] + list(add)) for b in ids]

answered = ('Answered: Q1 one page, 5 sections · Q2 LinkedIn dates, CV roles · Q3 fold 765 / 568 · Q4 44×44 · '
            'Q5 iZone, Digital Form, MyInsights · Q6 timeline, then Minor. Round 6 feedback: R3 kept; Main Projects need something '
            'more artistic than picture-left / text-right; History = a clickable bar, one period shown below, enough info per segment.')
task = ('Dominant task (SCAN-14): judge his engineering from the decisions, then decide to interview or contact '
        '(hiring manager, tech lead; desktop). Recruiter scans title, tools, tenure; designer peer browses on a phone.\n')
TOP = ['F0ry', 'GLm', 'KCf', 'H4', 'H5', 'P0f']
END = ['X1', 'HB', 'HP', 'MB2', 'FM']
def top_rows():
    return [[cell(8, pl(['F0ry'], 'hero, 8 columns', ['HIER-01'])), cell(4, pl(['GLm'], 'beside the hero, after it in reading order'))],
            [cell(12, pl(['KCf'], 'Worked with strip, full width'))],
            [cell(6, pl(['H4'], 'left half')), cell(6, pl(['H5'], 'right half'))],
            [cell(12, pl(['P0f'], 'full-width heading'))]]
def end_rows():
    return [[gap(2), cell(8, pl(['X1'], 'cols 3–10')), gap(2)],
            [cell(12, pl(['HB'], 'full-width history bar'))],
            [gap(2), cell(8, pl(['HP'], 'the chosen period, directly under the bar'))],
            [cell(12, pl(['MB2'], 'full-width bento'))],
            [cell(12, pl(['FM'], 'closing band'))]]
def opt(i, name, axis, note, main, main_rows):
    order = TOP + main + END
    return {'id': i, 'name': name, 'axis': axis, 'note': task + note + '\n' + answered,
            'artboards': [compact(order, footer='C1f'),
                          {'width': 1440, 'margin': 80, 'rows': [HDR(), {'landmark': 'main', 'rows': top_rows() + main_rows + end_rows()},
                                                                 FTR([gap(2), cell(8, pl(['C1f'], 'footer, cols 3–10')), gap(2)])]}]}
COMMON = (' History (all three): a bar of five segments, newest first, each sized by its months and labelled with period, employer (mark where one exists) and role; '
          'Adam Digital Assets sits as a chip inside FPT because the two overlapped. Choosing a segment opens only that period below (AvePoint by default).')
options = [
    opt('SB', 'R3 · storyboard', 'Moodboard filmstrip (Aristide) and "cinematic but calm": each project is four film panels, problem → decision → trade-off → outcome, each a captioned sketch',
        'Option SB: every Main Project reads like a storyboard: four panels in a row, each with its label, a sketch captioned from the real content, and the text; role and tools run under it like film credits.' + COMMON,
        ['SB1', 'SB2', 'SB3'], [[cell(12, pl([f'SB{n}'], 'full-width storyboard', ['GRID-01']))] for n in (1, 2, 3)]),
    opt('AD', 'R3 · annotated diagram', 'A11Y-04 locality: one diagram per project, numbered pins on it matching numbered notes under it (LinkedIn: C4 diagrams)',
        'Option AD: each Main Project is one wide diagram drawn in code (its architecture, its systems, its flow) with four numbered pins; the numbered notes underneath say what happens at each pin. Role and tools close it.' + COMMON,
        ['AD1', 'AD2', 'AD3'], [[gap(1), cell(10, pl([f'AD{n}'], 'cols 2–11')), gap(1)] for n in (1, 2, 3)]),
    opt('PS', 'R3 · poster shelf', 'Brief "album art, minimalist movie posters": the three projects stand as posters; choosing one opens its liner notes below (same pattern as the history bar)',
        'Option PS: the three Main Projects stand side by side as posters: number, poster art, the decision as the title, the project name, and a billing line with role and tools. Choosing a poster opens its liner notes (every field) below, the same way the history bar works.' + COMMON,
        ['PS', 'PSD1', 'PSD2', 'PSD3'],
        [[cell(12, pl(['PS'], 'full-width shelf'))], [gap(2), cell(8, pl(['PSD1', 'PSX'], 'liner notes, under the shelf')), gap(2)]]),
]

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
FAIL = json.load(open(ARGS6[2])) if len(ARGS6) > 2 and os.path.exists(ARGS6[2]) else {}
spec = {'title': 'Portfolio block-out · round 6', 'fold': {'320': 568, '1440': 765}, 'blocks': blocks,
        'options': options, 'failures': FAIL}
json.dump(spec, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('blocks', len(blocks), 'options', len(options))
