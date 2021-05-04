import re
from pathlib import Path
from typing import Union
from src.config import FileData
from src.database.models import File as FileDB


class File:
    """ File in project """

    def __init__(
            self,
            path: Union[str, Path],
            relative_root: Path = None
    ):
        """
        :param path: Full path to file (/home/user/project/about.vue)
        :param relative_root: Full path to relative path (/home/user/project)
        """
        self._path = Path(path)
        self._file_name = self._path.name
        self._name, self._suffix, self._extension = self._get_file_data()
        self._relative_root = relative_root

    def __str__(self) -> str:
        if self._relative_root:
            return f'File: {self.relative_path}'
        return f'File: {self._file_name}'

    def __call__(self) -> Path:
        return self._path

    def _get_file_data(self) -> FileData:
        """ Return file data by regex """
        res = re.match(
            r'^(\w+([-.]\w+)*)(--(critical|main))?\.(scss|vue|css)?$',
            self._file_name
        )
        return FileData(
            name=res.group(1),
            suffix=res.group(3),
            extension=res.group(5),
            path=str(self._path.parent)
        )

    def save_db(self) -> None:
        """ Save this file in database """
        FileDB.get_or_create(
            name=self._name,
            suffix=self._suffix,
            extension=self._extension,
            path=self.parent
        )

    def _remove_db(self, file_id: int) -> None:
        """ Remove this file from database """
        FileDB.delete_by_id(file_id)

    @property
    def name(self) -> str:
        """
        :return: file name
        """
        return self._name

    @property
    def suffix(self) -> str:
        """
        :return: file suffix starts with --
        """
        return self._suffix

    @property
    def extension(self) -> str:
        """
        :return: file extension name
        """
        return self._extension

    @property
    def parent(self) -> Path:
        """
        :return: path to file parent directory
        """
        return self._path.parent

    @property
    def filename(self) -> str:
        """
        :return: full file name
        """
        return self._file_name

    @property
    def relative_path(self):
        """
        :return: full path from relative path
        """
        return self._path.relative_to(self._relative_root)

    def exists(self) -> bool:
        """
        :return: is file exists
        """
        return self._path.exists()
