#!/usr/bin/env bash
# Default: check ids, report what each deck would deliver, regenerate the registry.
#   ./build.sh             — report only; writes no packages
#   ./build.sh --full      — also build complete decks into build/ (fresh collection / recovery)
# To deliver a deck:        python3 skill/scripts/generate_deck.py decks/X.json --delta
set -euo pipefail
python3 -c "import genanki" 2>/dev/null || pip install genanki --break-system-packages -q
mkdir -p build
echo "== id check ==";            python3 skill/scripts/check_ids.py
echo; echo "== pending deliveries (new or changed since last delivered) =="
for f in decks/*.json; do python3 skill/scripts/generate_deck.py "$f" --delta --dry-run | sed -n 1p; done
if [[ "${1:-}" == "--full" ]]; then
  echo; echo "== full builds =="
  for f in decks/*.json; do python3 skill/scripts/generate_deck.py "$f" -o build | sed -n 1p; done
fi
echo; echo "== registry ==";           python3 skill/scripts/gen_registry.py
