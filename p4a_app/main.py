# SPDX-License-Identifier: MIT
# p4a SDL2 bootstrap requires this filename.
import os
import sys

try:
    import utils.path  # noqa: F401
except ImportError:
    pass

# Phone defaults for packaged desktop board_config (env-driven sizes).
# For TV / 10-foot UI, import board_config_tv before paint (or set these env vars).
if sys.platform == "android":
    os.environ.setdefault("PYDISPLAY_WIDTH", "720")
    os.environ.setdefault("PYDISPLAY_HEIGHT", "1280")
    os.environ.setdefault("PYDISPLAY_SCALE", "1.0")
    os.environ.setdefault("PYDISPLAY_ROTATION", "0")

import paint  # noqa: E402
