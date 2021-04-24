from src.file import File
from pathlib import Path


class TestFile:

    def __repr__(self):
        return '"TestFile" test for file.py'

    def setup(self):
        self.file1 = File(Path.cwd() / 'sections' / 'test.vue')
        self.file2 = File(Path.cwd() / 'sections' / 'test-test.vue')
        self.file3 = File(Path.cwd() / 'sections' / 'test.test.vue')

    def test_magic_str(self):
        assert self.file1.__str__() == 'File: test.vue'
        assert self.file2.__str__() == 'File: test-test.vue'
        assert self.file3.__str__() == 'File: test.test.vue'

    def test_file_property_name(self):
        assert self.file1.name == 'test'
        assert self.file2.name == 'test-test'
        assert self.file3.name == 'test.test'

    def test_file_property_extension(self):
        assert self.file1.extension == 'vue'
        assert self.file2.extension == 'vue'
        assert self.file3.extension == 'vue'

    def test_file_property_filename(self):
        assert self.file1.filename == 'test.vue'
        assert self.file2.filename == 'test-test.vue'
        assert self.file3.filename == 'test.test.vue'

    def test_file_property_parent(self):
        assert self.file1.parent == Path(Path.cwd()) / 'sections'
        assert self.file2.parent == Path(Path.cwd()) / 'sections'
        assert self.file3.parent == Path(Path.cwd()) / 'sections'

    def test_file_property_path(self):
        assert self.file1.path == Path.cwd() / 'sections' / 'test.vue'
        assert self.file2.path == Path.cwd() / 'sections' / 'test-test.vue'
        assert self.file3.path == Path.cwd() / 'sections' / 'test.test.vue'

    def test_file_property_content(self):
        assert self.file1.content == ''
        assert self.file2.content == ''
        assert self.file3.content == ''

    def test_file_is_empty(self):
        assert not self.file1.exists()
        assert not self.file2.exists()
        assert not self.file3.exists()
