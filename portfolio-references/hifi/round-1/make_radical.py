# Radical directions C (Engineering manual), D (Title sequence), E (The book).
# Same real content as round 10; structure and look change.
import json
_src = open('make_hifi.py').read()
exec(_src.split('# ---------------- shared pieces ----------------')[0])  # content + SANS/SERIF/MONO

NOTES_ALL = {
 0: NOTES,
 1: [('The problem', 'Maybank had no internal form platform. A vendor built the forms, and nothing confidential could go in them.'),
     ('The choice', 'Question types built to be extended, so each MVP added new types and features and made the platform more stable.'),
     ('What it cost', 'Each new question type added complexity.'),
     ('What happened', 'Used across Maybank. By the fifth MVP it had over 80 forms, with thousands of submissions and users.'),
     ('My part', 'I was the only developer, and also the Technical Lead and Product Owner.'),
     ('Tools', None)],
 2: [('The problem', 'Auditors checked exceptions by hand, on files and paper.'),
     ('The choice', 'A fixed set of roles, each tied to its own business rules.'),
     ('What it cost', 'Not much, as far as I could see.'),
     ('What happened', 'Auditors moved audit exceptions into one place and worked through them in the system, not on files and paper.'),
     ('My part', 'One of four developers; I wasn’t the lead. I built user management, permissions and front-end screens, and parts of the audit rules and the data sync.'),
     ('Tools', None)],
}
TOOLS_ALL = {0: IZTOOLS, 1: 'OutSystems O11', 2: 'OutSystems O11'}
ORG = {0: [('Sunway University, via ', False), ('AvePoint', True)], 1: [('Maybank', True)], 2: [('PETRONAS', True), (', via ', False), ('FPT Software', True)]}
FIG = {0: ('40,000', 'enrolments in a 20-minute load test'), 1: ('80+', 'forms by the fifth MVP'), 2: None}
PIX = ['map motif, Sarawak data', 'QR-pattern motif', 'mosque-signage motif']
HIST = [('Jan 2026 – present', 'AvePoint', 'Full-stack developer', '9 mos', True),
        ('Apr 2026 – present', '↳ Sunway University, client', 'Senior Technical Lead', '', False),
        ('Sep 2024 – Jan 2026', 'Maybank', 'Senior OutSystems Engineer', '1 yr 5 mos', True),
        ('May – Jul 2024', 'Adam Digital Assets', 'Part-time', '3 mos', False),
        ('Sep 2022 – Sep 2024', 'FPT Software Malaysia', 'Software Consultant', '2 yrs 1 mo', True),
        ('', '↳ PETRONAS Digital, client', '', '', True),
        ('Apr – Aug 2022', 'Career break', 'Time for personal goals', '5 mos', False),
        ('Apr 2021 – May 2022', 'Impact Business Solutions', 'Software Consultant', '1 yr 2 mos', False)]
ABOUT_PH = '[PLACEHOLDER: About, in your words. Who you are, with the title. One decision, told before the word OutSystems. Your interest in front-end and design.]'
HOW_PH = '[PLACEHOLDER: one short paragraph, in your words, on architecture calls and running a team.]'
POST_PH = '[PLACEHOLDER: a short note in your words]'
AH = ' aria-hidden="true"'
LI_URL = 'https://www.linkedin.com/in/wan-zayd-abdullah-690033230'

def slot(px, color):
    return (f'<span aria-hidden="true" style="display:inline-block;flex-shrink:0;width:{px}px;height:{px}px;box-sizing:border-box;border:1px dashed {color}"></span>')

def orgline(n, sc, px):
    return ''.join((slot(px, sc) if mk else '') + t for t, mk in ORG[n])

def page(title, w, h, helmet, root, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
{helmet}
<div id="top" style="width:{w}px;height:{h}px;box-sizing:border-box;overflow:hidden;display:flex;flex-direction:column;-webkit-font-smoothing:antialiased;{root}">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''

ANIM = '''@keyframes wz-rtl{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@keyframes wz-ltr{from{transform:translateX(-50%)}to{transform:translateX(0)}}
.drift-rtl{animation:wz-rtl 70s linear infinite}.drift-ltr{animation:wz-ltr 80s linear infinite}.marq{animation:wz-rtl 32s linear infinite}
.strip:hover .drift-rtl,.strip:hover .drift-ltr,.strip:focus-within .drift-rtl,.strip:focus-within .drift-ltr,.marq-wrap:hover .marq{animation-play-state:paused}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.qs{list-style:none}.qs::-webkit-details-marker{display:none}
h1,h2,h3{text-wrap:balance}p,dd,td{text-wrap:pretty}
@media (prefers-reduced-motion:reduce){.drift-rtl,.drift-ltr,.marq{animation:none}.strip{overflow-x:auto}*{transition:none!important}}'''

def pause_btn(label, style):
    bars = ('<span aria-hidden="true" style="display:inline-flex;gap:3px"><span style="display:block;width:2px;height:10px;background:currentColor"></span>'
            '<span style="display:block;width:2px;height:10px;background:currentColor"></span></span>')
    return (f'<button type="button" class="pb" aria-pressed="false" aria-label="Pause {label}" style="display:inline-flex;align-items:center;gap:10px;min-height:44px;min-width:44px;'
            f'padding:0 12px;background:transparent;cursor:pointer;{style}">{bars}Pause</button>')

def strip(items_html, height, direction, mask=True, extra=''):
    m = 'linear-gradient(90deg, rgba(0,0,0,0), #000 8%, #000 92%, rgba(0,0,0,0))'
    ms = f'-webkit-mask-image:{m};mask-image:{m};' if mask else ''
    return (f'<div class="strip" style="overflow:hidden;height:{height}px;{ms}{extra}"><div class="drift-{direction}" style="display:flex;width:max-content;height:{height}px;align-items:center">'
            + items_html(False) + items_html(True) + '</div></div>')

def marquee(px, color, pad, weight=700, ls='-0.05em', font=SANS, bg='transparent'):
    one = f'<span style="padding-right:{px//2}px;white-space:nowrap">Wan Zayd Abdullah</span>'
    return (f'<div class="marq-wrap" aria-hidden="true" style="overflow:hidden;padding:{pad}px 0;background:{bg}">'
            f'<div class="marq" style="display:flex;width:max-content;font-family:{font};font-size:{px}px;line-height:1;font-weight:{weight};letter-spacing:{ls};color:{color}">' + one * 4 + '</div></div>')

# =====================================================================
# C · ENGINEERING MANUAL  (Devouring Details, swiss-minimal-cv, Müller-Brockmann)
# =====================================================================
CG, CI, C2, CO, CW = '#EDEDED', '#141414', '#555555', '#F24E1E', '#FCFCFC'
SW = "'Helvetica Neue',Helvetica,-apple-system,'Segoe UI',Arial,sans-serif"
CM = "ui-monospace,'SF Mono',Menlo,Consolas,monospace"
C_HELMET = '''<helmet>
<style>
body{margin:0;background:#EDEDED;color:#141414;font-family:"Helvetica Neue",Helvetica,-apple-system,"Segoe UI",Arial,sans-serif}
a{color:#141414;text-decoration-color:#F24E1E;text-decoration-thickness:2px;text-underline-offset:4px}a:hover{color:#141414;background:#F24E1E}
::selection{background:#F24E1E;color:#141414}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid #F24E1E;outline-offset:2px}
.nv:hover{background:#141414;color:#EDEDED}
.pb{transition:background-color .15s,color .15s}.pb:hover{background:#141414;color:#EDEDED}
.wk:hover{color:#F24E1E}
.bar{transition:filter .15s}.bar:hover{filter:brightness(1.25)}
.row:hover td{background:rgba(20,20,20,0.04)}
.post{transform:rotate(-1.5deg)}.post.b{transform:rotate(1.2deg)}
''' + ANIM + '''
</style>
</helmet>'''

def c_label(px=12, color=C2):
    return f'font-family:{CM};font-size:{px}px;line-height:1.4;letter-spacing:0.02em;text-transform:uppercase;font-weight:400;color:{color}'

def c_sec(id_, label, counter, body, wide, pad_b):
    c = f' <span style="color:{C2}">({counter})</span>' if counter else ''
    if wide:
        return (f'<section aria-labelledby="{id_}" style="margin:0 48px;border-top:2px solid {CI};display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;padding:14px 0 {pad_b}px">'
                f'<h2 id="{id_}" style="grid-column:1 / span 3;margin:0;{c_label(13, CI)}">{label}{c}</h2>'
                f'<div style="grid-column:4 / span 9">{body}</div></section>')
    return (f'<section aria-labelledby="{id_}" style="margin:0 16px;border-top:2px solid {CI};padding:12px 0 {pad_b}px">'
            f'<h2 id="{id_}" style="margin:0 0 20px;{c_label(12, CI)}">{label}{c}</h2>{body}</section>')

def c_cell(label, value, px, extra=''):
    return (f'<div style="border-top:1px solid {CI};padding:10px 0 18px;{extra}"><p style="margin:0 0 6px;{c_label(11)}">{label}</p>'
            f'<div style="font-size:{px}px;line-height:1.5;color:{CI}">{value}</div></div>')

def c_worked(px, gap):
    def items(hidden):
        lis = ''.join(f'<li class="wk" style="display:flex;align-items:center;gap:10px;font-size:{px}px;font-weight:700;letter-spacing:-0.02em;white-space:nowrap">'
                      + (slot(px - 4, CI) if m else '') + f'{n}</li>' for n, m in WORKED)
        return f'<ul{AH if hidden else ""} style="display:flex;align-items:center;gap:{gap}px;margin:0;padding:0 {gap//2}px;list-style:none">{lis}</ul>'
    return items

def c_sheet(n, wide):
    title, name, credit, tools, _ = POSTERS[n]
    notes = dict(NOTES_ALL[n])
    fig = FIG[n]
    org = f'<span style="display:inline-flex;align-items:center;gap:6px;flex-wrap:wrap">{orgline(n, CI, 14)}</span>'
    tl = f'<span style="display:inline-flex;align-items:center;gap:6px;flex-wrap:wrap">{slot(14, CI)}{TOOLS_ALL[n]}</span>'
    figure = ''
    if fig:
        figure = (f'<div style="border-top:1px solid {CI};padding:10px 0 18px"><p style="margin:0 0 6px;{c_label(11)}">Result</p>'
                  f'<p style="margin:0;font-size:{64 if wide else 44}px;line-height:1;font-weight:700;letter-spacing:-0.04em;color:{CO}">{fig[0]}</p>'
                  f'<p style="margin:6px 0 0;font-size:14px;color:{CI}">{fig[1]}</p></div>')
    four = [('The problem', notes['The problem']), ('The choice', notes['The choice']), ('What it cost', notes['What it cost']), ('What happened', notes['What happened'])]
    if wide:
        return (f'<article aria-labelledby="c-p{n}" style="margin:0 48px 88px;border-top:2px solid {CI};display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;padding-top:14px">'
                f'<div style="grid-column:1 / span 3;display:flex;flex-direction:column;gap:6px"><p style="margin:0;{c_label(13, CI)}">{name}</p><p style="margin:0;font-size:14px;line-height:1.5;color:{C2}">{credit}</p></div>'
                f'<div style="grid-column:4 / span 9"><h3 id="c-p{n}" style="margin:0 0 36px;max-width:16ch;font-size:60px;line-height:1.0;font-weight:700;letter-spacing:-0.045em">{title}</h3>'
                f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));column-gap:24px">'
                + c_cell('Client', org, 15) + c_cell('My part', notes['My part'], 15) + c_cell('Tools', tl, 15) + '</div>'
                f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:24px;margin-top:8px">'
                + ''.join(c_cell(l, v, 17) for l, v in four) + '</div>'
                + (f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));column-gap:24px;margin-top:8px">{figure}</div>' if figure else '')
                + '</div></article>')
    return (f'<article aria-labelledby="c-p{n}" style="margin:0 16px 56px;border-top:2px solid {CI};padding-top:12px">'
            f'<p style="margin:0 0 4px;{c_label(12, CI)}">{name}</p><p style="margin:0 0 16px;font-size:13px;color:{C2}">{credit}</p>'
            f'<h3 id="c-p{n}" style="margin:0 0 24px;font-size:32px;line-height:1.02;font-weight:700;letter-spacing:-0.04em">{title}</h3>'
            + c_cell('Client', org, 15) + ''.join(c_cell(l, v, 16) for l, v in four) + figure + c_cell('My part', notes['My part'], 15) + c_cell('Tools', tl, 15)
            + '</article>')

def c_ruler():
    W, PX = 1344, 1344 / 66
    def bar(s, e, lane, label, fill, fg, href, sel=False, hatch=False, lab_out=None):
        x, w = s * PX, (e - s) * PX - 2
        top = 0 if lane == 0 else 58
        h = 44 if lane == 0 else 26
        bg = f'repeating-linear-gradient(135deg, {CI} 0 1px, transparent 1px 7px)' if hatch else fill
        border = f'border:1px solid {CI};' if hatch else ''
        inner = f'<span style="padding:0 10px;white-space:nowrap;overflow:hidden;text-overflow:clip">{label}</span>' if not lab_out else ''
        a = (f'<a class="bar" href="#c-hist-t" aria-label="{label}" style="position:absolute;left:{x:.1f}px;top:{top}px;width:{w:.1f}px;height:{h}px;box-sizing:border-box;{border}'
             f'background:{bg};color:{fg};display:flex;align-items:center;font-size:{14 if lane == 0 else 12}px;font-weight:700;text-decoration:none">{inner}</a>')
        if lab_out:
            a += f'<span aria-hidden="true" style="position:absolute;left:{x + w + 6:.1f}px;top:{top + 5}px;font-size:12px;font-weight:700;white-space:nowrap;color:{CI}">{lab_out}</span>'
        return a
    bars = (bar(0, 14, 0, 'Impact Business Solutions', CI, CG, '') + bar(17, 41, 0, 'FPT Software Malaysia · ↳ PETRONAS Digital', CI, CG, '')
            + bar(41, 57, 0, 'Maybank', CI, CG, '') + bar(57, 66, 0, 'AvePoint', CO, CI, '')
            + bar(12, 17, 1, 'Career break', '', CI, '', hatch=True, lab_out='Career break')
            + bar(37, 40, 1, 'Adam Digital Assets', CI, CG, '', lab_out='Adam Digital Assets, part-time')
            + bar(60, 66, 1, 'Sunway University', CO, CI, '', lab_out=None))
    ticks = (f'<span aria-hidden="true" style="position:absolute;left:0;top:100px;width:{W}px;height:10px;border-top:1px solid {CI};'
             f'background:repeating-linear-gradient(90deg, {CI} 0 1px, transparent 1px {PX:.3f}px)"></span>')
    years = ''
    for label, m in (('Apr 2021', 0), ('2022', 9), ('2023', 21), ('2024', 33), ('2025', 45), ('2026', 57)):
        years += (f'<span aria-hidden="true" style="position:absolute;left:{m * PX:.1f}px;top:100px;height:26px;border-left:1px solid {CI}"></span>'
                  f'<span aria-hidden="true" style="position:absolute;left:{m * PX + 6:.1f}px;top:114px;{c_label(11, CI)}">{label}</span>')
    years += f'<span aria-hidden="true" style="position:absolute;right:0;top:114px;{c_label(11, CO if False else CI)}">Sep 2026</span>'
    return f'<div role="img" aria-label="Career drawn to scale, April 2021 to September 2026. The table below lists every period." style="position:relative;width:{W}px;height:140px">{bars}{ticks}{years}</div>'

def c_hist_table(wide):
    rows = ''
    for period, org, role, dur, mk in HIST:
        sub = org.startswith('↳')
        o = (slot(13, CI) if mk else '') + org
        cur = ' style="background:rgba(242,78,30,0.12)"' if org == 'AvePoint' else ''
        if wide:
            rows += (f'<tr class="row"{cur}><td style="padding:10px 12px 10px 0;border-bottom:1px solid {CI};font-family:{CM};font-size:13px;white-space:nowrap">{period}</td>'
                     f'<td style="padding:10px 12px;border-bottom:1px solid {CI};font-size:16px;font-weight:{400 if sub else 700};{"color:" + C2 if sub else ""}"><span style="display:inline-flex;align-items:center;gap:8px">{o}</span></td>'
                     f'<td style="padding:10px 12px;border-bottom:1px solid {CI};font-size:15px">{role}</td>'
                     f'<td style="padding:10px 0 10px 12px;border-bottom:1px solid {CI};font-family:{CM};font-size:13px;text-align:right;white-space:nowrap">{dur}</td></tr>')
        else:
            rows += (f'<li style="border-top:1px solid {CI};padding:10px 0 12px"><p style="margin:0 0 4px;display:flex;justify-content:space-between;gap:8px;{c_label(11, CI)}"><span>{period}</span><span>{dur}</span></p>'
                     f'<p style="margin:0;display:flex;align-items:center;gap:8px;font-size:16px;font-weight:{400 if sub else 700}">{o}</p>'
                     + (f'<p style="margin:2px 0 0;font-size:14px;color:{C2}">{role}</p>' if role else '') + '</li>')
    if wide:
        th = f'text-align:left;padding:0 12px 8px 0;border-bottom:2px solid {CI};{c_label(11, CI)}'
        return (f'<table id="c-hist-t" style="width:100%;border-collapse:collapse;margin-top:40px"><thead><tr><th style="{th}">Period</th><th style="{th}">Organisation</th><th style="{th}">Role</th>'
                f'<th style="{th};text-align:right;padding-right:0">Length</th></tr></thead><tbody>{rows}</tbody></table>')
    return f'<ol id="c-hist-t" style="list-style:none;margin:0;padding:0;border-bottom:1px solid {CI}">{rows}</ol>'

def c_minor(wide):
    rows = ''
    for name, (desc, parts) in MINOR.items():
        emp = parts[0][0]
        tools = parts[1][0]
        mk_e, mk_t = parts[0][1], parts[1][1]
        d = desc.replace('Cut a daily process from 6 hours to 30 minutes.', f'Cut a daily process from <strong style="background:{CO};padding:0 3px">6 hours to 30 minutes</strong>.')
        e_html = f'<span style="display:inline-flex;align-items:center;gap:6px">{slot(12, CI) if mk_e else ""}{emp}</span>'
        t_html = f'<span style="display:inline-flex;align-items:center;gap:6px">{slot(12, CI) if mk_t else ""}{tools}</span>'
        if wide:
            td = f'padding:12px 16px 14px 0;border-bottom:1px solid {CI};vertical-align:top'
            rows += (f'<tr class="row"><td style="{td};font-size:17px;font-weight:700;white-space:nowrap">{name}</td><td style="{td};font-size:15px;line-height:1.5">{d}</td>'
                     f'<td style="{td};font-size:14px">{e_html}</td><td style="{td};font-family:{CM};font-size:13px;padding-right:0">{t_html}</td></tr>')
        else:
            rows += (f'<li style="border-top:1px solid {CI};padding:12px 0 14px"><p style="margin:0 0 4px;font-size:17px;font-weight:700">{name}</p>'
                     f'<p style="margin:0 0 8px;font-size:14px;line-height:1.5">{d}</p><p style="margin:0;display:flex;flex-wrap:wrap;gap:4px 14px;{c_label(11, CI)}">{e_html}{t_html}</p></li>')
    if wide:
        th = f'text-align:left;padding:0 16px 8px 0;border-bottom:2px solid {CI};{c_label(11, CI)}'
        table = (f'<table style="width:100%;border-collapse:collapse"><thead><tr><th style="{th}">Project</th><th style="{th}">What it is</th><th style="{th}">Employer</th><th style="{th};padding-right:0">Tools</th></tr></thead>'
                 f'<tbody>{rows}</tbody></table>')
    else:
        table = f'<ul style="list-style:none;margin:0;padding:0;border-bottom:1px solid {CI}">{rows}</ul>'
    figs = ''.join(f'<figure style="margin:0"><div style="aspect-ratio:4 / 3;border:1px solid {CI};background:repeating-linear-gradient(135deg, rgba(20,20,20,0.10) 0 1px, transparent 1px 9px)"></div>'
                   f'<figcaption style="margin-top:8px;{c_label(11, CI)}">Fig. {p} (picture to add)</figcaption></figure>' for p in PIX)
    posts = ''.join(f'<p class="post{" b" if i else ""}" style="margin:0;padding:14px 16px;background:{CW};box-shadow:0 1px 0 {CI},0 10px 24px rgba(20,20,20,0.10);font-family:{CM};font-size:13px;line-height:1.5">'
                    f'<span style="display:block;margin-bottom:6px;{c_label(10, CO)}">Note</span>{POST_PH}</p>' for i in range(2))
    if wide:
        return (table + f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));column-gap:24px;margin-top:40px">{figs}</div>'
                f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));column-gap:24px;margin-top:32px">{posts}</div>')
    return (table + f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:28px">{figs}{posts}</div>')

def c_quals(wide):
    data = [(q[0], 'OutSystems' if 'OutSystems' in q[0] else ('Universiti Teknologi MARA' if 'MARA' in q[1] else '[PLACEHOLDER: issuer]'),
             '[year]' if 'MARA' not in q[1] else q[1].split(', ')[1]) for q in QUALS]
    if wide:
        th = f'text-align:left;padding:0 16px 8px 0;border-bottom:2px solid {CI};{c_label(11, CI)}'
        td = f'padding:12px 16px 12px 0;border-bottom:1px solid {CI};vertical-align:top'
        rows = ''.join(f'<tr class="row"><td style="{td};font-size:17px;font-weight:700">{a}</td><td style="{td};font-size:15px">{b}</td>'
                       f'<td style="{td};font-family:{CM};font-size:13px;white-space:nowrap;padding-right:0;color:{C2 if c == "[year]" else CI}">{c}</td></tr>' for a, b, c in data)
        return (f'<table style="width:100%;border-collapse:collapse"><thead><tr><th style="{th}">Qualification</th><th style="{th}">Issuer</th><th style="{th};padding-right:0">Year</th></tr></thead>'
                f'<tbody>{rows}</tbody></table><p style="margin:10px 0 0;font-family:{CM};font-size:12px;color:{C2}">[year]: [PLACEHOLDER: certification years]</p>')
    rows = ''.join(f'<li style="border-top:1px solid {CI};padding:10px 0 12px"><p style="margin:0 0 4px;font-size:16px;font-weight:700;line-height:1.35">{a}</p>'
                   f'<p style="margin:0;display:flex;justify-content:space-between;gap:10px;{c_label(11, CI)}"><span>{b}</span><span>{c}</span></p></li>' for a, b, c in data)
    return f'<ul style="list-style:none;margin:0;padding:0;border-bottom:1px solid {CI}">{rows}</ul>'

def c_contact(wide):
    lab = c_label(11)
    if wide:
        return (f'<footer id="contact" aria-labelledby="c-contact" style="flex-grow:1;margin:0 48px;border-top:2px solid {CI};display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;align-content:start;padding:14px 0 96px">'
                f'<h2 id="c-contact" style="grid-column:1 / span 3;margin:0;{c_label(13, CI)}">Contact</h2>'
                f'<div style="grid-column:4 / span 9"><p style="margin:0 0 40px;font-size:60px;line-height:1.0;font-weight:700;letter-spacing:-0.045em">Happy to talk about any of this.</p>'
                f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:24px">'
                f'<div style="border-top:1px solid {CI};padding-top:10px"><p style="margin:0 0 6px;{lab}">Email</p><button type="button" class="pb" style="min-height:44px;padding:0;border:0;background:transparent;font-family:{SW};font-size:22px;font-weight:700;color:{CI};text-align:left;cursor:pointer;text-decoration:underline;text-decoration-color:{CO};text-decoration-thickness:2px;text-underline-offset:5px">[PLACEHOLDER: email address]</button></div>'
                f'<div style="border-top:1px solid {CI};padding-top:10px"><p style="margin:0 0 6px;{lab}">LinkedIn</p><a href="{LI_URL}" style="display:inline-flex;align-items:center;min-height:44px;font-size:22px;font-weight:700">{LINKEDIN}</a></div>'
                '</div></div></footer>')
    return (f'<footer id="contact" aria-labelledby="c-contact" style="flex-grow:1;margin:0 16px;border-top:2px solid {CI};padding:12px 0 64px">'
            f'<h2 id="c-contact" style="margin:0 0 20px;{c_label(12, CI)}">Contact</h2>'
            f'<p style="margin:0 0 28px;font-size:32px;line-height:1.02;font-weight:700;letter-spacing:-0.04em">Happy to talk about any of this.</p>'
            f'<div style="border-top:1px solid {CI};padding-top:10px"><p style="margin:0 0 4px;{lab}">Email</p><button type="button" class="pb" style="min-height:44px;padding:0;border:0;background:transparent;font-family:{SW};font-size:17px;font-weight:700;color:{CI};text-align:left;cursor:pointer;text-decoration:underline;text-decoration-color:{CO};text-decoration-thickness:2px;text-underline-offset:5px">[PLACEHOLDER: email address]</button></div>'
            f'<div style="border-top:1px solid {CI};padding-top:10px;margin-top:10px"><p style="margin:0 0 4px;{lab}">LinkedIn</p><a href="{LI_URL}" style="display:inline-flex;align-items:center;min-height:44px;font-size:15px;font-weight:700;overflow-wrap:anywhere">{LINKEDIN}</a></div>'
            '</footer>')

def c_desktop():
    cell = f'padding:12px 16px;border-left:1px solid {CI};display:flex;flex-direction:column;justify-content:space-between;gap:6px'
    tb = (f'<header style="margin:24px 48px 0;border:1px solid {CI};display:grid;grid-template-columns:3fr 3fr 2fr 4fr;min-height:88px;background:{CW}">'
          f'<div style="padding:12px 16px;display:flex;flex-direction:column;justify-content:space-between;gap:6px"><span style="{c_label(11)}">Name</span><a href="#top" style="font-size:20px;font-weight:700;letter-spacing:-0.02em;text-decoration:none">Wan Zayd Abdullah</a></div>'
          f'<div style="{cell}"><span style="{c_label(11)}">Title</span><span style="font-size:18px;font-weight:700;letter-spacing:-0.01em">OutSystems Technical Lead</span></div>'
          f'<div style="{cell}"><span style="{c_label(11)}">Experience</span><span style="font-family:{CM};font-size:15px">5 years · since Apr 2021</span></div>'
          f'<nav aria-label="Sections" style="{cell};padding:0 0 0 16px"><span style="{c_label(11)};padding-top:12px">Sections</span><ul style="list-style:none;margin:0;padding:0;display:flex">'
          + ''.join(f'<li style="flex:1"><a class="nv" href="#{t}" style="display:flex;align-items:center;min-height:44px;padding:0 12px;border-top:1px solid {CI};{"border-left:1px solid " + CI + ";" if i else ""}font-family:{CM};font-size:14px;text-decoration:none">{t}</a></li>' for i, t in enumerate(('work', 'history', 'contact')))
          + '</ul></nav></header>')
    hero = (f'<section aria-labelledby="c-hero" style="margin:0 48px;padding:72px 0 56px">'
            f'<h1 id="c-hero" style="margin:0;max-width:20ch;font-size:96px;line-height:0.96;font-weight:700;letter-spacing:-0.055em">{TAGLINE}</h1></section>')
    glance = (f'<section aria-labelledby="c-glance" style="margin:0 48px 72px"><h2 id="c-glance" class="sr">At a glance</h2><ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:2px solid {CI}">'
              + ''.join(f'<li style="padding:12px 16px 16px {0 if i == 0 else 16}px;{"border-left:1px solid " + CI if i else ""}"><span style="display:block;font-size:80px;line-height:1;font-weight:700;letter-spacing:-0.05em">{n}</span>'
                        f'<span style="display:block;margin-top:8px;{c_label(12, CI)}">{t}</span></li>' for i, (n, t) in enumerate((('5', 'employers'), ('11', 'projects, 3 in detail'), ('5', 'qualifications'))))
              + '</ul></section>')
    worked = (f'<section aria-labelledby="c-worked" style="margin:0 48px 96px;border-top:1px solid {CI};border-bottom:1px solid {CI};display:grid;grid-template-columns:3fr 9fr">'
              f'<div style="display:flex;flex-direction:column;justify-content:space-between;padding:10px 16px 6px 0;border-right:1px solid {CI}"><h2 id="c-worked" style="margin:0;{c_label(13, CI)}">Worked with</h2>'
              f'{pause_btn("Worked with", f"border:1px solid {CI};font-family:{CM};font-size:12px;text-transform:uppercase;color:{CI};align-self:flex-start")}</div>'
              + strip(c_worked(30, 64), 88, 'rtl') + '</section>')
    about = c_sec('c-about', 'About', None, f'<p style="margin:0;max-width:40ch;font-size:26px;line-height:1.35;font-weight:400;color:{C2}">{ABOUT_PH}</p>', True, 88)
    qual = c_sec('c-qual', 'Qualifications', '5', c_quals(True), True, 120)
    projects = (f'<section id="work" aria-labelledby="c-proj" style="margin:0 48px 40px"><h2 id="c-proj" style="margin:0;font-size:140px;line-height:0.9;font-weight:700;letter-spacing:-0.06em">Projects<span style="color:{C2};font-weight:400"> (3)</span></h2>'
                f'<p style="margin:20px 0 0;max-width:40ch;font-size:20px;line-height:1.5">Three projects, each with what was wrong, what we chose and what it cost.</p></section>'
                + ''.join(c_sheet(n, True) for n in range(3)))
    how = c_sec('c-how', 'How I work', None, f'<p style="margin:0;max-width:40ch;font-size:26px;line-height:1.35;color:{C2}">{HOW_PH}</p>', True, 120)
    hist = (f'<section id="history" aria-labelledby="c-hist" style="margin:0 48px;border-top:2px solid {CI};padding:14px 0 120px">'
            f'<h2 id="c-hist" style="margin:0 0 40px;{c_label(13, CI)}">History, to scale</h2>' + c_ruler() + c_hist_table(True) + '</section>')
    minor = c_sec('c-minor', 'Minor Projects', '8', c_minor(True), True, 120)
    body = tb + '<main style="display:flex;flex-direction:column">' + hero + glance + worked + about + qual + projects + how + hist + minor + marquee(200, CG, 36, bg=CI) + '</main>' + c_contact(True)
    return page('Portfolio C, desktop', 1440, 7600, C_HELMET, f'background:{CG};color:{CI};font-family:{SW}', body)

def c_phone():
    tb = (f'<header style="margin:16px 16px 0;border:1px solid {CI};background:{CW}">'
          f'<div style="display:grid;grid-template-columns:1fr 1fr"><div style="padding:10px 12px"><span style="display:block;{c_label(10)}">Name</span><a href="#top" style="display:block;margin-top:4px;font-size:16px;font-weight:700;line-height:1.2;text-decoration:none">Wan Zayd Abdullah</a></div>'
          f'<div style="padding:10px 12px;border-left:1px solid {CI}"><span style="display:block;{c_label(10)}">Title</span><span style="display:block;margin-top:4px;font-size:14px;font-weight:700;line-height:1.25">OutSystems Technical Lead</span></div></div>'
          f'<div style="padding:8px 12px;border-top:1px solid {CI};font-family:{CM};font-size:13px">5 years · since Apr 2021</div>'
          f'<nav aria-label="Sections"><ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:1px solid {CI}">'
          + ''.join(f'<li><a class="nv" href="#{t}" style="display:flex;align-items:center;justify-content:center;min-height:44px;{"border-left:1px solid " + CI + ";" if i else ""}font-family:{CM};font-size:13px;text-decoration:none">{t}</a></li>' for i, t in enumerate(('work', 'history', 'contact')))
          + '</ul></nav></header>')
    hero = f'<section aria-labelledby="c-hero" style="margin:0 16px;padding:40px 0 32px"><h1 id="c-hero" style="margin:0;font-size:38px;line-height:0.98;font-weight:700;letter-spacing:-0.05em">{TAGLINE}</h1></section>'
    glance = (f'<section aria-labelledby="c-glance" style="margin:0 16px 56px"><h2 id="c-glance" class="sr">At a glance</h2><ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:2px solid {CI}">'
              + ''.join(f'<li style="padding:10px 8px 10px {0 if i == 0 else 8}px;{"border-left:1px solid " + CI if i else ""}"><span style="display:block;font-size:40px;line-height:1;font-weight:700;letter-spacing:-0.05em">{n}</span>'
                        f'<span style="display:block;margin-top:6px;{c_label(10, CI)}">{t}</span></li>' for i, (n, t) in enumerate((('5', 'employers'), ('11', 'projects, 3 in detail'), ('5', 'qualifications'))))
              + '</ul></section>')
    worked = (f'<section aria-labelledby="c-worked" style="margin:0 0 56px"><div style="display:flex;justify-content:space-between;align-items:center;margin:0 16px;border-top:2px solid {CI};padding-top:6px">'
              f'<h2 id="c-worked" style="margin:0;{c_label(12, CI)}">Worked with</h2>{pause_btn("Worked with", f"border:1px solid {CI};font-family:{CM};font-size:11px;text-transform:uppercase;color:{CI}")}</div>'
              + strip(c_worked(22, 40), 88, 'rtl', extra=f'border-bottom:1px solid {CI};') + '</section>')
    about = c_sec('c-about', 'About', None, f'<p style="margin:0;font-size:19px;line-height:1.4;color:{C2}">{ABOUT_PH}</p>', False, 56)
    qual = c_sec('c-qual', 'Qualifications', '5', c_quals(False) + f'<p style="margin:8px 0 0;font-family:{CM};font-size:11px;color:{C2}">[year]: [PLACEHOLDER: certification years]</p>', False, 72)
    projects = (f'<section id="work" aria-labelledby="c-proj" style="margin:0 16px 28px"><h2 id="c-proj" style="margin:0;font-size:56px;line-height:0.9;font-weight:700;letter-spacing:-0.06em">Projects<span style="color:{C2};font-weight:400"> (3)</span></h2>'
                f'<p style="margin:14px 0 0;font-size:16px;line-height:1.5">Three projects, each with what was wrong, what we chose and what it cost.</p></section>'
                + ''.join(c_sheet(n, False) for n in range(3)))
    how = c_sec('c-how', 'How I work', None, f'<p style="margin:0;font-size:19px;line-height:1.4;color:{C2}">{HOW_PH}</p>', False, 72)
    def tape(hidden):
        lis = ''
        for period, name, mk, role, client in TL:
            lis += (f'<li style="display:flex;flex-direction:column;justify-content:center;gap:3px;height:96px;box-sizing:border-box;padding:0 24px;border-left:1px solid {CI};white-space:nowrap">'
                    f'<span style="{c_label(10, CI)}">{period}</span><span style="display:flex;align-items:center;gap:6px;font-size:16px;font-weight:700">{slot(14, CI) if mk else ""}{name}</span>'
                    f'<span style="display:flex;align-items:center;gap:6px;font-size:12px;color:{C2}">{role}{(slot(12, CI) + client) if client else ""}</span></li>')
        return f'<ol{AH if hidden else ""} style="display:flex;margin:0;padding:0;list-style:none">{lis}</ol>'
    hist = (f'<section id="history" aria-labelledby="c-hist" style="margin:0 0 72px"><div style="display:flex;justify-content:space-between;align-items:center;margin:0 16px;border-top:2px solid {CI};padding-top:6px">'
            f'<h2 id="c-hist" style="margin:0;{c_label(12, CI)}">History</h2>{pause_btn("History", f"border:1px solid {CI};font-family:{CM};font-size:11px;text-transform:uppercase;color:{CI}")}</div>'
            + strip(tape, 96, 'ltr', extra=f'border-bottom:1px solid {CI};background:repeating-linear-gradient(90deg, {CI} 0 1px, transparent 1px 8px) bottom / 100% 8px no-repeat;')
            + f'<div style="margin:24px 16px 0">' + c_hist_table(False) + '</div></section>')
    minor = c_sec('c-minor', 'Minor Projects', '8', c_minor(False), False, 64)
    body = tb + '<main style="display:flex;flex-direction:column">' + hero + glance + worked + about + qual + projects + how + hist + minor + marquee(80, CG, 20, bg=CI) + '</main>' + c_contact(False)
    return page('Portfolio C, phone', 320, 9000, C_HELMET, f'background:{CG};color:{CI};font-family:{SW}', body)

# =====================================================================
# D · TITLE SEQUENCE  (Art of the Title, MUBI, Megha one-accent hero)
# =====================================================================
DB, DT, D2, DR, DD = '#0B0B0C', '#F2F2F2', '#9A9A9A', '#FF0048', '#6E6E6E'
D_HELMET = '''<helmet>
<style>
body{margin:0;background:#0B0B0C;color:#F2F2F2;font-family:-apple-system,"Segoe UI",system-ui,sans-serif}
a{color:#F2F2F2;text-decoration-color:#FF0048;text-underline-offset:6px}a:hover{color:#FF0048}
::selection{background:#FF0048;color:#0B0B0C}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid #FF0048;outline-offset:4px}
.nv:hover{color:#FF0048}.pb:hover{color:#F2F2F2}
.wk{transition:color .5s ease}.wk:hover{color:#F2F2F2}
.scene .fade{transition:opacity .6s ease}
''' + ANIM + '''
</style>
</helmet>'''

def d_caps(px=12, color=D2, ls='0.28em'):
    return f'font-size:{px}px;line-height:1.5;letter-spacing:{ls};text-transform:uppercase;font-weight:500;color:{color}'

def d_beam(at, a=0.10):
    m = f'radial-gradient(70% 80% at {at}, #000 5%, rgba(0,0,0,0) 70%)'
    return (f'<span aria-hidden="true" style="position:absolute;inset:0;pointer-events:none;background:repeating-conic-gradient(from 90deg at {at}, rgba(242,242,242,{a}) 0deg 1deg, rgba(242,242,242,0) 1deg 7deg);'
            f'filter:blur(8px);-webkit-mask-image:{m};mask-image:{m}"></span>')

VIGNETTE = '<span aria-hidden="true" style="position:absolute;inset:0;pointer-events:none;background:radial-gradient(80% 70% at 50% 45%, rgba(40,40,44,0.55), rgba(11,11,12,0) 70%)"></span>'

def d_credits(rows, wide, lw=None):
    # centred axis: label right-aligned, value left-aligned (film credits)
    out = ''
    for lab, val in rows:
        if wide:
            out += (f'<div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);column-gap:40px;align-items:baseline">'
                    f'<p style="margin:0;text-align:right;{d_caps(12)}">{lab}</p><div style="font-size:19px;line-height:1.6;color:{DT};max-width:{lw or 44}ch">{val}</div></div>')
        else:
            out += f'<div style="text-align:center"><p style="margin:0 0 6px;{d_caps(11)}">{lab}</p><div style="font-size:16px;line-height:1.6;color:{DT}">{val}</div></div>'
    return out

def d_worked(px, gap):
    def items(hidden):
        lis = ''.join(f'<li class="wk" style="display:flex;align-items:center;gap:12px;font-size:{px}px;font-weight:500;letter-spacing:-0.03em;color:{DD};white-space:nowrap">'
                      + (slot(max(16, px // 2), DD) if m else '') + f'{n}</li>' for n, m in WORKED)
        return f'<ul{AH if hidden else ""} style="display:flex;align-items:center;gap:{gap}px;margin:0;padding:0 {gap//2}px;list-style:none">{lis}</ul>'
    return items

def d_project(n, wide):
    title, name, credit, tools, _ = POSTERS[n]
    notes = NOTES_ALL[n]
    orgtxt = f'<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap;justify-content:center">{orgline(n, D2, 12)}</span>'
    billing = f'{credit}   ·   {TOOLS_ALL[n] if n else "OutSystems ODC, Aurora PostgreSQL"}'
    beam_at = ['50% -10%', '0% 40%', '100% 110%'][n]
    rows = []
    for lab, val in notes:
        if val is None:
            val = f'<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">{slot(14, D2)}{TOOLS_ALL[n]}</span>'
        rows.append((lab, val))
    fig = FIG[n]
    if wide:
        poster = (f'<section class="scene" aria-labelledby="d-p{n}" style="position:relative;overflow:hidden;height:820px;display:flex;flex-direction:column;justify-content:space-between;align-items:center;padding:72px 80px 64px;box-sizing:border-box;text-align:center">'
                  + VIGNETTE + d_beam(beam_at, 0.09) +
                  f'<p style="position:relative;margin:0;{d_caps(13)}">{name}</p>'
                  f'<h3 id="d-p{n}" style="position:relative;margin:0;max-width:13ch;font-size:112px;line-height:0.95;font-weight:500;letter-spacing:-0.055em;color:{DT}">{title}</h3>'
                  f'<div style="position:relative;display:flex;flex-direction:column;gap:10px;align-items:center"><p style="margin:0;{d_caps(12, D2, "0.22em")}">{orgtxt}</p>'
                  f'<p style="margin:0;white-space:pre;{d_caps(12, DT, "0.22em")}">{billing}</p></div></section>')
        story = (f'<div style="display:flex;flex-direction:column;gap:28px;padding:40px 80px 160px">' + d_credits(rows, True)
                 + (f'<div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);column-gap:40px;align-items:baseline;margin-top:24px"><p style="margin:0;text-align:right;font-size:96px;line-height:1;font-weight:500;letter-spacing:-0.05em;color:{DT}">{fig[0]}</p>'
                    f'<p style="margin:0;{d_caps(12)}">{fig[1]}</p></div>' if fig else '') + '</div>')
        return poster + story
    poster = (f'<section class="scene" aria-labelledby="d-p{n}" style="position:relative;overflow:hidden;height:520px;display:flex;flex-direction:column;justify-content:space-between;align-items:center;padding:40px 20px 36px;box-sizing:border-box;text-align:center">'
              + VIGNETTE + d_beam(beam_at, 0.09) +
              f'<p style="position:relative;margin:0;{d_caps(11)}">{name}</p>'
              f'<h3 id="d-p{n}" style="position:relative;margin:0;font-size:40px;line-height:0.98;font-weight:500;letter-spacing:-0.05em;color:{DT}">{title}</h3>'
              f'<div style="position:relative;display:flex;flex-direction:column;gap:8px;align-items:center"><p style="margin:0;{d_caps(10, D2, "0.18em")}">{orgtxt}</p>'
              f'<p style="margin:0;{d_caps(10, DT, "0.18em")}">{credit}</p><p style="margin:0;{d_caps(10, D2, "0.18em")}">{TOOLS_ALL[n] if n else "OutSystems ODC, Aurora PostgreSQL"}</p></div></section>')
    story = (f'<div style="display:flex;flex-direction:column;gap:26px;padding:24px 20px 96px">' + d_credits(rows, False)
             + (f'<div style="text-align:center;margin-top:8px"><p style="margin:0;font-size:56px;line-height:1;font-weight:500;letter-spacing:-0.05em">{fig[0]}</p><p style="margin:8px 0 0;{d_caps(10)}">{fig[1]}</p></div>' if fig else '') + '</div>')
    return poster + story

def d_endcredits(wide):
    hist_rows = []
    for period, org, role, dur, mk in HIST:
        o = f'<span style="display:inline-flex;align-items:center;gap:8px">{slot(14, D2) if mk else ""}{org}</span>'
        val = f'<span style="display:block;font-size:{22 if wide else 18}px;font-weight:500;letter-spacing:-0.01em">{o}</span>' + (f'<span style="display:block;font-size:15px;color:{D2}">{role}{", " + dur if dur else ""}</span>' if role else '')
        hist_rows.append((period or ' ', val))
    minor_rows = []
    for name, (desc, parts) in MINOR.items():
        meta = ', '.join(p[0] for p in parts)
        minor_rows.append((meta, f'<span style="display:block;font-size:{22 if wide else 18}px;font-weight:500;letter-spacing:-0.01em">{name}</span><span style="display:block;font-size:15px;color:{D2}">{desc}</span>'))
    head = lambda t, i: f'<h2 id="{i}" style="margin:0 0 {40 if wide else 28}px;text-align:center;{d_caps(13 if wide else 12, DR)}">{t}</h2>'
    gap = 22 if wide else 22
    stills = ''.join(f'<figure style="margin:0"><div style="aspect-ratio:16 / 9;position:relative;overflow:hidden;background:#161618">{d_beam("50% -20%", 0.08)}</div>'
                     f'<figcaption style="margin-top:10px;text-align:center;{d_caps(10)}">Still: {p}</figcaption></figure>' for p in PIX)
    notes = ''.join(f'<p style="margin:0;text-align:center;font-family:{SERIF};font-style:italic;font-size:{22 if wide else 18}px;line-height:1.4;color:{D2}">“{POST_PH}”</p>' for _ in range(2))
    if wide:
        return (f'<section id="history" aria-labelledby="d-hist" style="padding:120px 80px 80px">{head("History", "d-hist")}<div style="display:flex;flex-direction:column;gap:{gap}px">{d_credits(hist_rows, True, 40)}</div></section>'
                f'<section aria-labelledby="d-minor" style="padding:80px 80px 80px">{head("Minor Projects (8)", "d-minor")}<div style="display:flex;flex-direction:column;gap:{gap}px">{d_credits(minor_rows, True, 40)}</div>'
                f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin-top:88px">{stills}</div>'
                f'<div style="display:flex;flex-direction:column;gap:18px;margin:72px auto 0;max-width:40ch">{notes}</div></section>')
    return (f'<section id="history" aria-labelledby="d-hist" style="padding:72px 20px 48px">{head("History", "d-hist")}<div style="display:flex;flex-direction:column;gap:{gap}px">{d_credits(hist_rows, False)}</div></section>'
            f'<section aria-labelledby="d-minor" style="padding:48px 20px 48px">{head("Minor Projects (8)", "d-minor")}<div style="display:flex;flex-direction:column;gap:{gap}px">{d_credits(minor_rows, False)}</div>'
            f'<div style="display:grid;gap:20px;margin-top:48px">{stills}</div><div style="display:flex;flex-direction:column;gap:14px;margin-top:40px">{notes}</div></section>')

def d_quals(wide):
    rows = []
    for name, d1, d2 in QUALS:
        issuer = 'OutSystems' if 'OutSystems' in name else ('Universiti Teknologi MARA' if 'MARA' in d1 else '[PLACEHOLDER: issuer]')
        year = d1.split(', ')[1] if 'MARA' in d1 else '[year]'
        rows.append((f'{issuer}, {year}', f'<span style="font-size:{19 if wide else 16}px">{name}</span>'))
    return rows

def d_desktop():
    header = (f'<header style="position:relative;z-index:1;display:flex;justify-content:space-between;align-items:center;height:72px;padding:0 48px">'
              f'<a href="#top" style="{d_caps(12, DT)};text-decoration:none;display:flex;align-items:center;min-height:44px">Wan Zayd Abdullah</a>'
              f'<nav aria-label="Sections"><ul style="list-style:none;margin:0;padding:0;display:flex;gap:36px">'
              + ''.join(f'<li><a class="nv" href="#{t}" style="display:flex;align-items:center;min-height:44px;{d_caps(12, D2)};text-decoration:none">{t}</a></li>' for t in ('work', 'history', 'contact'))
              + '</ul></nav></header>')
    title = (f'<section class="scene" aria-labelledby="d-hero" style="position:relative;overflow:hidden;height:828px;margin-top:-72px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 120px;box-sizing:border-box">'
             + VIGNETTE + d_beam('50% -15%', 0.10) +
             f'<p style="position:relative;margin:0 0 36px;{d_caps(14, DR, "0.32em")}">OutSystems Technical Lead</p>'
             f'<h1 id="d-hero" style="position:relative;margin:0;max-width:18ch;font-size:84px;line-height:1.0;font-weight:500;letter-spacing:-0.05em;color:{DT}">{TAGLINE}</h1>'
             f'<p style="position:relative;margin:40px 0 0;{d_caps(12)}">5 years · since Apr 2021</p>'
             f'<ul style="position:absolute;left:0;right:0;bottom:48px;list-style:none;margin:0;padding:0;display:flex;justify-content:center;gap:56px">'
             + ''.join(f'<li style="{d_caps(11, D2, "0.22em")}"><span style="color:{DT}">{n}</span> {t}</li>' for n, t in (('5', 'employers'), ('11', 'projects, 3 in detail'), ('5', 'qualifications')))
             + '</ul></section>')
    worked = (f'<section aria-labelledby="d-worked" style="padding:96px 0 120px"><div style="display:flex;justify-content:center;align-items:center;gap:24px;margin-bottom:28px">'
              f'<h2 id="d-worked" style="margin:0;{d_caps(12)}">Worked with</h2>{pause_btn("Worked with", f"border:0;{d_caps(11, D2)}")}</div>'
              + strip(d_worked(64, 96), 88, 'rtl') + '</section>')
    prologue = (f'<section aria-labelledby="d-about" style="padding:80px 80px 120px;text-align:center"><h2 id="d-about" style="margin:0 0 28px;{d_caps(12)}">About</h2>'
                f'<p style="margin:0 auto;max-width:34ch;font-size:30px;line-height:1.4;font-weight:400;letter-spacing:-0.01em;color:{D2}">{ABOUT_PH}</p></section>'
                f'<section aria-labelledby="d-qual" style="padding:40px 80px 160px"><h2 id="d-qual" style="margin:0 0 40px;text-align:center;{d_caps(12)}">Qualifications (5)</h2>'
                f'<div style="display:flex;flex-direction:column;gap:18px">{d_credits(d_quals(True), True, 40)}</div>'
                f'<p style="margin:28px 0 0;text-align:center;{d_caps(10, DD)}">[year]: [PLACEHOLDER: certification years]</p></section>')
    projhead = (f'<section id="work" aria-labelledby="d-proj" style="padding:40px 80px 40px;text-align:center"><h2 id="d-proj" style="margin:0;{d_caps(12, DR)}">Projects (3)</h2>'
                f'<p style="margin:16px auto 0;max-width:40ch;font-size:20px;line-height:1.5;color:{D2}">Three projects, each with what was wrong, what we chose and what it cost.</p></section>')
    projects = ''.join(d_project(n, True) for n in range(3))
    how = (f'<section aria-labelledby="d-how" style="padding:40px 80px 80px;text-align:center"><h2 id="d-how" style="margin:0 0 28px;{d_caps(12)}">How I work</h2>'
           f'<p style="margin:0 auto;max-width:34ch;font-size:30px;line-height:1.4;color:{D2}">{HOW_PH}</p></section>')
    final = (f'<footer id="contact" aria-labelledby="d-contact" style="flex-grow:1;position:relative;overflow:hidden;display:flex;flex-direction:column;align-items:center;text-align:center;padding:200px 80px 0">'
             + VIGNETTE + d_beam('50% 120%', 0.08) +
             f'<h2 id="d-contact" style="position:relative;margin:0 0 32px;{d_caps(12)}">Contact</h2>'
             f'<p style="position:relative;margin:0 0 56px;max-width:14ch;font-size:96px;line-height:0.98;font-weight:500;letter-spacing:-0.055em">Happy to talk about any of this.</p>'
             f'<div style="position:relative;display:flex;gap:64px;margin-bottom:160px">'
             f'<button type="button" style="display:flex;flex-direction:column;align-items:center;gap:8px;min-height:44px;padding:0;background:transparent;border:0;color:{DT};font-family:{SANS};cursor:pointer"><span style="{d_caps(11)}">Email</span><span style="font-size:22px;text-decoration:underline;text-decoration-color:{DR};text-underline-offset:6px">[PLACEHOLDER: email address]</span></button>'
             f'<a href="{LI_URL}" style="display:flex;flex-direction:column;align-items:center;gap:8px;min-height:44px;text-decoration:none"><span style="{d_caps(11)}">LinkedIn</span><span style="font-size:22px;text-decoration:underline;text-decoration-color:{DR};text-underline-offset:6px">{LINKEDIN}</span></a></div>'
             f'<div style="position:relative;align-self:stretch;margin:0 -80px">{marquee(220, "#1E1E21", 24, 500)}</div></footer>')
    body = header + '<main style="display:flex;flex-direction:column">' + title + worked + prologue + projhead + projects + how + d_endcredits(True) + '</main>' + final
    return page('Portfolio D, desktop', 1440, 12000, D_HELMET, f'background:{DB};color:{DT};font-family:{SANS}', body)

def d_phone():
    header = (f'<header style="position:relative;z-index:1;padding:10px 20px 0;text-align:center">'
              f'<a href="#top" style="{d_caps(11, DT)};text-decoration:none;display:inline-flex;align-items:center;min-height:44px">Wan Zayd Abdullah</a>'
              f'<nav aria-label="Sections"><ul style="list-style:none;margin:0;padding:0;display:flex;justify-content:center;gap:12px">'
              + ''.join(f'<li><a class="nv" href="#{t}" style="display:flex;align-items:center;justify-content:center;min-height:44px;min-width:44px;{d_caps(10, D2, "0.2em")};text-decoration:none">{t}</a></li>' for t in ('work', 'history', 'contact'))
              + '</ul></nav></header>')
    title = (f'<section class="scene" aria-labelledby="d-hero" style="position:relative;overflow:hidden;height:470px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 20px;box-sizing:border-box">'
             + VIGNETTE + d_beam('50% -15%', 0.10) +
             f'<p style="position:relative;margin:0 0 22px;{d_caps(11, DR, "0.26em")}">OutSystems Technical Lead</p>'
             f'<h1 id="d-hero" style="position:relative;margin:0;font-size:33px;line-height:1.02;font-weight:500;letter-spacing:-0.045em;color:{DT}">{TAGLINE}</h1>'
             f'<p style="position:relative;margin:24px 0 0;{d_caps(10)}">5 years · since Apr 2021</p></section>'
             f'<ul style="list-style:none;margin:0 20px 64px;padding:0;display:flex;flex-direction:column;align-items:center;gap:6px">'
             + ''.join(f'<li style="{d_caps(10, D2, "0.2em")}"><span style="color:{DT}">{n}</span> {t}</li>' for n, t in (('5', 'employers'), ('11', 'projects, 3 in detail'), ('5', 'qualifications')))
             + '</ul>')
    worked = (f'<section aria-labelledby="d-worked" style="padding:0 0 88px"><div style="display:flex;justify-content:center;align-items:center;gap:8px;margin-bottom:12px">'
              f'<h2 id="d-worked" style="margin:0;{d_caps(11)}">Worked with</h2>{pause_btn("Worked with", f"border:0;{d_caps(10, D2)}")}</div>'
              + strip(d_worked(34, 56), 88, 'rtl') + '</section>')
    prologue = (f'<section aria-labelledby="d-about" style="padding:0 20px 88px;text-align:center"><h2 id="d-about" style="margin:0 0 18px;{d_caps(11)}">About</h2>'
                f'<p style="margin:0;font-size:20px;line-height:1.45;color:{D2}">{ABOUT_PH}</p></section>'
                f'<section aria-labelledby="d-qual" style="padding:0 20px 96px"><h2 id="d-qual" style="margin:0 0 28px;text-align:center;{d_caps(11)}">Qualifications (5)</h2>'
                f'<div style="display:flex;flex-direction:column;gap:20px">{d_credits(d_quals(False), False)}</div>'
                f'<p style="margin:20px 0 0;text-align:center;{d_caps(9, DD)}">[year]: [PLACEHOLDER: certification years]</p></section>')
    projhead = (f'<section id="work" aria-labelledby="d-proj" style="padding:0 20px 16px;text-align:center"><h2 id="d-proj" style="margin:0;{d_caps(11, DR)}">Projects (3)</h2>'
                f'<p style="margin:12px 0 0;font-size:16px;line-height:1.5;color:{D2}">Three projects, each with what was wrong, what we chose and what it cost.</p></section>')
    projects = ''.join(d_project(n, False) for n in range(3))
    how = (f'<section aria-labelledby="d-how" style="padding:0 20px 24px;text-align:center"><h2 id="d-how" style="margin:0 0 18px;{d_caps(11)}">How I work</h2>'
           f'<p style="margin:0;font-size:20px;line-height:1.45;color:{D2}">{HOW_PH}</p></section>')
    def reel(hidden):
        lis = ''.join(f'<li style="display:flex;flex-direction:column;justify-content:center;align-items:center;gap:4px;height:96px;padding:0 28px;white-space:nowrap;text-align:center">'
                      f'<span style="{d_caps(9)}">{p}</span><span style="display:flex;align-items:center;gap:6px;font-size:17px;font-weight:500">{slot(14, D2) if mk else ""}{n}</span>'
                      f'<span style="font-size:12px;color:{D2}">{r}{(" " + c) if c else ""}</span></li>' for p, n, mk, r, c in TL)
        return f'<ol{AH if hidden else ""} style="display:flex;margin:0;padding:0;list-style:none">{lis}</ol>'
    reel_s = (f'<section aria-label="History, moving" style="padding:72px 0 0"><div style="display:flex;justify-content:center;margin-bottom:8px">{pause_btn("History", f"border:0;{d_caps(10, D2)}")}</div>'
              + strip(reel, 96, 'ltr') + '</section>')
    final = (f'<footer id="contact" aria-labelledby="d-contact" style="flex-grow:1;position:relative;overflow:hidden;display:flex;flex-direction:column;align-items:center;text-align:center;padding:120px 20px 0">'
             + VIGNETTE + d_beam('50% 120%', 0.08) +
             f'<h2 id="d-contact" style="position:relative;margin:0 0 20px;{d_caps(11)}">Contact</h2>'
             f'<p style="position:relative;margin:0 0 36px;font-size:44px;line-height:0.98;font-weight:500;letter-spacing:-0.05em">Happy to talk about any of this.</p>'
             f'<div style="position:relative;display:flex;flex-direction:column;gap:22px;margin-bottom:80px">'
             f'<button type="button" style="display:flex;flex-direction:column;align-items:center;gap:6px;min-height:44px;padding:0;background:transparent;border:0;color:{DT};font-family:{SANS};cursor:pointer"><span style="{d_caps(10)}">Email</span><span style="font-size:17px;text-decoration:underline;text-decoration-color:{DR};text-underline-offset:6px">[PLACEHOLDER: email address]</span></button>'
             f'<a href="{LI_URL}" style="display:flex;flex-direction:column;align-items:center;gap:6px;min-height:44px;text-decoration:none"><span style="{d_caps(10)}">LinkedIn</span><span style="font-size:15px;overflow-wrap:anywhere;text-decoration:underline;text-decoration-color:{DR};text-underline-offset:6px">{LINKEDIN}</span></a></div>'
             f'<div style="position:relative;align-self:stretch;margin:0 -20px">{marquee(96, "#1E1E21", 12, 500)}</div></footer>')
    body = header + '<main style="display:flex;flex-direction:column">' + title + worked + prologue + projhead + projects + how + reel_s + d_endcredits(False) + '</main>' + final
    return page('Portfolio D, phone', 320, 11400, D_HELMET, f'background:{DB};color:{DT};font-family:{SANS}', body)

# =====================================================================
# E · THE BOOK  (Practical Typography, Stripe Press, Craig Mod, Lynn Fisher)
# =====================================================================
EP, EI, EO, EC = '#E3D3D0', '#262032', '#4A2E2E', '#8E5A4F'
DIDONE = "Didot,'Bodoni MT','Noto Serif Display','URW Palladio L',P052,Sylfaen,serif"
BOOK = "ui-serif,'Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif"
E_HELMET = '''<helmet>
<style>
body{margin:0;background:#E3D3D0;color:#262032;font-family:ui-serif,"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif}
a{color:#262032;text-decoration-color:#8E5A4F;text-decoration-thickness:1px;text-underline-offset:4px}a:hover{color:#4A2E2E;text-decoration-thickness:2px}
::selection{background:#262032;color:#E3D3D0}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid #262032;outline-offset:3px}
.toc a{text-decoration:none}.toc a:hover .t{text-decoration:underline;text-decoration-color:#8E5A4F}
.wk:hover{color:#262032}.pb:hover{color:#262032}
.onum{font-variant-numeric:oldstyle-nums proportional-nums}
.post{transform:rotate(-1.5deg)}.post.b{transform:rotate(1.2deg)}
''' + ANIM + '''
</style>
</helmet>'''

def e_sc(px=12, color=EO, ls='0.12em'):
    return f'font-family:{BOOK};font-size:{px}px;line-height:1.5;letter-spacing:{ls};text-transform:uppercase;font-weight:400;color:{color}'

def leader(left, right, px, href=None, lc=EI, rc=EO, extra=''):
    dots = f'<span aria-hidden="true" style="flex:1 1 auto;min-width:24px;margin:0 8px;border-bottom:1.5px dotted {EO};transform:translateY(-5px)"></span>'
    inner = (f'<span class="t" style="color:{lc}">{left}</span>{dots}<span class="onum" style="color:{rc};white-space:nowrap">{right}</span>')
    if href:
        return f'<a href="{href}" style="display:flex;align-items:baseline;min-height:44px;box-sizing:border-box;padding-top:10px;font-size:{px}px;line-height:1.3;{extra}">{inner}</a>'
    return f'<div style="display:flex;align-items:baseline;font-size:{px}px;line-height:1.35;{extra}">{inner}</div>'

TOC = [('About', '#e-about', ''), ('Qualifications', '#e-qual', '5'), ('iZone rebuild', '#e-p0', 'AvePoint'), ('Digital Form', '#e-p1', 'Maybank'),
       ('MyInsights', '#e-p2', 'FPT Software'), ('How I work', '#e-how', ''), ('History', '#history', '2021 – 2026'), ('Minor Projects', '#e-minor', '8'), ('Contact', '#contact', '')]

def e_toc(px):
    return (f'<nav aria-label="Contents" class="toc"><p style="margin:0 0 4px;{e_sc(12)}">Contents</p><ol style="list-style:none;margin:0;padding:0">'
            + ''.join(f'<li>{leader(t, r, px, h)}</li>' for t, h, r in TOC) + '</ol></nav>')

def e_worked(px, gap):
    def items(hidden):
        lis = ''.join(f'<li class="wk" style="display:flex;align-items:center;gap:10px;font-family:{BOOK};font-style:italic;font-size:{px}px;color:{EO};white-space:nowrap">'
                      + (slot(px - 8, EO) if m else '') + f'{n}</li>' for n, m in WORKED)
        return f'<ul{AH if hidden else ""} style="display:flex;align-items:center;gap:{gap}px;margin:0;padding:0 {gap//2}px;list-style:none">{lis}</ul>'
    return items

def e_chapter(n, wide):
    title, name, credit, tools, _ = POSTERS[n]
    notes = dict(NOTES_ALL[n])
    fig = FIG[n]
    paras = ''
    for lab in ('The problem', 'The choice', 'What it cost', 'What happened', 'My part'):
        paras += (f'<p style="margin:0 0 {18 if wide else 16}px;font-size:{20 if wide else 17}px;line-height:1.6;text-indent:0">'
                  f'<span style="{e_sc(14 if wide else 12)};margin-right:8px">{lab}</span>{notes[lab]}</p>')
    tools_note = (f'<p style="margin:0 0 6px;{e_sc(11)}">Tools</p><p style="margin:0;display:flex;align-items:center;gap:6px;flex-wrap:wrap;font-style:italic;font-size:15px;line-height:1.5">{slot(12, EO)}{TOOLS_ALL[n]}</p>')
    fig_note = (f'<p style="margin:0;font-family:{DIDONE};font-size:{48 if wide else 40}px;line-height:1;color:{EC}">{fig[0]}</p><p style="margin:6px 0 0;font-style:italic;font-size:14px;line-height:1.4;color:{EO}">{fig[1]}</p>' if fig else '')
    head = (f'<p style="margin:0 0 12px;{e_sc(13 if wide else 12, EC)}">{name}</p>'
            f'<h3 id="e-p{n}" style="margin:0 0 14px;font-family:{DIDONE};font-weight:400;font-size:{50 if wide else 34}px;line-height:1.05;letter-spacing:-0.01em">{title}</h3>'
            f'<p style="margin:0 0 {32 if wide else 24}px;display:flex;align-items:center;gap:6px;flex-wrap:wrap;font-style:italic;font-size:{19 if wide else 16}px;color:{EO}">{orgline(n, EO, 13)}. {credit}.</p>')
    if wide:
        return (f'<article aria-labelledby="e-p{n}" style="display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;padding:0 80px 120px">'
                f'<div style="grid-column:5 / span 6">{head}{paras}</div>'
                f'<aside style="grid-column:11 / span 2;padding-top:{148}px;display:flex;flex-direction:column;gap:28px;border-top:0">{fig_note}<div>{tools_note}</div></aside></article>')
    return (f'<article aria-labelledby="e-p{n}" style="padding:0 20px 72px">{head}{paras}'
            f'<aside style="margin-top:8px;padding:16px 0 0 16px;border-left:1px solid {EC};display:flex;flex-direction:column;gap:18px">{fig_note}<div>{tools_note}</div></aside></article>')

def e_ledger(wide):
    out = ''
    for period, org, role, dur, mk in HIST:
        sub = org.startswith('↳')
        o = f'<span style="display:inline-flex;align-items:center;gap:8px">{slot(13, EO) if mk else ""}{org}</span>'
        right = period or ''
        out += (f'<li style="padding:{10 if wide else 8}px 0 {6}px {24 if sub else 0}px">'
                + leader(o, right, 20 if wide and not sub else (18 if wide else 16), lc=(EO if sub else EI))
                + (f'<p style="margin:2px 0 0;font-style:italic;font-size:{16 if wide else 14}px;color:{EO}">{role}{", " + dur if dur else ""}</p>' if role else '') + '</li>')
    return f'<ol style="list-style:none;margin:0;padding:0">{out}</ol>'

def e_index(wide):
    out = ''
    for name, (desc, parts) in MINOR.items():
        emp = parts[0][0]
        right = f'<span style="display:inline-flex;align-items:center;gap:6px">{slot(12, EO) if parts[0][1] else ""}{emp}</span>'
        d = desc.replace('from 6 hours to 30 minutes', f'from <span style="font-family:{DIDONE};font-size:1.25em;color:{EC}">6 hours</span> to <span style="font-family:{DIDONE};font-size:1.25em;color:{EC}">30 minutes</span>')
        out += (f'<li style="break-inside:avoid;padding:0 0 {22 if wide else 18}px">' + leader(f'<span style="font-weight:600">{name}</span>', right, 19 if wide else 17)
                + f'<p style="margin:4px 0 0;font-size:{16 if wide else 15}px;line-height:1.55">{d} <span style="font-style:italic;color:{EO}">{parts[1][0]}.</span></p></li>')
    return f'<ol style="list-style:none;margin:0;padding:0;{"columns:2;column-gap:48px" if wide else ""}">{out}</ol>'

def e_plates(wide):
    plates = ''.join(f'<figure style="margin:0"><div style="aspect-ratio:{"3 / 4" if wide else "4 / 3"};border:1px solid {EO};background:radial-gradient(90% 70% at 50% 0%, rgba(252,252,252,0.45), rgba(227,211,208,0) 70%), linear-gradient(180deg, #D8C3BF 0%, #CDB4AF 100%)"></div>'
                     f'<figcaption style="margin-top:10px;font-style:italic;font-size:14px;line-height:1.4;color:{EO}"><span style="{e_sc(11)}">Plate</span> {p} (picture to add)</figcaption></figure>' for p in PIX)
    return f'<div style="display:grid;grid-template-columns:{"repeat(3,minmax(0,1fr))" if wide else "1fr"};gap:{24 if wide else 20}px">{plates}</div>'

def e_marginalia(wide):
    return ''.join(f'<p class="post{" b" if i else ""}" style="margin:0;padding:14px 16px;background:#F1E7E5;box-shadow:0 1px 1px rgba(38,32,50,0.10),0 10px 22px rgba(38,32,50,0.10);font-style:italic;font-size:{16 if wide else 15}px;line-height:1.45">'
                   f'<span style="display:block;margin-bottom:6px;{e_sc(10)}">Note</span>{POST_PH}</p>' for i in range(2))

def e_quals(px):
    out = ''
    for name, d1, d2 in QUALS:
        right = d1.split(', ')[1] if 'MARA' in d1 else '[year]'
        issuer = 'OutSystems' if 'OutSystems' in name else ('Universiti Teknologi MARA' if 'MARA' in d1 else '[PLACEHOLDER: issuer]')
        out += f'<li style="padding:8px 0">{leader(name, right, px)}<p style="margin:2px 0 0;font-style:italic;font-size:{px - 3}px;color:{EO}">{issuer}</p></li>'
    return f'<ol style="list-style:none;margin:0;padding:0">{out}</ol><p style="margin:10px 0 0;font-style:italic;font-size:14px;color:{EO}">[year]: [PLACEHOLDER: certification years]</p>'

def e_desktop():
    G = 'display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;padding:0 80px'
    pinned = (f'<header style="grid-column:1 / span 3;padding-top:88px;display:flex;flex-direction:column;gap:14px">'
              f'<a href="#top" style="font-family:{DIDONE};font-size:44px;line-height:1.02;letter-spacing:-0.01em;text-decoration:none">Wan Zayd Abdullah</a>'
              f'<p style="margin:0;font-style:italic;font-size:21px;line-height:1.3;color:{EO}">OutSystems Technical Lead</p>'
              f'<p class="onum" style="margin:0 0 36px;{e_sc(12)}">5 years · since Apr 2021</p>' + e_toc(17) + '</header>')
    opening = (f'<section aria-labelledby="e-hero" style="grid-column:5 / span 7;padding-top:88px">'
               f'<h1 id="e-hero" style="margin:0 0 40px;font-family:{DIDONE};font-weight:400;font-size:64px;line-height:1.04;letter-spacing:-0.015em">{TAGLINE}</h1>'
               f'<p style="margin:0 0 56px;max-width:36ch;font-size:23px;line-height:1.55;color:{EO}">Five employers, eleven projects (three told here in detail) and five qualifications.</p>'
               f'<section aria-labelledby="e-about-h" id="e-about"><h2 id="e-about-h" style="margin:0 0 14px;{e_sc(13)}">About</h2>'
               f'<p style="margin:0;max-width:40ch;font-style:italic;font-size:22px;line-height:1.55;color:{EO}">{ABOUT_PH}</p></section></section>')
    top = f'<div style="{G}">{pinned}{opening}</div>'
    worked = (f'<section aria-labelledby="e-worked" style="margin:120px 80px 120px;border-top:1px solid {EO};border-bottom:1px solid {EO}">'
              f'<div style="display:flex;justify-content:space-between;align-items:center;padding-top:6px"><h2 id="e-worked" style="margin:0;{e_sc(12)}">Worked with</h2>'
              f'{pause_btn("Worked with", f"border:0;{e_sc(11)}")}</div>' + strip(e_worked(34, 72), 88, 'rtl') + '</section>')
    qual = (f'<section id="e-qual" aria-labelledby="e-qual-h" style="{G};padding-bottom:140px"><h2 id="e-qual-h" style="grid-column:1 / span 3;margin:0;{e_sc(13)}">Qualifications</h2>'
            f'<div style="grid-column:5 / span 6">{e_quals(20)}</div></section>')
    part = (f'<section id="work" aria-labelledby="e-proj" style="{G};padding-bottom:88px"><div style="grid-column:5 / span 6;border-top:1px solid {EO};padding-top:28px">'
            f'<h2 id="e-proj" style="margin:0 0 12px;{e_sc(13, EC)}">Projects</h2>'
            f'<p style="margin:0;font-family:{DIDONE};font-size:40px;line-height:1.15">Three projects, each with what was wrong, what we chose and what it cost.</p></div></section>')
    chapters = ''.join(e_chapter(n, True) for n in range(3))
    how = (f'<section id="e-how" aria-labelledby="e-how-h" style="{G};padding-bottom:140px"><div style="grid-column:5 / span 6"><h2 id="e-how-h" style="margin:0 0 14px;{e_sc(13)}">How I work</h2>'
           f'<p style="margin:0;font-style:italic;font-size:22px;line-height:1.55;color:{EO}">{HOW_PH}</p></div></section>')
    hist = (f'<section id="history" aria-labelledby="e-hist" style="{G};padding-bottom:140px"><h2 id="e-hist" style="grid-column:1 / span 3;margin:0;{e_sc(13)}">History</h2>'
            f'<div style="grid-column:5 / span 6">{e_ledger(True)}</div></section>')
    minor = (f'<section id="e-minor" aria-labelledby="e-minor-h" style="{G};padding-bottom:120px"><h2 id="e-minor-h" style="grid-column:1 / span 3;margin:0;{e_sc(13)}">Minor Projects <span class="onum">(8)</span></h2>'
             f'<div style="grid-column:5 / span 8">{e_index(True)}</div>'
             f'<div style="grid-column:1 / span 3;margin-top:56px;display:flex;flex-direction:column;gap:22px">{e_marginalia(True)}</div>'
             f'<div style="grid-column:5 / span 8;margin-top:56px">{e_plates(True)}</div></section>')
    contact = (f'<footer id="contact" aria-labelledby="e-contact" style="flex-grow:1;{G};align-content:start;padding-top:40px;padding-bottom:120px">'
               f'<div style="grid-column:5 / span 6;border-top:1px solid {EO};padding-top:28px"><h2 id="e-contact" style="margin:0 0 12px;{e_sc(13)}">Contact</h2>'
               f'<p style="margin:0 0 32px;font-family:{DIDONE};font-size:52px;line-height:1.05">Happy to talk about any of this.</p>'
               + leader('Email', '<button type="button" style="min-height:44px;padding:0;border:0;background:transparent;font:inherit;font-style:italic;color:#262032;cursor:pointer;text-decoration:underline;text-decoration-color:#8E5A4F;text-underline-offset:4px">[PLACEHOLDER: email address]</button>', 20, rc=EI)
               + leader('LinkedIn', f'<a href="{LI_URL}" style="display:inline-flex;align-items:center;min-height:44px;font-style:italic">{LINKEDIN}</a>', 20, rc=EI) + '</div></footer>')
    body = '<main style="display:flex;flex-direction:column">' + top + worked + qual + part + chapters + how + hist + minor + '</main>' + contact
    return page('Portfolio E, desktop', 1440, 7400, E_HELMET, f'background:{EP};color:{EI};font-family:{BOOK}', body)

def e_phone():
    P = 20
    title = (f'<header style="padding:48px {P}px 0;text-align:center">'
             f'<a href="#top" style="display:inline-block;font-family:{DIDONE};font-size:38px;line-height:1.02;text-decoration:none">Wan Zayd Abdullah</a>'
             f'<p style="margin:12px 0 6px;font-style:italic;font-size:19px;color:{EO}">OutSystems Technical Lead</p>'
             f'<p class="onum" style="margin:0;{e_sc(11)}">5 years · since Apr 2021</p></header>')
    opening = (f'<section aria-labelledby="e-hero" style="padding:48px {P}px 40px"><h1 id="e-hero" style="margin:0 0 24px;font-family:{DIDONE};font-weight:400;font-size:34px;line-height:1.08;text-align:center">{TAGLINE}</h1>'
               f'<p style="margin:0;font-size:18px;line-height:1.55;color:{EO};text-align:center">Five employers, eleven projects (three told here in detail) and five qualifications.</p></section>')
    toc = (f'<details open="{{{{ true }}}}" style="margin:0 {P}px 64px;border-top:1px solid {EO};border-bottom:1px solid {EO}"><summary class="qs" style="display:flex;justify-content:space-between;align-items:center;min-height:44px;cursor:pointer;{e_sc(12)}">'
           f'<span>Contents</span><span aria-hidden="true" style="font-size:18px">−</span></summary><div style="padding-bottom:12px">'
           + f'<ol style="list-style:none;margin:0;padding:0">' + ''.join(f'<li>{leader(t, r, 16, h)}</li>' for t, h, r in TOC) + '</ol></div></details>')
    worked = (f'<section aria-labelledby="e-worked" style="margin:0 0 72px;border-top:1px solid {EO};border-bottom:1px solid {EO}">'
              f'<div style="display:flex;justify-content:space-between;align-items:center;padding:4px {P}px 0"><h2 id="e-worked" style="margin:0;{e_sc(11)}">Worked with</h2>'
              f'{pause_btn("Worked with", f"border:0;{e_sc(10)}")}</div>' + strip(e_worked(24, 44), 88, 'rtl') + '</section>')
    about = (f'<section id="e-about" aria-labelledby="e-about-h" style="padding:0 {P}px 72px"><h2 id="e-about-h" style="margin:0 0 12px;{e_sc(12)}">About</h2>'
             f'<p style="margin:0;font-style:italic;font-size:19px;line-height:1.55;color:{EO}">{ABOUT_PH}</p></section>')
    qual = f'<section id="e-qual" aria-labelledby="e-qual-h" style="padding:0 {P}px 80px"><h2 id="e-qual-h" style="margin:0 0 8px;{e_sc(12)}">Qualifications</h2>{e_quals(17)}</section>'
    part = (f'<section id="work" aria-labelledby="e-proj" style="padding:0 {P}px 56px"><div style="border-top:1px solid {EO};padding-top:20px"><h2 id="e-proj" style="margin:0 0 10px;{e_sc(12, EC)}">Projects</h2>'
            f'<p style="margin:0;font-family:{DIDONE};font-size:27px;line-height:1.15">Three projects, each with what was wrong, what we chose and what it cost.</p></div></section>')
    chapters = ''.join(e_chapter(n, False) for n in range(3))
    how = (f'<section id="e-how" aria-labelledby="e-how-h" style="padding:0 {P}px 80px"><h2 id="e-how-h" style="margin:0 0 12px;{e_sc(12)}">How I work</h2>'
           f'<p style="margin:0;font-style:italic;font-size:19px;line-height:1.55;color:{EO}">{HOW_PH}</p></section>')
    def band(hidden):
        lis = ''.join(f'<li style="display:flex;flex-direction:column;justify-content:center;gap:3px;height:96px;padding:0 26px;white-space:nowrap">'
                      f'<span class="onum" style="{e_sc(10)}">{p}</span><span style="display:flex;align-items:center;gap:6px;font-size:18px">{slot(13, EO) if mk else ""}{n}</span>'
                      f'<span style="font-style:italic;font-size:13px;color:{EO}">{r}{(" " + c) if c else ""}</span></li>' for p, n, mk, r, c in TL)
        return f'<ol{AH if hidden else ""} style="display:flex;margin:0;padding:0;list-style:none">{lis}</ol>'
    hist = (f'<section id="history" aria-labelledby="e-hist" style="margin:0 0 80px;border-top:1px solid {EO};border-bottom:1px solid {EO}">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;padding:4px {P}px 0"><h2 id="e-hist" style="margin:0;{e_sc(11)}">History</h2>'
            f'{pause_btn("History", f"border:0;{e_sc(10)}")}</div>' + strip(band, 96, 'ltr') + '</section>')
    minor = (f'<section id="e-minor" aria-labelledby="e-minor-h" style="padding:0 {P}px 56px"><h2 id="e-minor-h" style="margin:0 0 14px;{e_sc(12)}">Minor Projects <span class="onum">(8)</span></h2>{e_index(False)}'
             f'<div style="margin-top:32px">{e_plates(False)}</div><div style="margin-top:32px;display:flex;flex-direction:column;gap:18px">{e_marginalia(False)}</div></section>')
    contact = (f'<footer id="contact" aria-labelledby="e-contact" style="flex-grow:1;padding:0 {P}px 72px"><div style="border-top:1px solid {EO};padding-top:20px">'
               f'<h2 id="e-contact" style="margin:0 0 10px;{e_sc(12)}">Contact</h2>'
               f'<p style="margin:0 0 24px;font-family:{DIDONE};font-size:32px;line-height:1.08">Happy to talk about any of this.</p>'
               f'<p style="margin:0 0 4px;{e_sc(11)}">Email</p><button type="button" style="min-height:44px;padding:0;border:0;background:transparent;font:inherit;font-style:italic;font-size:17px;color:#262032;text-align:left;cursor:pointer;text-decoration:underline;text-decoration-color:#8E5A4F;text-underline-offset:4px">[PLACEHOLDER: email address]</button>'
               f'<p style="margin:14px 0 4px;{e_sc(11)}">LinkedIn</p><a href="{LI_URL}" style="display:inline-flex;align-items:center;min-height:44px;font-style:italic;font-size:15px;overflow-wrap:anywhere">{LINKEDIN}</a></div></footer>')
    body = title + '<main style="display:flex;flex-direction:column">' + opening + toc + worked + about + qual + part + chapters + how + hist + minor + '</main>' + contact
    return page('Portfolio E, phone', 320, 9500, E_HELMET, f'background:{EP};color:{EI};font-family:{BOOK}', body)

BOARDS = {
 'C-Phone.dc.html': (c_phone, 320, 'C · Engineering manual · Phone 320'),
 'C-Desktop.dc.html': (c_desktop, 1440, 'C · Engineering manual · Desktop 1440'),
 'D-Phone.dc.html': (d_phone, 320, 'D · Title sequence · Phone 320'),
 'D-Desktop.dc.html': (d_desktop, 1440, 'D · Title sequence · Desktop 1440'),
 'E-Phone.dc.html': (e_phone, 320, 'E · The book · Phone 320'),
 'E-Desktop.dc.html': (e_desktop, 1440, 'E · The book · Desktop 1440'),
}
if __name__ == '__main__':
    import re, sys
    out = sys.argv[1] if len(sys.argv) > 1 else 'canvas/'
    heights = {}
    for f, (fn, w, t) in BOARDS.items():
        html = fn()
        heights[f] = int(re.search(r'height:(\d+)px;box-sizing', html).group(1))
        open(out + f, 'w').write(html)
    c = json.load(open(out + 'canvas.json'))
    c['pages'] = [{'id': 'round1', 'name': 'A and B'}, {'id': 'radical', 'name': 'Radical: C, D, E'}]
    for k in ('t1', 't2'):
        c['notes'][k]['page'] = 'round1'
    for k in ('Main.dc.html', 'Desktop.dc.html', 'B-Phone.dc.html', 'B-Desktop.dc.html'):
        c['boards'][k]['page'] = 'round1'
    x = 0
    for d, label in (('C', 'C · Engineering manual (grey, black, one orange)'), ('D', 'D · Title sequence (black, one red)'), ('E', 'E · The book (rose-stone paper, serif)')):
        for f, dx in ((f'{d}-Phone.dc.html', 0), (f'{d}-Desktop.dc.html', 400)):
            c['boards'][f] = {'x': x + dx, 'y': 0, 'w': BOARDS[f][1], 'h': heights[f], 'title': BOARDS[f][2], 'page': 'radical'}
            if f not in c['order']:
                c['order'].append(f)
        c['notes'][f't{d}'] = {'x': x, 'y': -300, 'text': label, 'kind': 'title1', 'maxW': 1840, 'page': 'radical'}
        x += 1840 + 320
    json.dump(c, open(out + 'canvas.json', 'w'), indent=1)
    print('ok', heights)
