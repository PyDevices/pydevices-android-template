# SPDX-License-Identifier: MIT
"""python-for-android recipe: eventsys (TestPyPI pure-Python wheel)."""

from pythonforandroid.recipe import PyProjectRecipe


class EventsysRecipe(PyProjectRecipe):
    version = "0.0.39"
    name = "eventsys"
    depends = []
    call_hostpython_via_targetpython = False


recipe = EventsysRecipe()
