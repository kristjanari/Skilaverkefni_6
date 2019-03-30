from Models.bst import BinarySearchTree

class SportGroup:

    def __init__(self, sport, name, age_from, age_to):
        self.sport = sport
        self.name = name
        self.age_range = range(age_from,age_to + 1)
        self.members = BinarySearchTree()

    def add_member(self, member_id):
        self.members.add(member_id)

    def remove_member(self, member_id):
        self.members.remove(member_id)