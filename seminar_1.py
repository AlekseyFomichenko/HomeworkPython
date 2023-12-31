# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

user_input = int(input('Введите число: '))
result = 0
while user_input > 0:
    result += user_input % 10
    user_input //= 10
print(f"Сумма цифр цисла: {result}")

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

'''
дано
x y z
s = x + y + z
x = z
s = x + y + x
y = 4x
s = x + 4x + x
x = s / 6
'''
user_input2 = int(input("Введите общее количество журавликов: "))
x = user_input2 / 6
print("Петя сделал {}, Катя сделала {}, Серега {}".format(x ,4 * x, x))

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket = input("Введите номер билета: ")
if len(ticket) != 6:
    print("Некорректно введён номер!")
else:
    result1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if result1: 
        print("Ура! У тебя счастливый билетик!")
    else:
        print("Увы, у тебя обычный билет")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите длину шололадки: "))
m = int(input("Введите ширину шоколадки: "))
k = int(input("Количество долек, которое хотите отломить: "))
if (k % n == 0 or k % m == 0) and k < m * n:
    print("Yes")
else:
    print("No")