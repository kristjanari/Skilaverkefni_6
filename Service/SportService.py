from Repository.SportRepository import SportRepository
from Models.Sport import Sport

class SportService:

    def __init__(self):
        self.sport_repo = SportRepository()
        self.sport_map = self.sport_repo.read_sports()

    def add_sport(self, name):
        sport = Sport(name)
        if not self.sport_map.get(name, False):
            self.sport_map[name] = sport
            return True
        return False

    def remove_sport(self, sport):
        del self.sport_map[sport]

    def remove_member_from_sports(self, id, sports):
        for sport in sports:
            sport.remove_member(id)

    def save_sports(self):
        self.sport_repo.write_sports(self.sport_map)

    def get_all_sports(self):
        sport_list = []
        sport_name_list = []
        for key, value in self.sport_map.items():
            sport_list.append(value)
            sport_name_list.append(key)
        return sport_list, sport_name_list

    def get_all_groups(self, sport):
        group_member_list = []
        group_name_list = []
        sport_instance = self.sport_map[sport]
        groups_dict = sport_instance.groups
        for group, value in groups_dict.items():
            group_member_list.append(value.members)
            group_name_list.append(group)
        return group_member_list, group_name_list


    def assign_member_to_group(self, member_id, member, sport, group, year):
        sport_instance = self.sport_map[sport]
        groups_dict = sport_instance.groups
        leagal = self.sport_map[sport].add_member(member_id, groups_dict[group], year)
        if leagal:
            member.add_group(sport, group)
        return leagal


    def add_group(self, name, age_from, age_to, sport):
        return self.sport_map[sport].add_group(name, age_from, age_to)

    def remove_member_from_selected_sport(self, member_id, sport):
        sport = self.sport_map[sport]
        sport.remove_member(member_id)