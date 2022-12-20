#Xuôi
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def add_node_x(self, dataval):
        NewNode = Node(dataval)
        if self.headval is None:
            self.headval = NewNode
            return
        lastval = self.headval
        while(lastval.nextval):
            lastval = lastval.nextval
        lastval.nextval=NewNode
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
list1 = SLinkedList()
n = int(input("Nhập số phần tử: "))
for i in range(n):
    m = input("Nhập phần tử: ")
    list1.add_node_x(m)
list1.listprint()

#Ngược
class Node(object):
    def __init__(self):
        self.data = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.headval = None
    def add_node(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.headval
        self.headval = new_node
    def list_print(self):
        node = self.headval
        while node:
            print (node.data)
            node = node.next
list2 = LinkedList()
n = int(input("Nhập số phần tử: "))
for i in range(n):
    m = input("Nhập phần tử: ")
    list2.add_node(m)
list2.list_print()