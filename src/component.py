# from pathlib import Path
from caseconverter import kebabcase
from src.file import File


class Component:
    def __init__(self, vue_file: File, scss_file: File):
        assert kebabcase(self.vue_file.name) == kebabcase(self.scss_file.name)

        self.vue_file = vue_file
        self.scss_file = scss_file

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name}'

    @property
    def name(self):
        return self.vue_file.name
