import array as arr
numbers = arr.array('i',[])
print(numbers)
n = int(input("Nhập..."))
for j in range(n):
    #t = int(input("Nhập số thứ %d: "%(j + 1)))
    numbers.append(int(input("Nhập số thứ %d: "%(j + 1))))
print(numbers)
for i in range(len(numbers)):
    print(numbers[i])
numbersSum = sum(numbers)
print("Tổng là", numbersSum)