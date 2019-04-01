from os import system, name
from time import sleep
import datetime

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

    def print_group(self, groups_members, text):
        print(text)
        for  index, group in enumerate(groups_members):
            print("{}.{}".format(index + 1, group))
            print("\tMembers:")
            for member in group.members:
                print("\tID: {}\tName: {}".format(member, self.member_service.members_map.get(int(member)).name))

    def print_sentence(self):
        system("clear")
        print("Please Select one, If you want to quit press 'q' to go back press 'b'")
        print("-"*60)

    def action_eaquals_quit(self, action):
        if action == "q":
            return action
        return ""


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

    def view_all_sports(self, member_id = False, year = None):
        action = ''
        while action != "b" and action != "q" and action != "n":
            sport_list, sport_name_list = self.sport_service.get_all_sports()
            if sport_list != []:
                self.print_sport(sport_list, "All sports: ")
                sport_index = input("Select a sport: ")
                try:
                    sport = sport_name_list[int(sport_index) - 1]
                except:
                    action = self.not_a_valid_index()
                    if action == "y":
                        continue
                    else:
                        return "b"
                if member_id:
                    action = '1'
                else:
                    self.print_sentence()
                    texti = "1. See groups in {}\n2. Add a group to {}\n3. Delete {}\n".format(sport, sport, sport)
                    action = input(texti).lower()
                if action == "1":
                    if member_id:
                        return self.view_groups(sport, member_id, year)
                    else:
                        return self.view_groups(sport)
                elif action == "2":
                    action = self.register_group(sport)
                elif action == "3":
                    member_id_list = self.sport_service.sport_map[sport].get_all_members()
                    member_list = []
                    for member_id in member_id_list:
                        member_list.append(self.member_service.members_map[member_id])
                    self.member_service.remove_sport_from_members(sport, member_list)
                    self.sport_service.remove_sport(sport)
                    try:
                        del self.member_service.sport_map[sport]
                    except:
                        pass
                    print("Sport deleted")
                    sleep(1)
                    action = "b"
            else:
                print("No sport in system")
                sleep(1)
                action = 'b'
        return self.action_eaquals_quit(action)

    def not_a_valid_index(self):
        self.print_sentence()
        print("Not valid index!")
        return input("Try again?").lower()

    def view_groups(self, sport, member_id = False, year = None):
        action = ''
        while action != "b" and action != "q" and action != "n":
            group_member_list, group_name_list = self.sport_service.get_all_groups(sport)
            texti = "All groups in {}:\n".format(sport)
            system("clear")
            self.print_group(group_member_list, texti)
            if member_id:
                date = datetime.datetime.now()
                print("\nMembers ID: {}\nAge: {}".format(member_id, int(date.year) - int(year)))
                group_index = input("Select a group: ")
                try:
                    group = group_name_list[int(group_index) - 1]
                except:
                    action = self.not_a_valid_index()
                    if action == "n":
                        return "b"
                    else:
                        continue
                leagal, right_age = self.sport_service.assign_member_to_group(member_id, self.member_service.members_map[member_id],sport, group, year)
                if not right_age:
                    print("Member is not in appropriate age range")
                    sleep(1)
                else:
                    action = self.check_if_leagl(leagal, "Member")
                    if action == "ok":
                        self.member_service.sport_map[sport] = self.member_service.sport_map.get(sport ,[]) + [member_id]
                        return 'b'
                self.print_sentence()
                action = input("Do you want to try again?")
            else:
                ok = input("Press enter to continue")
                return 'b'
        return self.action_eaquals_quit(action)

    def register_sport(self):
        name = input("Name: ")
        leagl = self.sport_service.add_sport(name)
        return self.check_if_leagl(leagl, name)

    def register_group(self, sport):
        name = input("Name: ")
        while True:
            try:
                age_from = int(input("Age From: "))
                age_to =int(input("Age limit: "))
                break
            except:
                print("please enter a valid number")
        capacity = input("Max number of members: ")
        leagal = self.sport_service.add_group(name, age_from, age_to, sport, capacity)
        return self.check_if_leagl(leagal, name)

    def check_if_leagl(self, leagal, texti):
        if leagal == True:
            print("{} registerd".format(texti))
            sleep(1)
            return "ok"
        elif leagal == False:
            print("{} already exist".format(texti))
            sleep(1)
            return ""
        elif leagal == None:
            print("Group is full.{} has been added to waiting list".format(texti))
            sleep(2)
            return "ok"
