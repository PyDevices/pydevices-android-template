# SPDX-License-Identifier: MIT
"""python-for-android recipe: pdwidgets (TestPyPI pure-Python wheel)."""

from pythonforandroid.recipe import PyProjectRecipe


class PdwidgetsRecipe(PyProjectRecipe):
    version = None
    name = "pdwidgets"
    depends = ["palettes"]
    call_hostpython_via_targetpython = False


recipe = PdwidgetsRecipe()
