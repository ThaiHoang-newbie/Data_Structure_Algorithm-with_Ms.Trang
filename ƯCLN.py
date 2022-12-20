"""def ucln(p,q):
    c = 0
    if p %  q == 0:
        c = q
    else:
        if p % q != 0:
            c = ucln(q, p%q)
    return c
p = int(input("Nhập số thứ nhất:"))
q = int(input("Nhập số thứ hai:"))
if p < q:
    while p < q:
        p = int(input("Nhập lại số thứ nhất:"))
        q = int(input("Nhập lại số thứ hai:"))
print(ucln(p,q))"""

def ucln(p,q):
    c = p % q 
    if p % q == 0:
        c = q
    else:
        while p % q != 0:
            p = q
            q = c
            c = p % q
    return q
p = int(input("Nhập số thứ nhất:"))
q = int(input("Nhập số thứ hai:"))
if p < q:
    while p < q:
        p = int(input("Nhập lại số thứ nhất:"))
        q = int(input("Nhập lại số thứ hai:"))
print(ucln(p,q))

            
    