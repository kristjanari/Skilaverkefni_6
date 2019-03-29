from sortedcontainers import *
# from bst import BinarySearchTree

class Member:

    def __init__(self, name, phone, email, birth_year):
        self.name = name
        self.phone = phone
        self.email = email
        self.birth_year = birth_year

    def __str__(self):
        return "Name: {}\nPhone number: {}\nEmail: {}\nYear of birth: {}\n".format(self.name,
            self.phone, self.email, self.birth_year)


# class Sport:

#     def __init__(self, name):
#         self.name = name
#         self.members = BinarySearchTree()

#     def add_member(self, member_id):
#         self.members.add(member_id)

#     def remove_member(self, member_id):
#         self.members.remove(member_id)

