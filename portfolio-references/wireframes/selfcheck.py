import json,re,os,glob
from playwright.sync_api import sync_playwright
C=json.load(open('canvas/project/canvas.json'))
fold={320:568,1440:765}
out={}
with sync_playwright() as pw:
    br=pw.chromium.launch()
    for name in C['order']:
        b=C['boards'][name]; w=b['w']
        s=open('canvas/project/'+name).read()
        view=re.sub(r'<script.*?</script>','',s,flags=re.S).replace('<helmet>','').replace('</helmet>','')
        pg=br.new_page(viewport={'width':w,'height':900}); pg.set_content(view)
        d=pg.evaluate("""(fold)=>{const r=document.querySelector('[data-root]');const top=r.getBoundingClientRect().top;
        const y=e=>Math.round(e.getBoundingClientRect().top-top);
        // chars per line of P1 Problem
        const p1=document.querySelector('[data-block="P1"]'); let cpl=null;
        if(p1){const dd=p1.querySelectorAll('dd')[1]; const lh=parseFloat(getComputedStyle(dd).lineHeight); const lines=Math.round(dd.getBoundingClientRect().height/lh); cpl=Math.round(dd.textContent.length/lines); }
        // targets
        const small=[...document.querySelectorAll('nav a, summary, [data-block="C1"] a, [data-block="H1"] a[href="#top"]')].map(e=>{const b=e.getBoundingClientRect();return {t:e.textContent.slice(0,30),w:Math.round(b.width),h:Math.round(b.height)}}).filter(o=>o.w<44||o.h<44);
        // overflow
        const over=[...r.querySelectorAll('*')].filter(e=>e.getBoundingClientRect().right>r.getBoundingClientRect().right+1).map(e=>e.tagName+':'+e.textContent.slice(0,20));
        // first decision vs first platform name
        const h1=document.querySelector('[data-block="H2"] h1'); const dy=h1?y(h1):null;
        const walker=document.createTreeWalker(r,NodeFilter.SHOW_TEXT); let py=1e9,n; while(n=walker.nextNode()){ if(/OutSystems/.test(n.textContent)){const rg=document.createRange(); rg.selectNodeContents(n); const t=Math.round(rg.getBoundingClientRect().top-top); if(t<py)py=t;}}
        // false floor: is fold inside a block or within 24px gap?
        const blocks=[...document.querySelectorAll('[data-block]')].map(e=>({id:e.dataset.block,y:y(e),b:y(e)+Math.round(e.getBoundingClientRect().height)}));
        const inside=blocks.filter(o=>o.y<fold&&o.b>fold).map(o=>o.id);
        const above=blocks.filter(o=>o.y<fold).length;
        // tools field y of P1
        const tools=p1?[...p1.querySelectorAll('dt')].find(e=>e.textContent=='Tools'):null;
        const dec=p1?[...p1.querySelectorAll('dt')].find(e=>e.textContent=='Decision'):null;
        return {cpl, small, over:over.slice(0,3), decisionY:dy, firstOutSystemsY:py, foldInside:inside, blocksAboveFold:above, p1ToolsY:tools?y(tools):null, p1DecisionY:dec?y(dec):null, h:Math.ceil(r.scrollHeight)}}""", fold[w])
        out[name]=d; pg.close()
    br.close()
for k,v in out.items(): print(k, json.dumps(v))
