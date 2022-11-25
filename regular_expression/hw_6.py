""" ДЗ**: У вас есть файл MOCK_DATA.txt, в котором 1000 строк с данными (Имя и Фамилия, емайл, название файла с расширением и код цвета)
1. Написать программу, где отображается меню с опциями: 1 - Считать имена и фамилии,
2 - Считать все емайлы, 3 - Считать названия файлов, 4 - Считать цвета, 5 - Выход
2. При выборе опции меню необходимо считать соответствующую информацию из файла
с данными при помощи регулярных выражений и сохранить считанные данные в новый файл.
3. Если пользователь выбирает пункт в меню 1: считываются все имена и фамилии (1000 строк)
и сохраняются в файл под названием names.txt. Если пользователь выбирает
пункт в меню 2: считываются все емайлы (1000 строк) и сохраняются в файл под названием emails.txt и тд.
4. До тех пор пока пользователь не выбрал пункт 5 программа работает и предлагает опции меню.
5. При повторном выборе какого-то из пунктов меню, существующий файл с данными,
например names.txt - полностью перезаписывается."""

import re

option = '''1 - Считать имена и фамилии
2 - Считать все емайлы
3 - Считать названия файлов
4 - Считать цвета
5 - Выход'''


POINT = True
while POINT:
    TOTAL = 0
    print(option)
    BUTTON = int(input('='))
    with open('MOCK_DATA.txt', 'r') as file:
        content = file.read()

    if BUTTON == 1:
        with open('names.txt', 'w') as file:
            names = re.findall(r'[A-Z][a-z]+\s', content)
            print(names)
            for i in names:
                TOTAL += 1
                file.write(f'{i}\t')
                if TOTAL % 2 == 0:
                    file.write(f"\n")
                if TOTAL == 2000:
                    break

    elif BUTTON == 2:
        with open('email.txt', 'w') as file:
            emails = re.findall(r'[a-zA-Z0-9]+@+[\w\-|w+.]+[a-z]{1,3}', content)
            for i in emails:
                file.write(f'{i}\n')

    elif BUTTON == 3:
        with open('filenames.txt', 'w') as file:
            file_names = re.findall(r'\s+[A-Za-z]+\.[a-z0-9]+', content)
            for i in file_names:
                file.write(f'{i}\n')

    elif BUTTON == 4:
        with open('color.txt', 'w') as file:
            colors = re.findall(r'#[a-z0-9]+', content)
            for i in colors:
                file.write(f'{i}\n')

    elif BUTTON == 5:
        POINT = False





