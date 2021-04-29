from pathlib import Path
from src.component import Component
from src.file import File


class TestComponent:
    def setup(self):
        self.component = Component(
            File(Path.cwd() / 'sections' / 'Test.vue', '', Path.cwd()),
            File(Path.cwd() / 'sections' / 'test--main.scss', '', Path.cwd()),
            File(Path.cwd() / 'sections' / 'test--critical.scss', '', Path.cwd())
        )
        pass

    def test_property_name(self):
        assert self.component.name == 'Test'

    def test_property_parent(self):
        assert self.component.parent == Path('sections')
