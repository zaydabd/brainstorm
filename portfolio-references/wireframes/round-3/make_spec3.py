"""Round 3: fewer type-only ideas, more slots for rhythm and fun.
Keeps I, K, L, M from round 2 (now with slots) and adds N, O, P built around the slots.
Reuses blocks and helpers from make_spec2.py (which reuses make_spec.py)."""
import json, sys, os

ARGS3 = sys.argv[:]
src2 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_spec2.py'), encoding='utf-8').read()
sys.argv = [sys.argv[0], '/dev/null']
exec(src2[:src2.index('# ---------- options ----------')])
OUT = ARGS3[1]

# ---------- doc lines for the new slots ----------
D.update({
    'visual': '"add more placeholders for content which helps with rhythm or fun" (your message); "the page carries no image of Wan Zayd or of his work" (details, Rule 10)',
    'fun_row': '"Full-row hover highlight · Emil: a soft fill slides behind the whole row. For the Minor Projects and timeline rows" (moodboard, Fun that fits 14 KB)',
    'fun_reveal': '"Staged scroll reveals · sections fade and rise in. CSS view() timeline" (moodboard, Fun that fits 14 KB)',
    'fun_grey': '"Grey until touched · the employer marks sit in ice grey and turn to their own colours on hover" (moodboard, Fun that fits 14 KB)',
    'fun_ruler': '"Scroll ruler as the timeline spine · On a page-as-timeline, its ticks are the years." (moodboard, Fun that fits 14 KB)',
    'fun_marquee': '"The name as a marquee · a huge looping headline, paused on hover." (moodboard, Fun that fits 14 KB)',
    'fun_rays': '"Rays that follow the cursor · Off on touch and under reduced motion." (moodboard, Fun that fits 14 KB)',
    'fun_copy': '"Rauno\'s click-to-copy email with a \\"Copied\\" confirmation" (references, Digest of your picks)',
})

def fun(label):
    return (f'<span style="display:inline-block;border:1px dotted #333333;background:#ffffff;color:#333333;font-size:11px;'
            f'line-height:16px;padding:1px 6px;margin:0 4px 6px 0;font-weight:600">FUN · {label}</span>')

def visual(what, ratio='4/3'):
    return (f'<div style="aspect-ratio:{ratio};border:2px dashed #888888;display:flex;align-items:center;justify-content:center;'
            f'text-align:center;padding:12px;background:repeating-linear-gradient(45deg,#e6e6e6 0 10px,#f3f3f3 10px 20px);'
            f'font-size:13px;color:#333333">[PLACEHOLDER: visual · {what} · drawn in code, never a photo or screenshot]</div>')

# ---------- generic visual slots ----------
block('HV', 'Home · visual slot beside the decision', visual('opening visual'),
      ['HIER-03', 'HIER-01', 'CPLX-01'], 'visual')
for n, nm in ((1, 'iZone rebuild'), (2, 'Digital Form'), (3, 'MyInsights')):
    block(f'V{n}', f'Project case study · visual slot for {nm}', visual(f'for {nm}'),
          ['HIER-02', 'SCAN-12', 'HIER-03'], 'visual')
for n, nm in ((1, 'iZone rebuild'), (2, 'Digital Form'), (3, 'MyInsights')):
    block(f'VL{n}', f'Project case study · wide visual interlude after {nm}', visual(f'interlude after {nm}', '3/1'),
          ['HIER-03', 'SCAN-12', 'CPLX-02'], 'visual')
for n in (1, 2, 3):
    block(f'VT{n}', f'History · visual tile {n} in the wall', visual(f'wall tile {n}', '1/1'),
          ['GRID-01', 'GRID-03', 'GRP-01'], 'visual')

# ---------- fun slots ----------
block('F0r', 'Home · title card with a light-rays layer behind it',
      '<div style="position:relative">'
      '<div style="position:absolute;inset:0;border:2px dashed #aaaaaa;background:repeating-linear-gradient(120deg,#ececec 0 18px,#f6f6f6 18px 36px)"></div>'
      '<div style="position:relative;padding:12px">' + B['F0']['html']
      + fun('light rays behind this card follow the pointer · off on touch and reduced motion') + '</div></div>',
      ['HIER-01', 'HIER-04', 'SCAN-03', 'CPLX-02', 'PRIO-01'], 'fun_rays')
block('P0f', 'Project case study · heading, projects rise in as they enter view',
      B['P0']['html'] + fun('each project rises in as it enters view · text visible from first paint'),
      ['HIER-02', 'SCAN-05'], 'fun_reveal')
block('X2f', 'About/Experience · timeline, full-row hover',
      fun('full-row hover on every entry') + B['X2']['html'],
      B['X2']['rules'], 'fun_row')
block('M1f', 'Projects list · Minor Projects, full-row hover',
      fun('full-row hover on every row') + B['M1']['html'],
      B['M1']['rules'], 'fun_row')
block('FM', 'Closing · the name as a marquee (loops, pauses on hover, still under reduced motion)',
      fun('loops · pauses on hover · still under reduced motion')
      + '<p aria-hidden="true" style="margin:0;white-space:nowrap;overflow:hidden;font-size:clamp(40px,7vw,104px);font-weight:800;line-height:1;color:#bbbbbb">'
        'Wan Zayd Abdullah · Wan Zayd Abdullah · Wan Zayd Abdullah</p>',
      ['HIER-03', 'SCAN-01', 'CONV-05'], 'fun_marquee')
block('C1f', 'Contact · email copies on click, "Copied" shows beside it',
      B['C1']['html'] + '<p style="margin:8px 0 0">' + fun('click Email to copy it · "Copied" appears next to it') + '</p>',
      B['C1']['rules'] + ['INT-12', 'A11Y-04'], 'fun_copy')
block('KCf', 'Home · credits strip, marks grey until touched',
      fun('marks grey until touched · hover or tap') + B['KC']['html'],
      B['KC']['rules'], 'fun_grey')
block('MT0f', 'About/Experience · wall heading, marks grey until touched',
      B['MT0']['html'] + fun('marks grey until touched · hover or tap'),
      B['MT0']['rules'], 'fun_grey')
block('LP1f', 'Project case study · iZone rebuild with marks trailing, grey until touched',
      fun('marks grey until touched · hover or tap') + B['LP1']['html'],
      B['LP1']['rules'], 'fun_grey')
YEARS = ['2026', '2025', '2024', '2023', '2022', '2021']
block('FR', 'History · scroll ruler, ticks are the years (pinned)',
      fun('ticks track your position') +
      '<nav aria-label="Timeline position" style="display:flex;flex-wrap:wrap;gap:4px">'
      + ''.join(f'<a href="#history" style="flex:1 0 56px;display:flex;align-items:center;min-height:44px;border-top:2px solid #555555;font-size:13px">{y}</a>' for y in YEARS)
      + '</nav>',
      ['CONV-04', 'A11Y-03', 'INT-16', 'Asked Q4'], 'fun_ruler')

# list pane with small visual slots on the three Main rows
block('ILv', 'Projects list · list pane with a visual thumb on each Main row, full-row hover',
      fun('full-row hover on every row') +
      f'<h2 id="work" style="{H2}">Projects list <span style="color:#555555">(3 + 8)</span></h2><ol style="list-style:none;margin:0;padding:0">'
      + ''.join(f'<li style="border-top:1px solid #cccccc;padding:8px 0;display:flex;gap:12px;align-items:flex-start{";background:#e2e2e2" if n == 1 else ""}">'
                f'<div style="flex:1 1 auto;min-width:0"><a href="#{DEC[n][1]}" style="font-weight:700;{TAP};padding:0">0{n} · {DEC[n][0]}</a>'
                f'<p style="margin:0;{SMALL}">{SHORT[n][0]}</p></div>'
                f'<div style="flex:0 0 72px;height:54px;border:2px dashed #888888;background:#eeeeee;font-size:10px;display:flex;align-items:center;justify-content:center;text-align:center">visual</div></li>'
                for n in (1, 2, 3))
      + '</ol><ul style="list-style:none;margin:12px 0 0;padding:0">'
      + ''.join(f'<li style="border-top:1px solid #dddddd;padding:6px 0;font-size:14px"><b>{a}</b> — {b}<br><span style="color:#555555">{c} · {d}</span></li>' for a, b, c, d in MINORS)
      + '</ul>',
      ['RESP-06', 'SCAN-10', 'SCAN-12', 'SCAN-04', 'Asked Q4', 'Asked Q5'], 'listdetail')

# ---------- options ----------
HDR = lambda where='top bar': {'landmark': 'header', 'rows': [[cell(12, [P('H1', where, ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]}
FTR = lambda cells: {'landmark': 'footer', 'rows': [cells]}
def pl(ids, where, add=()):
    return [P(b, where, B[b]['rules'] + list(add)) for b in ids]

answered = ('Answered: Q1 one page, your 5 pages = sections · Q2 LinkedIn dates, CV roles · Q3 fold 765 / 568 · '
            'Q4 44×44 key controls · Q5 iZone, Digital Form, MyInsights · Q6 timeline, then Minor. '
            'Round 3: type-only options F, G, H, J dropped; slots added: fun (moodboard "Fun that fits 14 KB") and generic visuals '
            '(never photos or screenshots, Rule 10); I, K, L, M kept with slots, N, O, P new.')
task = ('Dominant task (SCAN-14): judge his engineering from the decisions, then decide to interview or contact '
        '(hiring manager, tech lead; desktop). Recruiter scans title, tools, tenure; designer peer browses on a phone. '
        'Goal-directed, so SCAN-01, -03, -07, -08 strict.\n')
def opt(i, name, axis, note, order, rows1440, margin=80):
    return {'id': i, 'name': name, 'axis': axis, 'note': task + note + '\n' + answered,
            'artboards': [compact(order, footer='C1f'), {'width': 1440, 'margin': margin, 'rows': rows1440}]}

options = []

I_ORDER = ['H2', 'H3', 'HV', 'H4', 'H5', 'ILv', 'IP1', 'IP2', 'IP3', 'X1', 'X2f', 'FM']
options.append(opt('I', 'List + detail reader, with slots', 'RESP-06 two panes · slots: opening visual, a visual thumb per Main row (SCAN-12, one side), row hover, marquee, copy email',
    'Option I (kept): the round-2 reader plus an opening visual beside the decision, a visual thumb trailing each Main row, full-row hover on the list and timeline, the name marquee as a closing band and click-to-copy email.',
    I_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(6, pl(['H2', 'H3'], 'left half: decision, then title')), cell(3, pl(['HV'], 'beside the decision, never above it')), cell(3, pl(['H4', 'H5'], 'right'))],
          [cell(4, pl(['ILv'], 'list pane, pinned'), sticky=True), cell(8, pl(['IP1', 'IPX'], 'detail pane'))],
          [cell(6, pl(['X1'], 'left half')), cell(6, pl(['X2f'], 'right half'))],
          [cell(12, pl(['FM'], 'closing band, full width'))]]},
      FTR([cell(12, pl(['C1f'], 'footer'))])]))

K_ORDER = ['F0r', 'KCf', 'H4', 'H5', 'P0f', 'P1', 'V1', 'P2', 'V2', 'P3', 'V3', 'X1', 'X2f', 'M1f', 'FM']
options.append(opt('K', 'Credits poster, with slots', 'HIER-03 marks after the decision · slots: light rays behind the title card, marks grey until touched, a visual after each project (SCAN-12, trailing side)',
    'Option K (kept): the title card gains a light-rays layer (1440, pointer only); the credits strip greys its marks until touched; each Main Project gets a trailing visual; rows hover; the name marquee closes the page.',
    K_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(10, pl(['F0r'], 'title card, cols 1–10', ['HIER-01'])), gap(2)],
          [cell(12, pl(['KCf'], 'credits strip, full width'))],
          [gap(2), cell(6, pl(['H4', 'H5', 'P0f'], 'cols 3–8', ['TYPE-01'])), gap(4)]]
        + [[gap(2), cell(6, pl([f'P{n}'], 'cols 3–8', ['TYPE-01'])), cell(4, pl([f'V{n}'], 'trailing, beside its project', ['GRID-02']))] for n in (1, 2, 3)]
        + [[gap(2), cell(6, pl(['X1', 'X2f', 'M1f'], 'cols 3–8', ['TYPE-01'])), gap(4)],
           [cell(12, pl(['FM'], 'closing band, full width'))]]},
      FTR([gap(2), cell(6, pl(['C1f'], 'footer, cols 3–8')), gap(4)])]))

L_ORDER = ['H2', 'H3', 'HV', 'H4', 'H5', 'P0f', 'LP1f', 'VL1', 'LP2', 'VL2', 'LP3', 'VL3', 'X1', 'LX2', 'M1f', 'FM']
options.append(opt('L', 'Mark spine, with slots', 'SCAN-12 marks on the trailing edge · slots: a full-width visual interlude after each project for rhythm, marks grey until touched',
    'Option L (kept): the mark spine stays on the trailing edge; between projects a full-width visual interlude sets a text / picture / text beat; marks grey until touched; closing marquee; copy email.',
    L_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [gap(2), cell(5, pl(['H2', 'H3'], 'cols 3–7')), cell(3, pl(['HV'], 'beside the decision')), gap(2)],
          [gap(2), cell(7, pl(['H4', 'H5', 'P0f'], 'cols 3–9', ['TYPE-01'])), gap(3)]]
        + [r for n, lp in ((1, 'LP1f'), (2, 'LP2'), (3, 'LP3')) for r in (
            [gap(2), cell(7, pl([lp], 'cols 3–9, marks trailing', ['TYPE-01'])), gap(3)],
            [cell(12, pl([f'VL{n}'], 'full-width interlude after its project'))])]
        + [[gap(2), cell(7, pl(['X1', 'LX2', 'M1f'], 'cols 3–9', ['TYPE-01'])), gap(3)],
           [cell(12, pl(['FM'], 'closing band, full width'))]]},
      FTR([gap(2), cell(7, pl(['C1f'], 'footer, cols 3–9')), gap(3)])]))

M_ORDER = ['H2', 'H3', 'HV', 'H4', 'H5', 'P0f', 'P1', 'P2', 'P3', 'X1', 'MT0f', 'MT1', 'VT1', 'MT2', 'MT3', 'VT2', 'MT4', 'MT5', 'VT3', 'MT6', 'M1f', 'FM']
options.append(opt('M', 'Employer wall, with slots', 'GRP-01 one tile per employer · slots: visual tiles woven into the wall for a checkerboard rhythm, marks grey until touched',
    'Option M (kept): the wall becomes a 4-across checkerboard (1440) of employer tiles and visual tiles, newest first, read row by row; marks grey until touched; rows hover; closing marquee.',
    M_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [gap(2), cell(5, pl(['H2', 'H3'], 'cols 3–7')), cell(3, pl(['HV'], 'beside the decision')), gap(2)],
          [gap(2), cell(6, pl(['H4', 'H5', 'P0f', 'P1', 'P2', 'P3', 'X1'], 'one column, cols 3–8', ['TYPE-01'])), gap(4)],
          [cell(12, pl(['MT0f'], 'wall heading'))],
          [cell(3, pl(['MT1'], 'wall row 1')), cell(3, pl(['VT1'], 'wall row 1')), cell(3, pl(['MT2'], 'wall row 1')), cell(3, pl(['MT3'], 'wall row 1'))],
          [cell(3, pl(['VT2'], 'wall row 2')), cell(3, pl(['MT4'], 'wall row 2')), cell(3, pl(['MT5'], 'wall row 2')), cell(3, pl(['VT3'], 'wall row 2'))],
          [cell(3, pl(['MT6'], 'wall row 3')), gap(9)],
          [gap(2), cell(6, pl(['M1f'], 'cols 3–8')), gap(4)],
          [cell(12, pl(['FM'], 'closing band, full width'))]]},
      FTR([gap(2), cell(6, pl(['C1f'], 'footer, cols 3–8')), gap(4)])]))

N_ORDER = ['H2', 'H3', 'HV', 'H4', 'H5', 'P0f', 'P1', 'V1', 'P2', 'V2', 'P3', 'V3', 'X1', 'X2f', 'M1f', 'FM']
options.append(opt('N', 'Zigzag rhythm', 'SCAN-12: zigzag is allowed for 2–3 rows · text and visual trade sides down the three Main Projects',
    'Option N (new): the three Main Projects alternate text and visual sides at 1440 (text leads rows 1 and 3, the visual leads row 2 by CSS order; DOM keeps text first, A11Y-C1). At 320 each project reads text, then its visual.',
    N_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(7, pl(['H2', 'H3'], 'leading seven columns', ['HIER-01'])), cell(5, pl(['HV'], 'trailing, beside the decision'))],
          [gap(2), cell(6, pl(['H4', 'H5', 'P0f'], 'cols 3–8', ['TYPE-01'])), gap(4)],
          [cell(7, pl(['P1'], 'row 1: text leading', ['TYPE-01'])), cell(5, pl(['V1'], 'row 1: visual trailing'))],
          [cell(5, [P('V2', 'row 2: visual leading (CSS order; DOM text first)', ['SCAN-12', 'A11Y-C1', 'HIER-03'])]), cell(7, pl(['P2'], 'row 2: text trailing', ['TYPE-01']))],
          [cell(7, pl(['P3'], 'row 3: text leading', ['TYPE-01'])), cell(5, pl(['V3'], 'row 3: visual trailing'))],
          [gap(2), cell(6, pl(['X1', 'X2f', 'M1f'], 'cols 3–8', ['TYPE-01'])), gap(4)],
          [cell(12, pl(['FM'], 'closing band, full width'))]]},
      FTR([gap(2), cell(6, pl(['C1f'], 'footer, cols 3–8')), gap(4)])]))

O_ORDER = ['F0r', 'HV', 'H4', 'H5', 'P0f', 'P1', 'V1', 'P2', 'P3', 'V2', 'X1', 'V3', 'X2f', 'M1f', 'FM']
options.append(opt('O', 'Bento board', 'GRP-C3: every item in its own tile (GRP-01) against keeping block count low (CPLX-01) · brief "bento layouts"',
    'Option O (new): at 1440 the page is a tile board: the title card with its rays, an opening visual, About and Qualifications, the three Main Projects at different tile sizes with visual tiles between them, then History and Minor Projects side by side. Row by row, it keeps the master order.',
    O_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(8, pl(['F0r'], 'hero tile, 8 columns', ['HIER-01'])), cell(4, pl(['HV'], 'visual tile beside the hero'))],
          [cell(6, pl(['H4'], 'tile')), cell(6, pl(['H5'], 'tile'))],
          [cell(12, pl(['P0f'], 'full-width heading'))],
          [cell(8, pl(['P1'], 'large tile', ['TYPE-01'])), cell(4, pl(['V1'], 'visual tile'))],
          [cell(4, pl(['P2'], 'tile')), cell(4, pl(['P3'], 'tile')), cell(4, pl(['V2'], 'visual tile'))],
          [cell(8, pl(['X1'], 'tile')), cell(4, pl(['V3'], 'visual tile'))],
          [cell(6, pl(['X2f'], 'tile')), cell(6, pl(['M1f'], 'tile'))],
          [cell(12, pl(['FM'], 'closing band, full width'))]]},
      FTR([cell(12, pl(['C1f'], 'footer'))])]))

P_ORDER = ['H2', 'H3', 'HV', 'H4', 'H5', 'P0f', 'P1', 'V1', 'P2', 'V2', 'P3', 'V3', 'X1', 'FR', 'X2f', 'M1f', 'FM']
options.append(opt('P', 'Ruler spine', 'CONV-04 leading rail: the scroll ruler, ticks are the years · moodboard "Scroll ruler as the timeline spine"',
    'Option P (new): at 1440 a thin ruler pins to the leading edge, one tick per year 2026 → 2021, tracking your place; one column of content with visuals trailing each project. At 320 the ruler becomes a strip that pins under the header once History starts (A11Y-03: reserve scroll padding).',
    P_ORDER, [HDR(),
      {'landmark': 'main', 'rows': [
          [cell(1, [P('FR', 'leading ruler, pinned (CSS-positioned independent region, A11Y-C1)', ['CONV-04', 'A11Y-03', 'A11Y-C1', 'Asked Q4'])], sticky=True),
           cell(7, pl(['H2', 'H3', 'H4', 'H5', 'P0f', 'P1', 'V1', 'P2', 'V2', 'P3', 'V3', 'X1', 'X2f', 'M1f'], 'content column, cols 2–8; each visual straight after its project', ['TYPE-01'])),
           cell(4, pl(['HV'], 'trailing, beside the decision'))],
          [cell(12, pl(['FM'], 'closing band, full width'))]]},
      FTR([gap(1), cell(7, pl(['C1f'], 'footer, cols 2–8')), gap(4)])]))

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

FAIL = json.load(open(ARGS3[2])) if len(ARGS3) > 2 and os.path.exists(ARGS3[2]) else {}
spec = {'title': 'Portfolio block-out · round 3', 'fold': {'320': 568, '1440': 765}, 'blocks': blocks,
        'options': options, 'failures': FAIL}
json.dump(spec, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('blocks', len(blocks), 'options', len(options))
