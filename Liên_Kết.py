"""# Hàm để khởi tạo
# Đối tượng nút
class Node: 
    def __init__(self, data = None):
        # Gán dữ liệu
        self.data = data
        # Khởi tạo tiếp theo dưới dạng vô giá trị
        self.next = None
class LinkedList: # Lớp danh sách đã được liên kết
    def __init__(self): # Hàm để khởi tạo
        self.head = None # Đối tượng danh sách được liên kết
list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.head.next = e2 # Liên kết nút đầu tiên với nút thứ hai
e2.next = e3 # Liên kết nút thứ hai với nút thứ ba"""

"""class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2 # Liên kết nút đầu tiên với nút thứ hai
e2.nextval = e3 # Liên kết nút thứ hai với nút thứ ba
list.listprint()"""

#Duyệt qua một danh sách liên kết
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()



#Chèn một phần tử vào danh sách

"""class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
# In danh sách liên kết
    def listprint(self):
        printval = self.headval
        while printval is not None:    
            print (printval.dataval)
            printval = printval.nextval
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.listprint()"""

