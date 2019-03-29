class Node:

    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        self.root = self._add(value, self.root)
        self.size += 1
        
    def _add(self, value, node):
        if node != None:
            if value < node.data:
                node.left = self._add(value, node.left)
            if value > node.data:
                node.right = self._add(value, node.right)
        if node == None:
            return Node(value)
        return node

    def contains(self, value):
        return self._contains(value, self.root)
        
    def _contains(self, value, node):
        if node == None:
            return False
        if value < node.data:
            return self._contains(value, node.left)
        if value > node.data:
            return self._contains(value, node.right)
        return True

    def remove(self, value):
        self._remove(value, self.root)
        self.size -= 1

    def _remove(self, value, node):
        if value < node.data:
            node.left = self._remove(value, node.left)
        elif value > node.data:
            node.right = self._remove(value, node.right)
        else:
            node = self.remove_node(node)
        return node

    def remove_node(self, node):
        if node.left == None and node.right == None:
            return None
        elif node.left == None:
            return node.right
        elif node.right == None:
            return node.left
        else:
            node.data = self.find_rightmost(node.left)
            return node
        
    def find_rightmost(self, node):
        if node.right == None:
            value = node.data
            self._remove(value, self.root)
            return value
        return self.find_rightmost(node.right)

    def __str__(self):
        if self.root.data == None:
            return ""
        return self.str_helper(self.root).strip()

    def str_helper(self, node):
        if node == None:
            return " "
        return self.str_helper(node.left) + str(node.data) + self.str_helper(node.right)
