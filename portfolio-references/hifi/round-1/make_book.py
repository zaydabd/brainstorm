# F · The book, white. Minimal copy; photos and a hero video supplied by Wan Zayd (metadata stripped).
import json, sys

PAPER, INK, SL, RULE, CLAY, OX = '#FCFCFC', '#262032', '#373F47', '#C9D3DE', '#8E5A4F', '#4A2E2E'
DIDONE = "Didot,'Bodoni MT','Noto Serif Display','URW Palladio L',P052,Sylfaen,serif"
BOOK = "ui-serif,'Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif"
B = {'video': '/_blob/982b8513fa164c4e5d4b5a5bb8199c9b', 'poster': '/_blob/2d74618e849433069242f727cbc5a165',
     'shadows': '/_blob/28cea1090f6087cd4d65d795241e9267', 'plants': '/_blob/826383981c95ef1f11aa8c1622e6b2f3',
     'street': '/_blob/5c788df47191487d560b509c782cb330', 'harp': '/_blob/d3282f304996981614eaaff9ddea37c0',
     'orchid': '/_blob/a10f7274e63db6b0f3a239c020c64fea'}
TAGLINE = 'I design and build enterprise systems: on my own, in a team, and leading one.'
LI_URL = 'https://www.linkedin.com/in/wan-zayd-abdullah-690033230'
LI = 'linkedin.com/in/wan-zayd-abdullah-690033230'
AH = ' aria-hidden="true"'

# Three Main Projects, cut to a few lines each (from the round-7 notes; nothing new added)
PROJ = [
 dict(key='izone', name='iZone rebuild', photo='shadows', org=[('Sunway University, via ', 0), ('AvePoint', 1)],
      title='Row locking for enrolment', credit='I led a team of three', tools='OutSystems ODC, Aurora PostgreSQL',
      lines=[('Problem', 'The old portal crashed at every enrolment peak.'),
             ('Cost', 'A replica that wasn’t well optimised, and I coded as well as led.'),
             ('Result', 'Load-tested with 40,000 enrolments over 20 minutes. Live, not yet in use.')]),
 dict(key='form', name='Digital Form', photo='plants', org=[('Maybank', 1)],
      title='Question types added one MVP at a time', credit='Just me: lead, product owner and developer', tools='OutSystems O11',
      lines=[('Problem', 'Maybank had no internal form platform.'),
             ('Cost', 'Each new question type added complexity.'),
             ('Result', 'Over 80 forms by the fifth MVP.')]),
 dict(key='myinsights', name='MyInsights', photo='street', org=[('PETRONAS', 1), (', via ', 0), ('FPT Software', 1)],
      title='A fixed set of roles, each with its own rules', credit='One of four developers', tools='OutSystems O11',
      lines=[('Problem', 'Auditors checked exceptions by hand, on files and paper.'),
             ('Result', 'Auditors now work through exceptions in one system.')]),
]
MINOR = [('CAB-Q', 'Maybank', 1, 'Deployment approvals: a daily 6 hours cut to 30 minutes.', 'OutSystems O11'),
         ('Audit Log', 'Maybank', 1, 'Audit logging for every OutSystems app.', 'OutSystems O11'),
         ('Tokenizer', 'Maybank', 1, 'Tokenised display strings, encrypted database.', 'OutSystems O11'),
         ('MPowered', 'Maybank', 1, 'Stability and defect work on an agile platform.', 'OutSystems O11'),
         ('RPSST', 'Maybank', 1, 'Prototype to modernise RBS transactions.', 'OutSystems O11'),
         ('VIP Dashboard', 'Impact', 0, 'Sarawak data for a VIP presentation.', 'Power BI, QGIS'),
         ('QR Asset Management', 'Impact', 0, 'QR-based asset tracking.', 'Flutter, Firebase'),
         ('Adam Digital Assets', 'Adam', 0, 'Mosque signage app and website.', 'Flutter')]
HIST = [('AvePoint', 1, 'Jan 2026 – present', 'Full-stack developer'),
        ('↳ Sunway University', 0, 'Apr 2026 – present', 'Senior Technical Lead'),
        ('Maybank', 1, 'Sep 2024 – Jan 2026', 'Senior OutSystems Engineer'),
        ('Adam Digital Assets', 0, 'May – Jul 2024', 'Part-time'),
        ('FPT Software Malaysia', 1, 'Sep 2022 – Sep 2024', 'Software Consultant'),
        ('↳ PETRONAS Digital', 1, '', ''),
        ('Career break', 0, 'Apr – Aug 2022', ''),
        ('Impact Business Solutions', 0, 'Apr 2021 – May 2022', 'Software Consultant')]
TL = [('Jan 2026 – present', 'AvePoint', 1), ('Sep 2024 – Jan 2026', 'Maybank', 1), ('May – Jul 2024', 'Adam Digital Assets', 0),
      ('Sep 2022 – Sep 2024', 'FPT Software Malaysia', 1), ('Apr – Aug 2022', 'Career break', 0), ('Apr 2021 – May 2022', 'Impact Business Solutions', 0)]
WORKED = [('AvePoint', 1), ('Sunway University', 0), ('Maybank', 1), ('Adam Digital Assets', 0), ('FPT Software', 1), ('PETRONAS', 1), ('Impact Business Solutions', 0)]
QUALS = [('OutSystems Associate Developer Specialist (O11)', '[year]'), ('OutSystems Associate Technical Lead (O11)', '[year]'),
         ('Professional Scrum Developer', '[year]'), ('BSc Information Systems, UiTM', '2019 – 2021'), ('Diploma in Computer Science, UiTM', '2015 – 2019')]

HELMET = '''<helmet>
<style>
body{margin:0;background:#FCFCFC;color:#262032;font-family:ui-serif,"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif}
a{color:#262032;text-decoration-color:#8E5A4F;text-decoration-thickness:1px;text-underline-offset:4px}a:hover{color:#8E5A4F}
::selection{background:#262032;color:#FCFCFC}
a:focus-visible,button:focus-visible{outline:2px solid #8E5A4F;outline-offset:3px}
h1,h2,h3{text-wrap:balance}p{text-wrap:pretty}
.onum{font-variant-numeric:oldstyle-nums proportional-nums}
.nv{text-decoration:none}.nv:hover{text-decoration:underline}
.wk{transition:color .4s ease}.wk:hover{color:#262032}
.pl img{transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}.pl:hover img{transform:scale(1.02)}
.vb{transition:background-color .2s}.vb:hover{background:rgba(13,11,18,0.7)}
@keyframes wz-rtl{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@keyframes wz-ltr{from{transform:translateX(-50%)}to{transform:translateX(0)}}
.drift-rtl{animation:wz-rtl 70s linear infinite}.drift-ltr{animation:wz-ltr 80s linear infinite}
.strip:hover .drift-rtl,.strip:hover .drift-ltr,.strip:focus-within .drift-rtl,.strip:focus-within .drift-ltr{animation-play-state:paused}
@media (prefers-reduced-motion:reduce){.drift-rtl,.drift-ltr{animation:none}.strip{overflow-x:auto}.pl img{transition:none}}
</style>
</helmet>'''

SCRIPT = '''class Component extends DCLogic {
renderVals() {
const paused = !!(this.state && this.state.paused);
return {
vref: (el) => {
this.v = el;
if (!el) return;
el.muted = true;
const still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (still || paused) { el.pause(); return; }
const p = el.play && el.play();
if (p && p.catch) p.catch(() => {});
},
toggle: () => {
const v = this.v;
if (!v) return;
if (v.paused) { const p = v.play(); if (p && p.catch) p.catch(() => {}); this.setState({ paused: false }); }
else { v.pause(); this.setState({ paused: true }); }
},
vlabel: paused ? 'Play' : 'Pause',
};
}
}'''

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
<div id="top" style="width:{w}px;height:{h}px;box-sizing:border-box;overflow:hidden;display:flex;flex-direction:column;background:{PAPER};color:{INK};font-family:{BOOK};-webkit-font-smoothing:antialiased">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
{SCRIPT}
</script>
</body>
</html>
'''

def sc(px=12, color=CLAY, ls='0.14em'):
    return f'font-size:{px}px;line-height:1.5;letter-spacing:{ls};text-transform:uppercase;font-weight:400;color:{color}'

def slot(px, color=SL):
    return f'<span aria-hidden="true" style="display:inline-block;flex-shrink:0;width:{px}px;height:{px}px;box-sizing:border-box;border:1px dashed {color}"></span>'

def org(p, px):
    return ''.join((slot(px) if mk else '') + t for t, mk in p['org'])

def leader(left, right, px, rc=SL):
    return (f'<div style="display:flex;align-items:baseline;font-size:{px}px;line-height:1.35"><span>{left}</span>'
            f'<span aria-hidden="true" style="flex:1 1 auto;min-width:20px;margin:0 8px;border-bottom:1px dotted {SL};transform:translateY(-5px)"></span>'
            f'<span class="onum" style="white-space:nowrap;color:{rc}">{right}</span></div>')

def strong(n):
    return f'<strong style="font-weight:600">{n}</strong>'

def emp(e, mk):
    return f'<span style="display:inline-flex;align-items:center;gap:6px">{slot(12) if mk else ""}{e}</span>'

def photo(key, style):
    return f'<figure class="pl" style="margin:0;overflow:hidden;{style}"><img src="{B[key]}" alt="" style="display:block;width:100%;height:100%;object-fit:cover"></figure>'

def video(style, btn_pos):
    return (f'<div style="position:relative;overflow:hidden;background:#14111C;{style}">'
            f'<video ref="{{{{ vref }}}}" src="{B["video"]}" poster="{B["poster"]}" autoPlay="{{{{ true }}}}" muted="{{{{ true }}}}" loop="{{{{ true }}}}" playsInline="{{{{ true }}}}" preload="auto"{AH} '
            f'style="display:block;width:100%;height:100%;object-fit:cover"></video>'
            f'<button type="button" class="vb" onClick="{{{{ toggle }}}}" aria-label="Pause or play the background video" style="position:absolute;{btn_pos};display:inline-flex;align-items:center;gap:8px;min-height:44px;min-width:44px;padding:0 14px;'
            f'border:0;background:rgba(13,11,18,0.45);color:#FCFCFC;cursor:pointer;font-family:{BOOK};{sc(11, "#FCFCFC")}">{{{{ vlabel }}}}</button></div>')

def strip(items, height, direction):
    m = 'linear-gradient(90deg, rgba(0,0,0,0), #000 8%, #000 92%, rgba(0,0,0,0))'
    return (f'<div class="strip" style="overflow:hidden;height:{height}px;-webkit-mask-image:{m};mask-image:{m}"><div class="drift-{direction}" style="display:flex;width:max-content;height:{height}px;align-items:center">'
            + items(False) + items(True) + '</div></div>')

def worked(px, gap):
    def items(h):
        lis = ''.join(f'<li class="wk" style="display:flex;align-items:center;gap:10px;font-style:italic;font-size:{px}px;color:{SL};white-space:nowrap">{slot(px - 10) if mk else ""}{n}</li>' for n, mk in WORKED)
        return f'<ul{AH if h else ""} style="display:flex;align-items:center;gap:{gap}px;margin:0;padding:0 {gap//2}px;list-style:none">{lis}</ul>'
    return items

def project_text(p, wide):
    lines = ''.join(f'<p style="margin:0 0 {10 if wide else 8}px;font-size:{19 if wide else 16}px;line-height:1.55"><span style="{sc(12 if wide else 11)};margin-right:10px">{l}</span>{t}</p>' for l, t in p['lines'])
    return (f'<p style="margin:0 0 14px;{sc(13 if wide else 11)}">{p["name"]}</p>'
            f'<h3 id="f-{p["key"]}" style="margin:0 0 12px;font-family:{DIDONE};font-weight:400;font-size:{52 if wide else 32}px;line-height:1.04;letter-spacing:-0.01em">{p["title"]}</h3>'
            f'<p style="margin:0 0 {28 if wide else 20}px;display:flex;align-items:center;gap:6px;flex-wrap:wrap;font-style:italic;font-size:{18 if wide else 15}px;color:{SL}">{org(p, 13)}</p>'
            + lines +
            f'<p style="margin:{18 if wide else 14}px 0 0;padding-top:12px;border-top:1px solid {RULE};display:flex;align-items:center;gap:8px;flex-wrap:wrap;{sc(11, SL, "0.1em")}">'
            f'<span>{p["credit"]}</span><span aria-hidden="true">·</span>{slot(12)}<span>{p["tools"]}</span></p>')

# ---------------- desktop ----------------
def desktop():
    G = 'display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;padding:0 80px'
    nav = (f'<nav aria-label="Sections"><ul style="list-style:none;margin:0;padding:0;display:flex;gap:28px">'
           + ''.join(f'<li><a class="nv" href="#{h}" style="display:flex;align-items:center;min-height:44px;font-style:italic;font-size:18px;color:{SL}">{t}</a></li>' for t, h in (('work', 'work'), ('history', 'history'), ('contact', 'contact')))
           + '</ul></nav>')
    front = (f'<section aria-labelledby="f-name" style="display:grid;grid-template-columns:1fr 1fr;height:900px">'
             + video('height:900px', 'left:24px;bottom:24px') +
             f'<div style="display:flex;flex-direction:column;justify-content:space-between;padding:40px 96px 72px 88px">{nav}'
             f'<div><h1 id="f-name" style="margin:0 0 16px;font-family:{DIDONE};font-weight:400;font-size:80px;line-height:0.98;letter-spacing:-0.015em">Wan Zayd Abdullah</h1>'
             f'<p style="margin:0 0 40px;font-style:italic;font-size:26px;color:{SL}">OutSystems Technical Lead</p>'
             f'<p style="margin:0;max-width:24ch;font-size:26px;line-height:1.4">{TAGLINE}</p></div>'
             f'<p class="onum" style="margin:0;{sc(12)}">5 years · since Apr 2021</p></div></section>')
    about = (f'<section aria-labelledby="f-about" style="{G};padding-top:160px;padding-bottom:160px;align-items:start">'
             + photo('harp', 'grid-column:1 / span 4;height:560px') +
             f'<div style="grid-column:6 / span 6"><h2 id="f-about" style="margin:0 0 14px;{sc(13)}">About</h2>'
             f'<p style="margin:0 0 20px;font-style:italic;font-size:22px;line-height:1.55;color:{SL}">[PLACEHOLDER: About, three lines in your words]</p>'
             f'<p style="margin:0 0 64px;font-size:22px;line-height:1.5">Five employers, eleven projects and five qualifications.</p>'
             f'<h2 id="f-qual" style="margin:0 0 6px;{sc(13)}">Qualifications</h2>'
             + ''.join(f'<div style="padding:8px 0">{leader(n, y, 18)}</div>' for n, y in QUALS)
             + f'<p style="margin:10px 0 0;font-style:italic;font-size:14px;color:{SL}">[year]: [PLACEHOLDER: certification years]</p></div></section>')
    wk = (f'<section aria-labelledby="f-worked" style="margin:0 80px 160px;border-top:1px solid {RULE};border-bottom:1px solid {RULE}">'
          f'<h2 id="f-worked" style="margin:0;padding-top:8px;{sc(12)}">Worked with</h2>' + strip(worked(32, 72), 88, 'rtl') + '</section>')
    projs = (f'<section id="work" aria-labelledby="f-proj" style="padding:0 80px 40px"><h2 id="f-proj" style="margin:0;{sc(13)}">Projects</h2></section>')
    for i, p in enumerate(PROJ):
        img = photo(p['photo'], f'grid-column:{1 if i % 2 == 0 else 7} / span 6;grid-row:1;height:720px')
        txt = f'<article aria-labelledby="f-{p["key"]}" style="grid-column:{8 if i % 2 == 0 else 1} / span 5;grid-row:1">{project_text(p, True)}</article>'
        projs += f'<div style="{G};padding-bottom:120px;align-items:center">{img}{txt}</div>'
    hist = (f'<section id="history" aria-labelledby="f-hist" style="{G};padding-top:40px;padding-bottom:160px;align-items:start">'
            f'<div style="grid-column:1 / span 4"><h2 id="f-how" style="margin:0 0 14px;{sc(13)}">How I work</h2>'
            f'<p style="margin:0;font-style:italic;font-size:21px;line-height:1.55;color:{SL}">[PLACEHOLDER: one short paragraph, in your words]</p></div>'
            f'<div style="grid-column:6 / span 7"><h2 id="f-hist" style="margin:0 0 6px;{sc(13)}">History</h2>'
            + ''.join(f'<div style="padding:{6 if n.startswith("↳") else 10}px 0 0 {22 if n.startswith("↳") else 0}px">'
                      + leader(f'<span style="display:inline-flex;align-items:center;gap:8px;{"font-style:italic;color:" + SL if n.startswith("↳") else ""}">{slot(13) if mk else ""}{n}</span>', per, 19 if not n.startswith('↳') else 17)
                      + (f'<p style="margin:0;font-style:italic;font-size:15px;color:{SL}">{r}</p>' if r else '') + '</div>' for n, mk, per, r in HIST)
            + '</div></section>')
    minor = (f'<section aria-labelledby="f-minor" style="{G};padding-bottom:160px"><h2 id="f-minor" style="grid-column:1 / span 12;margin:0 0 14px;{sc(13)}">Minor Projects</h2>'
             f'<ol style="grid-column:1 / span 12;list-style:none;margin:0;padding:0;columns:2;column-gap:72px">'
             + ''.join(f'<li style="break-inside:avoid;padding:0 0 22px">{leader(strong(n), emp(e, mk), 19)}'
                       f'<p style="margin:4px 0 0;font-size:16px;line-height:1.5">{d} <span style="font-style:italic;color:{SL}">{t}</span></p></li>' for n, e, mk, d, t in MINOR)
             + '</ol></section>')
    close = (f'<footer id="contact" aria-labelledby="f-contact" style="flex-grow:1;{G};align-content:start;align-items:center;padding-bottom:120px">'
             f'<div style="grid-column:1 / span 5"><h2 id="f-contact" style="margin:0 0 14px;{sc(13)}">Contact</h2>'
             f'<p style="margin:0 0 36px;font-family:{DIDONE};font-size:56px;line-height:1.04">Happy to talk about any of this.</p>'
             + leader('Email', f'<button type="button" style="min-height:44px;padding:0;border:0;background:transparent;font:inherit;font-style:italic;color:{INK};cursor:pointer;text-decoration:underline;text-decoration-color:{CLAY};text-underline-offset:4px">[PLACEHOLDER: email address]</button>', 19, INK)
             + leader('LinkedIn', f'<a href="{LI_URL}" style="display:inline-flex;align-items:center;min-height:44px;font-style:italic">{LI}</a>', 19, INK)
             + '</div>' + photo('orchid', 'grid-column:7 / span 6;height:720px') + '</footer>')
    body = '<main style="display:flex;flex-direction:column">' + front + about + wk + projs + hist + minor + '</main>' + close
    return page('Portfolio F, desktop', 1440, 7200, body)

# ---------------- phone ----------------
def phone():
    P = 20
    front = (f'<section aria-labelledby="f-name">' + video('height:340px', 'left:12px;bottom:12px') +
             f'<div style="padding:22px {P}px 0"><h1 id="f-name" style="margin:0 0 6px;font-family:{DIDONE};font-weight:400;font-size:38px;line-height:1.0">Wan Zayd Abdullah</h1>'
             f'<p style="margin:0;font-style:italic;font-size:19px;color:{SL}">OutSystems Technical Lead</p>'
             f'<nav aria-label="Sections" style="margin-top:4px"><ul style="list-style:none;margin:0;padding:0;display:flex;gap:18px">'
             + ''.join(f'<li><a class="nv" href="#{t}" style="display:flex;align-items:center;min-height:44px;font-style:italic;font-size:17px;color:{SL}">{t}</a></li>' for t in ('work', 'history', 'contact'))
             + '</ul></nav></div></section>')
    intro = (f'<section aria-label="Introduction" style="padding:40px {P}px 64px"><p style="margin:0 0 16px;font-family:{DIDONE};font-size:28px;line-height:1.12">{TAGLINE}</p>'
             f'<p class="onum" style="margin:0;{sc(11)}">5 years · since Apr 2021</p></section>')
    wk = (f'<section aria-labelledby="f-worked" style="margin:0 0 72px;border-top:1px solid {RULE};border-bottom:1px solid {RULE}">'
          f'<h2 id="f-worked" style="margin:0;padding:6px {P}px 0;{sc(11)}">Worked with</h2>' + strip(worked(24, 44), 88, 'rtl') + '</section>')
    about = (f'<section aria-labelledby="f-about" style="padding:0 {P}px 72px"><h2 id="f-about" style="margin:0 0 10px;{sc(12)}">About</h2>'
             f'<p style="margin:0 0 20px;font-style:italic;font-size:18px;line-height:1.55;color:{SL}">[PLACEHOLDER: About, three lines in your words]</p>'
             f'<p style="margin:0;font-size:18px;line-height:1.5">Five employers, eleven projects and five qualifications.</p></section>')
    qual = (f'<section aria-labelledby="f-qual" style="padding:0 {P}px 80px"><h2 id="f-qual" style="margin:0 0 4px;{sc(12)}">Qualifications</h2>'
            + ''.join(f'<div style="padding:7px 0">{leader(n, y, 16)}</div>' for n, y in QUALS)
            + f'<p style="margin:8px 0 0;font-style:italic;font-size:13px;color:{SL}">[year]: [PLACEHOLDER: certification years]</p></section>')
    projs = f'<section id="work" aria-labelledby="f-proj" style="padding:0 {P}px 20px"><h2 id="f-proj" style="margin:0;{sc(12)}">Projects</h2></section>'
    for p in PROJ:
        projs += (f'<article aria-labelledby="f-{p["key"]}" style="padding-bottom:80px">' + photo(p['photo'], 'height:240px')
                  + f'<div style="padding:22px {P}px 0">{project_text(p, False)}</div></article>')
    how = (f'<section aria-labelledby="f-how" style="padding:0 {P}px 72px"><h2 id="f-how" style="margin:0 0 10px;{sc(12)}">How I work</h2>'
           f'<p style="margin:0;font-style:italic;font-size:18px;line-height:1.55;color:{SL}">[PLACEHOLDER: one short paragraph, in your words]</p></section>')
    def band(h):
        lis = ''.join(f'<li style="display:flex;flex-direction:column;justify-content:center;gap:4px;height:96px;padding:0 26px;white-space:nowrap">'
                      f'<span class="onum" style="{sc(10)}">{per}</span><span style="display:flex;align-items:center;gap:6px;font-size:18px">{slot(13) if mk else ""}{n}</span></li>' for per, n, mk in TL)
        return f'<ol{AH if h else ""} style="display:flex;margin:0;padding:0;list-style:none">{lis}</ol>'
    hist = (f'<section id="history" aria-labelledby="f-hist" style="margin:0 0 72px;border-top:1px solid {RULE};border-bottom:1px solid {RULE}">'
            f'<h2 id="f-hist" style="margin:0;padding:6px {P}px 0;{sc(11)}">History</h2>' + strip(band, 96, 'ltr') + '</section>')
    minor = (f'<section aria-labelledby="f-minor" style="padding:0 {P}px 72px"><h2 id="f-minor" style="margin:0 0 10px;{sc(12)}">Minor Projects</h2><ol style="list-style:none;margin:0;padding:0">'
             + ''.join(f'<li style="padding:0 0 16px">{leader(strong(n), emp(e, mk), 16)}'
                       f'<p style="margin:3px 0 0;font-size:15px;line-height:1.45">{d} <span style="font-style:italic;color:{SL}">{t}</span></p></li>' for n, e, mk, d, t in MINOR)
             + '</ol></section>')
    close = (f'<footer id="contact" aria-labelledby="f-contact" style="flex-grow:1">' + photo('orchid', 'height:360px')
             + f'<div style="padding:28px {P}px 72px"><h2 id="f-contact" style="margin:0 0 10px;{sc(12)}">Contact</h2>'
             f'<p style="margin:0 0 22px;font-family:{DIDONE};font-size:32px;line-height:1.06">Happy to talk about any of this.</p>'
             f'<p style="margin:0;{sc(11)}">Email</p><button type="button" style="min-height:44px;padding:0;border:0;background:transparent;font:inherit;font-style:italic;font-size:17px;color:{INK};text-align:left;cursor:pointer;text-decoration:underline;text-decoration-color:{CLAY};text-underline-offset:4px">[PLACEHOLDER: email address]</button>'
             f'<p style="margin:12px 0 0;{sc(11)}">LinkedIn</p><a href="{LI_URL}" style="display:inline-flex;align-items:center;min-height:44px;font-style:italic;font-size:15px;overflow-wrap:anywhere">{LI}</a></div></footer>')
    body = '<main style="display:flex;flex-direction:column">' + front + intro + wk + about + qual + projs + how + hist + minor + '</main>' + close
    return page('Portfolio F, phone', 320, 6400, body)

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'canvas/'
    import os; os.makedirs(out, exist_ok=True)
    open(out + 'F-Phone.dc.html', 'w').write(phone())
    open(out + 'F-Desktop.dc.html', 'w').write(desktop())
    print('ok')
