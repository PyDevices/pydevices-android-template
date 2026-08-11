# SPDX-License-Identifier: MIT
"""python-for-android recipe: displaydev (TestPyPI pure-Python wheel).

Pin the published floor so hostpython pip does not reuse a stale cached wheel
when ``version = None`` resolves against a warm cache.
"""

from pythonforandroid.recipe import PyProjectRecipe


class DisplaydevRecipe(PyProjectRecipe):
    version = "0.0.39"
    name = "displaydev"
    depends = []
    call_hostpython_via_targetpython = False


recipe = DisplaydevRecipe()
