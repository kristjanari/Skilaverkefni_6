from Models.SportGroup import SportGroup

class Sport:

    def __init__(self, name):
        self.name = name
        self.groups = {}

    def add_group(self, name, age_from, age_to):
        sport_group = SportGroup(name, age_from, age_to)
        self.groups[name] = sport_group

    def remove_member(self, name):
        del self.groups[name]

    def add_member(self, member_id, group):
        group.add_member(member_id)