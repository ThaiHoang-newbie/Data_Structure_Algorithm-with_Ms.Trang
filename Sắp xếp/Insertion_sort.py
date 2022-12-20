import array as arr
def insertion_sort(list): 
    list = arr.array('i',[])
    n = int(input("Nhập số phần tử của list: "))
    for i in range(n):
        list.append(int(input("Nhập số thứ %d: "%(i + 1)))) 
    for i in range(1, len(list)):  
        value = list[i]
        j = i - 1  
        while j >= 0 and value < list[j]:  
            list[j + 1] = list[j]  
            j -= 1  
        list[j + 1] = value  
    return list
"""
a = insertion_sort(list)
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
x = int(input("Nhập số cần tìm: "))
b = binary_search(a, x, low = 0, high = None)
if b == -1:
    print("Dãy này không có số cần tìm")
else:
    print("Số cần tìm ở vị trí",binary_search(a, x, low = 0, high = None))"""
