from pathlib import Path
from os import listdir
from terminaltables import AsciiTable
from caseconverter import pascalcase

from src.database.models import (
    create_tables,
    File as FileDB,
    Component as ComponentDB
)
from src.config import (
    ROOT_PATH, SRC_PATH, SCSS_PATH, COMPONENTS_PATH,
    Paths
)
from src.tools import get_files
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
        self._update_db_tables()

        # component: ComponentDB = ComponentDB.get(
        #   ComponentDB.name == 'Tooltip'
        # )
        # print(component.scss_critical_file.path)
        # print(component.vue_file.path)

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

    def _update_db_tables(self):
        vue_files = get_files(self._PATH.components)
        scss_files = get_files(self._PATH.scss)

        for files in [vue_files, scss_files]:
            for file in files:
                file, _ = FileDB.get_or_create(
                    name=file.name,
                    suffix=file.suffix,
                    extension=file.extension,
                    path=file.path
                )

        for file in FileDB.select().where(FileDB.extension == 'vue'):
            ComponentDB.get_or_create(
                name=file.name,
                path=file.path,
                vue_file=file
            )

        for file in FileDB.select().where(FileDB.extension == 'scss'):
            component: ComponentDB = ComponentDB.get_or_none(
                name=pascalcase(file.name)
            )
            if component:
                if file.suffix == '--critical':
                    component.scss_critical_file = file
                elif file.suffix == '--main':
                    component.scss_main_file = file

                component.save()

        for component in ComponentDB.select():
            if component.scss_critical_file and component.scss_main_file:
                component.is_style = True
                component.save()

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
            ['№', 'Parent', 'Component', 'IsStyle']
        ]
        table = AsciiTable(table_data)
        table.table_data.extend([
            (
                index + 1,
                Path(component.path).relative_to(self._PATH.components),
                component.name,
                component.is_style
            )
            for index, component in enumerate(ComponentDB.select())
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
