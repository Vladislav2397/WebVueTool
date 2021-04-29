import copy
from typing import List
from pathlib import Path
from src.component import Component
from src.file import File


class ListComponents:

    def __init__(self, vue_path: Path):
        self._vue_path = vue_path
        self._rel_path = copy.copy(vue_path)
        # TODO: Create gen for components
        self._components = self._get_components()

    def _get_components(self) -> list:
        return [
            Component(file)
            for file in self._get_files(self._vue_path)
        ]

    def _get_files(self, path: Path) -> List[File]:
        """
            :param path: path to directory with files
            :return: all files from path
        """
        files = list()
        for item in path.iterdir():
            if item.is_file():
                files.append(File(item, relative_root=self._rel_path))
            elif item.is_dir():
                files.extend(self._get_files(path / item))
        return files

    def add_component(self, name: str):
        pass

    def remove_component(self, name: str):
        pass

    def update_component(self, name: str):
        pass

    def get_component(self, name: str):
        pass

    @property
    def components(self):
        return self._components
