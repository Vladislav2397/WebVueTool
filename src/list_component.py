from typing import List
from pathlib import Path
from os import walk

from caseconverter import kebabcase

from src.component import Component
from src.file import File


class StyleFiles:
    def __init__(self, critical: File = None, main: File = None):
        self.critical = critical
        self.main = main


class ListComponents:

    def __init__(self, vue_path: Path, style_path: Path = None):
        self._vue_path = vue_path
        self._style_path = style_path
        self._components = self._get_components()

    def _get_components(self) -> list:
        vue_files = self._get_files(self._vue_path)
        style_files = self._get_files(self._style_path)
        components = []

        for vue in vue_files:
            styles = StyleFiles(None, None)
            for style in style_files:
                if kebabcase(vue.name) == style.name and style.suffix:
                    if style.suffix == '--main':
                        styles.main = style
                    elif style.suffix == '--critical':
                        styles.critical = style
            components.append(Component(vue, styles))
        return components

    def _get_files(self, path: Path) -> List[File]:
        """
            :param path: path to directory with files
            :return: all files from path
        """
        list_files = list()
        exclude = ['__pycache__', '.git', '.idea']
        for path, dirs, files in walk(path, topdown=True):
            dirs[:] = [d for d in dirs if d not in exclude]
            for file in files:
                list_files.append(files)
        # for item in path.iterdir():
        #     if item.is_file():
        #         files.append(File(item))
        #     elif item.is_dir():
        #         files.extend(self._get_files(path / item))
        return list_files

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
