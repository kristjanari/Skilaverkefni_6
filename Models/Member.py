from sortedcontainers import *

class Member:

    def __init__(self, name, phone, email, birth_year):
        self.name = name
        self.phone = phone
        self.email = email
        self.birth_year = birth_year
        self.sports = SortedDict()

    def add_sport(self, sport, group):
        self.sports[sport.name] = self.sports.get(sport.name, []) + [group.name]

    def remove_group(self, group):
        sport_name = group.sport
        if len(self.sports[sport_name]) > 1:
                self.sports[sport_name].remove(group.name)
        else:
            del self.sports[sport_name]

    def remove_sport(self, sport_name):
        del self.sports[sport_name]

    def __str__(self):
        return "Name: {}\nPhone number: {}\nEmail: {}\nYear of birth: {}\n".format(self.name,
            self.phone, self.email, self.birth_year)

    def _print_one_line(self):
        return "{}, {}, {}, {}".format(self.name,
            self.phone, self.email, self.birth_year)
