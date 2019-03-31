from ui.SportUI import SportUI
from ui.MemberUI import MemberUI
from os import system, name
from Service.MemberService import MemberService
from Service.SportService import SportService
from time import sleep

class RegistrationUI:

    def __init__(self):
        self.__member_service = MemberService()
        self.__sport_service = SportService()
        self.__sportUI = SportUI(self.__member_service, self.__sport_service)
        self.__memberUI = MemberUI(self.__member_service, self.__sport_service)

    def main_menu(self):
        action = ''
        while action != "q":
            system("clear")
            print("Please Select one, If you want to quit press 'q'")
            print("-"*60)
            action = input("1. Sport\n2. Member\n3. Save\n").lower()
            if action == "1":
                action = self.__sportUI.sport_menu()
            elif action == "2":
                action = self.__memberUI.member_menu()
            elif action == "3":
                self.__memberUI.save()
                self.__sportUI.save()
                print("Files Saved")
                sleep(1)


