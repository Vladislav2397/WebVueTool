from pathlib import Path
from caseconverter import pascalcase, kebabcase
from src.tools import get_file_name, create_directory


class File:
    """ File in project """

    def __init__(
            self,
            path: str,
            content: str = ''
    ):
        posix_path = Path(path)
        self._name, self._extension = get_file_name(posix_path.name)
        self._parent = posix_path.parent
        self._content = content

    def __str__(self):
        return f'File: {self.filename}'

    def exists(self):
        return self.path.exists()

    def is_empty(self):
        """
        :return: False if file is not empty else True
        """
        return self.path.exists()

    def create(self):
        """ Create directory with file and write content into file """
        create_directory(self.path.parent)
        self.write(self._get_content())

    def write(self, content: str):
        """ Write content into file """
        if self.is_empty():
            with open(self.path, 'w', encoding='utf-8') as file:
                file.write(content)

    def _get_content(self) -> str:
        """ Return content for file """
        return self.name

    @property
    def name(self):
        """ :return: name of filename """
        return self._name

    @property
    def extension(self):
        """ :return: extension of filename """
        return self._extension

    @property
    def parent(self) -> Path:
        """ :return: path to filename parent """
        return self._parent

    @property
    def content(self) -> list:
        return self._content

    @property
    def filename(self) -> str:
        """ :return: filename with extension """
        return f'{self._name}.{self._extension}'

    @property
    def path(self) -> Path:
        """ :return: path to filename with extension """
        return self.parent / self.filename


class VueFile(File):
    def __init__(self, path: Path, content: str = ''):
        super().__init__(
            name=pascalcase(get_file_name_without_ext(path.name)),
            extension='vue',
            path=path,
            content=content
        )

    def _get_content(self):
        return f'''<template lang="pug">
    +b.SECTION.{kebabcase(self.name)}
</template>

<script lang="ts">
import {{ Component, Vue }} from 'vue-property-decorator'

@Component

export default {pascalcase(self.name)} extends Vue {{

}}
</script>'''


class ScssFile(File):
    def __init__(self, path: Path, content: str = ''):
        super().__init__(
            name=kebabcase(get_file_name_without_ext(path.name)),
            extension='scss',
            path=path.parent / kebabcase(path.name) / kebabcase(path.name),
            content=content
        )

    def _get_content(self):
        return f'''.{kebabcase(self.name)} {{
    // draft {kebabcase(self.name)}
}}'''


class Component:
    def __init__(self, file_component: File):
        self.file = file_component

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name}'

    @property
    def name(self) -> str:
        return self.file.name

    @property
    def path(self) -> Path:
        return self.file.parent


class VueComponent(Component):
    pass


class ScssComponent(Component):
    def __init__(self, file_component: File, is_parent: bool = False, children: list = None):
        super().__init__(file_component)
        self._is_parent = is_parent
        self._children = children or list()

    @property
    def children(self):
        return self._children
