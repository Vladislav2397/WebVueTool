from src.file import File
from pathlib import Path
from caseconverter import pascalcase, kebabcase


class TestFile:

    def __repr__(self):
        return '"TestFile" test for file.py'

    def setup(self):
        self.vue_inputs = (
            'test.vue',
            'test-test.vue',
            'test.test.vue',
            'test.test-test.vue'
        )
        self.vue_files = [
            File(Path.cwd() / 'sections' / name, case_convert_fn=pascalcase)
            for name in self.vue_inputs
        ]
        self.vue_outputs = [
            ('Test', '', 'vue'),
            ('TestTest', '', 'vue'),
            ('TestTest', '', 'vue'),
            ('TestTestTest', '', 'vue')
        ]

        self.zip_vue_files_result = zip(self.vue_files, self.vue_outputs)

        self.scss_inputs = (
            'test.scss',
            'test-test.scss',
            'test--critical.scss',
            'test--main.scss',
            'test-test--main.scss',
            'test.test--main.scss'
        )

        self.scss_files = [
            File(Path.cwd() / 'sections' / name, case_convert_fn=kebabcase)
            for name in self.scss_inputs
        ]

        self.scss_outputs = [
            ('test', '', 'scss'),
            ('test-test', '', 'scss'),
            ('test', '--critical', 'scss'),
            ('test', '--main', 'scss'),
            ('test-test', '--main', 'scss'),
            ('test-test', '--main', 'scss')
        ]

        self.zip_scss_files_result = zip(self.scss_files, self.scss_outputs)

    def test_magic_str(self):
        for file, result in self.zip_vue_files_result:
            assert file.__str__() == f'File: {result[0]}{result[1]}.{result[2]}'

        for file, result in self.zip_scss_files_result:
            assert file.__str__() == f'File: {result[0]}{result[1]}.{result[2]}'

    def test_file_property_name(self):
        for file, result in self.zip_vue_files_result:
            assert file.name == result[0]

        for file, result in self.zip_scss_files_result:
            assert file.name == result[0]

    def test_file_property_suffix(self):
        for file, result in self.zip_vue_files_result:
            assert not file.suffix

        for file, result in self.zip_scss_files_result:
            assert file.suffix == (result[1] if result[1] else None)

    def test_file_property_extension(self):
        for file, result in self.zip_vue_files_result:
            assert file.extension == 'vue'

        for file, result in self.zip_scss_files_result:
            assert file.extension == 'scss'

    def test_file_property_filename(self):
        for file, result in self.zip_vue_files_result:
            assert file.filename == f'{result[0]}.{result[2]}'

        for file, result in self.zip_scss_files_result:
            assert file.filename == f'{result[0]}{result[1]}.{result[2]}'

    def test_file_property_parent(self):
        for file, result in self.zip_vue_files_result:
            assert file.parent == Path.cwd() / 'sections'

        for file, result in self.zip_scss_files_result:
            assert file.parent == Path(Path.cwd()) / 'sections'

    def test_file_property_path(self):
        for file, result in self.zip_vue_files_result:
            assert file.path == Path.cwd() / 'sections' / f'{result[0]}.{result[2]}'

        for file, result in self.zip_scss_files_result:
            assert file.path == Path.cwd() / 'sections' / f'{result[0]}{result[1]}.{result[2]}'

    def test_file_property_content(self):
        for file, result in self.zip_vue_files_result:
            assert file.content == ''

        for file, result in self.zip_scss_files_result:
            assert file.content == ''

    def test_file_property_relative(self):
        for file, result in self.zip_vue_files_result:
            assert file.relative_path == Path('sections') / f'{result[0]}{result[1]}.{result[2]}'

    def test_file_exists(self):
        for file, result in self.zip_vue_files_result:
            assert not file.exists()

        for file, result in self.zip_scss_files_result:
            assert not file.exists()
