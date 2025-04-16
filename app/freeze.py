from flask_frozen import Freezer
import os
import shutil

from app import app

# -------------------------

freezer = Freezer(app)

dir_templates = os.path.join(os.path.dirname(__file__), 'templates')
dir_build = os.path.join(os.path.dirname(__file__), 'build')
shutil.copy(os.path.join(dir_templates, 'README.md'), os.path.join(dir_build, 'README.md'))

# -------------------------

if __name__ == '__main__':
    freezer.freeze()
