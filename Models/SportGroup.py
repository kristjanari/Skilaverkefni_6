from Models.bst import BinarySearchTree
from Models.Queue import LinkedList
import datetime

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

    def add_member(self, member_id, year):
        question = self.is_member_right_age(year)
        if member_id in self.members or not question:
            return False, question
        if self.size >= self.capacity:
            self.add_to_waiting_queue((member_id, year))
            return None, question
        else:
            self.members.append(member_id)
            self.size += 1
            return True, question
        
    def remove_member(self, member_id_year_tuple):
        if member_id_year_tuple[0] in self.members:
            self.members.remove(member_id_year_tuple[0])
            if self.queue.size > 0:
                new_member = self.queue.pop()
                self.add_member(new_member[0], new_member[1])

    def __str__(self):
        return "{}: {}-{} years".format(self.name, self.age_from, self.age_to)

    def add_to_waiting_queue(self, member_id):
        self.queue.add(member_id)

    def get_next_in_waiting_queue(self):
        return self.queue.pop()
        
    def is_member_right_age(self, year):
        date = datetime.datetime.now()
        age = int(date.year) - int(year)
        if int(self.age_from) <= age and int(self.age_to) >= age:
            return True
        return False
