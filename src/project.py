from terminaltables import AsciiTable
from os import listdir, walk
from src.config import (
    ROOT_PATH, SRC_PATH, SCSS_PATH, COMPONENTS_PATH,
    Paths, Path
)
from src.tools import create_directory


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

    @property
    def list_components(self):
        return [component.name for component in self._vue_components]

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

    # def _update_components(self) -> None:
    #     """
    #     Update components
    #
    #     :return: None
    #     """
        # component_files: List[File] = [
        #     File(Path(path) / file, case_convert_fn=pascalcase)
        #     for path, _, files in walk(self._PATH.components)
        #     for file in files
        # ]
        #
        # self._vue_components: list = [
        #     file(file)
        #     for file in component_files
        # ]

    def _create_vue(self, vue_file_path: Path) -> None:
        """
            Create vue file in components dir

            :param vue_file_path: path to vue component file
            :return: None
        """

        vue_file = VueFile(vue_file_path)

        if vue_file_path.parent.name not in self.component_dirs:
            create_directory(vue_file_path.parent)
            vue_file.create()
        elif vue_file.name in listdir(vue_file_path.parent):
            print(f'{vue_file} is already has')
        else:
            vue_file.create()

    def _create_scss(self, scss_file_path: Path):
        """
            Create scss file in assets/scss dir

            :param scss_file_path: path to scss style file without extension
            :return: None
        """
        scss_file = ScssFile(scss_file_path)

        try:
            scss_file.create()
        except Exception:
            print(f'{scss_file} is already has')

    #                           => sections            => Test
    def create_component(self, component_parent: str, component_name: str):

        vue_path = self._PATH.components / component_parent / component_name
        scss_path = self._PATH.scss / component_parent / component_name

        self._create_vue(vue_path)
        self._create_scss(scss_path)

    def print_table(self):
        table_data = [
            ['Components', 'styles']
        ]
        table_data.extend([component] for component in self.list_components)
        table = AsciiTable(table_data)
        print(table.table)

    def print_tree(self):
        print('Components:')
        for directory in self.component_dirs:
            print(f'|-- {directory}:')
            for subdir in listdir(self._PATH.components / directory):
                print(f'\t|-- {subdir}')


if __name__ == '__main__':
    # test_type = 'sections'
    # test_component = 'cardBonus'

    Project().print_tree()
