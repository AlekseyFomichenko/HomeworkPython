from random import randint
#Task1
size, lower_bound, upper_bound = int(input('Размер списка: ')), int(input('Мин значение диапазона: ')), int(input('Макс значение диапазона: '))
print('Список: ', list_1 := [randint(1, 20) for _ in range(size)])
print('Индексы: ', list_2 := [x for x in range(len(list_1)) if lower_bound < list_1[x] < upper_bound])

#Task2
d = int(input('Введите разность(шаг) прогрессии: '))
first_value = int(input('Введите первый элемент массива: '))
size = int(input('Введите размер массива: '))
print('Элементы ариф. прогрессии:', *range(first_value, first_value + d * size, d))
