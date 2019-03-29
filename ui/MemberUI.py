from ui.RegistrationUI import *
from os import system, name


class MemberUI:

    def __init__(self):
        pass

    def member_menu(self):
        action = ''
        while action != "b" and action != "q":
            system("clear")
            print("Please Select one, If you want to quit press 'q' to go back press 'b'")
            action = input("1. Register new member\n2. view all members\n3. Look up a member").lower()
            if action == "1":
                action = self.register_new_member
            elif action == "2":
                action = self.view_all_members()
            elif action == "3":
                action =self.look_up_a_member()
        return action

    def look_up_a_member(self):
        action = ''
        while action != "b" and action != "q":
            system("clear")
            print("Please Select one, If you want to quit press 'q' to go back press 'b'")
            print('Look up a member by:')
            action = input("1. Name\n2. Phone\n3. Email\n4. year of birth\n").lower()
            if action == "1":
                #send to a function that takes in name and returns member ID
                pass
            elif action == "2":
                #send to a function that takes in phone and returns member ID
                pass
            elif action == "3":
                #send to a function that takes in email and returns member ID
                pass
            elif action == "4":
                #send to a function that takes in year and returns member ID
                pass
            if action != "b" and action != "q":
                question = input("Do you want to:\n1. Sign a member to a sport\n2. Remove member from a sport\n3. Delete member\n4. Home\n")
                if question == "1":
                    pass
                elif action == "2":
                    pass
                elif action == "3":
                    pass
                elif action == "4":
                    action == "b"
        return action

    def view_all_members(self):
        action = ''
        while action != "b" and action != "q":
            system("clear")
            print("Please Select one, If you want to quit press 'q' to go back press 'b'")
            print('Orderd by:')
            action = input("1. Name\n2. age\n3. sport\n").lower()
            if action == "1":
                pass
            elif action == "2":
                pass
            elif action == "3":
                pass
        return action

    def register_new_member():
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        year = input("Year of birth: ")
        #SENDA UPPL YFIR i Servise
        print("Member registerd")
        return 'OK'
