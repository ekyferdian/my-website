from pathlib import Path
import json
import re

BASE = Path('c:/Users/ACEH/Documents/web eky/content/articles')
output_path = BASE / 'index.json'
article_files = sorted(p for p in BASE.glob('*.md'))

articles = []
for file_path in article_files:
    text = file_path.read_text(encoding='utf-8')
    match = re.match(r'^---\s*\n(.*?\n)---\s*\n(.*)$', text, re.S)
    metadata = {}
    body = ''
    if match:
        frontmatter, body = match.groups()
        for line in frontmatter.strip().splitlines():
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
    title = metadata.get('title', file_path.stem)
    summary = metadata.get('description', '').strip()
    if not summary:
        summary = body.strip().splitlines()[0] if body.strip() else ''
    articles.append({
        'title': title,
        'summary': summary,
        'url': f'article-detail.html?file={file_path.name}'
    })

output_data = {'articles': articles}
output_path.write_text(json.dumps(output_data, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'Wrote {output_path} with {len(articles)} articles.')