
class Node:

    def __init__(self, next = None, data = None):
        self.next = next
        self.data = data

    def __str__(self):
        return str(self.data)

class LinkedList():

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(None, data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        if self.head == None:
            return
        value = self.head
        self.head = self.head.next
        self.size -= 1
        return value

    def get_string(self, node):
        if node == None:
            return ""
        if node.next == None:
            return str(node)
        else:
            return str(node) + " " + self.get_string(node.next)

    def get_size(self):
        return self.size

    def __str__(self):
        list_str = self.get_string(self.head)
        return list_str