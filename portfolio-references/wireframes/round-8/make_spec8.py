"""Round 8: round-7 PS kept. On a phone the history is one container with every period open (no tapping);
the desktop keeps the clickable bar and panel. Minor Projects pictures spread across the bento.
Reuses blocks from make_spec7.py (and, through it, rounds 1-6)."""
import json, sys, os

ARGS8 = sys.argv[:]
src7 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_spec7.py'), encoding='utf-8').read()
sys.argv = [sys.argv[0], '/dev/null']
exec(src7[:src7.index('\n# ---------- options ----------')])
OUT = ARGS8[1]

D.update({
    'hist_one': '"for mobile the hirtory doesnt really need the feature of click and see details one container to show most of it is fine.." (your feedback, round 7)',
    'bento3': '"for the minor projects youspread the picture placehodler bit more" (your feedback, round 7)',
})

# ---------- History on a phone: one container, every period open ----------
TL8 = [  # period, months label, mark, name, role, client line, tools, months
    ('Jan 2026 – present', '9 mos', mark('AvePoint'), 'AvePoint', 'Full-stack developer · full-time',
     '↳ Sunway University · Apr 2026 – present · Senior Technical Lead',
     mark('OutSystems') + 'OutSystems ODC, Aurora PostgreSQL, Microsoft single sign-on, private gateway', 9),
    ('Sep 2024 – Jan 2026', '1 yr 5 mos', mark('Maybank'), 'Maybank', 'Senior OutSystems Engineer · full-time', '',
     mark('OutSystems') + 'OutSystems O11', 17),
    ('May 2024 – Jul 2024', '3 mos', '', 'Adam Digital Assets', 'part-time', '', '', 3),
    ('Sep 2022 – Sep 2024', '2 yrs 1 mo', mark('FPT Software'), 'FPT Software Malaysia', 'Software Consultant · contract',
     '↳ ' + mark('PETRONAS') + 'PETRONAS Digital · OutSystems Developer', mark('OutSystems') + 'OutSystems O11', 25),
    ('Apr 2022 – Aug 2022', '5 mos', '', 'Career break', 'Time for personal goals', '', '', 5),
    ('Apr 2021 – May 2022', '1 yr 2 mos', '', 'Impact Business Solutions', 'Software Consultant · contract', '', 'Power BI, QGIS, Firebase', 14),
]
def tl8(i, t):
    period, dur, mk, name, role, client, tools, m = t
    return (f'<li style="padding:12px 14px;{"border-top:1px solid #cccccc" if i else ""}">'
            f'<p style="{LABEL}">{period} · {dur}</p>'
            f'<p style="margin:2px 0 0;font-weight:700">{mk}{name}</p>'
            f'<p style="margin:2px 0 0;font-size:14px">{role}</p>'
            + (f'<p style="margin:4px 0 0 16px;font-size:14px">{client}</p>' if client else '')
            + (f'<p style="margin:4px 0 0;{SMALL}">Tools: {tools}</p>' if tools else '')
            + f'<span aria-hidden="true" style="display:block;margin-top:8px;height:4px;width:{m * 9}px;max-width:100%;background:#333333;border-radius:0 2px 2px 0"></span></li>')
block('HBm', 'History · on a phone, one container with every period open (no tapping)',
      f'<h2 id="history" style="{H2}">History</h2>'
      '<ol style="list-style:none;margin:0;padding:0;border:1px solid #999999;background:#ffffff">'
      + ''.join(tl8(i, t) for i, t in enumerate(TL8)) + '</ol>'
      + '<p style="margin:8px 0 0">' + tag('PHONE', 'everything shows at once; the bar under each period is its length, 9 px a month · '
                                           'on desktop the same list becomes the clickable bar and panel')
      + tag('LIVE', 'AvePoint\'s months grow with "present"; periods and months come from LinkedIn') + '</p>',
      ['SCAN-10', 'GRP-01', 'GRP-05', 'RESP-08', 'A11Y-01', 'Asked Q2'], 'hist_one')

block('HB8', 'History · the clickable bar, desktop only (a phone gets the one-container list)',
      B['HB7']['html'].replace(tag('PHONE', 'rows stack newest first; the bar in each row is its length, 9 px a month'),
                               tag('PHONE', 'not shown on a phone; the one-container list takes its place')),
      ['SCAN-10', 'GRP-03', 'INT-12', 'RESP-05', 'RESP-08', 'Asked Q2', 'Asked Q4'], 'hist_one')
assert 'not shown on a phone' in B['HB8']['html']

# ---------- Minor Projects: pictures spread out, each beside its own project ----------
block('MB3', 'Projects list · Minor Projects bento, pictures spread across rows and set beside their projects',
      f'<h2 style="{H2};font-size:18px">Minor Projects <span style="color:#555555">(8)</span></h2>'
      + tag('FUN', 'tiles lift on hover or tap · post-its tilt back on hover')
      + '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));grid-auto-rows:minmax(110px,auto);grid-auto-flow:dense;gap:12px">'
      + t_min(*M['CAB-Q'], big='6 h → 30 min', rows='span 2')
      + t_min(*M['VIP Dashboard']) + t_pic('a map motif for the Sarawak data')
      + t_min(*M['Audit Log']) + t_post(-2)
      + t_post(2) + t_min(*M['Tokenizer'])
      + t_min(*M['QR Asset Management']) + t_pic('a QR-pattern motif')
      + t_pic('a mosque-signage motif', span='span 2') + t_min(*M['Adam Digital Assets'])
      + t_min(*M['MPowered']) + t_min(*M['RPSST'])
      + '</div>',
      ['GRP-01', 'GRID-01', 'CPLX-04', 'SCAN-04', 'Asked Q6'], 'bento3')

# ---------- options ----------
HDR = lambda: {'landmark': 'header', 'rows': [[cell(12, [P('H1', 'top bar', ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]}
FTR = lambda cells: {'landmark': 'footer', 'rows': [cells]}
def pl(ids, where, add=()):
    return [P(b, where, B[b]['rules'] + list(add)) for b in ids]

answered = ('Answered: Q1 one page, 5 sections · Q2 LinkedIn dates, CV roles · Q3 fold 765 / 568 · Q4 44×44 · '
            'Q5 iZone, Digital Form, MyInsights · Q6 timeline, then Minor. Round 8 feedback: on a phone the history is one container '
            'showing most of it, no tapping; spread the Minor Projects pictures.')
task = ('Dominant task (SCAN-14): judge his engineering from the decisions, then decide to interview or contact '
        '(hiring manager, tech lead; desktop). Recruiter scans title, tools, tenure; designer peer browses on a phone.\n')
TOP = ['F0h', 'GLh', 'KCm', 'H4', 'H5', 'P0h']
MAIN = ['PS7', 'PSD7_1', 'PSX7']
END320 = ['X1', 'HBm', 'MB3', 'FM']
rows1440 = ([[cell(8, pl(['F0h'], 'hero, 8 columns', ['HIER-01'])), cell(4, pl(['GLh'], 'beside the hero, after it in reading order'))],
             [cell(12, pl(['KCm'], 'Worked with strip, full width'))],
             [cell(6, pl(['H4'], 'left half')), cell(6, pl(['H5'], 'right half'))],
             [cell(12, pl(['P0h'], 'full-width heading'))],
             [cell(12, pl(['PS7'], 'full-width shelf'))],
             [gap(2), cell(8, pl(['PSD7_1', 'PSX7'], 'notes, under the shelf')), gap(2)],
             [gap(2), cell(8, pl(['X1'], 'cols 3–10')), gap(2)],
             [cell(12, pl(['HB8'], 'full-width history bar'))],
             [gap(2), cell(8, pl(['HP7'], 'the chosen period, directly under the bar'))],
             [cell(12, pl(['MB3'], 'full-width bento'))],
             [cell(12, pl(['FM'], 'closing band'))]])
note = ('Option PS, round 8. Same as round 7 except: on a phone the history is one container with every period open '
        '(dates, months, role, client, tools and a length bar), with nothing to tap; the desktop keeps the clickable bar and the panel under it. '
        'Minor Projects pictures now sit beside their own projects and fall in different rows and columns, not stacked in one corner.')
options = [{'id': 'PS', 'name': 'R3 · poster shelf, round 8', 'axis': 'Round-7 PS with a one-container phone history and a spread-out bento',
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
FAIL = json.load(open(ARGS8[2])) if len(ARGS8) > 2 and os.path.exists(ARGS8[2]) else {}
spec = {'title': 'Portfolio block-out · round 8', 'fold': {'320': 568, '1440': 765}, 'blocks': blocks,
        'options': options, 'failures': FAIL}
json.dump(spec, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('blocks', len(blocks), 'options', len(options))
