#!/usr/bin/env python3
"""Confere os links dos arquivos .md do repositório.

Uso:
    python scripts/check_links.py            # confere tudo (precisa de internet)
    python scripts/check_links.py --offline  # só links locais, âncoras e IDs de vídeo

O que é conferido:
  - links relativos (arquivo existe) e âncoras (#titulo) em arquivos .md;
  - se a thumbnail de um vídeo aponta para o mesmo ID do link do vídeo;
  - (online) se cada vídeo do YouTube existe, usando o endpoint público oEmbed;
  - (online) se os demais links externos respondem.

Erros (código de saída 1): arquivo ou âncora inexistente, thumbnail com ID diferente do vídeo,
vídeo do YouTube não encontrado. Avisos: sites que bloqueiam robôs, falhas de rede, vídeos com
incorporação desativada. Avisos não reprovam, mas vale abrir o link no navegador.
"""
import argparse
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {'.git', 'node_modules', '.venv', 'venv'}
SKIP_PREFIXES = ('../../issues', '../../pulls', '../../discussions', '../../actions')
UA = 'Mozilla/5.0 (compatible; learn-asklipe-link-check)'

LINK_RE = re.compile(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
HTML_RE = re.compile(r'(?:src|href)="([^"]+)"')
FENCE_RE = re.compile(r'```.*?```', re.S)
INLINE_CODE_RE = re.compile(r'`[^`\n]*`')
THUMB_RE = re.compile(r'\[!\[[^\]]*\]\(https://img\.youtube\.com/vi/([\w-]+)/[^)]*\)\]\(https://www\.youtube\.com/watch\?v=([\w-]+)[^)]*\)')
YT_WATCH_RE = re.compile(r'https://www\.youtube\.com/watch\?v=([\w-]+)')


def strip_code(text: str) -> str:
    return INLINE_CODE_RE.sub('', FENCE_RE.sub('', text))


def slug(heading: str) -> str:
    """Aproxima o slug de âncora do GitHub."""
    s = re.sub(r'[^\w\- ]', '', heading.strip().lower())
    return s.replace(' ', '-')


def anchors(path: Path, cache={}) -> set:
    if path not in cache:
        text = FENCE_RE.sub('', path.read_text(encoding='utf-8'))
        found, seen = set(), {}
        for m in re.finditer(r'^#{1,6}\s+(.+?)\s*#*\s*$', text, re.M):
            base = slug(re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', m.group(1)))
            n = seen.get(base, 0)
            found.add(base if n == 0 else f'{base}-{n}')
            seen[base] = n + 1
        cache[path] = found
    return cache[path]


def fetch(url: str, method: str = 'GET'):
    req = urllib.request.Request(url, method=method, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=12) as r:
        return r.status


def check_youtube(video_id: str):
    url = f'https://www.youtube.com/watch?v={video_id}'
    oembed = 'https://www.youtube.com/oembed?format=json&url=' + urllib.parse.quote(url, safe='')
    try:
        fetch(oembed)
        return 'ok', ''
    except urllib.error.HTTPError as e:
        if e.code in (404, 400):
            return 'erro', 'vídeo não encontrado'
        if e.code in (401, 403):
            return 'aviso', 'o vídeo existe, mas não permite incorporação ou está restrito'
        return 'aviso', f'HTTP {e.code}'
    except Exception as e:  # rede, DNS, timeout
        return 'aviso', f'sem resposta ({type(e).__name__})'


def check_external(url: str):
    try:
        try:
            fetch(url, 'HEAD')
        except urllib.error.HTTPError as e:
            if e.code in (403, 405, 501):
                fetch(url, 'GET')
            else:
                raise
        return 'ok', ''
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 429):
            return 'aviso', f'HTTP {e.code} (o site pode bloquear robôs)'
        return 'erro', f'HTTP {e.code}'
    except Exception as e:
        return 'aviso', f'sem resposta ({type(e).__name__})'


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--offline', action='store_true', help='não acessa a internet')
    args = ap.parse_args()

    errors, warnings = [], []
    external, videos = {}, {}
    md_files = [p for p in ROOT.rglob('*.md') if not (set(p.relative_to(ROOT).parts) & SKIP_DIRS)]

    for md in sorted(md_files):
        raw = md.read_text(encoding='utf-8')
        where = md.relative_to(ROOT)

        for thumb_id, link_id in THUMB_RE.findall(raw):
            if thumb_id != link_id:
                errors.append(f'{where}: thumbnail ({thumb_id}) e link ({link_id}) apontam para vídeos diferentes')

        text = strip_code(raw)
        targets = LINK_RE.findall(text) + HTML_RE.findall(text)
        for target in targets:
            if target.startswith(('mailto:', 'tel:', 'data:')):
                continue
            if target.startswith(('http://', 'https://')):
                m = YT_WATCH_RE.match(target)
                if m:
                    videos.setdefault(m.group(1), []).append(str(where))
                else:
                    external.setdefault(target, []).append(str(where))
                continue
            if target.startswith(SKIP_PREFIXES):
                continue
            path_part, _, frag = target.partition('#')
            path_part = urllib.parse.unquote(path_part.split('?')[0])
            dest = md if not path_part else (md.parent / path_part).resolve()
            if not dest.exists():
                errors.append(f'{where}: arquivo não encontrado -> {target}')
                continue
            if frag and dest.suffix == '.md' and dest.is_file():
                if urllib.parse.unquote(frag).lower() not in anchors(dest):
                    errors.append(f'{where}: âncora não encontrada -> {target}')

    if not args.offline:
        print(f'Conferindo {len(videos)} vídeos e {len(external)} links externos...')
        for vid, files in sorted(videos.items()):
            status, msg = check_youtube(vid)
            if status != 'ok':
                (errors if status == 'erro' else warnings).append(f'{files[0]}: vídeo {vid}: {msg}')
        for url, files in sorted(external.items()):
            status, msg = check_external(url)
            if status != 'ok':
                (errors if status == 'erro' else warnings).append(f'{files[0]}: {url}: {msg}')

    for w in warnings:
        print(f'AVISO  {w}')
    for e in errors:
        print(f'ERRO   {e}')
    print(f'\n{len(md_files)} arquivos .md · {len(errors)} erro(s) · {len(warnings)} aviso(s)'
          + (' · modo offline' if args.offline else ''))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
