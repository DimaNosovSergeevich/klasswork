#coding: utf-8

# Задача 1; 1)
n = 1 
while 3*n**4 - 730*n>= 5:
    n += 1 
print(n-1)
# Задача 1; 2)
m = 100
k = 0
while 4**k<m:
    k+=1
print(k-1)

# Задача 2
m = int(input("Введите число:"))
k = m//4
print("Наибольшее число ")

# Задача 3
n = int(input("Введите натуральное число: "))
r = (n+1)//2
b = 2 * r
print("Наименьшее 2R,которое превосходит n:",b)

# Задача 4
m = 10
fn_minus_2 = 1
fn_minus_1 = 1
fn = fn_minus_1 + fn_minus_2
while fn <= m:
    fn_minus_2 = fn_minus_1
    fn_minus_1 = fn 
    fn = fn_minus_1 + fn_minus_2
reselt = fn
print(fn)
