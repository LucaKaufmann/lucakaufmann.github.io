import json
import re
from pathlib import Path


articles_dir = Path("easymqtt/articles")
out_path = Path("easymqtt/articles.json")


def parse_frontmatter(text):
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}, text

    frontmatter = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            frontmatter[key.strip()] = value.strip().strip('"')

    body = text[match.end() :]
    return frontmatter, body


articles = []
for md_file in sorted(articles_dir.glob("*.md"), reverse=True):
    text = md_file.read_text(encoding="utf-8")
    frontmatter, _ = parse_frontmatter(text)
    if not frontmatter.get("title"):
        continue

    articles.append(
        {
            "title": frontmatter.get("title", ""),
            "category": frontmatter.get("category", ""),
            "summary": frontmatter.get("summary", ""),
            "date": frontmatter.get("date", ""),
            "file": f"articles/{md_file.name}",
        }
    )

articles.sort(key=lambda article: article["date"], reverse=True)
out_path.write_text(json.dumps(articles, indent=2, ensure_ascii=False) + "\n")
print(f"Wrote {len(articles)} articles to {out_path}")
