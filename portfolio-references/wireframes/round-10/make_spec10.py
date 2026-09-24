"""Round 10: round-9 PS kept. The hero says who he is in a general line from his CV, with no project figure;
About carries the decision-before-platform job. Reuses blocks from make_spec9.py (and, through it, rounds 1-8)."""
import json, sys, os

ARGS10 = sys.argv[:]
src9 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_spec9.py'), encoding='utf-8').read()
sys.argv = [sys.argv[0], '/dev/null']
exec(src9[:src9.index('\n# ---------- options ----------')])
OUT = ARGS10[1]

D.update({
    'hero_who': '"Entolment shouldnt be the jogh light that is just one rohect highligh should be who i am or a genral tagline summarizing my experience. '
                'enrolments 40k looks stupid if they want to know they should go to the projects" (your feedback, round 9); '
                '"Senior Technical Lead with 5 years of experience delivering enterprise OutSystems and full-stack platforms" (CV); '
                'journey, Hiring manager stage 2: "Find out who he is and whether to read further."',
    'about_job': 'journey: "Decision before platform: the About text and each Main Project must put a decision before the platform name"; '
                 'details, About: "one line on what he is, in the settled title. One line that lets a reader outside low-code calibrate OutSystems, '
                 'through a decision rather than the platform name. One line on the front-end and design interest the page itself shows."',
})

# ---------- hero: who he is, in general terms; no single-project figure ----------
block('F0t', 'Home · title card: a general line on who he is, then years and title',
      '<div style="position:relative">'
      '<div style="position:absolute;inset:0;border:2px dashed #aaaaaa;background:repeating-linear-gradient(120deg,#ececec 0 18px,#f6f6f6 18px 36px)"></div>'
      '<div style="position:relative;padding:12px">'
      '<h1 style="font-size:clamp(24px,3.4vw,48px);line-height:1.15;margin:0;padding-top:clamp(4px,3vw,48px);max-width:24ch">'
      'I design and build enterprise systems: on my own, in a team, and leading one.</h1>'
      '<p style="margin:clamp(16px,3vw,40px) 0 0;font-size:15px;font-weight:700">5 years · since Apr 2021</p>'
      '<p style="margin:4px 0 clamp(24px,2vw,40px);font-size:20px;font-weight:600">OutSystems Technical Lead</p>'
      + fun('light rays behind this card follow the pointer · off on touch and reduced motion') + LIVE + '</div></div>',
      ['HIER-01', 'SCAN-03', 'SCAN-01', 'PRIO-02', 'PRIO-03'], 'hero_who')

# ---------- About: now the first place a decision comes before the platform name ----------
block('H4d', 'Home · About, carrying the decision-before-platform line the hero no longer does',
      f'<h2 style="{LABEL}">About</h2><p style="margin:4px 0 0">'
      + ph('About, written by Wan Zayd, three short lines: who he is, in the settled title · one decision, told before the word OutSystems · '
           'his interest in front-end and design') + '</p>',
      ['SCAN-03', 'PRIO-01', 'HIER-02'], 'about_job')

# ---------- options ----------
HDR = lambda: {'landmark': 'header', 'rows': [[cell(12, [P('H1', 'top bar', ['CONV-01', 'CONV-04', 'INT-16', 'A11Y-02', 'Asked Q4'])])]]}
FTR = lambda cells: {'landmark': 'footer', 'rows': [cells]}
def pl(ids, where, add=()):
    return [P(b, where, B[b]['rules'] + list(add)) for b in ids]

answered = ('Answered: Q1 one page, 5 sections · Q2 LinkedIn dates, CV roles · Q3 fold 765 / 568 · Q4 44×44 · '
            'Q5 iZone, Digital Form, MyInsights · Q6 timeline, then Minor. Round 10 feedback: the hero says who he is, not one project; '
            'the load-test figure belongs in the project; check copy priority.')
task = ('Dominant task (SCAN-14): judge his engineering from the decisions, then decide to interview or contact '
        '(hiring manager, tech lead; desktop). Recruiter scans title, tools, tenure; designer peer browses on a phone.\n')
TOP = ['F0t', 'GLh', 'KCm', 'H4d', 'H5', 'P0h']
MAIN = ['PS7', 'PSD7_1', 'PSX7']
END320 = ['X1', 'HBs', 'MB3', 'FM']
rows1440 = ([[cell(8, pl(['F0t'], 'hero, 8 columns', ['HIER-01'])), cell(4, pl(['GLh'], 'beside the hero, after it in reading order'))],
             [cell(12, pl(['KCm'], 'Worked with strip, full width'))],
             [cell(6, pl(['H4d'], 'left half')), cell(6, pl(['H5'], 'right half'))],
             [cell(12, pl(['P0h'], 'full-width heading'))],
             [cell(12, pl(['PS7'], 'full-width shelf'))],
             [gap(2), cell(8, pl(['PSD7_1', 'PSX7'], 'notes, under the shelf')), gap(2)],
             [gap(2), cell(8, pl(['X1'], 'cols 3–10')), gap(2)],
             [cell(12, pl(['HB9'], 'full-width history bar'))],
             [gap(2), cell(8, pl(['HP7'], 'the chosen period, directly under the bar'))],
             [cell(12, pl(['MB3'], 'full-width bento'))],
             [cell(12, pl(['FM'], 'closing band'))]])
note = ('Option PS, round 10. Copy priority, top down: who he is (a general line from his CV, not one project), years, title; '
        'then who he has worked with; then About, where a decision comes before the platform name (journey: About and each Main Project). '
        'Figures such as the 40,000-enrolment load test stay inside their project. Phone history stays the moving strip.')
options = [{'id': 'PS', 'name': 'R3 · poster shelf, round 10', 'axis': 'Round-9 PS with a who-I-am hero and copy re-ranked',
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
FAIL = json.load(open(ARGS10[2])) if len(ARGS10) > 2 and os.path.exists(ARGS10[2]) else {}
spec = {'title': 'Portfolio block-out · round 10', 'fold': {'320': 568, '1440': 765}, 'blocks': blocks,
        'options': options, 'failures': FAIL}
json.dump(spec, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('blocks', len(blocks), 'options', len(options))
