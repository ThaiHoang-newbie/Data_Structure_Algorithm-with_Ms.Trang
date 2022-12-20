import array as arr
list = arr.array('i',[])
n = int(input("Nhập số phần tử của list: "))
for i in range(n):
    list.append(int(input("Nhập số thứ %d: "%(i + 1))))
for i in range(0,len(list) - 1):
    for j in range(i + 1, len(list)):
        if list[j] < list[i]:
            list[j] , list[i] = list[i] , list[j]
print(list)            
            