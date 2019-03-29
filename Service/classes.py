from sortedcontainers import *
from bst import BinarySearchTree

class Member:

    def __init__(self, name, phone, email, birth_year):
        self.name = name
        self.phone = phone
        self.email = email
        self.birth_year = birth_year

    def __str__(self):
        return "Name: {}\nPhone number: {}\nEmail: {}\nYear of birth: {}\n".format(self.name,
            self.phone, self.email, self.birth_year)

class Members:

    def __init__(self, name):
        self.members_map = {} 
        self.name_map = SortedDict()
        self.phone_map = {}
        self.email_map = {}
        self.year_map = SortedDict()
        self.unique_id = 1

    def add_member(self, member):
        self.members_map[self.unique_id] = member
        self.name_map[member.name] = self.name_map.get(member.name,[]) + [self.unique_id]
        self.phone_map[member.phone] = self.phone_map.get(member.phone,[]) + [self.unique_id]
        self.email_map[member.email] = self.unique_id
        self.year_map[member.birth_year] = self.year_map.get(member.birth_year ,[]) + [self.unique_id]
        self.unique_id += 1

    def remove_member(self, id):
        member = self.members_map.get(id)
        if contact != None:
            if len(self.name_map[member.name]) > 1:
                self.name_map[member.name].remove(id)
            else:
                del self.name_map[member.name]
            if len(self.phone_map[member.phone]) > 1:
                self.name_map[member.phone].remove(id)
            else:
                del self.phone_map[member.phone]
            del self.email_map[member.phone]
            if len(self.year_map[member.birth_year]) > 1:
                self.name_map[member.birth_year].remove(id)
            else:
                del self.year_map[member.birth_year]
            del self.members_map[id]


class Sport:

    def __init__(self, name):
        self.name = name
        self.members = BinarySearchTree()

    def add_member(self, member_id):
        self.members.add(member_id)

    def remove_member(self, member_id):
        self.members.remove(member_id)

