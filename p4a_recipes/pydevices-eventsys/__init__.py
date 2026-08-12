# SPDX-License-Identifier: MIT
"""python-for-android recipe: pydevices-eventsys (import eventsys)."""

from pythonforandroid.recipe import PyProjectRecipe


class EventsysRecipe(PyProjectRecipe):
    version = "0.0.16"
    name = "pydevices-eventsys"
    depends = ["pydevices-events", "pydevices-keys", "pydevices-multimer"]
    call_hostpython_via_targetpython = False


recipe = EventsysRecipe()
