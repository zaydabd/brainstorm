"""Round 5: option R refined from feedback. Minimal At a glance, Q's history component, a varied bento with
post-it and captioned picture tiles, and three less generic Main Project treatments (R1 flow, R2 carousel, R3 pinned split).
Reuses blocks from make_spec4.py (and, through it, rounds 1-3)."""
import json, sys, os

ARGS5 = sys.argv[:]
src4 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_spec4.py'), encoding='utf-8').read()
sys.argv = [sys.argv[0], '/dev/null']
exec(src4[:src4.index('\n# ---------- options ----------')])
OUT = ARGS5[1]

D.update({
    'glance_min': '"the at a glance could be mor minimal dont need to meniot enrolments twice" (your feedback, round 4 R)',
    'flow': '"Each gets a semi-detailed explanation: problem, decision, trade-off, role and team, outcome and tools." (proposal); "try change it to something less generic" (your feedback)',
    'carousel': '"work shown in a \\"01 / 04\\" carousel with tools on each project" (references, K2 Sousali, What I like); "less generic" (your feedback)',
    'pinned': '"Pinned name beside a scrolling list · The logo block stays fixed while the contents scroll underneath." (moodboard, Patterns); "less generic" (your feedback)',
    'bento2': '"keep the bento but differeing sizes and also some pictures/placeholders of other things.. like post it notes" (your feedback, round 4 R)',
})

# ---------- minimal At a glance ----------
block('GLm', 'Home · At a glance, minimal (no repeat of the load test)',
      f'<h2 style="{LABEL};margin-bottom:8px">At a glance</h2><ul style="list-style:none;margin:0;padding:0;display:grid;gap:6px">'
      + ''.join(f'<li><strong style="font-size:20px">{a}</strong> <span style="color:#444444">{b}</span></li>'
                for a, b in (('5', 'employers'), ('3 + 8', 'projects'), ('5', 'qualifications'))) + '</ul>',
      ['SCAN-01', 'CPLX-03', 'GRP-02', 'CPLX-01'], 'glance_min')

# ---------- R1: decision flow ----------
TRADE = {n: dict(REST[n])['Trade-off'] for n in (1, 2, 3)}
PROB = {n: dict(REST[n])['Problem'] for n in (1, 2, 3)}
OUTC = {n: dict(REST[n])['Outcome'] for n in (1, 2, 3)}
ROLE = {n: dict(REST[n])['Role and team'] for n in (1, 2, 3)}
TOOLS = {n: dict(REST[n])['Tools'] for n in (1, 2, 3)}
STEP = 'border-top:2px solid #444444;padding:10px 14px 12px'
def flow(n):
    name, anchor, org, dec, dec2 = DEC[n]
    return (f'<p style="{LABEL}">0{n} / 03</p><h3 id="{anchor}" style="margin:4px 0 0;font-size:24px">{name} — {SHORT[n][0]}</h3>'
            f'<p style="margin:4px 0 14px;{SMALL}">{org}</p>'
            f'<ol style="list-style:none;margin:0;padding:0;border-left:2px solid #444444;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">'
            f'<li style="{STEP}"><p style="{LABEL}">1 · Problem →</p><p style="margin:4px 0 0">{PROB[n]}</p></li>'
            f'<li style="{STEP};background:#e4e4e4"><p style="{LABEL}">2 · Decision →</p><p style="margin:4px 0 0;font-weight:600">{dec}{(" " + dec2) if dec2 else ""}</p>'
            f'<div style="margin-top:10px;border:1px dashed #555555;padding:8px;font-size:14px"><b>Cost</b> · {TRADE[n]}</div></li>'
            f'<li style="{STEP}"><p style="{LABEL}">3 · Outcome</p><p style="margin:4px 0 0">{OUTC[n]}</p></li></ol>'
            + figure(FIG[n], '32/9')
            + f'<p style="margin:0;{SMALL}"><b>Role and team</b> · {ROLE[n]}</p><p style="margin:4px 0 0;{SMALL}"><b>Tools</b> · {TOOLS[n]}</p>')
for n in (1, 2, 3):
    block(f'RF{n}', f'Project case study · {DEC[n][0]} as a flow: problem → decision → outcome', flow(n),
          ['GRP-03', 'HIER-01', 'SCAN-03', 'A11Y-01', 'A11Y-04', 'Asked Q5'], 'flow')

# ---------- R2: 01 / 03 carousel ----------
def slide(n):
    name, anchor, org, dec, dec2 = DEC[n]
    return (f'<article id="{anchor}" style="scroll-snap-align:start;border:1px solid #999999;background:#ffffff;padding:16px">'
            f'<p style="{LABEL}">0{n} / 03</p><h3 style="margin:4px 0 0;font-size:24px">{name}</h3><p style="margin:4px 0 12px;{SMALL}">{org}</p>'
            f'<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;align-items:start">'
            f'<div style="max-width:62ch">' + dl([('Decision', dec + (' ' + dec2 if dec2 else ''))] + REST[n]) + '</div>'
            + figure(FIG[n], '4/3') + '</div></article>')
block('RCar', 'Project case study · the three Main Projects as a 01 / 03 carousel (next one peeks in)',
      '<div role="region" aria-label="Main Projects" style="display:grid;grid-auto-flow:column;grid-auto-columns:88%;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:8px">'
      + ''.join(slide(n) for n in (1, 2, 3)) + '</div>'
      f'<nav aria-label="Project slides" style="display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-top:10px">'
      f'<a href="#izone" style="{TAP};border:1px solid #666666">← Previous</a>'
      + ''.join(f'<a href="#{DEC[n][1]}" style="{TAP}"{CUR if n == 1 else ""}>0{n}</a>' for n in (1, 2, 3))
      + f'<a href="#digital-form" style="{TAP};border:1px solid #666666">Next →</a></nav>'
      + tag('FUN', 'swipe or scroll sideways; slides snap'),
      ['INT-09', 'RESP-04', 'SCAN-02', 'HIER-02', 'Asked Q4', 'Asked Q5'], 'carousel')

# ---------- R3: pinned split ----------
for n in (1, 2, 3):
    name, anchor, org, dec, dec2 = DEC[n]
    block(f'RP{n}p', f'Project case study · {name} pin: number, name, decision, captioned visual',
          f'<p style="margin:0;font-size:56px;font-weight:800;line-height:1;color:#888888">0{n}</p>'
          f'<h3 id="{anchor}" style="margin:8px 0 0;font-size:26px">{name}</h3><p style="margin:4px 0 0;{SMALL}">{org}</p>'
          f'<p style="margin:10px 0 0;font-size:18px;font-weight:600">{SHORT[n][0]}</p>' + figure(FIG[n], '4/3'),
          ['HIER-02', 'HIER-01', 'A11Y-03', 'SCAN-04', 'Asked Q5'], 'pinned')
    block(f'RP{n}f', f'Project case study · {name} fields, scrolling beside its pin',
          dl([('Decision', dec + (' ' + dec2 if dec2 else ''))] + REST[n], ';max-width:62ch'),
          ['GRP-02', 'A11Y-04', 'TYPE-01', 'Asked Q5'], 'pinned')

# ---------- Minor Projects: varied bento with post-its and captioned picture tiles ----------
def t_min(name, line, emp, tools, big='', span='span 2', rows=''):
    return (f'<div style="grid-column:{span};{("grid-row:" + rows + ";") if rows else ""}border:1px solid #999999;background:#ffffff;padding:12px;display:flex;flex-direction:column;gap:6px">'
            + (f'<p style="margin:0;font-size:34px;font-weight:800;line-height:1.05">{big}</p>' if big else '')
            + f'<p style="margin:0;font-weight:700">{name}</p><p style="margin:0;font-size:14px">{line}</p>'
            f'<p style="margin:auto 0 0;font-size:13px;color:#555555">{emp} · {tools}</p></div>')
def t_pic(what, span='span 1', rows=''):
    return (f'<figure style="margin:0;grid-column:{span};{("grid-row:" + rows + ";") if rows else ""}display:flex;flex-direction:column">'
            f'<div style="flex:1 1 auto;min-height:90px;border:2px dashed #888888;{STRIPE}"></div>'
            f'<figcaption style="font-size:11px;color:#333333;margin-top:4px">[PLACEHOLDER: picture · {what} · drawn in code]</figcaption></figure>')
def t_post(rot):
    return (f'<div style="grid-column:span 1;transform:rotate({rot}deg);background:#dcdcdc;border:1px solid #aaaaaa;padding:12px;'
            f'font-size:13px;color:#222222;min-height:110px">[PLACEHOLDER: post-it · a short note in his words]</div>')
M = {m[0]: m for m in MINORS}
block('MB2', 'Projects list · Minor Projects as a varied bento with post-its and captioned picture tiles',
      f'<h2 style="{H2};font-size:18px">Minor Projects <span style="color:#555555">(8)</span></h2>'
      + tag('FUN', 'tiles lift on hover or tap · post-its tilt back on hover')
      + '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));grid-auto-rows:minmax(110px,auto);grid-auto-flow:dense;gap:12px">'
      + t_min(*M['CAB-Q'], big='6 h → 30 min', rows='span 2')
      + t_min(*M['Audit Log']) + t_post(-2) + t_min(*M['Tokenizer'])
      + t_min(*M['VIP Dashboard']) + t_pic('a map motif for the Sarawak data', rows='span 2')
      + t_min(*M['MPowered']) + t_min(*M['RPSST'])
      + t_min(*M['QR Asset Management']) + t_pic('a QR-pattern motif')
      + t_min(*M['Adam Digital Assets'], rows='span 2') + t_pic('a mosque-signage motif', span='span 2') + t_post(2)
      + '</div>',
      ['GRP-01', 'GRID-01', 'CPLX-04', 'SCAN-04', 'Asked Q6'], 'bento2')

# ---------- options ----------
HDR = lambda: {'landmark': 'header', 'rows': [[cell(12, [P('H1', 'top bar', ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]}
FTR = lambda cells: {'landmark': 'footer', 'rows': [cells]}
def pl(ids, where, add=()):
    return [P(b, where, B[b]['rules'] + list(add)) for b in ids]

answered = ('Answered: Q1 one page, 5 sections · Q2 LinkedIn dates, CV roles · Q3 fold 765 / 568 · Q4 44×44 · '
            'Q5 iZone, Digital Form, MyInsights · Q6 timeline, then Minor. Round 5 feedback: R chosen; At a glance minimal, '
            'no second load-test mention; Main Projects less generic; history = round-4 Q timeline; Minor bento with varied sizes, post-its and pictures.')
task = ('Dominant task (SCAN-14): judge his engineering from the decisions, then decide to interview or contact '
        '(hiring manager, tech lead; desktop). Recruiter scans title, tools, tenure; designer peer browses on a phone.\n')
TOP = ['F0ry', 'GLm', 'KCf', 'H4', 'H5', 'P0f']
END = ['X1', 'TBh', 'LX2n', 'MB2', 'FM']
def top_rows():
    return [[cell(8, pl(['F0ry'], 'hero, 8 columns', ['HIER-01'])), cell(4, pl(['GLm'], 'beside the hero, after it in reading order'))],
            [cell(12, pl(['KCf'], 'Worked with strip, full width'))],
            [cell(6, pl(['H4'], 'left half')), cell(6, pl(['H5'], 'right half'))],
            [cell(12, pl(['P0f'], 'full-width heading'))]]
def end_rows():
    return [[gap(2), cell(8, pl(['X1'], 'cols 3–10')), gap(2)],
            [cell(12, pl(['TBh'], 'History heading, then the five years as one bar'))],
            [gap(2), cell(7, pl(['LX2n'], 'timeline, marks trailing, cols 3–9', ['TYPE-01'])), gap(3)],
            [cell(12, pl(['MB2'], 'full-width bento'))],
            [cell(12, pl(['FM'], 'closing band'))]]
def opt(i, name, axis, note, main, main_rows):
    order = TOP + main + END
    return {'id': i, 'name': name, 'axis': axis, 'note': task + note + '\n' + answered,
            'artboards': [compact(order, footer='C1f'),
                          {'width': 1440, 'margin': 80, 'rows': [HDR(), {'landmark': 'main', 'rows': top_rows() + main_rows + end_rows()},
                                                                 FTR([gap(2), cell(8, pl(['C1f'], 'footer, cols 3–10')), gap(2)])]}]}
options = [
    opt('R1', 'Credits hero · decision flow', 'GRP-03: each project is a connected flow, problem → decision → outcome, the trade-off hanging off the decision as its cost',
        'Option R1: the round-4 R hero, Worked with and minimal At a glance, then each Main Project as a three-step flow joined by one line (GRP-03 binds the steps). The decision step is the heaviest (HIER-01) and carries its cost. A wide captioned visual and the role / tools line close each flow. History and the new bento follow.',
        ['RF1', 'RF2', 'RF3'], [[cell(12, pl([f'RF{n}'], 'full-width flow', ['GRID-01']))] for n in (1, 2, 3)]),
    opt('R2', 'Credits hero · 01 / 03 carousel', 'Moodboard pick Sousali "01 / 04" carousel · one project per slide, the next peeks in (SCAN-02), Previous left of Next (INT-09)',
        'Option R2: the same hero, Worked with and At a glance, then the three Main Projects on one sideways track: each slide holds every field beside its captioned visual; numbers 01 02 03 jump straight to a slide. History and the new bento follow.',
        ['RCar'], [[cell(12, pl(['RCar'], 'full-width track'))]]),
    opt('R3', 'Credits hero · pinned split', 'Moodboard "Pinned name beside a scrolling list" · each project\'s number, name, decision and visual pin on the left while its fields scroll on the right',
        'Option R3: the same hero, Worked with and At a glance, then each Main Project as a split: a big 01 / 02 / 03 with its name, short decision and captioned visual pinned on the left (5 columns), its fields scrolling beside it (7 columns). History and the new bento follow.',
        [x for n in (1, 2, 3) for x in (f'RP{n}p', f'RP{n}f')],
        [[cell(5, pl([f'RP{n}p'], 'pinned left, 5 columns'), sticky=True), cell(7, pl([f'RP{n}f'], 'scrolling right, 7 columns', ['TYPE-01']))] for n in (1, 2, 3)]),
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
FAIL = json.load(open(ARGS5[2])) if len(ARGS5) > 2 and os.path.exists(ARGS5[2]) else {}
spec = {'title': 'Portfolio block-out · round 5', 'fold': {'320': 568, '1440': 765}, 'blocks': blocks,
        'options': options, 'failures': FAIL}
json.dump(spec, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('blocks', len(blocks), 'options', len(options))
