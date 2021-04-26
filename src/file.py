from pathlib import Path
from src.tools import get_file_data


class File:
    """ File in project """

    def __init__(
            self,
            path: str,
            content: str = ''
    ):
        """ Get full path for file """
        self._full_path = Path(path)
        self._file_name = self._full_path.name
        self._name, self._suffix, self._extension = get_file_data(
            self._file_name
        )
        self._parent = self._full_path.parent
        self._content = content

    def __str__(self):
        return f'File: {self.filename}'

    def exists(self) -> bool:
        return self._full_path.exists()

    def _get_content(self) -> str:
        """ Return content for file """
        return self.name

    @property
    def name(self):
        """ :return: name of filename """
        return self._name

    @property
    def suffix(self):
        """ :return: suffix of filename """
        return self._suffix

    @property
    def extension(self):
        """ :return: extension of filename """
        return self._extension

    @property
    def filename(self) -> str:
        """ :return: filename with extension """
        suffix = self._suffix if self.suffix else ''
        return f'{self._name}{suffix}.{self._extension}'

    @property
    def parent(self) -> Path:
        """ :return: path to filename parent """
        return self._parent

    @property
    def path(self) -> Path:
        """ :return: path to filename with extension """
        return self._full_path

    @property
    def content(self) -> str:
        """ :return: content filename in list """
        return self._content

    @property
    def relative_path(self):
        return Path(self.parent.name) / self.filename


class Component:
    def __init__(self, file_component: File):
        self.file = file_component

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name}'

    @property
    def name(self) -> str:
        return self.file.name

    @property
    def parent(self) -> Path:
        return self.file.parent
