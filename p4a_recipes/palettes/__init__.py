# SPDX-License-Identifier: MIT
"""python-for-android recipe: palettes (TestPyPI pure-Python wheel)."""

from pythonforandroid.recipe import PyProjectRecipe


class PalettesRecipe(PyProjectRecipe):
    version = None
    name = "palettes"
    depends = []
    call_hostpython_via_targetpython = False


recipe = PalettesRecipe()
