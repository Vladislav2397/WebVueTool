from terminaltables import AsciiTable
from os import listdir
from typing import List

from src.config import (
    ROOT_PATH, SRC_PATH, SCSS_PATH, COMPONENTS_PATH,
    Paths, Path
)
from src.file import File
# from src.component import Component

# Select components view (as dict or object)
# 'component": {
#   'Test': {
#       'Test.vue': None,
#       'TestTest.vue': None
#   },
#   'blank': {
#       'About.vue': None
#   }
# }


class ListComponents:

    def __init__(self, vue_path: Path, scss_path: Path):
        self._vue_path = vue_path
        self._scss_path = scss_path
        self._components = [
            # TODO: Create gen for components
        ]

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


class Project:

    _PATH = Paths(
        root=ROOT_PATH,
        src=SRC_PATH,
        scss=SCSS_PATH,
        components=COMPONENTS_PATH
    )

    def __init__(self):
        self._check_project_dir()
        self.list_components = ListComponents(
            self._PATH.components, self._PATH.scss
        )

    def _check_project_dir(self):
        """
            Check current dir

            :return: sys.exit if src or package-lock.json not in dir
        """
        list_check = ['src', 'package-lock.json']
        for item in self.root_dirs:
            if item in list_check:
                list_check.remove(item)
        if list_check:
            raise Exception("It's not a project")

    def _get_paths_dict(self, path: Path, rel_path: Path = '/'):
        files = dict()
        for item in path.iterdir():
            if item.is_file():
                files[item.name] = None
            elif item.is_dir():
                files[item.relative_to(rel_path).name] = self._get_paths_dict(
                    path / item, rel_path
                )
        return files

    def _get_files(self, path: Path) -> List[File]:
        """
            :param path: path to directory with files
            :return: all files from path
        """
        files = list()
        for item in path.iterdir():
            if item.is_file():
                files.append(File(item, relative_root=self._PATH.components))
            elif item.is_dir():
                files.extend(self._get_files(path / item))
        return files

    @property
    def root_dirs(self):
        return listdir(self._PATH.root)

    @property
    def src_dirs(self):
        return listdir(self._PATH.src)

    @property
    def scss_dirs(self):
        return listdir(self._PATH.scss)

    @property
    def component_dirs(self):
        return listdir(self._PATH.components)

    def print_table(self):
        table_data = [
            ['Parent', 'Components', 'Styles']
        ]
        table = AsciiTable(table_data)
        table.table_data.extend([
            (file.relative_path.parent, file.name, True)
            for file in self._get_files(self._PATH.components)
        ])
        print(table.table)

    def create_component(self, name: str):
        pass

    def remove_component(self, name: str):
        pass

    def update_component(self, name: str):
        pass

    def get_component_content(self, name: str):
        pass

    def run(self):
        self.print_table()


if __name__ == '__main__':
    # test_type = 'sections'
    # test_component = 'cardBonus'

    Project().print_table()
