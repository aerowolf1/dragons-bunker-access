"""Publish only the manual list; requires no Discord or VRChat credentials."""
import json
import time
from pathlib import Path

def parse_names(text):
    names = []
    for line in text.splitlines():
        name = line.strip()
        if not name or name.startswith('#'):
            continue
        if len(name) > 128 or any(ord(c) < 32 for c in name):
            raise ValueError('Invalid display name')
        if name.startswith('usr_') or '://vrchat.com/' in name:
            raise ValueError('Use a display name, not a user ID or profile URL')
        if name not in names:
            names.append(name)
    if len(names) > 256:
        raise ValueError('Maximum 256 admins')
    return names

def main():
    root = Path(__file__).resolve().parent
    names = parse_names((root / 'admins.txt').read_text(encoding='utf-8-sig'))
    data = {'schemaVersion': 1,
            'fileTimeUtc': time.time_ns() // 100 + 116444736000000000,
            'adminDisplayNames': names}
    output = root / '_site'
    output.mkdir(exist_ok=True)
    (output / 'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (output / 'index.html').write_text('<!doctype html><title>Dragons Bunker access</title><p>Admin roster published.</p>', encoding='utf-8')
    print(f'Validated {len(names)} admin entries.')

if __name__ == '__main__':
    main()
