from os import system, name

class SportUI:

    def __init__(self, MemberService, SportService):
        self.member_service = MemberService
        self.sport_service = SportService

    def sport_menu(self):
        action = ''
        while action != "b" and action != "q":
            system("clear")
            print("Please Select one, If you want to quit press 'q' and to go back press 'b'")
            action = input("1. Register sport\n2. View all sports\n").lower()
            if action == "1":
                action = self.register_sport()
            elif action == "2":
                action = self.view_all_sports()
        return action

    def view_all_sports(self):
        #call a function in Service that gets list of all sports
        
        #print the list of all sport with the it's ID
        action = ''
        while action != "b" and action != "q":
            print("Please Select one, If you want to quit press 'q' and to go back press 'b'")
            action = input("1. Get a detailed information about sport\n2. Delete a sport\n").lower()
            if action == "1":
                action = "b"
            elif action == "2":
                action = "b"
        return action

    def register_sport(self):
        name = input("Name: ")
        #SENDA UPPL YFIR i Servise
        print("Sport registerd")
        return 'OK'
