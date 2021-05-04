import re
from os import makedirs, walk
from pathlib import Path
from caseconverter import kebabcase, pascalcase
from src.config import FileData


def get_template_parent_scss(component_name: str) -> str:
    return f"@import \'{component_name}\';\n"


# TODO: remove
def get_file_data(filename: str, path: str = None) -> FileData:
    res = re.match(
        r'(\w+([-.]\w+)*)(--(critical|main))?\.(scss|css|vue)$',
        filename
    )
    return FileData(
        name=res.group(1),
        suffix=res.group(3),
        extension=res.group(5),
        path=path
    )


# TODO: Simplify abstraction
def get_files(path: Path):
    list_files = []
    for path, dirs, files in walk(path, topdown=True):
        for file in files:
            list_files.append(get_file_data(file, path))
    return list_files


def write_file(file_path: str, content: str = '', mode: str = 'w') -> None:
    with open(file_path, mode) as file:
        file.write(content)
        file.close()


def create_directory(path: str):
    try:
        makedirs(path)
    except FileExistsError:
        print(f'"{path}" directory is already has')


def get_template_vue(name):
    return f'''<template lang="pug">
    +b.SECTION.{kebabcase(name)}
</template>

<script lang="ts">
import {{ Component, Vue }} from 'vue-property-decorator'

@Component

export default {pascalcase(name)} extends Vue {{

}}
</script>'''


def get_template_scss(name):
    return f'''.{kebabcase(name)} {{
    // draft {kebabcase(name)}
}}'''
