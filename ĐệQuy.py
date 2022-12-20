def giaithuat(n):
    gt = 1
    if n == 1:
        gt = 1
    else:
        gt = giaithuat(n - 1) + n
    return gt
n = int(input("Nhập số: "))
print(giaithuat(n))