from src.tools import get_file_name
from src.config import FileName


class TestTools:

    def setup(self):
        pass

    def test_get_file_name(self):
        file1 = 'test.vue'
        res_file1 = ('test', 'vue')
        file2 = 'test.template.vue'
        res_file2 = ('test.template', 'vue')
        file3 = 'test-template.vue'
        res_file3 = ('test-template', 'vue')

        assert FileName(*res_file1) == get_file_name(file1)
        assert FileName(*res_file2) == get_file_name(file2)
        assert FileName(*res_file3) == get_file_name(file3)
