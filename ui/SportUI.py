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
            print(sport)


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

    def view_all_sports(self):
        sport_list = self.sport_service.get_all_sports()
        self.print_sport(sport_list, "All sports: ")
        sport = input("Select a sport").lower()
        action = ''
        while action != "b" and action != "q":
            self.print_sentence()
            action = input("1. Get a detailed information about sport\n2. Delete a sport\n").lower()
            if action == "1":
                action = "b"
            elif action == "2":
                self.member_service.remove_sport_from_members(sport, self.sport_service.sport_map[sport].get_all_members())
                self.sport_service.remove_sport(sport)
                print("Sport deleted")
                sleep(2)
                action = "b"
        return action

    def register_sport(self):
        name = input("Name: ").lower()
        self.sport_service.add_sport(name)
        print("Sport registerd")
        sleep(2)
        return 'OK'
