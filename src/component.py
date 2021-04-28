# from pathlib import Path
from caseconverter import kebabcase, pascalcase
from pathlib import Path
from src.file import File


class Component:
    def __init__(self, vue_file: File, scss_path: Path):
        assert kebabcase(vue_file.name)

        self.vue_file = vue_file
        self.scss_path = scss_path
        # self.scss_critical_file =
        # self.scss_main_file =

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name}'

    @property
    def name(self):
        return pascalcase(self.vue_file.name)
