from pathlib import Path
from typing import NamedTuple


ROOT_PATH = Path(Path.cwd())
SRC_PATH = ROOT_PATH / 'src'
SCSS_PATH = SRC_PATH / 'assets' / 'scss'
COMPONENTS_PATH = SRC_PATH / 'components'


class Paths(NamedTuple):
    root: Path
    src: Path
    scss: Path
    components: Path


class Files(NamedTuple):
    path: Path
    files: list


class FileName(NamedTuple):
    name: str
    extension: str
