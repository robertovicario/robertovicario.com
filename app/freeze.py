from flask_frozen import Freezer
import os
import shutil

from app import app

# -------------------------

freezer = Freezer(app)

# -------------------------

if __name__ == '__main__':
    freezer.freeze()
