import base64
from pathlib import Path

root = Path(__file__).resolve().parent
png_files = [
    root / 'Screenshot 2026-09-01 232606.png',
    root / 'Screenshot 2026-09-01 232630.png',
]

svg_lines = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="260" viewBox="0 0 900 260" role="img" aria-label="GitHub achievements">',
    '  <rect width="900" height="260" rx="24" fill="#0d1117"/>',
]

for index, png in enumerate(png_files):
    encoded = base64.b64encode(png.read_bytes()).decode('ascii')
    x = 180 + (index * 360)
    svg_lines.append(
        f'  <image href="data:image/png;base64,{encoded}" x="{x}" y="20" width="220" height="220" preserveAspectRatio="xMidYMid meet"/>'
    )

svg_lines.append('</svg>')
svg_content = '\n'.join(svg_lines)

for filename in ['metrics.achievements.svg']:
    output = root / filename
    output.write_text(svg_content, encoding='utf-8')
    print(f'Created: {output}')
