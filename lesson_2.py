# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

a = ['0', '0', '0', '0', '0']
for i, b in enumerate(a):
    print (i + 1, b)

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print("Вы можете ввести 10 цифр")
i = 0
count = 0
for i in range(1, 11):
    print("Введите цифру:")
    a = int(input())
    if a == 5:
        count += 1
print("Цифра 5 введена", count, "раз")

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# Код из лекции
a = 0
for i in range(1,101):
    a += i
print("Сумма чисел от 1 до 100 = ", a)

# Вариант 2

a = 100
i = 1
b = 0
while i <= a:
    b = b + i
    i = i + 1
print("Сумма чисел от 1 до ", a, "=", b)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

a = 1
for i in range(1,11):
    a *= i
print("Произведение чисел от 1 до 10 =", a)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

a = 2129
b = []
while a > 0:
    b.append(a % 10)
    a = a//10
b.reverse()
for i in range(len(b)):
    print(b[i])

'''
Задача 6
Найти сумму цифр числа.
'''
a = int(input("Введите число и нажмите Enter:"))
b = 0
while a > 0:
    b += (a % 10)
    a = a//10
print(b)

'''
Задача 7
Найти произведение цифр числа.
'''
a = int(input("Введите число и нажмите Enter:"))
b = 1
while a > 0:
    b *= (a % 10)
    a = a//10
print(b)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
a = int(input("Введите число:"))
while a > 0:
    if a % 10 == 5:
        print ("Среди цифр есть число 5")
        break
    a = a//10
else:
    print("Среди цифр нет числа 5")

'''
Задача 9
Найти максимальную цифру в числе
'''
a = int(input("Введите число:"))
b = a % 10
while a > 0:
    if a%10 > b:
        b = a%10
    a = a//10
print(b)

'''
Задача 10
Найти количество цифр 5 в числе
'''

a = int(input("Введите число:"))
count = 0
while a > 0:
    if a % 10 == 5:
        count += 1
    a = a//10
print("Количество цифр 5 в числе равно", count)

