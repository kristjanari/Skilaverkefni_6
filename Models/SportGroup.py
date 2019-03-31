from Models.bst import BinarySearchTree

class SportGroup:

    def __init__(self, sport, name, age_from, age_to):
        self.sport = sport
        self.name = name
        self.age_from = age_from
        self.age_to = age_to
        self.members = []

    def add_member(self, member_id):
        if member_id in self.members:
            return False
        self.members.append(member_id)
        return True
        
    def remove_member(self, member_id):
        if member_id in self.members:
            self.members.remove(member_id)

    def __str__(self):
        return "{}: {}-{} years".format(self.name, self.age_from, self.age_to)