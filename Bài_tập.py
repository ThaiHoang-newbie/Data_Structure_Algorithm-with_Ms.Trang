"""def somu(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        c = somu(a, n - 1) * a
        return c
a = int(input())
n = int(input())
print(somu(a, n))"""
#
import array as arr
list = arr.array('i',[])
listFake = arr.array('i',[])
x = int(input("Nhập số phần tử: "))
for i in range(x):
    list.append(int(input("Nhập: ")))
def sum():
    x = 0
    for i in list:
        x = x + i
    return x
print("Tổng là",sum())


e = int(input("Nhập số cần tìm: "))
b = 0

for i in range(len(list)):
    if list[i] == e:
        listFake.append(i)
        b =  b + 1
if b >= 1:
    print("Vị trí của " + str(e) + " là: ",end="")
    for i in range(len(listFake)):
        print(listFake[i],end = " ")
else:
    print("Dãy này không có số" + str(e))
print()
for i in range(0, len(list)):
    for j in range(i + 1, x):
        if list[i] < list[j]:
            none = list[i]
            list[i] = list[j]
            list[j] = none
print("dãy sắp xếp theo thứ tự giảm dần: ", list)

