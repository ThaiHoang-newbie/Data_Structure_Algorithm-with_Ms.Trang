def somu(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        c = somu(a, n - 1) * a
        return c
a = int(input())
n = int(input())
print(somu(a, n))

