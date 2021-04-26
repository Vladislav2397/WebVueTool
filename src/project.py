# from terminaltables import AsciiTable
from os import listdir
from src.config import (
    ROOT_PATH, SRC_PATH, SCSS_PATH, COMPONENTS_PATH,
    Paths, Path
)
from src.tools import get_files


class Project:
    _PATH = Paths(
        root=ROOT_PATH,
        src=SRC_PATH,
        scss=SCSS_PATH,
        components=COMPONENTS_PATH
    )

    def __init__(self):
        self._check_project_dir()
        # self._update_components()

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
        # TODO: optimize get list directories
        return listdir(self._PATH.components)

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

    # def print_table(self):
    #     table_data = [
    #         ['Components', 'styles']
    #     ]
    #     table_data.extend([component] for component in self.list_components)
    #     table = AsciiTable(table_data)
    #     print(table.table)

    def print_tree(self):
        print('Components:')
        for dirs in get_files(self._PATH.components):
            for item in dirs:
                print(item)
        # for directory in self.component_dirs:
        #     print(f'|-- {directory}:')
        #     for subdir in listdir(self._PATH.components / directory):
        #         print(f'\t|-- {subdir}')


if __name__ == '__main__':
    # test_type = 'sections'
    # test_component = 'cardBonus'

    Project().print_tree()
