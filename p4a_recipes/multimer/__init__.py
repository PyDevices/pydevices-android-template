# SPDX-License-Identifier: MIT
"""python-for-android recipe: multimer (TestPyPI pure-Python wheel)."""

from pythonforandroid.recipe import PyProjectRecipe


class MultimerRecipe(PyProjectRecipe):
    version = None
    name = "multimer"
    depends = ["pydisplay-desktop"]
    call_hostpython_via_targetpython = False


recipe = MultimerRecipe()
