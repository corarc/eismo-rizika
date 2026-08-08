import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).parent.parent
RAW_509 = PROJECT_ROOT / "data" / "raw" / "509"

MIN_YEAR = 2013


def max_year() -> int:
    """Latest year covered by the ei_*.json snapshots in data/raw/509."""
    years = [int(p.stem.split("_")[1]) for p in RAW_509.glob("ei_*.json")]
    return max(years) if years else MIN_YEAR
