import json, datetime, re

VOID, DUSK, NIGHT, SLATE = '#0D0B12', '#14111C', '#262032', '#373F47'
FROST, ICE, IGREY = '#EAF2F8', '#C9D3DE', '#82909D'
ROCK, FCLAY, CCLAY = '#B88478', '#E3D3D0', '#8E5A4F'
SANS = "-apple-system,'Segoe UI',system-ui,sans-serif"
SERIF = "ui-serif,'Iowan Old Style','Palatino Linotype',Georgia,serif"
MONO = "ui-monospace,Menlo,Consolas,monospace"

def LABEL(px=12, color=IGREY):
    return f'font-size:{px}px;line-height:1.4;letter-spacing:0.08em;text-transform:uppercase;font-weight:500;color:{color}'

def slot(px):  # logo slot: a real vector mark replaces it
    return (f'<span aria-hidden="true" style="display:inline-block;flex-shrink:0;width:{px}px;height:{px}px;'
            f'box-sizing:border-box;border:1px dashed {IGREY}"></span>')

def haze(at, size='70% 60%', a=0.42):
    return (f'<span aria-hidden="true" style="position:absolute;inset:0;pointer-events:none;'
            f'background:radial-gradient({size} at {at}, rgba(184,132,120,{a}), rgba(142,90,79,0.14) 45%, rgba(13,11,18,0) 72%)"></span>')

def rays(at, reach='85% 75%', a=0.13, blur=7):
    m = f'radial-gradient({reach} at {at}, #000 8%, rgba(0,0,0,0) 72%)'
    return (f'<span aria-hidden="true" style="position:absolute;inset:0;pointer-events:none;'
            f'background:repeating-conic-gradient(from 90deg at {at}, rgba(234,242,248,{a}) 0deg 1.2deg, rgba(234,242,248,0) 1.2deg 6.5deg);'
            f'filter:blur({blur}px);-webkit-mask-image:{m};mask-image:{m}"></span>')

HELMET = '''<helmet>
<style>
body{margin:0;background:#0D0B12;color:#EAF2F8;font-family:-apple-system,"Segoe UI",system-ui,sans-serif}
a{color:#B88478;text-underline-offset:3px}a:hover{color:#E3D3D0}
::selection{background:#E3D3D0;color:#262032}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid #E3D3D0;outline-offset:3px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.nv:hover{color:#E3D3D0}
.wk{transition:color .3s ease}.wk:hover{color:#EAF2F8}
.pz{transition:transform .35s cubic-bezier(.2,.7,.2,1),border-color .35s ease}.pz:hover{transform:translateY(-6px);border-color:#82909D}
.pz.on{transform:translateY(-10px)}
.tile{transition:transform .3s ease,background-color .3s ease}.tile:hover{transform:translateY(-4px);background-color:#1B1726}
.post{transform:rotate(-2deg);transition:transform .3s ease}.post.b{transform:rotate(1.6deg)}.post:hover{transform:rotate(0)}
.seg{transition:background-color .3s ease}.seg:hover{background-color:rgba(227,211,208,0.06)}
.qs{list-style:none}.qs::-webkit-details-marker{display:none}.qs:hover{color:#E3D3D0}
.btn{transition:border-color .2s ease,color .2s ease}.btn:hover{border-color:#E3D3D0;color:#E3D3D0}
@keyframes wz-rtl{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@keyframes wz-ltr{from{transform:translateX(-50%)}to{transform:translateX(0)}}
.drift-rtl{animation:wz-rtl 60s linear infinite}
.drift-ltr{animation:wz-ltr 75s linear infinite}
.marq{animation:wz-rtl 28s linear infinite}
.strip:hover .drift-rtl,.strip:hover .drift-ltr,.strip:focus-within .drift-rtl,.strip:focus-within .drift-ltr,.marq-wrap:hover .marq{animation-play-state:paused}
@media (prefers-reduced-motion:reduce){.drift-rtl,.drift-ltr,.marq{animation:none}.strip{overflow-x:auto}.pz,.tile,.post,.seg,.wk,.btn{transition:none}}
</style>
</helmet>'''

def page(title, w, h, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
{HELMET}
<div id="top" style="width:{w}px;height:{h}px;box-sizing:border-box;overflow:hidden;display:flex;flex-direction:column;background:{VOID};color:{FROST};font-family:{SANS};-webkit-font-smoothing:antialiased">
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

# ---------------- content (round 10, real data only) ----------------
TAGLINE = 'I design and build enterprise systems: on my own, in a team, and leading one.'
WORKED = [('AvePoint', True), ('Sunway University', False), ('Maybank', True), ('Adam Digital Assets', False),
          ('FPT Software', True), ('PETRONAS', True), ('Impact Business Solutions', False)]
QUALS = [('OutSystems Associate Developer Specialist (O11)', 'Issuer: OutSystems. Year: ', '[PLACEHOLDER: year]'),
         ('OutSystems Associate Technical Lead (O11)', 'Issuer: OutSystems. Year: ', '[PLACEHOLDER: year]'),
         ('Professional Scrum Developer', 'Issuer: ', '[PLACEHOLDER: issuer]. Year: [PLACEHOLDER: year]'),
         ('Bachelor of Information System, Intelligent Systems Engineering', 'Universiti Teknologi MARA, 2019 – 2021', ''),
         ('Diploma in Computer Science', 'Universiti Teknologi MARA, 2015 – 2019', '')]
POSTERS = [('Row locking for enrolment', 'iZone rebuild', 'I led a team of three', 'OutSystems ODC, Aurora PostgreSQL', 'both'),
           ('Question types added one MVP at a time', 'Digital Form', 'Just me: lead, product owner and developer', 'OutSystems O11', 'haze'),
           ('A fixed set of roles, each with its own rules', 'MyInsights', 'One of four developers', 'OutSystems O11', 'rays')]
CODE = f'<span style="font-family:{MONO};font-size:0.92em">SELECT FOR UPDATE</span>'
NOTES = [('The problem', 'The old portal crashed at every enrolment peak. It counted submissions before they were committed, which breaks when many people submit at once. The interface was old too, and the client wanted it modernised.'),
         ('The choice', f'Row locking ({CODE} on Aurora PostgreSQL) for enrolment. I also kept the old database structure as a local replica.'),
         ('What it cost', 'The replica wasn’t well optimised. The team was small, so I wrote code as well as leading, and that stretched me.'),
         ('What happened', 'It’s live, but not in use yet. It was load-tested with 40,000 enrolments over 20 minutes.'),
         ('My part', 'Senior Technical Lead. I owned the architecture and worked with two developers, one junior and one mid-level.'),
         ('Tools', None)]
IZTOOLS = 'OutSystems ODC, Aurora PostgreSQL, Microsoft single sign-on, private gateway'
TL = [('Jan 2026 – present', 'AvePoint', True, 'Full-stack developer · ↳ Sunway University', None),
      ('Sep 2024 – Jan 2026', 'Maybank', True, 'Senior OutSystems Engineer', None),
      ('May – Jul 2024', 'Adam Digital Assets', False, 'part-time', None),
      ('Sep 2022 – Sep 2024', 'FPT Software Malaysia', True, 'Software Consultant · ↳ ', 'PETRONAS Digital'),
      ('Apr – Aug 2022', 'Career break', False, 'Time for personal goals', None),
      ('Apr 2021 – May 2022', 'Impact Business Solutions', False, 'Software Consultant', None)]
SEG = [('Jan 2026 – present', '9 mos', 9, 'AvePoint', True, 'Full-stack developer', '↳ Sunway University'),
       ('Sep 2024 – Jan 2026', '1 yr 5 mos', 17, 'Maybank', True, 'Senior OutSystems Engineer', ''),
       ('Sep 2022 – Sep 2024', '2 yrs 1 mo', 25, 'FPT Software Malaysia', True, 'Software Consultant', 'PETRONAS'),
       ('Apr 2022 – Aug 2022', '5 mos', 5, 'Career break', False, 'Time for personal goals', ''),
       ('Apr 2021 – May 2022', '1 yr 2 mos', 14, 'Impact Business Solutions', False, 'Software Consultant', '')]
MB = 'Maybank'; IMP = 'Impact Business Solutions'
MINOR = {
 'CAB-Q': ('Deployment approval tool. Cut a daily process from 6 hours to 30 minutes.', [(MB, True), ('OutSystems O11', True)]),
 'VIP Dashboard': ('Visualisations of Sarawak data for a VIP presentation.', [(IMP, False), ('Power BI, QGIS', False)]),
 'Audit Log': ('Standardised audit logging, adopted across every OutSystems application.', [(MB, True), ('OutSystems O11', True)]),
 'Tokenizer': ('Tokenisation for public display strings, with an encrypted database.', [(MB, True), ('OutSystems O11', True)]),
 'QR Asset Management': ('QR-based asset tracking.', [(IMP, False), ('Flutter, Firebase', False)]),
 'Adam Digital Assets': ('Islamic mosque signage app, plus a website twin. Two developers shared requirements, design and build.', [('Adam Digital Assets', False), ('Flutter', False)]),
 'MPowered': ('Internal agile project management platform. Stability and defect work.', [(MB, True), ('OutSystems O11', True)]),
 'RPSST': ('Prototype to modernise legacy RBS transaction processes.', [(MB, True), ('OutSystems O11', True)]),
}
LINKEDIN = 'linkedin.com/in/wan-zayd-abdullah-690033230'

# ---------------- shared pieces ----------------
def h2(text, px, counter=None, id_=None, mb=16):
    c = f' <span style="color:{IGREY}">({counter})</span>' if counter else ''
    i = f' id="{id_}"' if id_ else ''
    return f'<h2{i} style="margin:0 0 {mb}px;font-size:{px}px;line-height:1.1;font-weight:500;letter-spacing:-0.025em;color:{FROST}">{text}{c}</h2>'

def pause(label):
    return (f'<button type="button" class="btn" aria-pressed="false" aria-label="Pause {label}" style="display:inline-flex;align-items:center;gap:8px;'
            f'min-height:44px;min-width:44px;padding:0 14px;background:transparent;border:1px solid {IGREY};border-radius:0;color:{ICE};'
            f'font-family:{SANS};{LABEL(12, ICE)};cursor:pointer"><span aria-hidden="true" style="display:inline-flex;gap:3px"><span style="display:block;width:3px;height:10px;background:currentColor"></span><span style="display:block;width:3px;height:10px;background:currentColor"></span></span>Pause</button>')

def placeholder(tag, text, px=15):
    return (f'<div style="border:1px dashed {IGREY};padding:18px 20px;display:flex;flex-direction:column;gap:8px">'
            f'<span style="{LABEL(11)}">{tag}</span>'
            f'<p style="margin:0;font-size:{px}px;line-height:1.6;color:{ICE}">{text}</p></div>')

def worked_strip(gap):
    def items(hidden):
        lis = ''.join(
            f'<li class="wk" style="display:flex;align-items:center;gap:10px;font-size:19px;font-weight:500;letter-spacing:-0.01em;color:{IGREY};white-space:nowrap">'
            + (slot(24) if mk else '') + f'{name}</li>' for name, mk in WORKED)
        ah = ' aria-hidden="true"' if hidden else ''
        return f'<ul{ah} style="display:flex;align-items:center;gap:{gap}px;margin:0;padding:0 {gap//2}px;list-style:none">{lis}</ul>'
    m = 'linear-gradient(90deg, rgba(0,0,0,0), #000 10%, #000 90%, rgba(0,0,0,0))'
    return (f'<div class="strip" style="overflow:hidden;height:88px;border-top:1px solid {NIGHT};border-bottom:1px solid {NIGHT};'
            f'-webkit-mask-image:{m};mask-image:{m}"><div class="drift-rtl" style="display:flex;width:max-content;height:88px;align-items:center">'
            + items(False) + items(True) + '</div></div>')

def quals(px):
    out = []
    for i, (name, d1, d2) in enumerate(QUALS):
        op = ' open="{{ true }}"' if i == 0 else ''
        sign = '−' if i == 0 else '+'
        d2s = f'<span style="color:{IGREY}">{d2}</span>' if d2 else ''
        out.append(f'<li style="border-bottom:1px solid {NIGHT}"><details{op}>'
                   f'<summary class="qs" style="display:flex;justify-content:space-between;align-items:center;gap:16px;min-height:44px;padding:10px 0;cursor:pointer;font-size:{px}px;line-height:1.35;color:{FROST}">'
                   f'<span>{name}</span><span aria-hidden="true" style="color:{IGREY};font-size:20px;line-height:1">{sign}</span></summary>'
                   f'<p style="margin:0 0 14px;font-size:14px;line-height:1.5;color:{ICE}">{d1}{d2s}</p></details></li>')
    return f'<ul style="list-style:none;margin:0;padding:0;border-top:1px solid {NIGHT}">' + ''.join(out) + '</ul>'

def poster(i, p, w, h, title_px, top):
    title, name, credit, tools, light = p
    on = i == 0
    art = ''
    if light in ('both', 'haze'):
        art += haze('50% 0%', '90% 70%', 0.42 if light == 'haze' else 0.34)
    if light in ('both', 'rays'):
        art += rays('50% -6%', '95% 80%', 0.13, 6)
    cur = ' aria-current="true"' if on else ''
    cls = 'pz on' if on else 'pz'
    border = ROCK if on else NIGHT
    return (f'<a class="{cls}" href="#notes"{cur} style="position:relative;flex:0 0 {w}px;width:{w}px;height:{h}px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between;'
            f'padding:{max(18, w//14)}px;background:{DUSK};border:1px solid {border};color:{FROST};text-decoration:none;overflow:hidden;scroll-snap-align:start">'
            + art +
            f'<span style="position:relative;display:block;margin-top:{top}px;font-size:{title_px}px;line-height:1.04;font-weight:500;letter-spacing:-0.04em;color:{FROST}">{title}</span>'
            f'<span style="position:relative;display:flex;flex-direction:column;gap:6px;border-top:1px solid rgba(234,242,248,0.16);padding-top:14px">'
            f'<span style="font-family:{SERIF};font-style:italic;font-size:{20 if w < 300 else 24}px;line-height:1.2;color:{FROST}">{name}</span>'
            f'<span style="font-size:{13 if w < 300 else 15}px;line-height:1.4;color:{ICE}">{credit}</span>'
            f'<span style="display:flex;align-items:center;gap:8px;margin-top:4px;{LABEL(11)}">{slot(14)}{tools}</span>'
            f'</span></a>')

def notes(wide):
    rows = []
    for lab, val in NOTES:
        if val is None:
            val = f'<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">{slot(16)}{IZTOOLS}</span>'
        if wide:
            rows.append(f'<div style="display:grid;grid-template-columns:200px minmax(0,1fr);column-gap:24px;border-top:1px solid {NIGHT};padding-top:16px">'
                        f'<dt style="{LABEL(12)};padding-top:4px">{lab}</dt>'
                        f'<dd style="margin:0;max-width:48ch;font-size:17px;line-height:1.65;color:{FROST}">{val}</dd></div>')
        else:
            rows.append(f'<div><dt style="{LABEL(12)}">{lab}</dt>'
                        f'<dd style="margin:6px 0 0;font-size:16px;line-height:1.65;color:{FROST}">{val}</dd></div>')
    gap = 16 if wide else 22
    return (f'<h3 id="izone-h" style="margin:0;font-size:{32 if wide else 24}px;line-height:1.1;font-weight:500;letter-spacing:-0.025em">iZone rebuild</h3>'
            f'<p style="margin:8px 0 {28 if wide else 24}px;display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:{15 if wide else 14}px;color:{ICE}">Sunway University, via {slot(16)}AvePoint</p>'
            f'<dl style="margin:0;display:grid;gap:{gap}px">' + ''.join(rows) + '</dl>')

def tl_strip():
    def items(hidden):
        lis = []
        for period, name, mk, role, client in TL:
            role_html = role + ((slot(14) + client) if client else '')
            lis.append(f'<li style="display:flex;flex-direction:column;justify-content:center;gap:4px;height:96px;box-sizing:border-box;padding:0 28px;border-left:1px solid {NIGHT};white-space:nowrap">'
                       f'<span style="{LABEL(11)}">{period}</span>'
                       f'<span style="display:flex;align-items:center;gap:8px;font-size:16px;font-weight:500;color:{FROST}">' + (slot(16) if mk else '') + f'{name}</span>'
                       f'<span style="display:flex;align-items:center;gap:6px;font-size:13px;color:{ICE}">{role_html}</span></li>')
        ah = ' aria-hidden="true"' if hidden else ''
        return f'<ol{ah} style="display:flex;margin:0;padding:0;list-style:none">' + ''.join(lis) + '</ol>'
    m = 'linear-gradient(90deg, rgba(0,0,0,0), #000 10%, #000 90%, rgba(0,0,0,0))'
    return (f'<div class="strip" style="overflow:hidden;height:96px;border-top:1px solid {NIGHT};border-bottom:1px solid {NIGHT};'
            f'-webkit-mask-image:{m};mask-image:{m}"><div class="drift-ltr" style="display:flex;width:max-content;height:96px">'
            + items(False) + items(True) + '</div></div>')

def meta(parts):
    bits = []
    for txt, mk in parts:
        bits.append(f'<span style="display:inline-flex;align-items:center;gap:6px">' + (slot(12) if mk else '') + f'{txt}</span>')
    return f'<p style="margin:auto 0 0;display:flex;align-items:center;gap:6px 14px;flex-wrap:wrap;{LABEL(11)}">' + ''.join(bits) + '</p>'

def tile(name, place, minh, big=False):
    desc, parts = MINOR[name]
    stat = (f'<p style="margin:0 0 6px;font-size:{44 if "grid-row" in place else 40}px;line-height:1;font-weight:500;letter-spacing:-0.04em;color:{ROCK}">6 h → 30 min</p>' if big else '')
    return (f'<li class="tile" style="{place};box-sizing:border-box;min-height:{minh}px;padding:20px;background:{DUSK};border:1px solid {NIGHT};display:flex;flex-direction:column;gap:8px">'
            + stat +
            f'<h3 style="margin:0;font-size:19px;line-height:1.2;font-weight:500;letter-spacing:-0.015em;color:{FROST}">{name}</h3>'
            f'<p style="margin:0;font-size:14px;line-height:1.55;color:{ICE}">{desc}</p>' + meta(parts) + '</li>')

def pic(label, place, h, light):
    art = haze('20% 0%', '90% 80%', 0.30) if light == 'haze' else rays('80% -10%', '100% 90%', 0.12, 5)
    return (f'<li style="{place};position:relative;overflow:hidden;box-sizing:border-box;min-height:{h}px;border:1px dashed {IGREY};display:flex;align-items:flex-end;padding:14px">'
            + art + f'<span style="position:relative;{LABEL(11)}">{label}</span></li>')

def postit(place, h, b=False):
    cls = 'post b' if b else 'post'
    return (f'<li class="{cls}" style="{place};box-sizing:border-box;min-height:{h}px;padding:16px;background:{FCLAY};color:{NIGHT};display:flex;flex-direction:column;gap:8px">'
            f'<span style="{LABEL(10, CCLAY)}">Post-it</span>'
            f'<span style="font-family:{SERIF};font-style:italic;font-size:16px;line-height:1.35">[PLACEHOLDER: a short note in your words]</span></li>')

def marquee(px):
    one = f'<span style="padding-right:{px//2}px;white-space:nowrap">Wan Zayd Abdullah</span>'
    return (f'<div class="marq-wrap" aria-hidden="true" style="overflow:hidden;padding:{px//3}px 0;border-top:1px solid {NIGHT}">'
            f'<div class="marq" style="display:flex;width:max-content;font-size:{px}px;line-height:1;font-weight:500;letter-spacing:-0.05em;color:{FROST}">'
            + one * 4 + '</div></div>')

def contact(wide):
    pad = '96px 80px 120px' if wide else '48px 16px 72px'
    lay = 'flex-direction:row;gap:12px' if wide else 'flex-direction:column;gap:10px'
    item = f'display:flex;flex-direction:{"row" if wide else "column"};align-items:{"center" if wide else "flex-start"};gap:{12 if wide else 4}px;min-height:44px;box-sizing:border-box;padding:{"0 18px" if wide else "10px 16px"};border:1px solid {IGREY};border-radius:0;background:transparent;font-family:{SANS};font-size:15px;text-align:left;cursor:pointer'
    inner = (h2('Contact', 44 if wide else 26, id_='contact-h', mb=12)
             + f'<p style="margin:0 0 {28 if wide else 24}px;font-size:{20 if wide else 17}px;line-height:1.5;color:{ICE}">Happy to talk about any of this.</p>'
             f'<ul style="list-style:none;margin:0;padding:0;display:flex;{lay}">'
             f'<li><button type="button" class="btn" style="{item};color:{FROST}"><span style="{LABEL(11)}">Email</span><span>[PLACEHOLDER: email address]</span></button></li>'
             f'<li><a class="btn" href="https://www.linkedin.com/in/wan-zayd-abdullah-690033230" style="{item};color:{FROST};text-decoration:none"><span style="{LABEL(11)}">LinkedIn</span><span style="overflow-wrap:anywhere">{LINKEDIN}</span></a></li>'
             '</ul>')
    if wide:
        inner = f'<div style="grid-column:3 / span 8">{inner}</div>'
        return (f'<footer id="contact" aria-labelledby="contact-h" style="flex-grow:1;position:relative;overflow:hidden;display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;align-content:start;padding:{pad};border-top:1px solid {NIGHT}">'
                + haze('85% 100%', '60% 70%', 0.22) + f'<div style="grid-column:3 / span 8;position:relative">' + inner[len('<div style="grid-column:3 / span 8">'):] + '</footer>')
    return (f'<footer id="contact" aria-labelledby="contact-h" style="flex-grow:1;position:relative;overflow:hidden;padding:{pad};border-top:1px solid {NIGHT}">'
            + haze('90% 100%', '80% 60%', 0.22) + f'<div style="position:relative">{inner}</div></footer>')

# ---------------- phone, 320 ----------------
def phone():
    P = 16
    header = (f'<header style="padding:8px {P}px 4px;border-bottom:1px solid {NIGHT}">'
              f'<a href="#top" style="display:flex;align-items:center;min-height:44px;color:{FROST};text-decoration:none;font-size:15px;font-weight:500;letter-spacing:-0.01em">Wan Zayd Abdullah</a>'
              f'<nav aria-label="Sections"><ul style="list-style:none;margin:0;padding:0;display:flex;gap:6px">'
              + ''.join(f'<li><a class="nv" href="#{t}" style="display:flex;align-items:center;min-height:44px;min-width:44px;padding-right:10px;font-family:{SERIF};font-style:italic;font-size:18px;color:{ICE};text-decoration:none">{t}</a></li>' for t in ('work', 'history', 'contact'))
              + '</ul></nav></header>')
    hero = (f'<section aria-labelledby="hero-h" style="position:relative;overflow:hidden;padding:64px {P}px 44px">'
            + haze('10% -5%', '110% 70%', 0.42) + rays('12% -8%', '120% 85%', 0.13, 6) +
            f'<div style="position:relative;display:flex;flex-direction:column;gap:18px">'
            f'<h1 id="hero-h" style="margin:0;font-size:31px;line-height:1.08;font-weight:500;letter-spacing:-0.04em;color:{FROST}">{TAGLINE}</h1>'
            f'<p style="margin:6px 0 0;{LABEL(12)}">5 years · since Apr 2021</p>'
            f'<p style="margin:0;font-family:{SERIF};font-style:italic;font-size:23px;line-height:1.2;color:{ICE}">OutSystems Technical Lead</p>'
            '</div></section>')
    glance = (f'<section aria-labelledby="glance-h" style="padding:4px {P}px 40px"><h2 id="glance-h" class="sr">At a glance</h2>'
              f'<ul style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;list-style:none;margin:0;padding:0">'
              + ''.join(f'<li style="border-top:1px solid {SLATE};padding-top:12px"><span style="display:block;font-size:32px;line-height:1;font-weight:500;letter-spacing:-0.03em;color:{FROST}">{n}</span>'
                        f'<span style="display:block;margin-top:8px;font-size:13px;line-height:1.35;color:{ICE}">{t}</span></li>'
                        for n, t in (('5', 'employers'), ('11', 'projects, 3 in detail'), ('5', 'qualifications')))
              + '</ul></section>')
    worked = (f'<section aria-labelledby="worked-h" style="padding:0 0 48px">'
              f'<div style="display:flex;justify-content:space-between;align-items:center;padding:0 {P}px 16px">{h2("Worked with", 22, id_="worked-h", mb=0)}{pause("Worked with")}</div>'
              + worked_strip(40) + '</section>')
    about = (f'<section aria-labelledby="about-h" style="padding:0 {P}px 48px">{h2("About", 22, id_="about-h")}'
             + placeholder('To write', '[PLACEHOLDER: About, in your words. Who you are, with the title. One decision, told before the word OutSystems. Your interest in front-end and design.]')
             + '</section>')
    qual = (f'<section aria-labelledby="qual-h" style="padding:0 {P}px 56px">{h2("Qualifications", 22, "5", "qual-h")}' + quals(16) + '</section>')
    projhead = (f'<section id="work" aria-labelledby="proj-h" style="padding:0 {P}px 8px">{h2("Projects", 30, "3", "proj-h", mb=12)}'
                f'<p style="margin:0;font-size:16px;line-height:1.6;color:{ICE}">Three projects, each with what was wrong, what we chose and what it cost.</p></section>')
    shelf = (f'<div style="display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding:22px {P}px 28px">'
             + ''.join(poster(i, p, 248, 372, 29, 64) for i, p in enumerate(POSTERS)) + '</div>')
    notes_s = f'<section id="notes" aria-labelledby="izone-h" style="padding:8px {P}px 56px">' + notes(False) + '</section>'
    how = (f'<section aria-labelledby="how-h" style="padding:0 {P}px 56px">{h2("How I work", 22, id_="how-h")}'
           + placeholder('To write', '[PLACEHOLDER: one short paragraph, in your words, on architecture calls and running a team.]') + '</section>')
    hist = (f'<section id="history" aria-labelledby="hist-h" style="padding:0 0 56px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;padding:0 {P}px 16px">{h2("History", 22, id_="hist-h", mb=0)}{pause("History")}</div>'
            + tl_strip() + '</section>')
    g = 'grid-column:span 2'
    one = 'grid-column:span 1'
    bento = ''.join([
        tile('CAB-Q', g, 210, big=True), tile('VIP Dashboard', g, 168),
        pic('Picture: map motif, Sarawak data', one, 138, 'haze'), postit(one, 138),
        tile('Audit Log', g, 168), tile('Tokenizer', g, 168), tile('QR Asset Management', g, 150),
        pic('Picture: QR-pattern motif', one, 138, 'rays'), postit(one, 138, b=True),
        pic('Picture: mosque-signage motif', g, 140, 'haze'), tile('Adam Digital Assets', g, 190),
        tile('MPowered', g, 168), tile('RPSST', g, 168)])
    minor = (f'<section aria-labelledby="minor-h" style="padding:0 {P}px 56px">{h2("Minor Projects", 22, "8", "minor-h", mb=20)}'
             f'<ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px">{bento}</ul></section>')
    main = (f'<main style="display:flex;flex-direction:column">' + hero + glance + worked + about + qual + projhead + shelf
            + notes_s + how + hist + minor + marquee(76) + '</main>')
    return page('Portfolio, phone', 320, 6700, header + main + contact(False))

# ---------------- desktop, 1440 ----------------
def desktop():
    M = 80
    GRID = 'display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px'
    header = (f'<header style="display:flex;justify-content:space-between;align-items:center;height:72px;box-sizing:border-box;padding:0 {M}px;border-bottom:1px solid {NIGHT}">'
              f'<a href="#top" style="display:flex;align-items:center;min-height:44px;color:{FROST};text-decoration:none;font-size:16px;font-weight:500;letter-spacing:-0.01em">Wan Zayd Abdullah</a>'
              f'<nav aria-label="Sections"><ul style="list-style:none;margin:0;padding:0;display:flex;gap:28px">'
              + ''.join(f'<li><a class="nv" href="#{t}" style="display:flex;align-items:center;min-height:44px;min-width:44px;font-family:{SERIF};font-style:italic;font-size:19px;color:{ICE};text-decoration:none">{t}</a></li>' for t in ('work', 'history', 'contact'))
              + '</ul></nav></header>')
    glance = (f'<section aria-labelledby="glance-h" style="grid-column:10 / span 3;align-self:end"><h2 id="glance-h" class="sr">At a glance</h2>'
              f'<ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column">'
              + ''.join(f'<li style="display:flex;align-items:baseline;gap:16px;border-top:1px solid {SLATE};padding:14px 0">'
                        f'<span style="flex:0 0 64px;font-size:44px;line-height:1;font-weight:500;letter-spacing:-0.04em;color:{FROST}">{n}</span>'
                        f'<span style="font-size:15px;line-height:1.4;color:{ICE}">{t}</span></li>'
                        for n, t in (('5', 'employers'), ('11', 'projects, 3 in detail'), ('5', 'qualifications')))
              + '</ul></section>')
    hero = (f'<div style="position:relative;overflow:hidden;{GRID};padding:88px {M}px 96px">'
            + haze('14% -8%', '70% 80%', 0.42) + rays('16% -12%', '75% 95%', 0.13, 8) +
            f'<section aria-labelledby="hero-h" style="grid-column:1 / span 8;position:relative;display:flex;flex-direction:column;gap:16px">'
            f'<h1 id="hero-h" style="margin:0;font-size:56px;line-height:1.04;font-weight:500;letter-spacing:-0.045em;color:{FROST}">{TAGLINE}</h1>'
            f'<p style="margin:16px 0 0;{LABEL(13)}">5 years · since Apr 2021</p>'
            f'<p style="margin:0;font-family:{SERIF};font-style:italic;font-size:30px;line-height:1.2;color:{ICE}">OutSystems Technical Lead</p>'
            '</section>' + f'<div style="grid-column:10 / span 3;position:relative;align-self:end">' + glance.replace('grid-column:10 / span 3;align-self:end', 'display:block') + '</div></div>')
    worked = (f'<section aria-labelledby="worked-h" style="padding:8px 0 96px">'
              f'<div style="display:flex;justify-content:space-between;align-items:center;padding:0 {M}px 20px">{h2("Worked with", 24, id_="worked-h", mb=0)}{pause("Worked with")}</div>'
              + worked_strip(64) + '</section>')
    aq = (f'<div style="{GRID};padding:0 {M}px 120px;align-items:start">'
          f'<section aria-labelledby="about-h" style="grid-column:1 / span 5">{h2("About", 28, id_="about-h", mb=20)}'
          + placeholder('To write', '[PLACEHOLDER: About, in your words. Who you are, with the title. One decision, told before the word OutSystems. Your interest in front-end and design.]', 17)
          + f'</section><section aria-labelledby="qual-h" style="grid-column:7 / span 6">{h2("Qualifications", 28, "5", "qual-h", mb=20)}' + quals(17) + '</section></div>')
    projhead = (f'<section id="work" aria-labelledby="proj-h" style="padding:0 {M}px 16px">{h2("Projects", 48, "3", "proj-h", mb=14)}'
                f'<p style="margin:0;max-width:60ch;font-size:19px;line-height:1.6;color:{ICE}">Three projects, each with what was wrong, what we chose and what it cost.</p></section>')
    shelf = (f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;padding:36px {M}px 72px">'
             + ''.join(poster(i, p, 411, 560, 42, 140).replace('flex:0 0 411px;width:411px', 'width:auto') for i, p in enumerate(POSTERS)) + '</div>')
    notes_s = (f'<div style="{GRID};padding:0 {M}px 120px"><section id="notes" aria-labelledby="izone-h" style="grid-column:3 / span 8">'
               + notes(True) + '</section></div>')
    how = (f'<div style="{GRID};padding:0 {M}px 120px"><section aria-labelledby="how-h" style="grid-column:3 / span 8">{h2("How I work", 28, id_="how-h", mb=20)}'
           + placeholder('To write', '[PLACEHOLDER: one short paragraph, in your words, on architecture calls and running a team.]', 17) + '</section></div>')
    segs = []
    for i, (period, dur, mos, name, mk, role, client) in enumerate(SEG):
        on = i == 0
        brk = name == 'Career break'
        top = f'3px solid {ROCK}' if on else (f'3px dashed {SLATE}' if brk else f'3px solid {NIGHT}')
        bg = 'rgba(227,211,208,0.06)' if on else 'transparent'
        cur = ' aria-current="true"' if on else ''
        cl = ''
        if client == 'PETRONAS':
            cl = f'<span style="display:flex;align-items:center;gap:6px;font-size:14px;color:{ICE}">↳ {slot(14)}PETRONAS Digital</span>'
        elif client:
            cl = f'<span style="font-size:14px;color:{ICE}">{client}</span>'
        link = (f'<a class="seg" href="#h-panel"{cur} style="display:flex;flex-direction:column;gap:6px;min-height:136px;box-sizing:border-box;padding:16px 16px 18px;border-top:{top};background:{bg};color:{FROST};text-decoration:none">'
                f'<span style="{LABEL(11, ROCK if on else IGREY)}">{period} · {dur}</span>'
                f'<span style="display:flex;align-items:center;gap:8px;font-size:17px;font-weight:500;letter-spacing:-0.01em;color:{ICE if brk else FROST}">' + (slot(16) if mk else '') + f'{name}</span>'
                f'<span style="font-size:14px;color:{ICE}">{role}</span>{cl}</a>')
        extra = ''
        if name.startswith('FPT'):
            extra = (f'<a class="seg" href="#h-panel" style="display:flex;align-items:center;min-height:44px;box-sizing:border-box;margin-top:4px;padding:0 14px;border:1px dashed {SLATE};color:{ICE};text-decoration:none;font-size:13px">'
                     '+ Adam Digital Assets, May – Jul 2024, 3 mos, part-time</a>')
        segs.append(f'<li style="flex:{mos} 1 0;min-width:176px">{link}{extra}</li>')
    hist = (f'<section id="history" aria-labelledby="hist-h" style="padding:0 {M}px 32px">{h2("History", 28, id_="hist-h", mb=24)}'
            f'<ol style="display:flex;gap:6px;list-style:none;margin:0;padding:0;align-items:flex-start">' + ''.join(segs) + '</ol></section>')
    panel = (f'<div style="{GRID};padding:0 {M}px 120px"><div id="h-panel" style="grid-column:3 / span 8;position:relative;overflow:hidden;background:{DUSK};border:1px solid {NIGHT};padding:28px 32px;display:flex;flex-direction:column;gap:12px">'
             + rays('100% -20%', '60% 90%', 0.10, 6) +
             f'<p style="position:relative;margin:0;{LABEL(12, ROCK)}">Jan 2026 – present, full-time</p>'
             f'<h3 style="position:relative;margin:0;display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:26px;line-height:1.15;font-weight:500;letter-spacing:-0.02em">{slot(22)}AvePoint <span style="font-weight:400;color:{ICE}">Full-stack developer</span></h3>'
             f'<p style="position:relative;margin:0;font-size:16px;line-height:1.6;color:{ICE}">↳ Sunway University, client. Apr 2026 – present. Senior Technical Lead.</p>'
             f'<p style="position:relative;margin:4px 0 0;font-size:16px;line-height:1.6;color:{FROST}"><span style="{LABEL(11)};margin-right:10px">Project in this period</span><a href="#notes">iZone rebuild ↑</a></p>'
             f'<p style="position:relative;margin:0;display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:16px;line-height:1.6;color:{FROST}"><span style="{LABEL(11)};margin-right:2px">Tools</span>{slot(16)}{IZTOOLS}</p>'
             '</div></div>')
    def at(c, r, cs=1, rs=1):
        return f'grid-column:{c} / span {cs};grid-row:{r} / span {rs}'
    bento = ''.join([
        tile('CAB-Q', at(1, 1, 1, 2), 212, big=True), tile('VIP Dashboard', at(2, 1), 212),
        pic('Picture: map motif, Sarawak data', at(3, 1), 212, 'haze'), tile('Audit Log', at(4, 1), 212),
        postit(at(2, 2), 212), tile('Tokenizer', at(3, 2), 212), postit(at(4, 2), 212, b=True),
        tile('QR Asset Management', at(1, 3), 212), pic('Picture: QR-pattern motif', at(2, 3), 212, 'rays'),
        pic('Picture: mosque-signage motif', at(3, 3, 2), 212, 'haze'),
        tile('MPowered', at(1, 4), 212), tile('RPSST', at(2, 4), 212), tile('Adam Digital Assets', at(3, 4, 2), 212)])
    minor = (f'<section aria-labelledby="minor-h" style="padding:0 {M}px 120px">{h2("Minor Projects", 28, "8", "minor-h", mb=28)}'
             f'<ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:minmax(212px,auto);gap:24px">{bento}</ul></section>')
    main = (f'<main style="display:flex;flex-direction:column">' + hero + worked + aq + projhead + shelf + notes_s + how + hist + panel
            + minor + marquee(168) + '</main>')
    return page('Portfolio, desktop', 1440, 6000, header + main + contact(True))

ROOT = 'canvas/'
open(ROOT + 'Main.dc.html', 'w').write(phone())
open(ROOT + 'Desktop.dc.html', 'w').write(desktop())
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": now}, "title": "Portfolio hi-fi", "launch": {"view": "canvas"}, "pages": [],
          "boards": {"Main.dc.html": {"x": 0, "y": 0, "w": 320, "h": 6700, "title": "Phone 320", "is_interactive": False},
                     "Desktop.dc.html": {"x": 400, "y": 0, "w": 1440, "h": 6000, "title": "Desktop 1440"}},
          "order": ["Main.dc.html", "Desktop.dc.html"],
          "notes": {"t1": {"x": 0, "y": -300, "text": "Hi-fi, Night light (palette v5)", "kind": "title1", "maxW": 1840}},
          "designSystems": []}
del canvas['boards']['Main.dc.html']['is_interactive']
json.dump(canvas, open(ROOT + 'canvas.json', 'w'), indent=1)
print('ok')
