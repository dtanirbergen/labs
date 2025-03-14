import shutil
import os

files = input("Введите названия файлов: ").split()

for item in files:
    if os.path.exists(item): 
        nw_n = input(f"Введите новое имя для копии {item}: ")
        shutil.copy(item, nw_n)  
        print(f"Файл {item} скопирован как {nw_n}!")
    else:
        print(f"Файл {item} не найден!")
