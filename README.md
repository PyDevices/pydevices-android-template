# pydisplay_android

Android APK template for [pydisplay](https://github.com/PyDevices/pydisplay): **python-for-android** recipes and a **buildozer** app (`p4a_app/`) others can clone and replace with their own code.

On Android there is no MicroPython port; pydisplay runs under **CPython** in a **python-for-android** APK with the **SDL2 bootstrap** (no Kivy). Runtime packages install from **[TestPyPI](https://test.pypi.org/)** as CPython wheels, not from local git checkouts. Pure-Python `usdl2` and the MCU-shaped `board_config` come from **pydevices-desktop**; p4a’s `sdl2` recipe supplies `libSDL2.so`.

The default APK is **PyDevices Launcher** (`org.pydevices.launcher`): a baked LVGL home screen. Buttons fetch apps on demand (`mip` from GitHub + PyDevices MIP index, or `pip` with TestPyPI primary / PyPI secondary). Cold start never auto-fetches. Stage host files over adb with **`scripts/android.sh`** (cwd path, like CLI Python — not PyScript gallery lookup; symlink from `~/bin/android.sh` keeps it on PATH).

Pages: [pydevices.github.io/pydisplay_android](https://pydevices.github.io/pydisplay_android/)

## TestPyPI packages

| PyPI name | Import | Role |
|-----------|--------|------|
| [pydevices-desktop](https://test.pypi.org/project/pydevices-desktop/) | `board_config`, `usdl2`, … | Desktop/Android board bundle + pure-Python SDL2 binding |
| [pydevices-pygraphics](https://test.pypi.org/project/pydevices-pygraphics/) | `pygraphics` | Native pygraphics (Android / desktop wheels) |
| [pydevices-displaydev](https://test.pypi.org/project/pydevices-displaydev/) | `displaydev` | Display core + backends (`AutoDisplay`, `SDLDisplay`, …) |
| [pydevices-audiodev](https://test.pypi.org/project/pydevices-audiodev/) | `audiodev` | Portable PCM audio API and Android SDL backend |
| [pydevices-eventsys](https://test.pypi.org/project/pydevices-eventsys/) | `eventsys` | Optional event runtime / input queue for non-LVGL apps |
| [pydevices-multimer](https://test.pypi.org/project/pydevices-multimer/) | `multimer` | Timers (`threading` on Android; not `sdl2`) |
| [pydevices-lvgl](https://test.pypi.org/project/pydevices-lvgl/) | `lvgl` | LVGL native extension |
| [pydevices-palettes](https://test.pypi.org/project/pydevices-palettes/) | `palettes` | Color palettes |
| [pydevices-pdwidgets](https://test.pypi.org/project/pydevices-pdwidgets/) | `pdwidgets` | Widgets |

Recipes pin the coordinated release versions so repeat Android builds are reproducible.


## 🚀 Build APK

```bash
./build_android.sh -y
./scripts/emulator.sh
```

Full prerequisites, icon/presplash, emulator/phone, Samsung USB debugging, and `sdkmanager` notes: **[docs/building.md](docs/building.md)**.

Package id: **`org.pydevices.launcher`** (launcher label: **PyDevices Launcher**). Host deps: `requirements-dev.txt`.

## App layout

| File | Role |
|------|------|
| `p4a_app/boot.py` | Startup (env / path / stdio), then `main.py` or REPL; Activity entry via build patch |
| `p4a_app/main.py` | User entry (default: LVGL launcher). Omit or replace via `android.sh` |
| `p4a_app/launcher.py` | Baked LVGL home (Update launcher / lv_test_timer buttons) |
| `p4a_app/paint.py` | Touch-paint demo (stage via `android.sh`, not cold-start default) |
| `p4a_app/stdio_sidecar.py` | Localhost stdio bridge for `android.sh` TTY attach / `-i` REPL |
| `p4a_app/board_config_tv.py` | Optional: set landscape TV env before entry |
| `p4a_app/utils/` | Full pydisplay `src/utils/` tree (`path`, `mip`, `tft_config`, `fonts`, …); synced from sibling pydisplay by `build_android.sh` |
| `p4a_app/icon.png` | Launcher icon + presplash |

`buildozer.spec` requirements:

```
python3,sdl2,setuptools,pip,pydevices-events,pydevices-keys,pydevices-multimer,pydevices-displaydev,pydevices-audiodev,pydevices-eventsys,pydevices-pygraphics,pydevices-palettes,pydevices-pdwidgets,pydevices-desktop,pydeviceslvgl
```

(`python3` unpinned — p4a pairs target/host Python; do not pin `python3==3.13`.)

## Stage examples from pydisplay

From `pydisplay/src` (path relative to cwd), with `android.sh` on PATH:

```bash
android.sh examples/lv_test_timer.py
android.sh examples/paint.py
android.sh -i               # >>> REPL in this terminal (like python -i)
android.sh --clear          # back to LVGL home
android.sh --logcat
android.sh --no-attach …    # launch only (no TTY stdio attach)
```

Or call `../pydisplay_android/scripts/android.sh` / this repo’s `./scripts/android.sh` directly. Matrix opt-in: `pydisplay/tools/example_test_kit.py --only-runtime android …`.

## Layout

| Path | Role |
|------|------|
| `p4a_app/` | buildozer project + launcher entry |
| `p4a_recipes/` | TestPyPI / PyPI `PyProjectRecipe` wrappers |
| `docs/` | Build / device guides |
| `scripts/` | Host helpers (`android.sh`, `phone.sh`, `emulator.sh`, `test_desktop.sh`, …) |
| `build_android.sh` | Build the debug APK |

## Customize

Almost everything for your APK lives under **`p4a_app/`** (entry, `launcher.py`, `buildozer.spec`, icon). Recipes and host tooling: see [docs/building.md](docs/building.md#your-own-app).
