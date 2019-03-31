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

    def print_sports(self, group_list, sport_list, text):
        print(text)
        for index, sport_name in enumerate(sport_list):
            print("{}.{}".format(index + 1, sport_name))
            print("\tGroups:")
            for group in group_list[index]:
                print("\t{}".format(group))
    
    def print_members(self, members, text):
        system("clear")
        print(text)
        for member in members:
            print("="*30)
            print("\tID: {}\n{}".format(member[0], member[1]))
        print("="*30)


    def print_sentence(self):
        system("clear")
        print("Please Select one, If you want to quit press 'q' to go back press 'b'")
        print("-"*60)
    
    def action_eaquals_quit(self, action):
        if action == "q":
            return action
        return ""


    def look_up_a_member(self):
        action = ""
        while action != "b" and action != "q" and action != "n":
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
        return self.action_eaquals_quit(action)

    def check_if_id_is_valid(self, selected_id, member_list):
        inside = False
        try:
            selected_id = int(selected_id)
        except:
            return inside
        for member in member_list:
            if selected_id == member[0]:
                year = member[1].birth_year
                inside = True
                break
        return inside, selected_id, year

    def allow_actions_with_member(self, member_list):
        action = ''
        while action != "b" and action != "q" and action != "n":
            if member_list != []:
                selected_id = input("Select a member's ID: ")
                inside, selected_id, year = self.check_if_id_is_valid(selected_id, member_list)
                if inside:
                    self.print_sentence()
                    action = input("Do you want to:\n1. Sign a member to a sport\n2. View all sports for that member\n3. Delete member\n").lower()
                    if action == "1":
                        action = self.sportUi.view_all_sports(selected_id, year)
                    elif action == "2":
                        while action != "b" and action != "q" and action != 'n':
                            sport_list, group_list = self.member_service.get_all_sports_for_member(selected_id)
                            if sport_list != []:
                                texti = "Sports for member {}".format(selected_id)
                                self.print_sports( group_list, sport_list, texti)
                                question = input('Do you want remove member from any sport?(y/n)').lower()
                                if question == "y":
                                    sport = int(input("Select a sport"))
                                    try:
                                        self.member_service.remove_sport_from_member(selected_id, sport_list[sport-1])
                                        self.sport_service.remove_member_from_selected_sport(selected_id, sport_list[sport-1])
                                        print("Member successfully removed from sport and all groups in that sport")
                                        sleep(1)
                                    except:
                                        print("invalid sport")
                                        action = input("want to try again?").lower()
                                else:
                                    action = "n"
                            else:
                                print("Member not assigned to any sport!")
                                sleep(1)
                                action = "n"
                    elif action == "3":
                        self.sport_service.remove_member_from_sports(selected_id, self.member_service.members_map[selected_id].sports)
                        self.member_service.remove_member(selected_id)
                        print("Member deleted")
                        sleep(2)
                        action = "b"
                else:
                    self.print_sentence
                    print("Invalid ID!")
                    action = input("Try again?")
            else:
                print("No members in system")
                actions = "b"
        return self.action_eaquals_quit(action)

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
                member_list = self.member_service.get_member_orderd_by_sport()
                self.print_members(member_list, "")
        return self.action_eaquals_quit(action)

    def register_new_member(self):
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        year = input("Year of birth: ")
        self.member_service.add_member(name, phone, email, year)
        print("Member registerd")
        sleep(2)
        return 'OK'
