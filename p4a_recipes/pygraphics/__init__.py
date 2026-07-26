# SPDX-License-Identifier: MIT
"""python-for-android recipe: pygraphics-cmod (TestPyPI native Android wheel)."""

from pythonforandroid.recipe import PyProjectRecipe


class PygraphicsRecipe(PyProjectRecipe):
    # buildozer requirement name is "pygraphics"; pip installs pygraphics-cmod.
    version = None
    name = "pygraphics"
    depends = []
    call_hostpython_via_targetpython = False

    def get_pip_name(self):
        return "pygraphics-cmod"


recipe = PygraphicsRecipe()
