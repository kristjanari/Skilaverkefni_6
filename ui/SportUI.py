class SportUI:

    def __init__(self):
        pass

    def sport_menu(self):
        action = ''
        while action != "q":
            print("Please Select one, If you want to quit press 'q'")
            action = input("1. Sport\n2. Member\n").lower()
            if action == "1":
                self.__sportUI = SportUI()
                self.__sportUI.sport_menu()
            elif action == "2":
                self.__memberUI = MemberUI()
                self.__memberUI.member_menu()