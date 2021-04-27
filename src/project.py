# from terminaltables import AsciiTable
from os import listdir

from src.config import (
    ROOT_PATH, SRC_PATH, SCSS_PATH, COMPONENTS_PATH,
    Paths, Path
)
from src.file import File


class Project:
    _PATH = Paths(
        root=ROOT_PATH,
        src=SRC_PATH,
        scss=SCSS_PATH,
        components=COMPONENTS_PATH
    )

    def __init__(self):
        self._check_project_dir()
        # self.vue_files = [
        #     item
        #     for item in self._get_files(self._PATH.components)
        # ]

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

    def _get_files(self, path: Path):
        pass

    def _print_files(self, path: Path):
        # TODO: Create function print tree for print from dict[str: list]
        parts = path.relative_to(self._PATH.components).parts
        indent = '\t' * (len(parts) - 1)
        sep = '|-- ' if len(parts) else ''

        print(indent + sep + path.name)
        for item in path.iterdir():
            if item.is_file():
                print((indent + '\t') + sep + item.name)
                pass
            elif item.is_dir():
                self._print_files(path / item)

    # def print_table(self):
    #     table_data = [
    #         ['Components', 'styles']
    #     ]
    #     table_data.extend([component] for component in self.list_components)
    #     table = AsciiTable(table_data)
    #     print(table.table)

    def print_tree(self):
        self._print_files(self._PATH.components)
        # for item in self.vue_files:
        #     if isinstance(item, str):
        #         print(item)
        #     else:
        #         for i in item:
        #             print(i)
        # for directory in self.component_dirs:
        #     print(f'|-- {directory}:')
        #     for subdir in listdir(self._PATH.components / directory):
        #         print(f'\t|-- {subdir}')


if __name__ == '__main__':
    # test_type = 'sections'
    # test_component = 'cardBonus'

    Project().print_tree()
