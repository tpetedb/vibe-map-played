"""Record one build result in repair.json.

Run it while the build is broken, repair the build, run it again: the file
then holds a failing run followed by a passing one, which is the evidence
`vibe check --fork repair` looks for. Nothing else writes this file.

    python3 tools/record_build.py
"""

from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = ROOT / "repair.json"
VERSION = 1


def main() -> int:
    out = subprocess.run(
        [sys.executable, "tools/build.py"], cwd=ROOT, capture_output=True, text=True
    )
    ok = out.returncode == 0
    data = {"version": VERSION, "runs": []}
    if MARKER.exists():
        data = json.loads(MARKER.read_text(encoding="utf-8"))
        if data.get("version") != VERSION:
            raise SystemExit(
                f"repair.json version {data.get('version')} is not {VERSION}"
            )
    error = (out.stderr or out.stdout).strip().splitlines()
    data["runs"].append(
        {
            "at": dt.datetime.now().isoformat(timespec="seconds"),
            "ok": ok,
            "error": "" if ok else error[-1][:200] if error else "no output",
        }
    )
    MARKER.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    said = "build passed" if ok else "build failed"
    print(f"{said}, {len(data['runs'])} run(s) recorded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
