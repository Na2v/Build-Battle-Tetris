"""Entry point for competitive online Tetris."""

import sys
from pathlib import Path

from src.paths import get_bundle_root, get_resource_packs_dir, get_settings_path

BUNDLE_ROOT: Path = get_bundle_root()
if str(BUNDLE_ROOT) not in sys.path:
    sys.path.insert(0, str(BUNDLE_ROOT))

from src.ui.app import TetrisApp


def main() -> None:
    app: TetrisApp = TetrisApp(
        bundle_root=BUNDLE_ROOT,
        resource_packs_dir=get_resource_packs_dir(),
        settings_path=get_settings_path(),
    )
    app.run()


if __name__ == "__main__":
    main()
