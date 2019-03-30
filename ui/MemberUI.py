from ui.RegistrationUI import *
from os import system, name
from Service.MemberService import MemberService


class MemberUI:

    def __init__(self):
        self.member_service = MemberService()

    def member_menu(self):
        action = ''
        while action != "b" and action != "q":
            self.print_sentence()
            action = input("1. Register new member\n2. view all members\n3. Look up a member\n").lower()
            if action == "1":
                action = self.register_new_member()
            elif action == "2":
                action = self.view_all_members()
            elif action == "3":
                action =self.look_up_a_member()
        return action

    def print_members(self, members, text):
        system("clear")
        print(text)
        for index, member in enumerate(members):
                    print("Member {} :\nID: {}\n{}".format(index + 1, member[0], member[1]))

    def print_sentence(self):
        system("clear")
        print("Please Select one, If you want to quit press 'q' to go back press 'b'")

    def look_up_a_member(self):
        action = ""
        while action != "n":
            self.print_sentence()
            print('Look up a member by:')
            action = input("1. Name\n2. Phone\n3. Email\n4. Year of birth\n").lower()
            if action == "1":
                name = input("Name: ")
                member_list = self.member_service.look_up_a_member(name, "name")
                text = "Members named {}:".format(name)
            elif action == "2":
                phone = input("Phone: ")
                member_list = self.member_service.look_up_a_member(phone, "phone")
                text = "Members with phone number {}:".format(phone)
            elif action == "3":
                email = input("Email: ")
                member_list = self.member_service.look_up_a_member(email, "email")
                text = "Members with email {}:".format(email)
            elif action == "4":
                year = input("Year: ")
                member_list = self.member_service.look_up_a_member(year, "year")
                text = "Members born {}:".format(year)
            if member_list:
                self.print_members(member_list, text)
                selcted_id = input("Select a member's ID: ")
                return self.do_somthing_with_the_meber()
            action = input("Member not found, do you want to search again? (y/n)").lower()
        return "b"

    def do_somthing_with_the_meber(self):
        action = ''
        while action != "b" and action != "q":
            self.print_sentence()
            action = input("Do you want to:\n1. Sign a member to a sport\n2. Remove member from a sport\n3. Delete member\n").lower()
            if action == "1":
                pass
            elif action == "2":
                pass
            elif action == "3":
                pass
        if action == "q":
            return action
        return ""

    def view_all_members(self):
        action = ''
        while action != "b" and action != "q":
            self.print_sentence()
            print('Orderd by:')
            action = input("1. Name\n2. age\n3. sport\n").lower()
            if action == "1":
                pass
            elif action == "2":
                pass
            elif action == "3":
                pass
        if action == "q":
            return action
        return ""

    def register_new_member(self):
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        year = input("Year of birth: ")
        self.member_service.add_member(name, phone, email, year)
        print("Member registerd")
        return 'OK'
