# pydisplay_android

Android APK template for [pydisplay](https://github.com/PyDevices/pydisplay): **python-for-android** recipes and a **buildozer** app (`p4a_app/`) others can clone and replace with their own code.

On Android there is no MicroPython port; pydisplay runs under **CPython** in a **python-for-android** APK with the **SDL2 bootstrap** (no Kivy). Runtime packages install from **[TestPyPI](https://test.pypi.org/)** as CPython wheels, not from local git checkouts. Pure-Python `usdl2` and the MCU-shaped `board_config` come from **pydisplay-desktop**; p4a’s `sdl2` recipe supplies `libSDL2.so`.

Use this repo when you want to turn a pydisplay app into an Android APK without building every dependency by hand. The usual loop is: edit the app under **`p4a_app/`**, adjust recipes or `buildozer.spec` only when the runtime dependency set changes, then rebuild with `./build_android.sh` and smoke-test on the emulator or a phone. Display/input wiring is packaged `board_config` + `displaysys.AutoDisplay` (set `PYDISPLAY_*` in `main.py`); change visible demo behavior in **`p4a_app/paint.py`** or **`p4a_app/main.py`**.

Pages: [pydevices.github.io/pydisplay_android](https://pydevices.github.io/pydisplay_android/)

## TestPyPI packages

| PyPI name | Import | Role |
|-----------|--------|------|
| [pydisplay-desktop](https://test.pypi.org/project/pydisplay-desktop/) | `board_config`, `usdl2`, … | Desktop/Android board bundle + pure-Python SDL2 binding |
| [pygraphics](https://test.pypi.org/project/pygraphics/) | `pygraphics` | Native pygraphics (Android / desktop wheels) |
| [displaysys](https://test.pypi.org/project/displaysys/) | `displaysys` | Display core + backends (`AutoDisplay`, `SDLDisplay`, …) |
| [eventsys](https://test.pypi.org/project/eventsys/) | `eventsys` | Event runtime / input queue |
| [multimer](https://test.pypi.org/project/multimer/) | `multimer` | Timers (`threading` on Android; not `sdl2`) |
| [lvgl-cpython](https://test.pypi.org/project/lvgl-cpython/) | `lvgl` | LVGL native extension (optional; not in paint `requirements`) |

Recipes leave versions unpinned so pip takes the latest matching wheel. Pin with `version = "…"` in a recipe when you need a frozen APK.


## 🚀 Build APK

```bash
./build_android.sh -y
./scripts/emulator.sh
```

Full prerequisites, icon/presplash, emulator/phone, Samsung USB debugging, and `sdkmanager` notes: **[docs/building.md](docs/building.md)**.

Package id: **`org.pydevices.p4a_app`**. Host deps: `requirements-dev.txt`.

## App layout

| File | Role |
|------|------|
| `p4a_app/main.py` | p4a entry: phone `PYDISPLAY_*` defaults, then `import paint` |
| `p4a_app/paint.py` | Touch-paint (default APK behavior); `from board_config import …` |
| `p4a_app/board_config_tv.py` | Optional: set landscape TV env before `paint` |
| `p4a_app/utils/path.py` | `sys.path` helper (same idea as pydisplay `utils.path`) |
| `p4a_app/icon.png` | Launcher icon + presplash |

`buildozer.spec` paint requirements:

```
python3,sdl2,pydisplay-desktop,displaysys,eventsys,pygraphics,multimer
```

(`python3` unpinned — p4a pairs target/host Python; do not pin `python3==3.13`.)

## Layout

| Path | Role |
|------|------|
| `p4a_app/` | buildozer project + sample entry |
| `p4a_recipes/` | TestPyPI `PyProjectRecipe` wrappers |
| `docs/` | Build / device guides |
| `scripts/` | Host helpers (`phone.sh`, `emulator.sh`, `test_desktop.sh`, …) |
| `build_android.sh` | Build the debug APK |

## Customize

Almost everything for your APK lives under **`p4a_app/`** (entry, `paint`, `buildozer.spec`, icon). Recipes and host tooling: see [docs/building.md](docs/building.md#your-own-app).
