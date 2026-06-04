from pathlib import Path
import json

BASE = Path('c:/Users/ACEH/Documents/web eky/content/guides')
output_path = Path('c:/Users/ACEH/Documents/web eky/content/pages/guides.json')
guide_files = sorted(p for p in BASE.glob('*.json'))

guides = []
for file_path in guide_files:
    data = json.loads(file_path.read_text(encoding='utf-8'))
    guides.append({
        'title': data.get('title', file_path.stem),
        'summary': data.get('summary', '').strip(),
        'url': data.get('url', '#')
    })

output_data = {'guides': guides}
output_path.write_text(json.dumps(output_data, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'Wrote {output_path} with {len(guides)} guide items.')
