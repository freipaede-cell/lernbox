"""Generate simple SVG-based PNG icons for Lernbox PWA"""
import subprocess, os

svg_192 = '''<svg xmlns="http://www.w3.org/2000/svg" width="192" height="192" viewBox="0 0 192 192">
  <rect width="192" height="192" rx="40" fill="#0f172a"/>
  <rect x="16" y="16" width="160" height="160" rx="30" fill="#1e293b"/>
  <rect x="36" y="50" width="120" height="85" rx="12" fill="#38bdf8" opacity="0.9"/>
  <rect x="44" y="58" width="104" height="69" rx="8" fill="#0f172a"/>
  <text x="96" y="100" text-anchor="middle" font-family="system-ui,sans-serif" font-size="28" font-weight="700" fill="#38bdf8">LB</text>
  <rect x="56" y="135" width="80" height="8" rx="4" fill="#4ade80" opacity="0.8"/>
  <rect x="56" y="148" width="50" height="6" rx="3" fill="#38bdf8" opacity="0.4"/>
</svg>'''

svg_512 = '''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="100" fill="#0f172a"/>
  <rect x="40" y="40" width="432" height="432" rx="80" fill="#1e293b"/>
  <rect x="96" y="130" width="320" height="230" rx="24" fill="#38bdf8" opacity="0.9"/>
  <rect x="116" y="150" width="280" height="190" rx="16" fill="#0f172a"/>
  <text x="256" y="265" text-anchor="middle" font-family="system-ui,sans-serif" font-size="72" font-weight="700" fill="#38bdf8">LB</text>
  <rect x="146" y="360" width="220" height="20" rx="10" fill="#4ade80" opacity="0.8"/>
  <rect x="146" y="395" width="140" height="14" rx="7" fill="#38bdf8" opacity="0.4"/>
</svg>'''

icons_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(icons_dir, 'icon-192.svg'), 'w') as f:
    f.write(svg_192)
with open(os.path.join(icons_dir, 'icon-512.svg'), 'w') as f:
    f.write(svg_512)

# Try to convert to PNG using sips (macOS built-in)
for size in [192, 512]:
    svg_path = os.path.join(icons_dir, f'icon-{size}.svg')
    png_path = os.path.join(icons_dir, f'icon-{size}.png')
    # Use python to create a simple PNG via macOS
    try:
        subprocess.run(['qlmanage', '-t', '-s', str(size), '-o', icons_dir, svg_path], 
                      capture_output=True, timeout=10)
        ql_output = os.path.join(icons_dir, f'icon-{size}.svg.png')
        if os.path.exists(ql_output):
            os.rename(ql_output, png_path)
            print(f"Created {png_path}")
        else:
            print(f"qlmanage failed for {size}, keeping SVG")
    except Exception as e:
        print(f"Error for {size}: {e}")

