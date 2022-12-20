import array as arr
def daynguoc():
    list = arr.array('i',[])
    n = int(input("Nhập số phần từ có trong dãy: "))
    for i in range(n):
        phantu = int(input("Nhập phần tử: "))
        list.insert(0, phantu)
    return list
a = daynguoc()
for i in range(len(a)):
    print(a[-1], end = " ")
    a = a[:1]