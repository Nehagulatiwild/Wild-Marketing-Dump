"""Render an issue to PDF (and PNG pages) with Playwright.
Usage: python3 tools/render.py issues/02.html out_dir
Writes out_dir/issue.pdf and out_dir/pNN.png, and prints any page that overflows.
Copy out_dir/issue.pdf to issues/NN.pdf before committing."""
import sys, os, asyncio
from playwright.async_api import async_playwright
async def main(issue, out):
    os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        await pg.goto('file://' + os.path.abspath(issue))
        await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(600)
        over = await pg.evaluate('''[...document.querySelectorAll('.sheet')].map((s,i)=>{const r=s.getBoundingClientRect();let o=[];s.querySelectorAll('*').forEach(e=>{const x=e.getBoundingClientRect();if(x.bottom>r.bottom+1||x.right>r.right+1)o.push(e.className||e.tagName)});return {page:i+1,overflow:[...new Set(o)].slice(0,5)}}).filter(x=>x.overflow.length)''')
        print('OVERFLOW:', over or 'none')
        for i, s in enumerate(await pg.query_selector_all('.sheet'), 1):
            await s.screenshot(path=f'{out}/p{i:02d}.png')
        await pg.pdf(path=f'{out}/issue.pdf', width='1080px', height='1350px', print_background=True, margin={'top':'0','bottom':'0','left':'0','right':'0'})
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2]))
