import os, json
for d, label in [(r'D:\===每日资讯===\AI科技早报\2026年5月', 'AI科技早报'), (r'D:\===每日资讯===\建筑行业日报\2026年5月', '建筑行业日报')]:
    files = [f for f in os.listdir(d) if f.endswith('.docx') and not f.startswith('_')]
    print(f'{label}:')
    for f in files:
        fp = os.path.join(d, f)
        print(f'  {f} ({os.path.getsize(fp)//1024}KB)')
    print()
h = json.load(open(r'D:\===每日资讯===\_history.json', encoding='utf-8'))
print(f'去重历史库：已记录 {len(h["articles"])} 条')
cats = {}
for a in h["articles"]:
    cats[a["category"]] = cats.get(a["category"], 0) + 1
for c, n in sorted(cats.items()):
    print(f'  {c}: {n}条')
