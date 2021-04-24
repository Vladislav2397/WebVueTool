from src.file import File
from pathlib import Path


class TestFile:

    def __repr__(self):
        return '"TestFile" test for file.py'

    def setup(self):
        self.file = File('name', 'ext', Path(Path.cwd() / 'name'))

    def test_magic_str(self):
        assert self.file.__str__() == 'File: name.ext'

    def test_file_property_name(self):
        assert self.file.name == 'name'

    def test_file_property_extension(self):
        assert self.file.extension == 'ext'

    def test_file_property_parent(self):
        assert self.file.parent == Path(Path.cwd())

    def test_file_property_path(self):
        assert self.file.path == Path(Path.cwd()) / 'name.ext'

    def test_file_property_filename(self):
        assert self.file.filename == 'name.ext'

    def test_file_property_content(self):
        assert self.file.content == ''

    def test_file_is_empty(self):
        assert self.file.is_empty()
