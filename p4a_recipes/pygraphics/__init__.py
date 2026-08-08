# SPDX-License-Identifier: MIT
"""python-for-android recipe: pygraphics (TestPyPI native Android wheel)."""

from pythonforandroid.recipe import PyProjectRecipe


class PygraphicsRecipe(PyProjectRecipe):
    version = None
    name = "pygraphics"
    depends = []
    call_hostpython_via_targetpython = False


recipe = PygraphicsRecipe()
