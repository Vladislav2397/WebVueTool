# import sys

from src.project import Project


class Main:
    def __init__(self, args: list = None):
        self.is_run = False
        self.project = Project()

        self.args = args or []

        if len(self.args) == 1:
            self.run()
        elif len(self.args) == 3:
            self._create(args[1], args[2])

    def run(self):
        self.is_run = True
        while self.is_run:
            command = input('>>> ')
            if command == 'create':
                self._create()
            elif command == 'dirs' or command == 'ls':
                self._print_directories()
            elif command == 'components' or command == 'cmp':
                self._print_table()
            elif command == 'exit' or command == 'quit':
                self._exit()
            else:
                print('unknown command')

    def _create(self, parent: str = '', name: str = ''):
        if not bool(parent and name):
            parent = input('parent component: ')
            name = input('name component: ')
        if name == 'exit' or parent == 'exit':
            return
        # self.project.create_component(parent, name)

    def _print_directories(self):
        self.project.print_tree()

    def _print_table(self):
        self.project.print_table()

    def runner(self):
        self.project.run()

    def _exit(self):
        self.is_run = False


if __name__ == '__main__':
    # Main()._print_directories()
    # Main()._print_table()
    Main().runner()
