import json,re,sys
from playwright.sync_api import sync_playwright
DIR=sys.argv[1]
C=json.load(open(DIR+'/project/canvas.json'))
fold={320:568,1440:765}
JS="""(fold)=>{const r=document.querySelector('[data-root]');const top=r.getBoundingClientRect().top;
const y=e=>Math.round(e.getBoundingClientRect().top-top);
const vis=e=>{const b=e.getBoundingClientRect();return b.width>0&&b.height>0};
const h1=document.querySelector('h1'); const decisionY=h1?y(h1):null;
let py=1e9; const w=document.createTreeWalker(r,NodeFilter.SHOW_TEXT); let n;
while(n=w.nextNode()){ if(/OutSystems/.test(n.textContent)&&n.parentElement&&vis(n.parentElement)){const g=document.createRange();g.selectNodeContents(n);const t=Math.round(g.getBoundingClientRect().top-top); if(t<py)py=t;}}
const proj='[data-block="SB1"],[data-block="AD1"],[data-block="PS"],[data-block="PSD1"],[data-block^="RF1"],[data-block="RCar"],[data-block^="RP1"],[data-block^="PF1"],[data-block^="IPF1"],[data-block^="RC1"],[data-block^="P1"],[data-block^="FP1"],[data-block="GI"],[data-block="HT1"],[data-block^="IL"],[data-block^="IP1"],[data-block="JP1"],[data-block^="LP1"]';
const pd=[...document.querySelectorAll(proj)].filter(vis);
let decY=1e9; for(const b of pd){ for(const e of b.querySelectorAll('dt,th,h3,li,summary,p')){ if(/Decision|Row locking/.test(e.textContent)&&vis(e)){decY=Math.min(decY,y(e));break;} } }
let toolsY=1e9; for(const b of pd){ for(const e of b.querySelectorAll('span')){ if(e.textContent.trim()=='Mark · OutSystems'&&vis(e)){toolsY=Math.min(toolsY,y(e));break;} } }
let cpl=null; const dt=[...document.querySelectorAll('dt')].find(e=>e.textContent=='Problem'&&vis(e));
if(dt){const dd=dt.nextElementSibling;const lh=parseFloat(getComputedStyle(dd).lineHeight);cpl=Math.round(dd.textContent.length/Math.round(dd.getBoundingClientRect().height/lh));}
else{const td=[...document.querySelectorAll('th')].find(e=>e.textContent=='Problem');if(td){const c=td.nextElementSibling;const lh=parseFloat(getComputedStyle(c).lineHeight)||24;cpl=Math.round(c.textContent.length/Math.round((c.getBoundingClientRect().height-16)/lh));}}
const small=[...document.querySelectorAll('nav a, summary, [data-block="HB"] a, [data-block="PS"] a, [data-block^="C1"] a, [data-block^="IL"] a, [data-block^="IP"] > a')].filter(vis).map(e=>{const b=e.getBoundingClientRect();return {t:e.textContent.slice(0,24),w:Math.round(b.width),h:Math.round(b.height)}}).filter(o=>o.w<44||o.h<44);
const R=r.getBoundingClientRect().right;
const over=[...r.querySelectorAll('*')].filter(e=>!e.closest('[style*="overflow-x:auto"]')&&e.getBoundingClientRect().right>R+1).map(e=>e.tagName+':'+e.textContent.slice(0,20));
const blocks=[...document.querySelectorAll('[data-block]')].map(e=>({id:e.dataset.block,y:y(e),b:y(e)+Math.round(e.getBoundingClientRect().height)}));
return {decisionY, firstOutSystemsY:py, firstProjDecisionY:decY, firstToolsY:toolsY, cpl, small, over:over.slice(0,3),
  foldInside:blocks.filter(o=>o.y<fold&&o.b>fold).map(o=>o.id), blocksAboveFold:blocks.filter(o=>o.y<fold).length, h:Math.ceil(r.scrollHeight)}}"""
with sync_playwright() as pw:
    br=pw.chromium.launch()
    for name in C['order']:
        b=C['boards'][name]; w=b['w']
        s=open(DIR+'/project/'+name).read()
        view=re.sub(r'<script.*?</script>','',s,flags=re.S).replace('<helmet>','').replace('</helmet>','')
        pg=br.new_page(viewport={'width':w,'height':900}); pg.set_content(view)
        print(b['title'].split(' · ')[0], w, json.dumps(pg.evaluate(JS, fold[w])))
        pg.close()
    br.close()
