
'''#ДЗУрок7 Дэдлайн 28.11.2022 23 59
ДЗ*:
1. Написать функцию binary_search, принимающую в качестве входящего параметра элемент для поиска и список в котором необходимо искать.
2. Алгоритм должен искать с помощью двоичного поиска, изображенного на блок-схеме презентации.
3. Функция в итоге должна распечатать результат. Применить 1 раз эту функцию
4. Написать функцию buble_sort или selection_sort, принимающую в качестве входящего параметра не отсортированный список.
5. Алгоритм функции должен сортировать список методом пузырьковой сортировки или методом сортировки выбором.
6. Функция в итоге должна возвращать отсортированный список. Применить 1 раз данную функцию'''


ls = [1, 2, 4, 6, 7, 9]


def binary_search(ls, val):
    first = 0
    last = len(ls)-1
    ResultOk = False
    while first <= last:
        middle = (last+first)//2
        if val == ls[middle]:
            first = middle
            last = first
            ResultOk = True
            Pos = middle
            if ResultOk:
                print(f'Элемент найден {Pos}')
                break

        else:
            if val > ls[middle]:
                first = middle+1
            else:
                last = middle-1

    else:
        print('element not found')


binary_search(ls, 6)


def bubble_sort(ls):
    length = len(ls)
    for running in range(length -1):
        for i in range(length - 1 ):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
    print(ls)


lst = [5, 7, 4, 3, 8, 2]
res = bubble_sort
res(lst)