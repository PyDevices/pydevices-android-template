# SPDX-License-Identifier: MIT
"""python-for-android recipe: pydisplay-desktop (TestPyPI; ships usdl2.py)."""

from pythonforandroid.recipe import PyProjectRecipe


class PydisplayDesktopRecipe(PyProjectRecipe):
    version = "0.0.12"
    name = "pydisplay-desktop"
    depends = ["sdl2", "displaydev"]
    call_hostpython_via_targetpython = False


recipe = PydisplayDesktopRecipe()
