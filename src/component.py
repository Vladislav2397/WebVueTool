from pathlib import Path

from caseconverter import pascalcase

from src.file import File


class Component:

    def __init__(
        self,
        vue_file: File,
        critical_style: File,
        main_style: File
    ):
        self._vue_file = vue_file
        self._critical_file = critical_style
        self._main_file = main_style

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name}'

    def save(self) -> None:
        """ Save this file in database """
        pass

    def remove(self, name: str):
        pass

    def update(self, name: str, **kwargs):
        pass

    def get_content(self):
        pass

    @property
    def name(self) -> str:
        return pascalcase(self._vue_file.name)

    @property
    def parent(self) -> Path:
        return self._vue_file.relative_path.parent

    @property
    def is_style(self) -> bool:
        return True
