from src.tools import get_file_data
from src.config import FileData


class TestTools:

    def setup(self):
        pass

    def test_get_file_name(self):
        file1 = 'test.vue'
        res_file1 = ('test', None, 'vue')

        file2 = 'test.template.vue'
        res_file2 = ('test.template', None, 'vue')

        file3 = 'test-template.vue'
        res_file3 = ('test-template', None, 'vue')

        file4 = 'test--main.scss'
        res_file4 = ('test', '--main', 'scss')

        file5 = 'test-test--main.scss'
        res_file5 = ('test-test', '--main', 'scss')

        # file6 = 'test.test--main.scss'
        # res_file6 = ('test.test', '--main', 'scss')

        assert FileData(*res_file1) == get_file_data(file1)
        assert FileData(*res_file2) == get_file_data(file2)
        assert FileData(*res_file3) == get_file_data(file3)
        assert FileData(*res_file4) == get_file_data(file4)
        assert FileData(*res_file5) == get_file_data(file5)
        # assert FileData(*res_file6) == get_file_data(file6)
