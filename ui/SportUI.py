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

    def print_group(self, groups_members, text, groups_name):
        print(text)
        for index, group_name in enumerate(groups_name):
            print("{}.{}".format(index + 1, group_name))
            for member in groups_members[index]:
                print("\tMembers ID:{}".format(member))

    def print_sentence(self):
        system("clear")
        print("Please Select one, If you want to quit press 'q' to go back press 'b'")
        print("-"*60)

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
        while action != "b" and action != "q" and action != "n":
            sport_list, sport_name_list = self.sport_service.get_all_sports()
            self.print_sport(sport_list, "All sports: ")
            sport_index = input("Select a sport: ")
            try:
                sport = sport_name_list[int(sport_index) - 1]
            except:
                action = self.not_a_valid_index()
                if action == "y":
                    continue
                else:
                    break
            if member_id:
                action = '1'
            else:
                self.print_sentence()
                action = input("1. See groups in that sport\n2. Add a group to that sport\n3. Delete that sport\n").lower()
            if action == "1":
                if member_id:
                    return self.view_groups(sport, member_id)
                else:
                    return self.view_groups(sport)
            elif action == "2":
                action = self.register_group(sport)
                action = "b"
            elif action == "3":
                self.member_service.remove_sport_from_members(sport, self.sport_service.sport_map[sport].get_all_members())
                self.sport_service.remove_sport(sport)
                print("Sport deleted")
                sleep(1)
                action = "b"
        return action

    def not_a_valid_index(self):
        self.print_sentence()
        print("Not valid index!")
        return input("Try again?").lower()


    def view_groups(self, sport, member_id = False):
        action = ''
        while action != "b" and action != "q":
            group_member_list, group_name_list = self.sport_service.get_all_groups(sport)
            texti = "All groups in {}:".format(sport)
            self.print_group(group_member_list, texti, group_name_list)
            if member_id:
                group_index = input("Select a group: ")
                try:
                    group = group_name_list[int(group_index) - 1]
                except:
                    action = self.not_a_valid_index()
                    if action == "y":
                        continue
                    else:
                        break
                self.print_sentence()
                leagal = self.sport_service.assign_member_to_group(member_id, sport, group)
                action = self.check_if_leagl(leagal, "Member")
                return 'b'
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
