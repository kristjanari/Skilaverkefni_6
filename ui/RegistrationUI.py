from ui.SportUI import SportUI
from ui.MemberUI import MemberUI
from os import system, name
class RegistrationUI:

    def __init__(self):
        pass
    
    def main_menu(self):
        action = ''
        while action != "q":
            system("clear")
            print("Please Select one, If you want to quit press 'q'")
            action = input("1. Sport\n2. Member\n3. Save\n").lower()
            if action == "1":
                self.__sportUI = SportUI()
                action = self.__sportUI.sport_menu()
            elif action == "2":
                self.__memberUI = MemberUI()
                action = self.__memberUI.member_menu()
            elif action == "3":
                pass