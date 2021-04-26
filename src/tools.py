import re
from os import makedirs
from caseconverter import kebabcase, pascalcase
from pathlib import Path
from src.config import FileData


def get_template_parent_scss(component_name: str) -> str:
    return f"@import \'{component_name}\';\n"


def get_file_name_without_ext(file: str):
    return re.sub(r'\.\w*$', '', file)


def get_file_data(filename: str, name_handler=None) -> FileData:
    res = re.match(
        r'(\w+([-.]\w+)*)(--(critical|main))?\.(scss|vue)$',
        filename
    )
    if name_handler:
        return FileData(
            name=name_handler(res.group(1), delimiters='-.'),
            suffix=res.group(3),
            extension=res.group(5)
        )
    else:
        return FileData(
            name=res.group(1),
            suffix=res.group(3),
            extension=res.group(5)
        )
    # raise SyntaxError('Files on current regex not found')


def get_files(path: Path):
    files = []
    for item in path.iterdir():
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            files.extend([get_files(path / item)])
    return files


def write_file(file_path: str, content: str = '', mode: str = 'w') -> None:
    with open(file_path, mode) as file:
        file.write(content)
        file.close()


def listdir(path: Path):
    return [dir.name for dir in path.iterdir()]


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
