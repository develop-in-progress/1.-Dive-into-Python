import os
import tempfile

"""
Интерфейс для работы с файлами. Интерфейс должен предоставлять следующие возможности по работе с файлами:
- чтение из файла, метод read возвращает строку с текущим содержанием файла
- запись в файл, метод write принимает в качестве аргумента строку с новым содержанием файла
- сложение объектов типа File, результатом сложения является объект класса File
 возвращать в качестве строкового представления объекта класса File полный путь до файла
- поддерживать протокол итерации, причем итерация проходит по строкам файла
При создании экземпляра класса File в конструктор передается полный путь до файла на файловой системе. 
Если файла с таким путем не существует, он должен быть создан при инициализации.
"""


class File:
    def __init__(self, path_to_file):

        self.path_to_file = path_to_file
        self.current = 0
        self.finish = None
        self.list_iter = None
        if not os.path.exists(self.path_to_file):
            with open(path_to_file, 'w') as f:
                pass

    def __str__(self):
        return self.path_to_file

    def __iter__(self):
        return self

    def __next__(self):

        with open(self.path_to_file, 'r') as f:
            raw_list = list(f.readlines())
        if len(raw_list) == 0 or raw_list is None or raw_list == []:
            raise StopIteration
        self.current += 1
        if self.current > len(raw_list):
            raise StopIteration
        return raw_list[self.current - 1]

    def __add__(self, obj):
        file1 = None
        file2 = None
        add_file = None
        path = os.path.join(tempfile.gettempdir(), 'new_file')
        with open(self.path_to_file, 'r') as f:
            file1 = f.read()
        with open(obj.path_to_file, 'r') as f:
            file2 = f.read()
        with open(path, 'w') as f:
            f.write(file1 + file2)
        with open(path, 'r') as f:
            add_file = f.read()
            new_file = File(path)
            new_file.write(add_file)

        return new_file

    def read(self):
        with open(self.path_to_file, 'r') as ff:
            return str(ff.read())

    def write(self, text_to_write):
        with open(self.path_to_file, 'w') as ff:
            ff.write(text_to_write)
