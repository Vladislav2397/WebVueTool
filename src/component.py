# from pathlib import Path
from caseconverter import pascalcase, kebabcase
from pathlib import Path
from src.file import File


class Component:

    def __init__(
        self,
        vue_file: File,
        scss_critical_file: File,
        scss_main_file: File
    ):
        self._vue_file = vue_file
        self._scss_critical_file = scss_critical_file
        self._scss_main_file = scss_main_file

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name}'

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
        # assert self._scss_critical_file.parent == self._scss_main_file.parent
        # assert self._scss_critical_file.name == self._scss_main_file.name

        vue = self._vue_file.parent / kebabcase(self._vue_file.name)
        scss = self._scss_critical_file.parent / self._scss_main_file.name

        return vue == scss
