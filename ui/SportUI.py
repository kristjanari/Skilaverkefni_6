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
        for index, sport in enumerate(sports):
            print("\t{}. {}".format(index + 1, sport))

    def print_group(self, groups, text, groups_name):
        print(text)
        for index, group_name in enumerate(groups_name):
            print("{}.{}".format(index + 1, group_name))
            for member in groups[index]:
                print("\tMember:{}".format(member))

    def print_sentence(self):
        system("clear")
        print("Please Select one, If you want to quit press 'q' to go back press 'b'")
        print("-"*30)

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
            sport_list, sport_name_list = self.sport_service.get_all_sports()
            self.print_sport(sport_list, "All sports: ")
            sport_index = input("Select a sport: ").lower()
            try:
                sport = sport_name_list[int(sport_index) - 1]
                self.print_sentence()
                if member_id:
                    action = '1'
                else:
                    action = input("1. See groups in that sport\n2. Add a group to that sport\n3. Delete that sport\n").lower()
                if action == "1":
                    if member_id:
                        action = self.view_groups(sport, member_id)
                        return action
                    else:
                        action = self.view_groups(sport)
                elif action == "2":
                    action = self.register_group(sport)
                elif action == "3":
                    self.member_service.remove_sport_from_members(sport, self.sport_service.sport_map[sport].get_all_members())
                    self.sport_service.remove_sport(sport)
                    print("Sport deleted")
                    sleep(1)
                    action = "b"
            except:
                self.print_sentence()
                print("Not valid index!")
                action = input("Try again?")
        return action

    def view_groups(self, sport, member_id = False):
        action = ''
        while action != "b" and action != "q":
            group_list, group_name_list = self.sport_service.get_all_groups(sport)
            texti = "All groups in {}:".format(sport)
            self.print_group(group_list, texti, group_name_list)
            if member_id:
                group_index = input("Select a group: ").lower()
                try:
                    group = group_name_list[int(group_index) - 1]
                    self.print_sentence()
                    leagal = self.sport_service.assign_member_to_group(member_id, sport, group)
                    action = self.check_if_leagl(leagal, "Member")
                    return 'b'
                except:
                    self.print_sentence()
                    print("Not valid index!")
                    action = input("Try again?")
            else:
                ok = input("Press enter to continu")
                return 'b'
        return action

    def register_sport(self):
        name = input("Name: ")
        leagl = self.sport_service.add_sport(name)
        return self.check_if_leagl(leagl, name)

    def register_group(self, sport):
        name = input("Name: ")
        age_from = input("Age From: ")
        age_to = input("Age limit: ")
        leagal = self.sport_service.add_group(name, age_from, age_to, sport)
        return self.check_if_leagl(leagal, name)

    def check_if_leagl(self, leagal, texti):
        if leagal:
            print("{} registerd".format(texti))
            sleep(1)
            return "ok"
        print("{} already excist".format(texti))
        sleep(1)
        return "ok"
