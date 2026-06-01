# PyInstaller spec — Battle Tetris (single executable, Windows / macOS)
# Build: pyinstaller battle_tetris.spec --noconfirm

import sys
from pathlib import Path

block_cipher = None
project_dir = Path(SPECPATH)
resource_packs = project_dir / "resource_packs"
assets_dir = project_dir / "assets"
icon_ico = assets_dir / "New-Piskel-_1_.ico"
icon_icns = assets_dir / "app.icns"


def resolve_pyinstaller_icon() -> str | None:
    if sys.platform == "darwin":
        if icon_icns.is_file():
            return str(icon_icns)
        return None
    if icon_ico.is_file():
        return str(icon_ico)
    return None


app_icon = resolve_pyinstaller_icon()

added_files: list[tuple[str, str]] = []
if resource_packs.exists():
    added_files.append((str(resource_packs), "resource_packs"))
if assets_dir.exists():
    added_files.append((str(assets_dir), "assets"))

default_settings = project_dir / "settings.json"
if default_settings.exists():
    added_files.append((str(default_settings), "."))

a = Analysis(
    ["main.py"],
    pathex=[str(project_dir)],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        "websockets",
        "websockets.asyncio",
        "websockets.asyncio.client",
        "websockets.asyncio.server",
        "pygame",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="BattleTetris",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=sys.platform == "darwin",
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=app_icon,
)

if sys.platform == "darwin":
    app = BUNDLE(
        exe,
        name="BattleTetris.app",
        icon=app_icon,
        bundle_identifier="com.battletetris.game",
        info_plist={
            "CFBundleName": "BattleTetris",
            "CFBundleDisplayName": "BattleTetris",
            "NSHighResolutionCapable": True,
        },
    )
