"""
Простой класс для чтения файлов FileReader(path_to_file)
"""


class FileReader:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def read(self):
        try:
            with open(self.path_to_file, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ''
