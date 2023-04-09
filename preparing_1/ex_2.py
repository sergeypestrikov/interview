# Реализовать функцию def print_directory_contents(Path).
# Функция принимает имя директории и выводит ее содержимое включая поддиректории.
# Использовать os.Walk нельзя
import os


# Генератор путей и имен файлов
def get_file_generator(files) -> iter:
    for file in files:
        if file.is_dir():
            with os.scandir(os.path.abspath(file.path)) as files:
                yield from get_file_generator(files)
        else:
            yield os.path.abspath(file.path), file.name


# Выводит имена и пути файлов
def print_directory_contents(sPath):
    with os.scandir(sPath) as files:
        for file in get_file_generator(files):
            print(file)


print_directory_contents('/Users/mac/')
