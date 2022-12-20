# Bài tập 6. Viết chương trình con dùng cài đặt danh sách bằng mảng:
#a. Nhận 1 dãy các số nguyên nhập từ bàn phím và lưu trữ nó theo đúng thứ tự nhập vào
#b. Nhận 1 dãy các số nguyên nhập từ bàn phím và lưu trữ theo thứ tự ngược lại với thứ tự nhập vào.
#c. In ra màn hình các phần tử trong danh sách theo thứ tự của nó trong danh sách.
import array as arr
def dayXuoi():
    list = arr.array('i',[])
    n = int(input("Nhập số phần từ có trong dãy: "))
    for i in range(n):
        phantu = int(input("Nhập phần tử: "))
        list.append(phantu)
    return list
def daynguoc():
    list = arr.array('i',[])
    n = int(input("Nhập số phần từ có trong dãy: "))
    for i in range(n):
        phantu = int(input("Nhập phần tử: "))
        list.insert(0, phantu)
    return list
a = dayXuoi()
for i in range(len(a)):
        print(a[i],end = " ")
print()
b = daynguoc()
for i in range(len(b)):
        print(b[i],end = " ")