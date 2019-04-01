
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
        return value.data
    
    def remove(self, id):
        if self.head == None:
            return
        if self.head.data[0] == id:
            self.head = self.head.next
            self.size -= 1
            return
        self.remove_helper(self.head, id)

    def remove_helper(self, node, id):
        if node.next == None:
            return
        if node.next.data[0] == id:
            node.next = node.next.next
            self.size -= 1
            return
        self.remove_helper(node.next, id)

    def get_size(self):
        return self.size