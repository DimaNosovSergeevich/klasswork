#Задание 25
x = abs(int(input("x")))
y = int(input("y"))
R = int(input("R"))
if y > 0:
    t = R - x
    c = ((t**2) + (y**2))**0.5
    print(c)
else:
    c = ((x**2) + (y**2))**0.5
    F = R - c
    print(F)