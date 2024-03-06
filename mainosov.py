#coding: utf-8

#Задание 23
x = int(input("Введите число: "))
y = int(input("Введите число: "))
r = int(input("Введите число: "))
R = int(input("Введите число: "))
print(r**2 < x**2 + y**2 < R**2)

#Заданире 24
x = int(input("Введите число: "))
y = int(input("Введите число: "))
if x > 0 and y > 0:
    print("1")
if x < 0 and y > 0:
    print("2 ")
if x < 0 and y < 0:
    print("3")
if x > 0 and y < 0:
    print("4 ")
#Задание 25

#Задание 26
x = int(input("Введите число: "))
y = int(input("Введите число: "))
if x > 0 and y > 0 or x < 0 and y > 0:
    print("координата находится в полуплоскости")
else:
    print("нет")
#Задание 27
a = int(input("Введите длину отрезка a: "))
b = int(input("Введите длину отрезка b: "))
c = int(input("Введите длину отрезка c: "))
if a + b > c and a + c > b and b + c > a:
    perimetr = a + b + c 
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))
    print("Периметр треугольника:", perimetr)
    print("Площадь трекгольника", area)
else:
    print("Треугольник с такими сторонами нету")