// usage: node render.js out_dir file1.html [file2.html ...]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [outDir, ...files] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1000, height: 1500 }, deviceScaleFactor: 1 });
  for (const f of files) {
    await page.goto('file://' + path.resolve(f));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(150);
    const out = path.join(outDir, path.basename(f).replace(/\.html$/, '.png'));
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: 1000, height: 1500 } });
    // report any element that spills outside the 1080x1350 frame or text overlap candidates
    const issues = await page.evaluate(() => {
      const res = [];
      const root = document.querySelector('[data-root]');
      if (!root) return res;
      const R = root.getBoundingClientRect();
      for (const el of root.querySelectorAll('[data-chk]')) {
        const b = el.getBoundingClientRect();
        if (b.right > R.right + 0.5 || b.bottom > R.bottom + 0.5 || b.left < R.left - 0.5 || b.top < R.top - 0.5)
          res.push('OUTSIDE ' + el.dataset.chk + ' ' + JSON.stringify([b.left, b.top, b.right, b.bottom].map(Math.round)));
        if (el.scrollWidth > el.clientWidth + 1) res.push('HOVERFLOW ' + el.dataset.chk);
      }
      const els = [...root.querySelectorAll('[data-chk]')];
      for (let i = 0; i < els.length; i++) for (let j = i + 1; j < els.length; j++) {
        if (els[i].contains(els[j]) || els[j].contains(els[i])) continue;
        const a = els[i].getBoundingClientRect(), b = els[j].getBoundingClientRect();
        const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left);
        const oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
        if (ox > 1 && oy > 1) res.push('OVERLAP ' + els[i].dataset.chk + ' x ' + els[j].dataset.chk);
      }
      return res;
    });
    console.log(path.basename(f), issues.length ? issues.join(' | ') : 'ok');
  }
  await browser.close();
})();
