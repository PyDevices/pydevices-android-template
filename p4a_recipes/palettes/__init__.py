# SPDX-License-Identifier: MIT
"""python-for-android recipe: palettes (TestPyPI pure-Python wheel).

Pin ``0.0.7``: PyPI also has an unrelated ``palettes`` 1.0.2 ("Random Hex Color
Codes"). With only ``--extra-index-url`` indexes, pip prefers that higher
version and the APK gets dist-info without our package. ``==0.0.7`` resolves
from TestPyPI.
"""

from pythonforandroid.recipe import PyProjectRecipe


class PalettesRecipe(PyProjectRecipe):
    version = "0.0.7"
    name = "palettes"
    depends = []
    call_hostpython_via_targetpython = False


recipe = PalettesRecipe()
