# pydisplay_android

Android APK template for [pydisplay](https://github.com/PyDevices/pydisplay): **python-for-android** recipes and a **buildozer** app (`p4a_app/`) others can clone and replace with their own code.

On Android there is no MicroPython port; pydisplay runs under **CPython** in a **python-for-android** APK with the **SDL2 bootstrap**. Runtime packages install from **[TestPyPI](https://test.pypi.org/)** — not from local git checkouts.

Use this repo when you want to turn a pydisplay app into an Android APK without building every dependency by hand. The usual loop is: edit the app under **`p4a_app/`**, adjust recipes or `buildozer.spec` only when the runtime dependency set changes, then rebuild with `./build_android.sh` and smoke-test on the emulator or a phone. If you are debugging display/input wiring, start in **`p4a_app/board_config.py`**; if you are changing the visible demo behavior, start in **`p4a_app/paint.py`** or **`p4a_app/main.py`**.

Pages: [pydevices.github.io/pydisplay_android](https://pydevices.github.io/pydisplay_android/)

## TestPyPI packages

| PyPI name | Import | Role |
|-----------|--------|------|
| [usdl2](https://test.pypi.org/project/usdl2/) | `usdl2` | Native SDL2 subset (Android wheels: `android_21_*`) |
| [pygraphics-cmod](https://test.pypi.org/project/pygraphics-cmod/) | `pygraphics` | Native pygraphics (`pygraphics` recipe → `pygraphics-cmod`) |
| [displaysys](https://test.pypi.org/project/displaysys/) | `displaysys` | Display core + backends (`SDLDisplay`, …) |
| [eventsys](https://test.pypi.org/project/eventsys/) | `eventsys` | Event runtime / input queue |
| [multimer](https://test.pypi.org/project/multimer/) | `multimer` | Timers (`_sdl2` backend on Android) |
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
| `p4a_app/main.py` | p4a entry: `import lib.path` then `import paint` |
| `p4a_app/paint.py` | Touch-paint (default APK behavior) |
| `p4a_app/board_config.py` | SDL display + `eventsys.Runtime` (from pydisplay sdldisplay idiom) |
| `p4a_app/lib/path.py` | `sys.path` helper (same idea as pydisplay `lib.path`) |
| `p4a_app/icon.png` | Launcher icon + presplash |

`buildozer.spec` paint requirements:

```
python3,sdl2,usdl2,displaysys,eventsys,pygraphics,multimer
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

Almost everything for your APK lives under **`p4a_app/`** (entry, `board_config`, `buildozer.spec`, icon). Recipes and host tooling: see [docs/building.md](docs/building.md#your-own-app).
