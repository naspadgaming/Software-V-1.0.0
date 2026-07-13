from pathlib import Path



# ==================================================
# Icon Directory
# ==================================================

ICON_DIR = Path(
    __file__
).parent / "icons"



# ==================================================
# Get Icon Path
# ==================================================

def icon_path(name):


    path = ICON_DIR / name



    if path.exists():

        return str(path)



    return ""