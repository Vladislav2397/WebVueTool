from pathlib import Path
from src.tools import get_file_data

# FIXME: Circular imports src.file src.tools


class File:
    """ File in project """

    def __init__(
            self,
            path: str,
            content: str = '',
            case_convert_fn=None
    ):
        file_data = get_file_data(Path(path).name, case_convert_fn)
        self._name = file_data.name
        self._suffix = file_data.suffix
        self._extension = file_data.extension
        self._parent = Path(path).parent
        self._content = content

    def __str__(self):
        return f'File: {self.filename}'

    def exists(self) -> bool:
        return self.path.exists()

    def is_empty(self) -> bool:
        """
        :return: False if file is not empty else True
        """
        return self.path.stat().st_size == 0

    # def create(self) -> None:
    #     """ Create directory with file and write content into file """
        # create_directory(self.path.parent)
        # self.write(self._get_content())

    # def write(self, content: str) -> None:
    #     """ Write content into file """
    #     if self.is_empty():
    #         with open(self.path, 'w', encoding='utf-8') as file:
    #             file.write(content)

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
        return self.parent / self.filename

    @property
    def content(self) -> list:
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
