from sortedcontainers import *

class Member:

    def __init__(self, name, phone, email, birth_year):
        self.name = name
        self.phone = phone
        self.email = email
        self.birth_year = birth_year
        self.sports = SortedDict()

    def add_group(self, sport, group, waiting_list = False):
        self.sports[sport] = self.sports.get(sport, []) + [(group, waiting_list)]

    def remove_group(self, group):
        sport_name = group.sport
        if len(self.sports[sport_name]) > 1:
            try:
                self.sports[sport_name].remove(group.name, True)
            except:
                self.sports[sport_name].remove(group.name, False)
        else:
            del self.sports[sport_name]

    def remove_sport(self, sport_name):
        del self.sports[sport_name]

    def __str__(self):
        return "\tName: {}\n\tPhone number: {}\n\tEmail: {}\n\tYear of birth: {}\n".format(self.name,
            self.phone, self.email, self.birth_year)

    def _print_one_line(self):
        return "{}, {}, {}, {}".format(self.name,
            self.phone, self.email, self.birth_year)