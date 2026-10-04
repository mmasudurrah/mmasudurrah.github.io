#!/usr/bin/env python3
"""Validate the deployable static website using only Python's standard library."""
import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids, self.canonicals, self.robots = [], set(), [], []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                raise ValueError('Duplicate HTML id: ' + attrs['id'])
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs.get('href', ''))
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.robots.append(attrs.get('content', ''))

def validate(root):
    root = root.resolve()
    manifest = json.loads((root / 'site-manifest.json').read_text())
    expected = manifest['files']
    actual = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
    if actual != set(expected) | {'site-manifest.json'}:
        raise ValueError('Unlisted or missing artifact files: ' + str(actual ^ (set(expected) | {'site-manifest.json'})))
    for name, digest in expected.items():
        path = root / name
        if not path.resolve().is_relative_to(root) or path.is_symlink():
            raise ValueError('Unsafe artifact path: ' + name)
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError('Artifact checksum mismatch: ' + name)
    pages = {}
    for path in root.rglob('*.html'):
        text = path.read_text()
        if any(marker in text for marker in ('{{', 'Local design preview', 'TODO: VERIFY', '/Users/')):
            raise ValueError('Unresolved or private build content: ' + str(path))
        page = Page(text)
        if len(page.canonicals) != 1 or any('noindex' in r for r in page.robots):
            raise ValueError('Invalid production metadata: ' + str(path))
        pages[path.resolve()] = page
        if '<main' in text and text.count('src="/analytics.js"') != 1:
            raise ValueError('Missing or duplicate Analytics tag: ' + str(path))
    analytics = (root / 'analytics.js').read_text()
    if not re.fullmatch(r'G-[A-Z0-9]+', manifest['analytics_id']) or manifest['analytics_id'] not in analytics:
        raise ValueError('Google Analytics measurement ID differs from the manifest')
    if "location.hostname !== 'mmasudurrah.github.io'" not in analytics:
        raise ValueError('Local previews must not send Analytics data')
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = (root / unquote(url.path).lstrip('/')) if url.path.startswith('/') else path.parent / unquote(url.path)
            if not url.path:
                target = path
            if target.is_dir():
                target /= 'index.html'
            target = target.resolve()
            if not target.is_relative_to(root) or not target.is_file():
                raise ValueError(f'Broken link in {path.relative_to(root)}: {link}')
            if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                raise ValueError(f'Broken section link in {path.relative_to(root)}: {link}')
    for path in ('index.html', 'research/index.html', 'publications/index.html', 'teaching/index.html', 'cv/index.html', 'news/index.html', '404.html', 'robots.txt', 'sitemap.xml', '.nojekyll', 'assets/pdf/CV_Md_Masudur_Rahman.pdf'):
        if not (root / path).is_file():
            raise ValueError('Missing required production route: ' + path)
    cv_pdf = (root / 'assets/cv.pdf').read_bytes()
    if cv_pdf != (root / 'assets/pdf/CV_Md_Masudur_Rahman.pdf').read_bytes():
        raise ValueError('Legacy CV download differs from the current PDF')
    publication_text = (root / 'publications/index.html').read_text()
    count = publication_text.count('<li>')
    if count != manifest['publication_entries']:
        raise ValueError('Publication count differs from build manifest')
    news = (root / 'news/index.html').read_text()
    if news.count('<time ') != manifest['news_entries']:
        raise ValueError('News count differs from build manifest')
    print(f'PASS: {len(pages)} HTML routes, {len(actual)} public files; local links, fragments, metadata, checksums, CV aliases, {count} publications, {manifest["news_entries"]} news entries.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path, nargs='?', default=Path('site'))
    validate(parser.parse_args().site)
