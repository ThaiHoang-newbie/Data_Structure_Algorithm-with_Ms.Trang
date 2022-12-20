# Bài 1
list = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    a = input("Nhập phần tử thứ " + str(i + 1) + ":")
    list.append(a)
for i in range(len(list)):
    print("Phần tử thứ " + str(i+1) + " là:",list[i])
    
# Bài 2
list = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    a = int(input("Nhập phần tử thứ " + str(i + 1) + ":"))
    list.append(a)
b = 0
for i in range(len(list)):
    b = list[i] + b
print(b)

# Bài 3
list = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    a = int(input("Nhập phần tử thứ " + str(i + 1) + ":"))
    list.append(a)
a = 0
x = int(input("Nhập số bạn muốn tìm trong dãy"))
for i in list:
    if i == x:
        a = a + 1
if a == 0:
    print("Dãy này không có số " + str(x))
else:
    print("Dãy này có số " + str(x))
    
# Bài 4
list = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    a = int(input("Nhập phần tử thứ " + str(i + 1) + ":"))
    list.append(a)
for i in range(n):
    for j in range(i + 1, n):
        if list[i] > list[j]:
                b = list[i]
                list[i] = list[j]
                list[j] = b
for i in range(len(list)):
    print(list[i])
    
# Exercise 1 with array
import array as arr 
n = arr.array('i',[])
b = 0
x = int(input("Nhập số phần tử: "))
for i in range(x):
    a = int(input("Nhập phần tử thứ " + str(i + 1) + ":"))
    n.append(a)
for i in range(x):
    for j in range(i + 1, x):
        if n[i] > n[j]:
                b = n[i]
                n[i] = n[j]
                n[j] = b
print(n)

# Exercise 2 with array
import array as arr 
A = arr.array('i',[])
x = int(input("Nhập số phần tử của dãy A: "))
for i in range(x):
    a = int(input("Nhập phần tử thứ " + str(i + 1) + " của dãy A:"))
    A.append(a)
B = arr.array('i',[])
x = int(input("Nhập số phần tử của dãy B: "))
for i in range(x):
    a = int(input("Nhập phần tử thứ " + str(i + 1) + " của dãy B:"))
    B.append(a)
C = A + B
print(C)

# Exercise 3 with array
import array as arr 
X = arr.array('f',[])
x = int(input("Nhập số phần tử của dãy A: "))
for i in range(x):
    a = float(input("Nhập phần tử thứ " + str(i + 1) + " của dãy A:"))
    X.append(a)
search = float(input("Nhập số cần tìm: "))
print(X)
if search not in X:
    print("Dãy này không có số " + str(search))
else:
    print("Dãy này có số " + str(search) + " ở vị trí ",end = "")
    for i in range(x):
        if X[i] == search:
            print(i, end = "  ")
            
# Bài: Nhập một dãy số nguyên từ bàn phím, sắp xếp chúng theo thứ tự tăng dần
# Bài: Nhập một dãy số nguyên từ bàn phím, cho biết số lần xuất hiện của từng số trong dãy số

import array as arr
a = arr.array('i',[])
phantu = int(input("Nhập số phần tử: "))
for i in range(phantu):
    x = int(input("Nhập số phần tử thứ" + str(i+1) + ":"))
    a.append(x)
for i in range(0, len(a) -1):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            none = a[i]
            a[i] = a[j]
            a[j] = none
print(a)
"""b = int(input("Nhập số cần biết số lần xuất hiện: "))
count = a.count(b)
print(count)"""
def dem(a, n, b):
    c = 0 
    for i in range(n):
        if x == a[i]:
            c += 1
    return c
n = len(a)
b = int(input("Nhập số cần biết số lần xuất hiện: "))
print(dem(a, n , b))