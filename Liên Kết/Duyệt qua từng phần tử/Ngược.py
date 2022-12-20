class Node(object):
    def __init__(self):
        self.data = None # Chứa dữ liệu
        self.next = None # chứa tham chiếu đến nút tiếp theo
class LinkedList:
    def __init__(self):
        self.cur_node = None
    def add_node(self, data):
        new_node = Node() # tạo nút mới
        new_node.data = data
        new_node.next = self.cur_node # liên kết nút mới với nút trước đó
        self.cur_node = new_node #  đặt nút hiện tại thành nút mới
    def list_print(self):
        node = self.cur_node # không thể chỉ vào ll!
        while node:
            print (node.data)
            node = node.next
ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.list_print()
