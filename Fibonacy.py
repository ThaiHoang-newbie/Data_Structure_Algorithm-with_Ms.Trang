def fibonacy(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacy(n - 1) + fibonacy(n - 2)
n = int(input())
print(fibonacy(n))