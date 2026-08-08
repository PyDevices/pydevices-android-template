# SPDX-License-Identifier: MIT
# p4a SDL2 bootstrap requires this filename.
"""Bootstrap: Android env, path layout, then staged run_entry or LVGL launcher."""

import importlib
import os
import sys

try:
    import utils.path  # noqa: F401
except ImportError:
    pass

# Phone defaults for packaged desktop board_config (env-driven sizes).
# For TV / 10-foot UI, import board_config_tv before the entry (or set these).
if sys.platform == "android":
    os.environ.setdefault("PYDISPLAY_WIDTH", "720")
    os.environ.setdefault("PYDISPLAY_HEIGHT", "1280")
    os.environ.setdefault("PYDISPLAY_SCALE", "1.0")
    os.environ.setdefault("PYDISPLAY_ROTATION", "0")
    # Must be set before ``import multimer`` (via board_config). CPython
    # SDL_AddTimer callbacks are not on the GLES thread — sdl2 timers cause
    # EGL_BAD_ACCESS and a blank/frozen display after the first presents.
    os.environ.setdefault("MULTIMER_BACKEND", "threading")


def _ensure_dir(name):
    path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(path)
    except OSError:
        pass
    if path not in sys.path:
        sys.path.insert(0, path)
    return path


def _read_text(name):
    try:
        with open(name, "r") as fh:
            return fh.read().strip()
    except OSError:
        return ""


def _apply_run_argv():
    """Optional ``run_argv``: whitespace-separated tokens appended to sys.argv."""
    raw = _read_text("run_argv")
    if not raw:
        return
    for tok in raw.split():
        if tok and tok not in sys.argv:
            sys.argv.append(tok)


# user_pkgs first so a mip-updated launcher.py wins over the baked copy.
_ensure_dir("user_pkgs")
_ensure_dir("run")
_apply_run_argv()

_entry = _read_text("run_entry")
if _entry:
    importlib.import_module(_entry)
else:
    import launcher

    launcher.start()
