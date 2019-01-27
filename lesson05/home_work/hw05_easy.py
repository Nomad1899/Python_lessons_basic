import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def new_dir():
    for i in range (1,10):
        d = os.path.join(os.getcwd(), f'dir_{i}')
        try:
            os.mkdir(d)
            print(f'dir_{i}, был создан ')
        except FileExistsError:
            print('Файл уже существует!')
def remove_dir():
    for i in range(1,10):
        d = os.path.join(os.getcwd(), f'dir_{i}')
        try:
            os.rmdir(d)
            print(f'dir_{i}, был удален ')
        except FileExistsError:
            print('фала не существует!')
new_dir()
remove_dir()
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_dir():
    d = os.path.join(os.getcwd())
    lst = os.listdir(d)
    for i in lst:
        print(i)
show_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    copy_file = __file__ + ' - copy'
    shutil.copy(__file__, copy_file)
