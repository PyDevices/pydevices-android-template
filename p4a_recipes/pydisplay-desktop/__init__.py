# SPDX-License-Identifier: MIT
"""python-for-android recipe: pydisplay-desktop (TestPyPI; ships usdl2.py)."""

from pythonforandroid.recipe import PyProjectRecipe


class PydisplayDesktopRecipe(PyProjectRecipe):
    version = None
    name = "pydisplay-desktop"
    depends = ["sdl2", "displaysys"]
    call_hostpython_via_targetpython = False


recipe = PydisplayDesktopRecipe()
