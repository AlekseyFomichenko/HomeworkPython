from random import randint
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input())
count = 0
count_orel = 0
count_reshka = 0
while count < n:
    orel_ili_reshka = randint(0, 1)
    print(orel_ili_reshka, end=" ")
    if orel_ili_reshka == 0:
        count_orel += 1 
    else:
        count_reshka += 1 
    count += 1
if count_reshka < count_orel:
    print(f'reshka: {count_reshka}')
else:
    print(f'orel: {count_orel}')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

x = int(input('summa: '))
y = int(input('product: '))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input())
i = 0
while 2 ** i <= N:
    print(2 ** i, end=" ")
    i += 1