from pathlib import Path
from os import listdir, walk
from terminaltables import AsciiTable

from src.database.models import (
    create_tables,
    File as FileDB
)
from src.config import (
    ROOT_PATH, SRC_PATH, SCSS_PATH, COMPONENTS_PATH,
    Paths
)
from src.tools import get_file_data
# from src.list_component import ListComponents
# from src.component import Component


class Project:

    _PATH = Paths(
        root=ROOT_PATH,
        src=SRC_PATH,
        scss=SCSS_PATH,
        components=COMPONENTS_PATH
    )

    def __init__(self):
        self._check_project_dir()

        create_tables()

        for file in self._get_vue_files():
            FileDB.get_or_create(
                name=file.name,
                suffix=file.suffix,
                extension=file.extension,
                path=file.path
            )

        # self._list_components = ListComponents(
        #     self._PATH.components, self._PATH.scss
        # )

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

    def _get_vue_files(self):
        list_files = []
        for path, dirs, files in walk(self._PATH.components, topdown=True):
            files[:] = [f for f in files if f.endswith('.vue')]
            for file in files:
                list_files.append(get_file_data(file, path))
        return list_files

    def _get_db_files(self):
        return (file for file in FileDB.select())

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
            ['Parent', 'Component', 'IsStyle']
        ]
        table = AsciiTable(table_data)
        table.table_data.extend([
            (
                Path(file.path).relative_to(self._PATH.components),
                file.name,
                True
            ) for file in self._get_db_files()
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
        # pass


if __name__ == '__main__':
    # test_type = 'sections'
    # test_component = 'cardBonus'

    Project().print_table()
