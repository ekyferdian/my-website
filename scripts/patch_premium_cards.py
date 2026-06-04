from pathlib import Path

files = [
    'index.html', 'guide.html', 'article.html', 'faq.html', 'tentang.html',
    'togel.html', 'blackjack.html', 'baccarat.html', 'poker.html', 'roulette.html', 'slots.html'
]
old_block = '<section class="section">\n    <div class="container" id="page-body">\n      <!-- Konten akan dimuat melalui CMS -->\n    </div>\n  </section>'
new_block = '<section class="section">\n    <div class="container">\n      <div class="card premium-card" id="page-body">\n        <!-- Konten akan dimuat melalui CMS -->\n      </div>\n    </div>\n  </section>'

for f in files:
    p = Path('c:/Users/ACEH/Documents/web eky') / f
    if not p.exists():
        print('missing', f)
        continue
    text = p.read_text(encoding='utf-8')
    norm = text.replace('\r\n', '\n')
    if old_block in norm:
        patched = norm.replace(old_block, new_block)
        if '\r\n' in text:
            patched = patched.replace('\n', '\r\n')
        p.write_text(patched, encoding='utf-8')
        print('patched', f)
    else:
        print('not found', f)
