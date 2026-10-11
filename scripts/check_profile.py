from pathlib import Path
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
readme = (root / "README.md").read_text(encoding="utf-8")
placeholders = re.compile(r"\[(?:your[^\]]*|project name|tech\s*\d*|repository url|username[^\]]*)\]|your-domain", re.I)
if placeholders.search(readme):
    raise SystemExit("README contém placeholders de template")
if "assets/profile-banner.svg" not in readme:
    raise SystemExit("README não referencia o banner local")
ET.parse(root / "assets/profile-banner.svg")
print("README sem placeholders e banner SVG válido")
