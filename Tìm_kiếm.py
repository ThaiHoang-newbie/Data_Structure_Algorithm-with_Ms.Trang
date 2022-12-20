# Tìm kiếm tuần tự
"""def search():
    list = []
    n = int(input("Nhập số phần tử của list: "))
    for i in range(n):
        list.append(int(input("Nhập số thứ %d: "%(i + 1))))
    tim = int(input("Nhập số cần tìm: "))
    for i in list:
        if tim == list[i]:
            return i
print(search())"""

# Tìm kiếm nhị phân

"""def search():
    list = [2 , 4, 6, 8, 9, 10, 14, 58, 100]
    left = 0
    right = len(list)-1
    while left <= right:
        mid = (left + right)// 2
        if list[mid] == tim:
            return "abc"
        elif list[mid] < tim:
            right = mid + 1
        else:
            left = mid - 1
    return -1
tim = int(input("Nhập ..."))
print(search())"""

def binary_search(a, x, low = 0, high = None):
    if high is None:
        high = len(a)
    while low < high:
        mid = (low + high )//2
        midval = a[mid]
        if midval < x:
            low = mid+1
        elif midval > x: 
            high = mid
        else:
            return mid
    return -1
a = [ 2, 3, 4, 10, 40 ]
x = 10
print("Số cần tìm ở vị trí",binary_search(a, x, low = 0, high = None))