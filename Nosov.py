#coding: utf-8

#Задание 1
a = int(input("Веведите первое число: "))
b = int(input("Веведите второе число: "))
if a > b:
    maximus = a
    minimus = b
else:
    maximus = b
    minimus = a
print("Ответ")
print("Максимальнок число:", maximus)
print("Минимальное число:", minimus)

#Задание 2
a = int(input("Введите сторону квадрата: "))
b = int(input("Введите радиус круга: "))
if 2*b <= a:
    print("круг впишется в квадрат")
else:
    print("круг не впишется в квадрат")
    
#Задание 3
a = int(input("Введите число: "))
if a > 0:
    b = 1/a*a
else:
    b = a*a
print(b)

#Задание 4
a = int(input("Введите сторону квадрата: "))
b = int(input("Введите радиус круга: "))
if 2*b >= a:
    print("квадрат впишется в круг")
else:
    print("квадрат не впишется в круг")

#Задание 5
a = int(input("Введите превое вещественное число: "))
b = int(input("Введите второе вещественное число: "))
if a > b:
    print("Первое вещественное число больше второго")
else:
    print("Второе вещесвтенное число больше первого")

#Задание 6
a = int(input("Введите число: "))
if a >= 0:
    b = 1/a*a
else:
    b = a*a
print(b)