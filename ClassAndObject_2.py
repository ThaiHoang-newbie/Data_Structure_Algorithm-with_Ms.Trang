class HSSV:
    def __init__(self, ten, tuoi, gioitinh):
        self.ten
        self.ten = ten
        self.tuoi = tuoi
        self.gioitinh = gioitinh
x = int(input("Nhập số HSSV: "))
for i in range(x):
    a = input("Nhập tên: ")
    b = input("Nhập tuổi: ")
    c = input("Nhập giới tính: ")
    m = HSSV(a, b, c)  
    print(m.ten, m.tuoi, m.gioitinh)