from Models.bst import BinarySearchTree
import datetime

class SportGroup:

    def __init__(self, sport, name, age_from, age_to):
        self.sport = sport
        self.name = name
        self.age_from = age_from
        self.age_to = age_to
        self.members = []

    def add_member(self, member_id, year):
        question = self.is_member_right_age(year)
        if member_id in self.members or not question:
            return False, question
        self.members.append(member_id)
        return True, question
        
    def remove_member(self, member_id):
        self.members.remove(member_id)

    def __str__(self):
        return "{}: {}-{} years".format(self.name, self.age_from, self.age_to)

    def is_member_right_age(self, year):
        date = datetime.datetime.now()
        age = date.year - year
        if self.age_from <= age and self.age_to <= year:
            return True
        return False
