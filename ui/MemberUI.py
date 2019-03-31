from os import system, name
from time import sleep
from ui.SportUI import SportUI



class MemberUI:

    def __init__(self, MemberService, SportService):
        self.member_service = MemberService
        self.sport_service = SportService
        self.sportUi = SportUI(self.member_service, self.sport_service)

    def save(self):
        self.member_service.save_members()

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
                    print("Member {} :\n\tID: {}\n{}".format(index + 1, member[0], member[1]))


    def print_sentence(self):
        system("clear")
        print("Please Select one, If you want to quit press 'q' to go back press 'b'")

    def look_up_a_member(self):
        action = ""
        while action != "n":
            self.print_sentence()
            print('Look up a member by:')
            action = input("1. Name\n2. Phone\n3. Email\n4. Year of birth\n").lower()
            member_list = False
            if action == "1":
                name = input("Name: ")
                member_list = self.member_service.find_member(name, "name")
                text = "Members named {}:".format(name)
            elif action == "2":
                phone = input("Phone: ")
                member_list = self.member_service.find_member(phone, "phone")
                text = "Members with phone number {}:".format(phone)
            elif action == "3":
                email = input("Email: ")
                member_list = self.member_service.find_member(email, "email")
                text = "Members with email {}:".format(email)
            elif action == "4":
                year = input("Year: ")
                member_list = self.member_service.find_member(year, "year")
                text = "Members born {}:".format(year)
            if member_list:
                self.print_members(member_list, text)
                return self.allow_actions_with_member(member_list)
            action = input("Member not found, do you want to search again? (y/n)").lower()
        return "b"

    def check_if_id_is_valid(self, selected_id, member_list):
        inside = False
        for member in member_list:
            if int(selected_id) == member[0]:
                inside = True
        return inside

    def allow_actions_with_member(self, member_list):
        action = ''
        while action != "b" and action != "q":
            selected_id = input("Select a member's ID: ")
            inside = self.check_if_id_is_valid(selected_id, member_list)
            if inside:
                self.print_sentence()
                action = input("Do you want to:\n1. Sign a member to a sport\n2. Remove member from a sport\n3. Delete member\n").lower()
                if action == "1":
                    action = self.sportUi.view_all_sports(selected_id)
                elif action == "2":
                    pass
                elif action == "3":
                    self.sport_service.remove_member_from_sports(int(selected_id), self.member_service.members_map[int(selected_id)].sports)
                    self.member_service.remove_member(int(selected_id))
                    print("Member deleted")
                    sleep(2)
                    action = "b"
            else:
                self.print_sentence
                print("Invalid ID!")
                action = input("Try again?")
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
                member_list = self.member_service.get_member_orderd_by_name()
                self.print_members(member_list, "")
                return self.allow_actions_with_member(member_list)
            elif action == "2":
                member_list = self.member_service.get_member_orderd_by_year()
                self.print_members(member_list, "")
                return self.allow_actions_with_member(member_list)
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
        sleep(2)
        return 'OK'
