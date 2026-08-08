# SPDX-License-Identifier: MIT
"""python-for-android recipe: displaysys (TestPyPI pure-Python wheel).

Pin the published floor so hostpython pip does not reuse a stale cached wheel
when ``version = None`` resolves against a warm cache.
"""

from pythonforandroid.recipe import PyProjectRecipe


class DisplaysysRecipe(PyProjectRecipe):
    version = "0.0.39"
    name = "displaysys"
    depends = []
    call_hostpython_via_targetpython = False


recipe = DisplaysysRecipe()
