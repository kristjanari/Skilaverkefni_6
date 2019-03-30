from Models.SportGroup import SportGroup

class Sport:

    def __init__(self, name):
        self.name = name
        self.groups = {}

    def add_group(self, name, age_from, age_to):
        sport_group = SportGroup(self.name, name, age_from, age_to)
        self.groups[name] = sport_group

    def remove_member(self, name):
        del self.groups[name]

    def add_member(self, member_id, group):
        group.add_member(member_id)

    def __str__(self):
        return_str = str(self.name) + ":\n"
        for group in self.groups:
            return_str += str(group) + "\n"
        return return_str

    