from terminaltables import SingleTable
from os import listdir

from src.config import (
    ROOT_PATH, SRC_PATH, SCSS_PATH, COMPONENTS_PATH,
    Paths
)
from src.list_component import ListComponents
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


class Project:

    _PATH = Paths(
        root=ROOT_PATH,
        src=SRC_PATH,
        scss=SCSS_PATH,
        components=COMPONENTS_PATH
    )

    def __init__(self):
        self._check_project_dir()
        self._list_components = ListComponents(self._PATH.components)

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
        table = SingleTable(table_data)
        table.table_data.extend([
            (file.parent, file.name, True)
            for file in self._list_components.components
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
