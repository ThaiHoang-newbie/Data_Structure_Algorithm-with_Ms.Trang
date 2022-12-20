# Câu 1a: Viết hàm đệ quy tính tổng các số từ 0 đến n ( n nguyên dương)

    
"""
def fibonacci(n):
    if n == 1:
        return 0;
    elif n==2:
        return 1;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) + 1;
x = int(input("Nhập số phần tử trong dãy Fibonacci mà bạn muốn tính tổng: "))

print(fibonacci(x))
"""

# Câu 1b: Viết hàm dảo ngược các phần tử trong mảng



"""
import array as arr

def daynguoc():
    list = arr.array('i',[])
    n = int(input("Nhập số phần từ có trong dãy: "))
    for i in range(n):
        phantu = int(input("Nhập phần tử: "))
        list.insert(0, phantu)
    return list
print(daynguoc())
"""


# Câu 2a: 	Viết hàm thực hiện giải thuật sắp xếp danh sách sinh viên giảm dần theo tuoi (tuổi) 
#           trên mảng mà mỗi phần tử là một sinh viên gồm maSV, ten, tuoi




# Câu 3: 

"""
a = int(input("Nhập a: "))
a = int(input("Nhập b: "))


a = a + b
b = a - b
a = a - b
print(a)
print(b)
"""




# Câu 4a: Viết hàm tìm giá trị của số FIBONACI thứ n (n>=2).



"""
def fibonacci(n):
    if n<0:
        return -1
    elif n==0 or n==1:
        return n
    else:
        return  fibonacci(n - 1) + fibonacci(n - 2)

n=int(input("Nhập n "))
for i in range(0,n):

    print(fibonacci(i))
"""



# Câu 4b: Viết hàm tìm các số không trùng lặp trong mảng các số nguyên




import array as arr

def check(l):
    l1 = []
    l2 = []
    for i in l:
        if i not in l1:
            l1.append(i)
        else:
            l2.append(i)
    for i in l2:
        if i in l1:
            l1.remove(i)
    return l1

l = arr.array('i',[])
n = int(input("Nhập số phần tử: "))
for j in range(n):
    l.append(int(input("Nhập số: ")))
print(check(l))



# Câu 4c:

"""
def fibonacci(n):
    if n<1:
        return -1
    elif n==1 or n==2:
        return n
    else:
        return  fibonacci(n - 1) + fibonacci(n - 2)+ 1;

n=int(input("Nhập n "))
print(fibonacci(n))
"""


#Câu 5a: Viết hàm in ra các số còn thiếu của mảng số nguyên a trong đoạn [a,b]



"""
import array as arr

def fill_blank(list, a, b):
    if a > b:
        while a > b:
            b = int(input("Nhập: "))
    for i in range(a, b - 1):
        list.append(i + 1)
    return list
l = arr.array('i',[])
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print(fill_blank(l, a, b))
"""

# Câu 7a: Viết hàm tính tổng n số nguyên tố đầu tiên



"""
def SNT(n):
    c = 2
    S = 0
    while n != 0:
        for i in range(2, c):
            if c % i == 0:
                break
        else:  
            S = S + c 
            n = n - 1
        c = c + 1 
    return S
n = int(input("Nhập số nguyên tố đầu tiên trong dãy mà bạn muốn tính tổng : "))   
print ("Tổng là: ",SNT(n))
"""




# Câu 7b: Viết hàm loại bỏ các số trùng lặp trong mảng các số nguyên




import array as arr

def check(l):
    l1 = []
    l2 = []
    for i in l:
        if i not in l1:
            l1.append(i)
        else:
            l2.append(i)
    for i in l2:
        if i in l1:
            l1.remove(i)
    return l1

l = arr.array('i',[])
n = int(input("Nhập số phần tử: "))
for j in range(n):
    l.append(int(input("Nhập số: ")))
print(check(l))



# Câu 9a: Viết hàm sắp xếp dãy số bằng thuật toán đổi chổ (Interchange)


















