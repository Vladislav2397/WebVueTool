import re
from pathlib import Path
from src.config import FileData


class File:
    """ File in project """

    def __init__(
            self,
            path: str,
            content: str = '',
    ):
        self._full_path = Path(path)
        self._file_name = self._full_path.name
        self._name, self._suffix, self._extension = self._get_file_data(
            self._file_name
        )
        self._content = content

    def __str__(self) -> str:
        return f'File: {self._file_name}'

    def __call__(self) -> Path:
        return self._full_path

    def _get_file_data(self, filename: str) -> FileData:
        res = re.match(
            r'^(\w+([-.]\w+)*)(--(critical|main))?\.(scss|vue)?$',
            filename
        )
        return FileData(
            name=res.group(1),
            suffix=res.group(3),
            extension=res.group(5)
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def suffix(self) -> str:
        return self._suffix

    @property
    def extension(self) -> str:
        return self._extension

    @property
    def parent(self) -> Path:
        return self._full_path.parent

    @property
    def filename(self) -> str:
        return self._file_name

    def exists(self) -> bool:
        return self._full_path.exists()
