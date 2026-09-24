"""Round 9: round-8 PS kept. On a phone the history is one minimal strip, like Worked with, drifting left to right;
the desktop keeps the clickable bar and panel. Reuses blocks from make_spec8.py (and, through it, rounds 1-7)."""
import json, sys, os

ARGS9 = sys.argv[:]
src8 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_spec8.py'), encoding='utf-8').read()
sys.argv = [sys.argv[0], '/dev/null']
exec(src8[:src8.index('\n# ---------- options ----------')])
OUT = ARGS9[1]

D.update({
    'hist_strip': '"regarding the mobile for timeline make it more minimal make the rntire thing just one compnent like the worked at companent '
                  'moving from left to right" (your feedback, round 8); WCAG 2.2.2 Pause, Stop, Hide: moving content that starts on its own '
                  'and lasts over 5 seconds needs a way to pause it',
})

# ---------- History on a phone: one minimal strip drifting left to right ----------
TL9 = [  # period, mark, name, role (client after ↳)
    ('Jan 2026 – present', mark('AvePoint'), 'AvePoint', 'Full-stack developer · ↳ Sunway University'),
    ('Sep 2024 – Jan 2026', mark('Maybank'), 'Maybank', 'Senior OutSystems Engineer'),
    ('May – Jul 2024', '', 'Adam Digital Assets', 'part-time'),
    ('Sep 2022 – Sep 2024', mark('FPT Software'), 'FPT Software Malaysia', 'Software Consultant · ↳ ' + mark('PETRONAS') + 'PETRONAS Digital'),
    ('Apr – Aug 2022', '', 'Career break', 'Time for personal goals'),
    ('Apr 2021 – May 2022', '', 'Impact Business Solutions', 'Software Consultant'),
]
def tl9(t):
    period, mk, name, role = t
    return (f'<li style="flex:0 0 auto;padding:0 20px;border-left:1px solid #bbbbbb;white-space:nowrap">'
            f'<p style="{LABEL}">{period}</p><p style="margin:2px 0 0;font-weight:700">{mk}{name}</p>'
            f'<p style="margin:2px 0 0;font-size:13px">{role}</p></li>')
SET9 = ''.join(tl9(t) for t in TL9)
OLS = 'list-style:none;margin:0;padding:0;display:flex;align-items:center;flex:0 0 auto'
block('HBs', 'History · on a phone, one minimal strip drifting left to right, newest first, with Pause',
      '<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:6px">'
      f'<h2 id="history" style="{H2};margin:0">History</h2>'
      f'<button type="button" aria-pressed="false" style="{TAP};border:1px solid #666666;background:#ffffff;font:inherit;font-size:14px">Pause</button></div>'
      '<div style="height:96px;overflow-x:auto;scrollbar-width:none;display:flex;align-items:center;border-block:1px solid #bbbbbb;'
      'mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent)">'
      f'<ol style="{OLS}">{SET9}</ol><ol aria-hidden="true" style="{OLS}">{SET9}</ol></div>'
      + '<p style="margin:8px 0 0">' + fun('drifts left to right in a loop, the other way from Worked with · same 96 px height all the way · '
                                            'pauses on hover, focus or Pause · the second set is a copy for the loop, hidden from screen readers · '
                                            'under reduced motion it stands still and swipes')
      + tag('PHONE', 'on desktop the clickable bar and panel take its place') + '</p>',
      ['GRP-01', 'A11Y-04', 'INT-15', 'RESP-04', 'RESP-08', 'SCAN-10', 'Asked Q2'], 'hist_strip')

block('HB9', 'History · the clickable bar, desktop only (a phone gets the moving strip)',
      B['HB8']['html'].replace(tag('PHONE', 'not shown on a phone; the one-container list takes its place'),
                               tag('PHONE', 'not shown on a phone; the moving strip takes its place')),
      B['HB8']['rules'], 'hist_strip')
assert 'the moving strip takes its place' in B['HB9']['html']

# ---------- options ----------
HDR = lambda: {'landmark': 'header', 'rows': [[cell(12, [P('H1', 'top bar', ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]}
FTR = lambda cells: {'landmark': 'footer', 'rows': [cells]}
def pl(ids, where, add=()):
    return [P(b, where, B[b]['rules'] + list(add)) for b in ids]

answered = ('Answered: Q1 one page, 5 sections · Q2 LinkedIn dates, CV roles · Q3 fold 765 / 568 · Q4 44×44 · '
            'Q5 iZone, Digital Form, MyInsights · Q6 timeline, then Minor. Round 9 feedback: on a phone the history is one minimal '
            'component like Worked with, moving left to right.')
task = ('Dominant task (SCAN-14): judge his engineering from the decisions, then decide to interview or contact '
        '(hiring manager, tech lead; desktop). Recruiter scans title, tools, tenure; designer peer browses on a phone.\n')
TOP = ['F0h', 'GLh', 'KCm', 'H4', 'H5', 'P0h']
MAIN = ['PS7', 'PSD7_1', 'PSX7']
END320 = ['X1', 'HBs', 'MB3', 'FM']
rows1440 = ([[cell(8, pl(['F0h'], 'hero, 8 columns', ['HIER-01'])), cell(4, pl(['GLh'], 'beside the hero, after it in reading order'))],
             [cell(12, pl(['KCm'], 'Worked with strip, full width'))],
             [cell(6, pl(['H4'], 'left half')), cell(6, pl(['H5'], 'right half'))],
             [cell(12, pl(['P0h'], 'full-width heading'))],
             [cell(12, pl(['PS7'], 'full-width shelf'))],
             [gap(2), cell(8, pl(['PSD7_1', 'PSX7'], 'notes, under the shelf')), gap(2)],
             [gap(2), cell(8, pl(['X1'], 'cols 3–10')), gap(2)],
             [cell(12, pl(['HB9'], 'full-width history bar'))],
             [gap(2), cell(8, pl(['HP7'], 'the chosen period, directly under the bar'))],
             [cell(12, pl(['MB3'], 'full-width bento'))],
             [cell(12, pl(['FM'], 'closing band'))]])
note = ('Option PS, round 9. Same as round 8 except the phone history: one strip, 96 px tall like Worked with, drifting left to right '
        '(the other way from Worked with). Each period shows only its dates, employer (mark where one exists) and role, with the client after ↳. '
        'Nothing to tap; Pause stops it. The desktop keeps the clickable bar and the panel under it.')
options = [{'id': 'PS', 'name': 'R3 · poster shelf, round 9', 'axis': 'Round-8 PS with a minimal moving history strip on phones',
            'note': task + note + '\n' + answered,
            'artboards': [compact(TOP + MAIN + END320, footer='C1h'),
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
FAIL = json.load(open(ARGS9[2])) if len(ARGS9) > 2 and os.path.exists(ARGS9[2]) else {}
spec = {'title': 'Portfolio block-out · round 9', 'fold': {'320': 568, '1440': 765}, 'blocks': blocks,
        'options': options, 'failures': FAIL}
json.dump(spec, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('blocks', len(blocks), 'options', len(options))
