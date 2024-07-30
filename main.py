import os
import time

directory = os.getcwd()
filepath = ''                       # Объявил переменные в начале, потому что в конечном принте он подчеркивал их
filetime = ''                       # желтым, но если их закомментить, всё будет работать
formatted_time = ''
filesize = ''
parent_dir = ''
file = ''
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        # print(filepath)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
# print(filetime)
# print(formatted_time)
# print(filesize)
# print(parent_dir)
print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
      f' {formatted_time}, Родительская директория: {parent_dir}')
