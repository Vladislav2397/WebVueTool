from pathlib import Path
from src.file import File


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
