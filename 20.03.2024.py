#coding utf-8

#Задание1
a = [0,1]
n = int(input())
for i in range(2, n+1):
    f = a[i-2]+a[i-1]
    a.append(f)
print(a)

#Задание2
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17]
b =[]
for i in a:
    if i % 2 == 0:
         b.append(i)
print(b)    

#Задание3
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17]
b = []
c = []
for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)
print(b, c)  

#Задание4
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17]
b = a
for i in a:
    if i % 3 == 0:
        a.append(i)
print(a)

#Задание5
a = int(input())
b = int(input())
c = int(input())
d = []
for i in range(a,b,c):
    d.append(i)
print(sorted(d, reverse=True))