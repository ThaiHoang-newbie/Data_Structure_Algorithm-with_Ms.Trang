import array as arr
def nhi(n):
    list = arr.array('i',[])
    while n != 0:
        m = n % 2
        n = n // 2 
        list.append(m)
    list1 = list[::-1]
    for i in list1:
        x = x + str(i)
    return x
n = int(input("Nhập số thập phân muốn đổi sang nhị phân: "))
print(nhi(n))
