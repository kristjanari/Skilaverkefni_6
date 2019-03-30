from Repository.SportRepository import SportRepository
from Models.Sport import Sport

class SportService:

    def __init__(self):
        self.sport_repo = SportRepository()
        self.sport_map = self.sport_repo.read_sports()

    def add_sport(self, name):
        self.sport_map[name] = Sport(name)

    def remove_sport(self, name):
        del self.sport_map[name]

    def save_sports(self):
        self.sport_repo.write_sports(self.sport_map)

    def get_all_sports(self):
        sport_list = []
        for sport in self.sport_map.values():
            sport_list.append(sport)
        return sport_list