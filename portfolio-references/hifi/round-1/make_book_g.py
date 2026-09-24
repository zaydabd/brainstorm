# G · the white book theme on the round-10 layout (hero + glance, worked with, about + quals,
# shelf + notes, how I work, history bar + panel, minor bento, marquee, contact).
import sys
import make_book as mb
from make_book import PAPER, INK, SL, RULE, CLAY, DIDONE, BOOK, B, TAGLINE, LI_URL, LI, AH, sc, leader, mark

mb.LOGO['Maybank'] = ('/_blob/3220e10666d87a2823f6de4bd8b5c52d', 44)  # tiger icon, not the full wordmark
mb.HELMET = mb.HELMET.replace('</style>', '''.cv{transition:transform .45s cubic-bezier(.2,.7,.2,1),box-shadow .45s ease}.cv:hover{transform:translateY(-6px);box-shadow:0 22px 44px rgba(38,32,50,0.14)}
.cv.on{transform:translateY(-12px);box-shadow:0 26px 52px rgba(38,32,50,0.16)}
.duo{background:linear-gradient(135deg,#E3D3D0 0%,#EAF2F8 55%,#C9D3DE 100%)}.duo img{filter:grayscale(1) contrast(1.08) brightness(1.04);mix-blend-mode:multiply;transition:filter .8s ease}.duo:hover img{filter:none}
.tile{transition:border-color .3s ease}.tile:hover{border-top-color:#8E5A4F}
.post{transform:rotate(-2deg);transition:transform .35s ease}.post.b{transform:rotate(1.6deg)}.post:hover{transform:rotate(0)}
.seg:hover .nm{text-decoration:underline;text-decoration-color:#8E5A4F}
.qs{list-style:none}.qs::-webkit-details-marker{display:none}.qs:hover{color:#8E5A4F}
.pb{transition:color .2s}.pb:hover{color:#262032}
.marq{animation:wz-rtl 40s linear infinite}.marq-wrap:hover .marq{animation-play-state:paused}
@media (prefers-reduced-motion:reduce){.marq{animation:none}.cv,.post{transition:none}}
</style>''')

CUR = ' aria-current="true"'
SPINE = ['#8E5A4F', '#373F47', '#262032']
MINOR = {m[0]: m for m in mb.MINOR}

def h2(text, px, id_, counter=None, mb_=16, didone=False):
    c = f'<span class="onum" style="color:{SL};font-style:italic"> ({counter})</span>' if counter else ''
    if didone:
        return f'<h2 id="{id_}" style="margin:0 0 {mb_}px;font-family:{DIDONE};font-weight:400;font-size:{px}px;line-height:1.05">{text}{c}</h2>'
    return f'<h2 id="{id_}" style="margin:0 0 {mb_}px;{sc(13 if px > 12 else 12)}">{text}{c}</h2>'

def pause(label):
    bars = ('<span aria-hidden="true" style="display:inline-flex;gap:3px"><span style="display:block;width:2px;height:10px;background:currentColor"></span>'
            '<span style="display:block;width:2px;height:10px;background:currentColor"></span></span>')
    return (f'<button type="button" class="pb" aria-pressed="false" aria-label="Pause {label}" style="display:inline-flex;align-items:center;gap:10px;min-height:44px;min-width:44px;'
            f'padding:0;border:0;background:transparent;cursor:pointer;font-family:{BOOK};{sc(11, SL)}">{bars}Pause</button>')

def glance(num_px, lab_px, cols=True):
    items = (('5', 'employers'), ('11', 'projects, 3 in detail'), ('5', 'qualifications'))
    return (f'<ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:{20 if cols else 12}px">'
            + ''.join(f'<li style="border-top:1px solid {RULE};padding-top:12px"><span class="onum" style="display:block;font-family:{DIDONE};font-size:{num_px}px;line-height:1">{n}</span>'
                      f'<span style="display:block;margin-top:6px;font-style:italic;font-size:{lab_px}px;line-height:1.35;color:{SL}">{t}</span></li>' for n, t in items)
            + '</ul>')

def quals(px):
    out = ''
    for i, (name, year) in enumerate(mb.QUALS):
        op = ' open="{{ true }}"' if i == 0 else ''
        issuer = 'OutSystems' if 'OutSystems' in name else ('Universiti Teknologi MARA' if 'UiTM' in name else '[PLACEHOLDER: issuer]')
        out += (f'<li style="border-bottom:1px solid {RULE}"><details{op}><summary class="qs" style="display:flex;justify-content:space-between;align-items:center;gap:16px;min-height:44px;padding:8px 0;cursor:pointer;font-size:{px}px;line-height:1.35">'
                f'<span>{name}</span><span aria-hidden="true" style="color:{SL};font-size:18px">{"−" if i == 0 else "+"}</span></summary>'
                f'<p class="onum" style="margin:0 0 12px;font-style:italic;font-size:{px - 2}px;color:{SL}">{issuer}, {year}</p></details></li>')
    return f'<ul style="list-style:none;margin:0;padding:0;border-top:1px solid {RULE}">{out}</ul>'

def cover(i, p, w, h, title_px):
    on = i == 0
    cls = 'cv on' if on else 'cv'
    cur = ' aria-current="true"' if on else ''
    wcss = f'flex:0 0 {w}px;width:{w}px;scroll-snap-align:start;' if w else ''
    return (f'<a class="{cls}" href="#notes"{cur} style="{wcss}position:relative;display:flex;flex-direction:column;justify-content:space-between;height:{h}px;box-sizing:border-box;'
            f'padding:{28 if not w else 20}px {28 if not w else 20}px {24 if not w else 18}px {44 if not w else 34}px;background:#FFFFFF;border:1px solid {RULE};color:{INK};text-decoration:none;'
            f'box-shadow:0 6px 16px rgba(38,32,50,0.06)">'
            f'<span aria-hidden="true" style="position:absolute;left:0;top:0;bottom:0;width:{14 if not w else 10}px;background:{SPINE[i]}"></span>'
            f'<span style="display:block;{sc(11)}">{p["name"]}</span>'
            f'<span style="display:block;font-family:{DIDONE};font-size:{title_px}px;line-height:1.05;letter-spacing:-0.01em">{p["title"]}</span>'
            f'<span style="display:flex;flex-direction:column;gap:6px;border-top:1px solid {RULE};padding-top:12px">'
            f'<span style="display:flex;align-items:center;gap:6px;flex-wrap:wrap;font-style:italic;font-size:{15 if not w else 13}px;color:{SL}">{mb.org(p, 12)}</span>'
            f'<span style="{sc(10, SL, "0.1em")}">{p["credit"]}</span></span></a>')

def notes(wide):
    p = mb.PROJ[0]
    lines = ''.join(f'<p style="margin:0 0 {10 if wide else 8}px;font-size:{19 if wide else 16}px;line-height:1.55"><span style="{sc(12 if wide else 11)};margin-right:10px">{l}</span>{t}</p>' for l, t in p['lines'])
    return (f'<h3 id="izone-h" style="margin:0 0 8px;font-family:{DIDONE};font-weight:400;font-size:{40 if wide else 28}px;line-height:1.05">{p["name"]}</h3>'
            f'<p style="margin:0 0 {24 if wide else 18}px;display:flex;align-items:center;gap:6px;flex-wrap:wrap;font-style:italic;font-size:{18 if wide else 15}px;color:{SL}">{mb.org(p, 13)}</p>'
            + lines + f'<p style="margin:14px 0 0;padding-top:12px;border-top:1px solid {RULE};{sc(11, SL, "0.1em")}">{p["credit"]} · {p["tools"]}</p>')

def tile(name, place, big=False):
    n, e, mk, d, t = MINOR[name]
    stat = (f'<p class="onum" style="margin:0 0 8px;white-space:nowrap;font-family:{DIDONE};font-size:44px;line-height:1;color:{CLAY}">6 h → 30 min</p>' if big else '')
    return (f'<li class="tile" style="{place};border-top:1px solid {RULE};padding-top:16px;display:flex;flex-direction:column;gap:6px">' + stat
            + f'<h3 style="margin:0;font-family:{DIDONE};font-weight:400;font-size:24px;line-height:1.1">{n}</h3>'
            f'<p style="margin:0;font-size:15px;line-height:1.5">{d}</p>'
            f'<p style="margin:auto 0 0;padding-top:6px;display:flex;align-items:center;gap:6px 12px;flex-wrap:wrap;{sc(10, SL, "0.1em")}">'
            f'<span style="display:inline-flex;align-items:center;gap:6px">{mark(e, 14) if mk else ""}{e}</span><span>{t}</span></p></li>')

Z = 'rgba(0,0,0,0)'
ANG = {'left': '90deg', 'right': '270deg', 'up': '180deg', 'down': '0deg'}
def slats(toward, solid=48, start=4, w=9, gap=6, extra=None):
    """Image solid from `solid`% on the far side, breaking into slats toward `toward`, gone by `start`%."""
    a = ANG[toward]
    core = f'linear-gradient({a}, {Z} {solid - 10}%, #000 {solid}%)'
    fade = f'linear-gradient({a}, {Z} {start}%, #000 {solid}%)'
    sl = f'repeating-linear-gradient({a}, #000 0 {w}px, {Z} {w}px {w + gap}px)'
    layers, comp, wk = [core, sl, fade], ['add', 'intersect'], ['source-over', 'source-in']
    if extra:
        layers, comp, wk = [extra] + layers, ['intersect'] + comp, ['source-in'] + wk
    img = ', '.join(layers)
    return f'-webkit-mask-image:{img};mask-image:{img};-webkit-mask-composite:{", ".join(wk)};mask-composite:{", ".join(comp)}'

def slatband(w=7, gap=6):
    """Horizontal slats dissolving at top and bottom (for a wide band)."""
    core = f'linear-gradient(0deg, {Z} 24%, #000 36%, #000 64%, {Z} 76%)'
    fade = f'linear-gradient(0deg, {Z} 2%, #000 36%, #000 64%, {Z} 98%)'
    sl = f'repeating-linear-gradient(0deg, #000 0 {w}px, {Z} {w}px {w + gap}px)'
    img = f'{core}, {sl}, {fade}'
    return f'-webkit-mask-image:{img};mask-image:{img};-webkit-mask-composite:source-over, source-in;mask-composite:add, intersect'

FEATHER = slats('left')
def blend(key, style, mask=FEATHER, pos='50% 50%'):
    return (f'<figure class="duo" aria-hidden="true" style="margin:0;overflow:hidden;{mask};{style}">'
            f'<img src="{B[key]}" alt="" style="display:block;width:100%;height:100%;object-fit:cover;object-position:{pos}"></figure>')

def vblend(style, mask, btn):
    return (f'<div style="{style};{mask}">'
            f'<video ref="{{{{ vref }}}}" src="{B["video"]}" poster="{B["poster"]}" autoPlay="{{{{ true }}}}" muted="{{{{ true }}}}" loop="{{{{ true }}}}" playsInline="{{{{ true }}}}" preload="auto"{AH} '
            f'style="display:block;width:100%;height:100%;object-fit:cover"></video>'
            f'<button type="button" class="vb" onClick="{{{{ toggle }}}}" aria-label="Pause or play the background video" style="position:absolute;{btn};display:inline-flex;align-items:center;min-height:44px;min-width:44px;padding:0 14px;'
            f'border:0;background:rgba(13,11,18,0.45);color:#FCFCFC;cursor:pointer;font-family:{BOOK};{sc(11, "#FCFCFC")}">{{{{ vlabel }}}}</button></div>')

PICDIR = {'orchid': 'down', 'shadows': 'right', 'plants': 'left'}
def pic(key, place, h):
    return (f'<li aria-hidden="true" style="{place};min-height:{h}px;display:flex">'
            + blend(key, 'flex:1;min-height:100%', slats(PICDIR[key], solid=58, start=0, w=6, gap=5)) + '</li>')
    

def postit(place, h, b=False):
    return (f'<li class="{"post b" if b else "post"}" style="{place};align-self:start;box-sizing:border-box;min-height:{h}px;padding:18px;background:#FFFFFF;border:1px solid {RULE};'
            f'box-shadow:0 12px 26px rgba(38,32,50,0.10);display:flex;flex-direction:column;gap:8px">'
            f'<span style="{sc(10)}">Note</span><span style="font-style:italic;font-size:17px;line-height:1.4">[PLACEHOLDER: a short note in your words]</span></li>')

def marquee(px):
    one = f'<span style="padding-right:{px//2}px;white-space:nowrap">Wan Zayd Abdullah</span>'
    return (f'<div class="marq-wrap" aria-hidden="true" style="overflow:hidden;padding:{px//5}px 0;border-top:1px solid {RULE}">'
            + '</div>')  # name text removed by Wan Zayd in the canvas

def contact_links(fs):
    btn = (f'<button type="button" style="min-height:44px;padding:0;border:0;background:transparent;font:inherit;font-style:italic;color:{INK};cursor:pointer;'
           f'text-decoration:underline;text-decoration-color:{CLAY};text-underline-offset:4px">[PLACEHOLDER: email address]</button>')
    return (leader('Email', btn, fs, INK)
            + leader('LinkedIn', f'<a href="{LI_URL}" style="display:inline-flex;align-items:center;min-height:44px;font-style:italic;overflow-wrap:anywhere">{LI}</a>', fs, INK))

# ---------------- desktop ----------------
def desktop():
    G = 'display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;padding:0 80px'
    header = (f'<header style="display:flex;justify-content:space-between;align-items:center;height:72px;padding:0 80px;border-bottom:1px solid {RULE}">'
              f'<a href="#top" style="display:flex;align-items:center;min-height:44px;font-family:{DIDONE};font-size:22px;text-decoration:none">Wan Zayd Abdullah</a>'
              f'<nav aria-label="Sections"><ul style="list-style:none;margin:0;padding:0;display:flex;gap:28px">'
              + ''.join(f'<li><a class="nv" href="#{t}" style="display:flex;align-items:center;min-height:44px;font-style:italic;font-size:19px;color:{SL}">{t}</a></li>' for t in ('work', 'history', 'contact'))
              + '</ul></nav></header>')
    hero = (f'<section aria-labelledby="g-hero" style="position:relative;{G};min-height:820px;align-items:center;margin-bottom:40px">'
            + vblend('position:absolute;top:0;right:0;width:940px;height:820px',
                     slats('left', solid=50, start=2, w=10, gap=7, extra=f'linear-gradient(0deg, {Z} 0%, #000 20%)'), 'right:28px;top:28px')
            + f'<div style="grid-column:1 / span 6;position:relative;display:flex;flex-direction:column;padding:88px 0 96px">'
            f'<h1 id="g-hero" style="margin:0 0 28px;font-family:{DIDONE};font-weight:400;font-size:66px;line-height:1.04;letter-spacing:-0.01em">{TAGLINE}</h1>'
            f'<p class="onum" style="margin:0 0 6px;{sc(12)}">5 years · since Apr 2021</p>'
            f'<p style="margin:0 0 64px;font-style:italic;font-size:28px;color:{SL}">OutSystems Technical Lead</p>'
            f'<h2 class="sr" id="g-glance">At a glance</h2>{glance(48, 16)}</div></section>')
    worked = (f'<section aria-labelledby="g-worked" style="margin:0 80px 120px;border-top:1px solid {RULE};border-bottom:1px solid {RULE}">'
              f'<div style="display:flex;justify-content:space-between;align-items:center">{h2("Worked with", 13, "g-worked", mb_=0)}{pause("Worked with")}</div>'
              + mb.strip(mb.worked(32, 80), 88, 'rtl') + '</section>')
    aq = (f'<div style="{G};padding-bottom:140px;align-items:start">'
          f'<section aria-labelledby="g-about" style="grid-column:1 / span 5">{h2("About", 13, "g-about")}'
          f'<p style="margin:0;font-style:italic;font-size:22px;line-height:1.55;color:{SL}">[PLACEHOLDER: About, three lines in your words. One decision, told before the word OutSystems.]</p></section>'
          f'<section aria-labelledby="g-qual" style="grid-column:7 / span 6">{h2("Qualifications", 13, "g-qual", "5")}{quals(18)}</section></div>')
    projects = (f'<section id="work" aria-labelledby="g-proj" style="padding:0 80px 36px">{h2("Projects", 13, "g-proj", "3")}</section>'
                f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;padding:12px 80px 88px">'
                + ''.join(cover(i, p, None, 540, 40) for i, p in enumerate(mb.PROJ)) + '</div>'
                f'<div style="{G};padding-bottom:140px"><section id="notes" aria-labelledby="izone-h" style="grid-column:3 / span 8">{notes(True)}</section></div>')
    how = (f'<div style="{G};padding-bottom:80px;align-items:center"><section aria-labelledby="g-how" style="grid-column:2 / span 5">{h2("How I work", 13, "g-how")}'
           f'<p style="margin:0;font-style:italic;font-size:22px;line-height:1.55;color:{SL}">[PLACEHOLDER: one short paragraph, in your words]</p></section>'
           + blend('harp', 'grid-column:8 / span 5;height:600px', slats('left', solid=46, start=0, w=8, gap=6)) + '</div>')
    SEG = [('Jan 2026 – present', '9 mos', 9, 'AvePoint', 'Full-stack developer', '↳ Sunway University'),
           ('Sep 2024 – Jan 2026', '1 yr 5 mos', 17, 'Maybank', 'Senior OutSystems Engineer', ''),
           ('Sep 2022 – Sep 2024', '2 yrs 1 mo', 25, 'FPT Software Malaysia', 'Software Consultant', '↳ PETRONAS Digital'),
           ('Apr 2022 – Aug 2022', '5 mos', 5, 'Career break', 'Time for personal goals', ''),
           ('Apr 2021 – May 2022', '1 yr 2 mos', 14, 'Impact Business Solutions', 'Software Consultant', '')]
    segs = ''
    for i, (per, dur, mos, name, role, client) in enumerate(SEG):
        on = i == 0
        top = f'border-top:2px solid {CLAY};padding-top:15px' if on else (f'border-top:1px dashed {SL};padding-top:16px' if name == 'Career break' else f'border-top:1px solid {RULE};padding-top:16px')
        cl = (f'<span style="display:flex;align-items:center;gap:6px;font-style:italic;font-size:15px;color:{SL}">{client[:2]}{mark(client, 14)}{client[2:]}</span>' if client else '')
        extra = (f'<a class="seg" href="#h-panel" style="display:flex;align-items:center;min-height:44px;margin-top:8px;font-style:italic;font-size:14px;color:{SL};text-decoration:underline;text-decoration-style:dotted;text-underline-offset:4px">'
                 '+ Adam Digital Assets, May – Jul 2024, part-time</a>' if name.startswith('FPT') else '')
        segs += (f'<li style="flex:{mos} 1 0;min-width:180px"><a class="seg" href="#h-panel"{CUR if on else ""} style="display:flex;flex-direction:column;gap:5px;min-height:44px;padding-right:16px;{top};color:{INK};text-decoration:none">'
                 f'<span class="onum" style="{sc(10, CLAY if on else SL, "0.1em")}">{per} · {dur}</span>'
                 f'<span class="nm" style="display:flex;align-items:center;gap:8px;font-size:20px">{mark(name, 16)}{name}</span>'
                 f'<span style="font-style:italic;font-size:15px;color:{SL}">{role}</span>{cl}</a>{extra}</li>')
    hist = (blend('street', 'height:440px;margin-bottom:-70px', slatband(), '50% 38%')
            + f'<section id="history" aria-labelledby="g-hist" style="position:relative;padding:0 80px 48px">{h2("History", 13, "g-hist", mb_=24)}'
            f'<ol style="display:flex;gap:10px;list-style:none;margin:0;padding:0;align-items:flex-start">{segs}</ol></section>'
            f'<div style="{G};padding-bottom:140px"><div id="h-panel" style="grid-column:3 / span 8;display:flex;flex-direction:column;gap:8px">'
            f'<p class="onum" style="margin:0;{sc(11)}">Jan 2026 – present, full-time</p>'
            f'<h3 style="margin:0;display:flex;align-items:center;gap:12px;flex-wrap:wrap;font-family:{DIDONE};font-weight:400;font-size:36px;line-height:1.1">{mark("AvePoint", 26)}AvePoint'
            f'<span style="font-family:{BOOK};font-style:italic;font-size:22px;color:{SL}">Full-stack developer</span></h3>'
            f'<p style="margin:0;font-size:18px;line-height:1.55">↳ Sunway University, client. Senior Technical Lead since Apr 2026. Project: <a href="#notes">iZone rebuild ↑</a></p></div></div>')
    def at(c, r, cs=1, rs=1):
        return f'grid-column:{c} / span {cs};grid-row:{r} / span {rs}'
    bento = ''.join([
        tile('CAB-Q', at(1, 1, 1, 2), big=True), tile('VIP Dashboard', at(2, 1)), pic('orchid', at(3, 1), 240), tile('Audit Log', at(4, 1)),
        tile('Tokenizer', at(3, 2)),  # desktop post-its removed by Wan Zayd in the canvas
        tile('QR Asset Management', at(1, 3)), pic('shadows', at(2, 3), 240), pic('plants', at(3, 3, 2), 240),
        tile('MPowered', at(1, 4)), tile('RPSST', at(2, 4)), tile('Adam Digital Assets', at(3, 4, 2))])
    minor = (f'<section aria-labelledby="g-minor" style="padding:0 80px 120px">{h2("Minor Projects", 13, "g-minor", "8", mb_=24)}'
             f'<ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:minmax(200px,auto);column-gap:24px;row-gap:40px">{bento}</ul></section>')
    contact = (f'<footer id="contact" aria-labelledby="g-contact" style="flex-grow:1;position:relative;{G};align-content:start;align-items:center;padding-top:40px;padding-bottom:120px">'
               + blend('orchid', 'position:absolute;right:0;top:0;width:800px;height:780px', slats('left', solid=52, start=6, w=10, gap=7), '50% 60%')
               + f'<div style="grid-column:1 / span 6;position:relative;padding-top:120px">{h2("Contact", 13, "g-contact")}'
               f'<p style="margin:0 0 32px;font-family:{DIDONE};font-size:56px;line-height:1.04">Happy to talk about any of this.</p>{contact_links(20)}</div></footer>')
    body = header + '<main style="display:flex;flex-direction:column">' + hero + worked + aq + projects + how + hist + minor + marquee(150) + '</main>' + contact
    return mb.page('Portfolio G, desktop', 1440, 7000, body)

# ---------------- phone ----------------
def phone():
    P = 20
    header = (f'<header style="padding:6px {P}px 0">'
              f'<a href="#top" style="display:flex;align-items:center;min-height:44px;font-family:{DIDONE};font-size:20px;text-decoration:none">Wan Zayd Abdullah</a>'
              f'<nav aria-label="Sections"><ul style="list-style:none;margin:0;padding:0;display:flex;gap:18px">'
              + ''.join(f'<li><a class="nv" href="#{t}" style="display:flex;align-items:center;min-height:44px;font-style:italic;font-size:17px;color:{SL}">{t}</a></li>' for t in ('work', 'history', 'contact'))
              + '</ul></nav></header>')
    hero = (f'<section aria-labelledby="g-hero">' + vblend('position:relative;height:420px', slats('down', solid=62, start=2, w=6, gap=5), 'right:12px;top:12px') +
            f'<div style="position:relative;margin-top:-72px;padding:0 {P}px 64px"><h1 id="g-hero" style="margin:0 0 16px;font-family:{DIDONE};font-weight:400;font-size:30px;line-height:1.08">{TAGLINE}</h1>'
            f'<p class="onum" style="margin:0 0 4px;{sc(11)}">5 years · since Apr 2021</p>'
            f'<p style="margin:0 0 28px;font-style:italic;font-size:20px;color:{SL}">OutSystems Technical Lead</p>'
            f'<h2 class="sr" id="g-glance">At a glance</h2>{glance(34, 13, False)}</div></section>')
    worked = (f'<section aria-labelledby="g-worked" style="margin:0 0 72px;border-top:1px solid {RULE};border-bottom:1px solid {RULE}">'
              f'<div style="display:flex;justify-content:space-between;align-items:center;padding:0 {P}px">{h2("Worked with", 12, "g-worked", mb_=0)}{pause("Worked with")}</div>'
              + mb.strip(mb.worked(24, 48), 88, 'rtl') + '</section>')
    about = (f'<section aria-labelledby="g-about" style="padding:0 {P}px 64px">{h2("About", 12, "g-about", mb_=10)}'
             f'<p style="margin:0;font-style:italic;font-size:18px;line-height:1.55;color:{SL}">[PLACEHOLDER: About, three lines in your words. One decision, told before the word OutSystems.]</p></section>')
    qual = f'<section aria-labelledby="g-qual" style="padding:0 {P}px 80px">{h2("Qualifications", 12, "g-qual", "5", mb_=10)}{quals(16)}</section>'
    projects = (f'<section id="work" aria-labelledby="g-proj" style="padding:0 {P}px 8px">{h2("Projects", 12, "g-proj", "3", mb_=0)}</section>'
                f'<div style="display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:{P}px;scrollbar-width:none;padding:22px {P}px 40px">'
                + ''.join(cover(i, p, 236, 340, 27) for i, p in enumerate(mb.PROJ)) + '</div>'
                f'<section id="notes" aria-labelledby="izone-h" style="padding:0 {P}px 80px">{notes(False)}</section>')
    how = (f'<section aria-labelledby="g-how" style="padding:0 {P}px 0">{h2("How I work", 12, "g-how", mb_=10)}'
           f'<p style="margin:0;font-style:italic;font-size:18px;line-height:1.55;color:{SL}">[PLACEHOLDER: one short paragraph, in your words]</p></section>'
           + blend('harp', 'height:320px;margin:8px 0 24px', slats('up', solid=40, start=0, w=6, gap=5)))
    def band(h):
        lis = ''.join(f'<li style="display:flex;flex-direction:column;justify-content:center;gap:4px;height:96px;padding:0 26px;white-space:nowrap">'
                      f'<span class="onum" style="{sc(10)}">{per}</span><span style="display:flex;align-items:center;gap:6px;font-size:18px">{mark(n, 16) if mk else ""}{n}</span></li>' for per, n, mk in mb.TL)
        return f'<ol{AH if h else ""} style="display:flex;margin:0;padding:0;list-style:none">{lis}</ol>'
    hist = (blend('street', 'height:260px;margin-bottom:-30px', slatband(5, 4), '50% 38%')
            + f'<section id="history" aria-labelledby="g-hist" style="position:relative;margin:0 0 72px;border-top:1px solid {RULE};border-bottom:1px solid {RULE}">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;padding:0 {P}px">{h2("History", 12, "g-hist", mb_=0)}{pause("History")}</div>'
            + mb.strip(band, 96, 'ltr') + '</section>')
    g, one = 'grid-column:span 2', 'grid-column:span 1'
    bento = ''.join([
        tile('CAB-Q', g, big=True), tile('VIP Dashboard', g), pic('orchid', one, 150), postit(one, 150),
        tile('Audit Log', g), tile('Tokenizer', g), tile('QR Asset Management', g), pic('shadows', one, 150), postit(one, 150, b=True),
        pic('plants', g, 180), tile('Adam Digital Assets', g), tile('MPowered', g), tile('RPSST', g)])
    minor = (f'<section aria-labelledby="g-minor" style="padding:0 {P}px 72px">{h2("Minor Projects", 12, "g-minor", "8", mb_=16)}'
             f'<ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:14px;row-gap:28px">{bento}</ul></section>')
    contact = (f'<footer id="contact" aria-labelledby="g-contact" style="flex-grow:1">'
               + blend('orchid', 'height:340px', slatband(5, 4), '60% 60%')
               + f'<div style="padding:0 {P}px 72px">{h2("Contact", 12, "g-contact", mb_=10)}'
               f'<p style="margin:0 0 22px;font-family:{DIDONE};font-size:32px;line-height:1.06">Happy to talk about any of this.</p>{contact_links(15)}</div></footer>')
    body = header + '<main style="display:flex;flex-direction:column">' + hero + worked + about + qual + projects + how + hist + minor + marquee(72) + '</main>' + contact
    return mb.page('Portfolio G, phone', 320, 6800, body)

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'canvas/'
    open(out + 'G-Phone.dc.html', 'w').write(phone())
    open(out + 'G-Desktop.dc.html', 'w').write(desktop())
    print('ok')
