from os import system, name
from time import sleep

class SportUI:

    def __init__(self, MemberService, SportService):
        self.member_service = MemberService
        self.sport_service = SportService

    def save(self):
        self.sport_service.save_sports()

    def print_sport(self, sports, text):
        system("clear")
        print(text)
        for sport in sports:
            print("{}".format(sport))

    def print_group(self, groups, text):
        system("clear")
        print(text)
        for group in groups:
            print(group[0])
            for member in group[1]:
                print("{:>5}".format(member))

    def print_sentence(self):
        system("clear")
        print("Please Select one, If you want to quit press 'q' to go back press 'b'")

    def sport_menu(self):
        action = ''
        while action != "b" and action != "q":
            self.print_sentence()
            action = input("1. Register sport\n2. View all sports\n").lower()
            if action == "1":
                action = self.register_sport()
            elif action == "2":
                action = self.view_all_sports()
        return action

    def view_all_sports(self, member_id = False):
        action = ''
        while action != "b" and action != "q":
            sport_list = self.sport_service.get_all_sports()
            self.print_sport(sport_list, "All sports: ")
            sport = input("Select a sport: ").lower()
            self.print_sentence()
            if member_id:
                action = input("1. Sign a member to a sport and see groups to that sport\n2. Delete a sport\n").lower()
            else:
                action = input("1. See groups to that sport\n2. Delete a sport\n").lower()
            if action == "1":
                if member_id:
                    action = self.view_groups(sport, member_id)
                    return action
                else:
                    action = self.view_groups(sport)
            elif action == "2":
                self.member_service.remove_sport_from_members(sport, self.sport_service.sport_map[sport].get_all_members())
                self.sport_service.remove_sport(sport)
                print("Sport deleted")
                sleep(2)
                action = "b"
        return action

    def view_groups(self, sport, member_id = False):
        action = ''
        while action != "b" and action != "q":
            group_list = self.sport_service.get_all_groups(sport)
            texti = "All groups in {}:".format(sport)
            self.print_group(group_list, texti)
            if member_id:
                group = input("Select a group: ").lower()
                self.print_sentence()
                action = input("1. sign a member to that \n2. Delete a sport\n").lower()
                self.sport_service.sign_member_to_group(member_id, sport, group)
            else:
                ok = input("Press enter to continu")
                return 'b'
        return action

    def register_sport(self):
        name = input("Name: ").lower()
        self.sport_service.add_sport(name)
        print("Sport registerd")
        sleep(2)
        return 'OK'
