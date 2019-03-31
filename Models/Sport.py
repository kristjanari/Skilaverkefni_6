from Models.SportGroup import SportGroup

class Sport:

    def __init__(self, name):
        self.name = name
        self.groups = {}

    def add_group(self, name, age_from, age_to, capacity):
        sport_group = SportGroup(self.name, name, age_from, age_to, capacity)
        if not self.groups.get(name, False):
            self.groups[name] = sport_group
            return True
        return False

    def remove_group(self, name):
        del self.groups[name]

    def remove_member(self, member_id):
        for group in self.groups:
            self.groups[group].remove_member(member_id)

    def add_member(self, member_id, group):
        return group.add_member(member_id)

    def get_all_members(self):
        members = set()
        for group in self.groups:
            for member in group.members:
                members.add(member)
        return members

    def __str__(self):
        return_str =  str(self.name) + "\n\t\tGroups:\n"
        for index, group in enumerate(self.groups):
            return_str += '\t\t' + str(index + 1) + ". "
            return_str += str(group) + "\n"
        return return_str

    