from Models.bst import BinarySearchTree
from Models.Queue import LinkedList

class SportGroup:

    def __init__(self, sport, name, age_from, age_to, capacity):
        self.sport = sport
        self.name = name
        self.age_from = age_from
        self.age_to = age_to
        self.capacity = int(capacity)
        self.members = []
        self.queue = LinkedList()
        self.size = 0

    def add_member(self, member_id):
        if member_id in self.members:
            return False
        if self.size >= self.capacity:
            self.add_to_waiting_queue(member_id)
            return None
        else:
            self.members.append(member_id)
            self.size += 1
            return True
        
    def remove_member(self, member_id):
        if member_id in self.members:
            self.members.remove(member_id)
            if self.queue.size > 0:
                self.add_member(self.queue.pop())

    def __str__(self):
        return "{}: {}-{} years".format(self.name, self.age_from, self.age_to)

    def add_to_waiting_queue(self, member_id):
        self.queue.add(member_id)

    def get_next_in_waiting_queue(self):
        return self.queue.pop()