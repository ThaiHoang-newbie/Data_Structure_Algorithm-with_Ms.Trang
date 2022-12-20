# S = 1 + 2 + 3 +..... + n
def sum(n):
    if n == 1:
        return 1
    else:
        a = sum(n - 1) * n
    return a
n = int(input("Nhập số: "))
print(sum(n))
# S = 2 + 4 + 6 +..... + 2n
def chan(n):
    if n == 1:
        return 2
    else:
        a = chan(n - 1) + n*2
    return a
n = int(input("Nhập số: "))
print(chan(n))
# S = 1 + 3 + 5 +..... + (2n -1)
def le(n):
    if n == 1:
        return 1
    else:
        a = le(n - 1) + (n *2 - 1)
    return a
n = int(input("Nhập số: "))
print(le(n))
# Hàm Q(a, b) = 0 nếu a < b
# Hàm Q(a, b) = Q(a - b, b) + 1 nếu a > b
def ham(a, b):
    q = 0
    if a < b:
        q = 0
    else:
        q = ham(a - b, b) + 1
    return q
a = int(input("Nhập số: "))
b = int(input("Nhập số: "))
print(ham(a, b))
