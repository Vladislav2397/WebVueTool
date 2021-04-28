# from pathlib import Path
from caseconverter import pascalcase
from pathlib import Path
from src.file import File


class Component:
    def __init__(self, vue_file: File, scss_path: Path):
        self._vue_file = vue_file
        self._scss_path = scss_path
        self._is_style = True
        # self._scss_critical_file =
        # self._scss_main_file =

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name}'

    @property
    def name(self) -> str:
        return pascalcase(self._vue_file.name)

    @property
    def parent(self) -> Path:
        return self._vue_file.relative_path.parent

    @property
    def is_style(self) -> bool:
        return self._is_style
