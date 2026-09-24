# Option B: "Day", palette v4 (black and white lead, ice supports, clay only as accent).
# Round-10 placement kept; no containers: space, hairlines and type do the grouping.
import json
_src = open('make_hifi.py').read()
exec(_src.split('# ---------------- shared pieces ----------------')[0])  # content + fonts only

SNOW, INK, SLATE, IGREY = '#FCFCFC', '#262032', '#373F47', '#82909D'
ICE, FROST, CLAY, OX, FCLAY = '#C9D3DE', '#EAF2F8', '#8E5A4F', '#4A2E2E', '#E3D3D0'

def LB(px=12, color=SLATE):
    return f'font-size:{px}px;line-height:1.4;letter-spacing:0.08em;text-transform:uppercase;font-weight:500;color:{color}'

def slot(px):
    return (f'<span aria-hidden="true" style="display:inline-block;flex-shrink:0;width:{px}px;height:{px}px;'
            f'box-sizing:border-box;border:1px dashed {IGREY}"></span>')

def fill(bg, extra=''):
    return f'<span aria-hidden="true" style="position:absolute;inset:0;pointer-events:none;background:{bg}{extra}"></span>'

def rays_on_ice(at, a=0.6, blur=5):
    m = f'radial-gradient(100% 90% at {at}, #000 10%, rgba(0,0,0,0) 75%)'
    return fill(f'repeating-conic-gradient(from 90deg at {at}, rgba(252,252,252,{a}) 0deg 1.3deg, rgba(252,252,252,0) 1.3deg 6.5deg)',
                f';filter:blur({blur}px);-webkit-mask-image:{m};mask-image:{m}')

DAWN = 'radial-gradient(110% 70% at 50% 0%, rgba(227,211,208,0.95), rgba(227,211,208,0) 65%), linear-gradient(180deg, #EAF2F8 0%, #C9D3DE 100%)'
DUSK_ART = 'radial-gradient(90% 60% at 50% 0%, rgba(142,90,79,0.6), rgba(142,90,79,0) 70%), linear-gradient(180deg, #373F47 0%, #262032 100%)'
ICEFIELD = 'linear-gradient(180deg, #C9D3DE 0%, #EAF2F8 100%)'

HELMET = '''<helmet>
<style>
body{margin:0;background:#FCFCFC;color:#262032;font-family:-apple-system,"Segoe UI",system-ui,sans-serif}
a{color:#8E5A4F;text-decoration-thickness:1px;text-underline-offset:4px}a:hover{color:#4A2E2E}
::selection{background:#E3D3D0;color:#262032}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid #8E5A4F;outline-offset:4px}
h1,h2,h3{text-wrap:balance}p,dd{text-wrap:pretty}
.num{font-variant-numeric:lining-nums tabular-nums}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.nv{transition:color .2s ease}.nv:hover{color:#8E5A4F}
.wk{transition:color .4s ease}.wk:hover{color:#262032}
.pz .art{transition:transform .5s cubic-bezier(.2,.7,.2,1)}.pz:hover .art{transform:translateY(-6px)}
.ix{transition:border-color .3s ease}.ix:hover{border-top-color:#8E5A4F}
.post{transform:rotate(-2deg);transition:transform .35s ease}.post.b{transform:rotate(1.6deg)}.post:hover{transform:rotate(0)}
.seg{transition:color .2s ease}.seg:hover{color:#8E5A4F}
.qs{list-style:none}.qs::-webkit-details-marker{display:none}.qs:hover{color:#8E5A4F}
.tb{transition:color .2s ease}.tb:hover{color:#8E5A4F}
@keyframes wz-rtl{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@keyframes wz-ltr{from{transform:translateX(-50%)}to{transform:translateX(0)}}
.drift-rtl{animation:wz-rtl 70s linear infinite}
.drift-ltr{animation:wz-ltr 80s linear infinite}
.marq{animation:wz-rtl 36s linear infinite}
.strip:hover .drift-rtl,.strip:hover .drift-ltr,.strip:focus-within .drift-rtl,.strip:focus-within .drift-ltr,.marq-wrap:hover .marq{animation-play-state:paused}
@media (prefers-reduced-motion:reduce){.drift-rtl,.drift-ltr,.marq{animation:none}.strip{overflow-x:auto}.pz .art,.post,.ix,.seg,.wk,.nv,.tb{transition:none}}
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
<div id="top" style="width:{w}px;height:{h}px;box-sizing:border-box;overflow:hidden;display:flex;flex-direction:column;background:{SNOW};color:{INK};font-family:{SANS};-webkit-font-smoothing:antialiased">
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

def h2(text, px, counter=None, id_=None, mb=16):
    c = f'<span class="num" style="color:{IGREY};font-weight:400"> ({counter})</span>' if counter else ''
    return f'<h2 id="{id_}" style="margin:0 0 {mb}px;font-size:{px}px;line-height:1.05;font-weight:500;letter-spacing:-0.035em;color:{INK}">{text}{c}</h2>'

def pause(label):
    bars = ('<span aria-hidden="true" style="display:inline-flex;gap:3px"><span style="display:block;width:2px;height:10px;background:currentColor"></span>'
            '<span style="display:block;width:2px;height:10px;background:currentColor"></span></span>')
    return (f'<button type="button" class="tb" aria-pressed="false" aria-label="Pause {label}" style="display:inline-flex;align-items:center;gap:10px;min-height:44px;min-width:44px;'
            f'padding:0;background:transparent;border:0;font-family:{SANS};{LB(12)};cursor:pointer">{bars}Pause</button>')

def towrite(text, px, lh=1.45):
    return (f'<p style="margin:0 0 10px;{LB(11)}">To write</p>'
            f'<p style="margin:0;font-family:{SERIF};font-style:italic;font-size:{px}px;line-height:{lh};color:{SLATE}">{text}</p>')

def worked_strip(px, gap, mk):
    def items(hidden):
        lis = ''.join(f'<li class="wk" style="display:flex;align-items:center;gap:12px;font-size:{px}px;font-weight:500;letter-spacing:-0.03em;color:{IGREY};white-space:nowrap">'
                      + (slot(mk) if m else '') + f'{n}</li>' for n, m in WORKED)
        ah = ' aria-hidden="true"' if hidden else ''
        return f'<ul{ah} style="display:flex;align-items:center;gap:{gap}px;margin:0;padding:0 {gap//2}px;list-style:none">{lis}</ul>'
    m = 'linear-gradient(90deg, rgba(0,0,0,0), #000 8%, #000 92%, rgba(0,0,0,0))'
    return (f'<div class="strip" style="overflow:hidden;height:88px;-webkit-mask-image:{m};mask-image:{m}">'
            f'<div class="drift-rtl" style="display:flex;width:max-content;height:88px;align-items:center">' + items(False) + items(True) + '</div></div>')

def quals(px):
    out = []
    for i, (name, d1, d2) in enumerate(QUALS):
        op = ' open="{{ true }}"' if i == 0 else ''
        d2s = f'<span style="font-style:italic;color:{SLATE}">{d2}</span>' if d2 else ''
        out.append(f'<li style="border-bottom:1px solid {ICE}"><details{op}>'
                   f'<summary class="qs" style="display:flex;justify-content:space-between;align-items:center;gap:20px;min-height:44px;padding:12px 0;cursor:pointer;font-size:{px}px;line-height:1.35;color:{INK}">'
                   f'<span>{name}</span><span aria-hidden="true" style="color:{SLATE};font-size:18px;font-weight:300;line-height:1">{"−" if i == 0 else "+"}</span></summary>'
                   f'<p style="margin:0 0 16px;font-size:15px;line-height:1.55;color:{SLATE}">{d1}{d2s}</p></details></li>')
    return f'<ul style="list-style:none;margin:0;padding:0;border-top:1px solid {ICE}">' + ''.join(out) + '</ul>'

ARTS = [(DAWN, INK, ''), (DUSK_ART, FROST, ''), (ICEFIELD, INK, 'rays')]
def project(i, p, art_h, title_px, name_px, credit_px, width=None):
    title, name, credit, tools, _ = p
    bg, tcol, extra = ARTS[i]
    on = i == 0
    art = fill(bg) + (rays_on_ice('50% -8%') if extra == 'rays' else '')
    rule = f'border-top:2px solid {CLAY};padding-top:15px' if on else f'border-top:1px solid {ICE};padding-top:16px'
    cur = ' aria-current="true"' if on else ''
    wcss = f'flex:0 0 {width}px;width:{width}px;scroll-snap-align:start;' if width else ''
    return (f'<a class="pz" href="#notes"{cur} style="{wcss}display:flex;flex-direction:column;gap:22px;color:{INK};text-decoration:none">'
            f'<span class="art" style="position:relative;display:flex;align-items:flex-end;height:{art_h}px;box-sizing:border-box;padding:{28 if not width else 20}px;overflow:hidden">'
            + art + f'<span style="position:relative;display:block;font-size:{title_px}px;line-height:1.02;font-weight:500;letter-spacing:-0.045em;color:{tcol};text-wrap:balance">{title}</span></span>'
            f'<span style="display:flex;flex-direction:column;gap:6px;{rule}">'
            f'<span style="font-family:{SERIF};font-style:italic;font-size:{name_px}px;line-height:1.2;color:{INK}">{name}</span>'
            f'<span style="font-size:{credit_px}px;line-height:1.45;color:{SLATE}">{credit}</span>'
            f'<span style="display:flex;align-items:center;gap:8px;margin-top:6px;{LB(11)}">{slot(13)}{tools}</span></span></a>')

def notes(wide):
    rows = []
    for lab, val in NOTES:
        if val is None:
            val = f'<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">{slot(15)}{IZTOOLS}</span>'
        if wide:
            rows.append(f'<div style="display:grid;grid-template-columns:200px minmax(0,1fr);column-gap:24px;border-top:1px solid {ICE};padding:20px 0 22px">'
                        f'<dt style="{LB(12)};padding-top:5px">{lab}</dt>'
                        f'<dd style="margin:0;max-width:50ch;font-size:18px;line-height:1.7;color:{INK}">{val}</dd></div>')
        else:
            rows.append(f'<div style="border-top:1px solid {ICE};padding:16px 0 18px"><dt style="{LB(11)}">{lab}</dt>'
                        f'<dd style="margin:8px 0 0;font-size:16px;line-height:1.65;color:{INK}">{val}</dd></div>')
    return (f'<h3 id="izone-h" style="margin:0;font-size:{44 if wide else 28}px;line-height:1.05;font-weight:500;letter-spacing:-0.035em">iZone rebuild</h3>'
            f'<p style="margin:10px 0 {36 if wide else 24}px;display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-family:{SERIF};font-style:italic;font-size:{19 if wide else 17}px;color:{SLATE}">Sunway University, via {slot(15)}AvePoint</p>'
            f'<dl style="margin:0;border-bottom:1px solid {ICE}">' + ''.join(rows) + '</dl>')

def tl_strip():
    def items(hidden):
        lis = []
        for period, name, mk, role, client in TL:
            role_html = role + ((slot(13) + client) if client else '')
            lis.append(f'<li style="display:flex;flex-direction:column;justify-content:center;gap:4px;height:96px;box-sizing:border-box;padding:0 30px;white-space:nowrap">'
                       f'<span class="num" style="{LB(11)}">{period}</span>'
                       f'<span style="display:flex;align-items:center;gap:8px;font-size:17px;font-weight:500;letter-spacing:-0.015em;color:{INK}">' + (slot(15) if mk else '') + f'{name}</span>'
                       f'<span style="display:flex;align-items:center;gap:6px;font-size:13px;color:{SLATE}">{role_html}</span></li>')
        ah = ' aria-hidden="true"' if hidden else ''
        return f'<ol{ah} style="display:flex;margin:0;padding:0;list-style:none">' + ''.join(lis) + '</ol>'
    m = 'linear-gradient(90deg, rgba(0,0,0,0), #000 10%, #000 90%, rgba(0,0,0,0))'
    return (f'<div class="strip" style="overflow:hidden;height:96px;border-top:1px solid {ICE};border-bottom:1px solid {ICE};-webkit-mask-image:{m};mask-image:{m}">'
            f'<div class="drift-ltr" style="display:flex;width:max-content;height:96px">' + items(False) + items(True) + '</div></div>')

def meta(parts):
    bits = ''.join(f'<span style="display:inline-flex;align-items:center;gap:6px">' + (slot(11) if mk else '') + f'{t}</span>' for t, mk in parts)
    return f'<p style="margin:6px 0 0;display:flex;align-items:center;gap:6px 14px;flex-wrap:wrap;{LB(11)}">{bits}</p>'

def item(name, place, big=False, big_px=44):
    desc, parts = MINOR[name]
    stat = (f'<p class="num" style="margin:4px 0 10px;white-space:nowrap;font-size:{big_px}px;line-height:1;font-weight:500;letter-spacing:-0.045em;color:{CLAY}">6 h → 30 min</p>' if big else '')
    return (f'<li class="ix" style="{place};border-top:1px solid {ICE};padding-top:18px;display:flex;flex-direction:column;gap:8px">'
            + stat + f'<h3 style="margin:0;font-size:21px;line-height:1.2;font-weight:500;letter-spacing:-0.02em;color:{INK}">{name}</h3>'
            f'<p style="margin:0;max-width:34ch;font-size:15px;line-height:1.6;color:{SLATE}">{desc}</p>' + meta(parts) + '</li>')

def pic(label, place, h, bg, cap=SLATE, extra=''):
    return (f'<li style="{place};position:relative;overflow:hidden;min-height:{h}px;display:flex;align-items:flex-end;padding:16px;box-sizing:border-box">'
            + fill(bg) + (rays_on_ice('80% -10%', 0.55, 4) if extra == 'rays' else '')
            + f'<span style="position:relative;{LB(11, cap)}">{label}</span></li>')

def postit(place, h, b=False):
    return (f'<li class="{"post b" if b else "post"}" style="{place};align-self:start;box-sizing:border-box;min-height:{h}px;padding:18px;background:{FCLAY};color:{INK};'
            f'box-shadow:0 1px 2px rgba(38,32,50,0.06),0 12px 28px rgba(38,32,50,0.08);display:flex;flex-direction:column;gap:10px">'
            f'<span style="{LB(10, OX)}">Post-it</span>'
            f'<span style="font-family:{SERIF};font-style:italic;font-size:17px;line-height:1.35">[PLACEHOLDER: a short note in your words]</span></li>')

def marquee(px):
    one = f'<span style="padding-right:{px//2}px;white-space:nowrap">Wan Zayd Abdullah</span>'
    return (f'<div class="marq-wrap" aria-hidden="true" style="overflow:hidden;padding:{px//4}px 0">'
            f'<div class="marq" style="display:flex;width:max-content;font-size:{px}px;line-height:1;font-weight:500;letter-spacing:-0.055em;color:{ICE}">' + one * 4 + '</div></div>')

def contact_links(wide):
    fs = 24 if wide else 18
    link = f'display:flex;flex-direction:column;align-items:flex-start;gap:6px;min-height:44px;padding:0;background:transparent;border:0;font-family:{SANS};text-align:left;cursor:pointer'
    val = f'font-size:{fs}px;line-height:1.3;letter-spacing:-0.01em;color:{INK};text-decoration:underline;text-decoration-color:{CLAY};text-decoration-thickness:1px;text-underline-offset:6px;overflow-wrap:anywhere'
    return (f'<ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:{"row" if wide else "column"};gap:{64 if wide else 24}px">'
            f'<li><button type="button" class="tb" style="{link}"><span style="{LB(11)}">Email</span><span style="{val}">[PLACEHOLDER: email address]</span></button></li>'
            f'<li><a class="tb" href="https://www.linkedin.com/in/wan-zayd-abdullah-690033230" style="{link};text-decoration:none"><span style="{LB(11)}">LinkedIn</span><span style="{val}">{LINKEDIN}</span></a></li></ul>')

HERO_LIGHT = fill('radial-gradient(55% 90% at 92% 0%, rgba(201,211,222,0.6), rgba(252,252,252,0) 70%), radial-gradient(35% 55% at 74% 0%, rgba(227,211,208,0.6), rgba(252,252,252,0) 70%)')
HERO_LIGHT_PH = fill('radial-gradient(90% 60% at 100% 0%, rgba(201,211,222,0.65), rgba(252,252,252,0) 70%), radial-gradient(70% 40% at 60% 0%, rgba(227,211,208,0.55), rgba(252,252,252,0) 70%)')

# ---------------- phone B, 320 ----------------
def phone():
    P = 20
    header = (f'<header style="padding:14px {P}px 0">'
              f'<a href="#top" style="display:flex;align-items:center;min-height:44px;color:{INK};text-decoration:none;font-size:15px;font-weight:500;letter-spacing:-0.01em">Wan Zayd Abdullah</a>'
              f'<nav aria-label="Sections"><ul style="list-style:none;margin:0;padding:0;display:flex;gap:6px">'
              + ''.join(f'<li><a class="nv" href="#{t}" style="display:flex;align-items:center;min-height:44px;min-width:44px;padding-right:10px;font-family:{SERIF};font-style:italic;font-size:18px;color:{SLATE};text-decoration:none">{t}</a></li>' for t in ('work', 'history', 'contact'))
              + '</ul></nav></header>')
    hero = (f'<section aria-labelledby="hero-h" style="position:relative;overflow:hidden;padding:52px {P}px 64px">' + HERO_LIGHT_PH +
            f'<div style="position:relative">'
            f'<h1 id="hero-h" style="margin:0;font-size:34px;line-height:1.04;font-weight:500;letter-spacing:-0.045em;color:{INK}">{TAGLINE}</h1>'
            f'<p class="num" style="margin:28px 0 8px;{LB(11)}">5 years · since Apr 2021</p>'
            f'<p style="margin:0;font-family:{SERIF};font-style:italic;font-size:24px;line-height:1.2;color:{OX}">OutSystems Technical Lead</p>'
            '</div></section>')
    glance = (f'<section aria-labelledby="glance-h" style="padding:0 {P}px 88px"><h2 id="glance-h" class="sr">At a glance</h2>'
              f'<ul style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;list-style:none;margin:0;padding:0">'
              + ''.join(f'<li style="border-top:1px solid {ICE};padding-top:14px"><span class="num" style="display:block;font-size:38px;line-height:1;font-weight:500;letter-spacing:-0.05em;color:{INK}">{n}</span>'
                        f'<span style="display:block;margin-top:8px;font-size:13px;line-height:1.35;color:{SLATE}">{t}</span></li>'
                        for n, t in (('5', 'employers'), ('11', 'projects, 3 in detail'), ('5', 'qualifications')))
              + '</ul></section>')
    worked = (f'<section aria-labelledby="worked-h" style="padding:0 0 88px">'
              f'<div style="display:flex;justify-content:space-between;align-items:center;padding:0 {P}px 12px">{h2("Worked with", 22, id_="worked-h", mb=0)}{pause("Worked with")}</div>'
              + worked_strip(26, 48, 20) + '</section>')
    about = f'<section aria-labelledby="about-h" style="padding:0 {P}px 88px">{h2("About", 22, id_="about-h", mb=18)}' + towrite(
        '[PLACEHOLDER: About, in your words. Who you are, with the title. One decision, told before the word OutSystems. Your interest in front-end and design.]', 19) + '</section>'
    qual = f'<section aria-labelledby="qual-h" style="padding:0 {P}px 104px">{h2("Qualifications", 22, "5", "qual-h", mb=18)}' + quals(16) + '</section>'
    projhead = (f'<section id="work" aria-labelledby="proj-h" style="padding:0 {P}px 32px">{h2("Projects", 44, "3", "proj-h", mb=14)}'
                f'<p style="margin:0;font-size:17px;line-height:1.55;color:{SLATE}">Three projects, each with what was wrong, what we chose and what it cost.</p></section>')
    shelf = (f'<div style="display:flex;gap:20px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:{P}px;scrollbar-width:none;padding:6px {P}px 64px">'
             + ''.join(project(i, p, 300, 27, 20, 14, width=236) for i, p in enumerate(POSTERS)) + '</div>')
    notes_s = f'<section id="notes" aria-labelledby="izone-h" style="padding:0 {P}px 104px">' + notes(False) + '</section>'
    how = f'<section aria-labelledby="how-h" style="padding:0 {P}px 104px">{h2("How I work", 22, id_="how-h", mb=18)}' + towrite(
        '[PLACEHOLDER: one short paragraph, in your words, on architecture calls and running a team.]', 19) + '</section>'
    hist = (f'<section id="history" aria-labelledby="hist-h" style="padding:0 0 104px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;padding:0 {P}px 12px">{h2("History", 22, id_="hist-h", mb=0)}{pause("History")}</div>'
            + tl_strip() + '</section>')
    g, one = 'grid-column:span 2', 'grid-column:span 1'
    bento = ''.join([
        item('CAB-Q', g, big=True, big_px=46), item('VIP Dashboard', g),
        pic('Picture: map motif, Sarawak data', one, 150, DAWN), postit(one, 150),
        item('Audit Log', g), item('Tokenizer', g), item('QR Asset Management', g),
        pic('Picture: QR-pattern motif', one, 150, ICEFIELD, extra='rays'), postit(one, 150, b=True),
        pic('Picture: mosque-signage motif', g, 170, DUSK_ART, cap=FROST), item('Adam Digital Assets', g),
        item('MPowered', g), item('RPSST', g)])
    minor = (f'<section aria-labelledby="minor-h" style="padding:0 {P}px 96px">{h2("Minor Projects", 22, "8", "minor-h", mb=24)}'
             f'<ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:14px;row-gap:36px">{bento}</ul></section>')
    contact = (f'<footer id="contact" aria-labelledby="contact-h" style="flex-grow:1;position:relative;overflow:hidden;padding:24px {P}px 80px">'
               + fill('radial-gradient(90% 40% at 100% 100%, rgba(227,211,208,0.55), rgba(252,252,252,0) 70%)') +
               f'<div style="position:relative"><h2 id="contact-h" style="margin:0 0 14px;{LB(11)}">Contact</h2>'
               f'<p style="margin:0 0 32px;font-size:32px;line-height:1.08;font-weight:500;letter-spacing:-0.04em;color:{INK}">Happy to talk about any of this.</p>'
               + contact_links(False) + '</div></footer>')
    main = '<main style="display:flex;flex-direction:column">' + hero + glance + worked + about + qual + projhead + shelf + notes_s + how + hist + minor + marquee(88) + '</main>'
    return page('Portfolio B, phone', 320, 7400, header + main + contact)

# ---------------- desktop B, 1440 ----------------
def desktop():
    M = 80
    GRID = 'display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px'
    header = (f'<header style="display:flex;justify-content:space-between;align-items:center;height:80px;box-sizing:border-box;padding:0 {M}px">'
              f'<a href="#top" style="display:flex;align-items:center;min-height:44px;color:{INK};text-decoration:none;font-size:16px;font-weight:500;letter-spacing:-0.01em">Wan Zayd Abdullah</a>'
              f'<nav aria-label="Sections"><ul style="list-style:none;margin:0;padding:0;display:flex;gap:32px">'
              + ''.join(f'<li><a class="nv" href="#{t}" style="display:flex;align-items:center;min-height:44px;min-width:44px;font-family:{SERIF};font-style:italic;font-size:20px;color:{SLATE};text-decoration:none">{t}</a></li>' for t in ('work', 'history', 'contact'))
              + '</ul></nav></header>')
    glance = (f'<section aria-labelledby="glance-h" style="grid-column:10 / span 3;position:relative;align-self:end"><h2 id="glance-h" class="sr">At a glance</h2>'
              f'<ul style="list-style:none;margin:0;padding:0">'
              + ''.join(f'<li style="display:flex;align-items:baseline;gap:18px;border-top:1px solid {ICE};padding:16px 0">'
                        f'<span class="num" style="flex:0 0 72px;font-size:52px;line-height:1;font-weight:500;letter-spacing:-0.05em;color:{INK}">{n}</span>'
                        f'<span style="font-size:15px;line-height:1.4;color:{SLATE}">{t}</span></li>'
                        for n, t in (('5', 'employers'), ('11', 'projects, 3 in detail'), ('5', 'qualifications')))
              + '</ul></section>')
    hero = (f'<div style="position:relative;overflow:hidden;{GRID};padding:96px {M}px 144px">' + HERO_LIGHT +
            f'<section aria-labelledby="hero-h" style="grid-column:1 / span 8;position:relative">'
            f'<h1 id="hero-h" style="margin:0;font-size:68px;line-height:1.0;font-weight:500;letter-spacing:-0.05em;color:{INK}">{TAGLINE}</h1>'
            f'<p class="num" style="margin:40px 0 10px;{LB(12)}">5 years · since Apr 2021</p>'
            f'<p style="margin:0;font-family:{SERIF};font-style:italic;font-size:34px;line-height:1.2;color:{OX}">OutSystems Technical Lead</p>'
            '</section>' + glance + '</div>')
    worked = (f'<section aria-labelledby="worked-h" style="padding:0 0 144px">'
              f'<div style="display:flex;justify-content:space-between;align-items:center;padding:0 {M}px 8px">{h2("Worked with", 24, id_="worked-h", mb=0)}{pause("Worked with")}</div>'
              + worked_strip(40, 88, 28) + '</section>')
    aq = (f'<div style="{GRID};padding:0 {M}px 160px;align-items:start">'
          f'<section aria-labelledby="about-h" style="grid-column:1 / span 5">{h2("About", 32, id_="about-h", mb=24)}'
          + towrite('[PLACEHOLDER: About, in your words. Who you are, with the title. One decision, told before the word OutSystems. Your interest in front-end and design.]', 24, 1.4)
          + f'</section><section aria-labelledby="qual-h" style="grid-column:7 / span 6">{h2("Qualifications", 32, "5", "qual-h", mb=24)}' + quals(17) + '</section></div>')
    projhead = (f'<section id="work" aria-labelledby="proj-h" style="padding:0 {M}px 48px">{h2("Projects", 88, "3", "proj-h", mb=20)}'
                f'<p style="margin:0;max-width:44ch;font-size:21px;line-height:1.5;color:{SLATE}">Three projects, each with what was wrong, what we chose and what it cost.</p></section>')
    shelf = (f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;padding:0 {M}px 144px">'
             + ''.join(project(i, p, 480, 42, 24, 16) for i, p in enumerate(POSTERS)) + '</div>')
    notes_s = (f'<div style="{GRID};padding:0 {M}px 160px"><section id="notes" aria-labelledby="izone-h" style="grid-column:3 / span 8">' + notes(True) + '</section></div>')
    how = (f'<div style="{GRID};padding:0 {M}px 160px"><section aria-labelledby="how-h" style="grid-column:3 / span 8">{h2("How I work", 32, id_="how-h", mb=24)}'
           + towrite('[PLACEHOLDER: one short paragraph, in your words, on architecture calls and running a team.]', 24, 1.4) + '</section></div>')
    segs = []
    for i, (period, dur, mos, name, mk, role, client) in enumerate(SEG):
        on = i == 0
        brk = name == 'Career break'
        top = f'border-top:3px solid {CLAY};padding-top:17px' if on else (f'border-top:1px dashed {IGREY};padding-top:19px' if brk else f'border-top:1px solid {ICE};padding-top:19px')
        cur = ' aria-current="true"' if on else ''
        cl = ''
        if client == 'PETRONAS':
            cl = f'<span style="display:flex;align-items:center;gap:6px;font-size:14px;color:{SLATE}">↳ {slot(13)}PETRONAS Digital</span>'
        elif client:
            cl = f'<span style="font-size:14px;color:{SLATE}">{client}</span>'
        link = (f'<a class="seg" href="#h-panel"{cur} style="display:flex;flex-direction:column;gap:6px;min-height:44px;padding-right:16px;{top};color:{INK};text-decoration:none">'
                f'<span class="num" style="{LB(11, CLAY if on else SLATE)}">{period} · {dur}</span>'
                f'<span style="display:flex;align-items:center;gap:8px;font-size:19px;font-weight:500;letter-spacing:-0.02em;color:{SLATE if brk else INK}">' + (slot(15) if mk else '') + f'{name}</span>'
                f'<span style="font-size:15px;color:{SLATE}">{role}</span>{cl}</a>')
        extra = ''
        if name.startswith('FPT'):
            extra = (f'<a class="seg" href="#h-panel" style="display:flex;align-items:center;min-height:44px;margin-top:10px;color:{SLATE};font-size:14px;text-decoration:underline;text-decoration-style:dotted;text-underline-offset:4px">'
                     '+ Adam Digital Assets, May – Jul 2024, 3 mos, part-time</a>')
        segs.append(f'<li style="flex:{mos} 1 0;min-width:176px">{link}{extra}</li>')
    hist = (f'<section id="history" aria-labelledby="hist-h" style="padding:0 {M}px 56px">{h2("History", 32, id_="hist-h", mb=32)}'
            f'<ol style="display:flex;gap:8px;list-style:none;margin:0;padding:0;align-items:flex-start">' + ''.join(segs) + '</ol></section>')
    panel = (f'<div style="{GRID};padding:0 {M}px 160px"><div id="h-panel" style="grid-column:3 / span 8;display:flex;flex-direction:column;gap:12px">'
             f'<p class="num" style="margin:0;{LB(12, CLAY)}">Jan 2026 – present, full-time</p>'
             f'<h3 style="margin:0;display:flex;align-items:center;gap:12px;flex-wrap:wrap;font-size:36px;line-height:1.1;font-weight:500;letter-spacing:-0.035em">{slot(24)}AvePoint'
             f'<span style="font-family:{SERIF};font-style:italic;font-weight:400;font-size:26px;letter-spacing:0;color:{SLATE}">Full-stack developer</span></h3>'
             f'<p style="margin:4px 0 0;font-size:17px;line-height:1.65;color:{SLATE}">↳ Sunway University, client. Apr 2026 – present. Senior Technical Lead.</p>'
             f'<p style="margin:12px 0 0;display:flex;align-items:baseline;gap:14px;font-size:17px;line-height:1.65"><span style="flex:0 0 200px;{LB(11)}">Project in this period</span><a href="#notes">iZone rebuild ↑</a></p>'
             f'<p style="margin:0;display:flex;align-items:baseline;gap:14px;font-size:17px;line-height:1.65;color:{INK}"><span style="flex:0 0 200px;{LB(11)}">Tools</span>'
             f'<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">{slot(15)}{IZTOOLS}</span></p>'
             '</div></div>')
    def at(c, r, cs=1, rs=1):
        return f'grid-column:{c} / span {cs};grid-row:{r} / span {rs}'
    bento = ''.join([
        item('CAB-Q', at(1, 1, 1, 2), big=True, big_px=46), item('VIP Dashboard', at(2, 1)),
        pic('Picture: map motif, Sarawak data', at(3, 1), 240, DAWN), item('Audit Log', at(4, 1)),
        postit(at(2, 2), 200), item('Tokenizer', at(3, 2)), postit(at(4, 2), 200, b=True),
        item('QR Asset Management', at(1, 3)), pic('Picture: QR-pattern motif', at(2, 3), 240, ICEFIELD, extra='rays'),
        pic('Picture: mosque-signage motif', at(3, 3, 2), 240, DUSK_ART, cap=FROST),
        item('MPowered', at(1, 4)), item('RPSST', at(2, 4)), item('Adam Digital Assets', at(3, 4, 2))])
    minor = (f'<section aria-labelledby="minor-h" style="padding:0 {M}px 120px">{h2("Minor Projects", 32, "8", "minor-h", mb=36)}'
             f'<ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));column-gap:24px;row-gap:56px">{bento}</ul></section>')
    contact = (f'<footer id="contact" aria-labelledby="contact-h" style="flex-grow:1;position:relative;overflow:hidden;{GRID};align-content:start;padding:56px {M}px 144px">'
               + fill('radial-gradient(45% 60% at 100% 100%, rgba(227,211,208,0.6), rgba(252,252,252,0) 70%), radial-gradient(35% 50% at 82% 100%, rgba(201,211,222,0.55), rgba(252,252,252,0) 70%)') +
               f'<div style="grid-column:1 / span 9;position:relative"><h2 id="contact-h" style="margin:0 0 20px;{LB(12)}">Contact</h2>'
               f'<p style="margin:0 0 48px;font-size:72px;line-height:1.0;font-weight:500;letter-spacing:-0.05em;color:{INK}">Happy to talk about any of this.</p>'
               + contact_links(True) + '</div></footer>')
    main = '<main style="display:flex;flex-direction:column">' + hero + worked + aq + projhead + shelf + notes_s + how + hist + panel + minor + marquee(200) + '</main>'
    return page('Portfolio B, desktop', 1440, 7000, header + main + contact)

open('canvas/B-Phone.dc.html', 'w').write(phone())
open('canvas/B-Desktop.dc.html', 'w').write(desktop())

c = json.load(open('canvas/canvas.json'))
X = 1840 + 320
c['boards']['B-Phone.dc.html'] = {"x": X, "y": 0, "w": 320, "h": 7400, "title": "B · Phone 320"}
c['boards']['B-Desktop.dc.html'] = {"x": X + 400, "y": 0, "w": 1440, "h": 7000, "title": "B · Desktop 1440"}
c['order'] += ['B-Phone.dc.html', 'B-Desktop.dc.html']
c['notes']['t1']['text'] = 'A · Night light (palette v5)'
c['notes']['t2'] = {"x": X, "y": -300, "text": "B · Day, no containers (palette v4)", "kind": "title1", "maxW": 1840}
json.dump(c, open('canvas/canvas.json', 'w'), indent=1)
print('ok')
