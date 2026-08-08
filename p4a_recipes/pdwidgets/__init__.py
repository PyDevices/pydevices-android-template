# SPDX-License-Identifier: MIT
"""python-for-android recipe: pdwidgets (TestPyPI pure-Python wheel)."""

from pythonforandroid.recipe import PyProjectRecipe


class PdwidgetsRecipe(PyProjectRecipe):
    # Pin so hostpython pip does not reuse a stale wheel from cache.
    version = "0.0.14"
    name = "pdwidgets"
    depends = ["palettes"]
    call_hostpython_via_targetpython = False


recipe = PdwidgetsRecipe()
