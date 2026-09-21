"""
Pinned Anki notetype and deck IDs.

DO NOT generate these at runtime. DO NOT call random.randrange().
A fresh model ID on every run is what produces Basic+, Basic++, Basic+++...

BEFORE FIRST USE — adopt, don't invent:
  1. Anki -> Tools -> Manage Note Types. List what already exists.
  2. Consolidate suffixed duplicates onto one type per role (Change Notetype),
     checking field mapping each time. Delete the emptied types.
  3. Replace the IDs below with the SURVIVING ids from your collection.
     (Manage Note Types -> select -> the id is shown in the window title on
     some versions; otherwise export one note as .apkg and read it, or just
     keep these and accept that year-one notes stay on their old types.)

Changing an ID after notes exist strands those notes on the old notetype
forever. Changing NAMES, CSS, or TEMPLATES under a stable ID is safe and is
how a styling fix reaches every existing card at once.
Adding or removing FIELDS under a live ID is not safe from a script — do that
in the Anki UI first, then mirror it here.
"""

MODEL_BASIC = 1607392319
MODEL_BIDIR = 1607392320
MODEL_CLOZE = 1607392321

# Everything generates into one staging deck and is sorted by hand in Anki.
# Deck IDs are deliberately not a registry.
STAGING_DECK_ID = 1607392330
STAGING_DECK_NAME = "Seminary::_Inbox"

# Names are prefixed so they can never collide with Anki's stock notetypes.
NAME_BASIC = "Seminary Basic"
NAME_BIDIR = "Seminary Bidirectional"
NAME_CLOZE = "Seminary Cloze"
