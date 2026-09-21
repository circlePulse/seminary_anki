#!/usr/bin/env bash
# Rebuild every deck from source. Run from the repo root.
set -euo pipefail

command -v python3 >/dev/null || { echo "python3 required"; exit 1; }
python3 -c "import genanki" 2>/dev/null || pip install genanki --break-system-packages -q

mkdir -p build

echo "== checking id lockfile =="
python3 skill/scripts/check_ids.py

echo
echo "== building =="
for f in decks/*.json; do
  python3 skill/scripts/generate_deck.py "$f" -o build
done

echo
echo "== regenerating registry =="
python3 skill/scripts/gen_registry.py

echo
echo "Done. .apkg files are in build/ (gitignored)."
echo "Commit any changes to decks/, ids.lock.json and registry/."
