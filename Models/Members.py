from Models.Member import Member
from sortedcontainers import SortedDict

class Members:

    def __init__(self):
        self.members_map = {} 
        self.name_map = SortedDict()
        self.phone_map = {}
        self.email_map = {}
        self.year_map = SortedDict()
        self.unique_id = 1

    def add_member(self, name, phone, email, year):
        member = Member(name, phone, email, year)
        self.members_map[self.unique_id] = member
        self.name_map[member.name] = self.name_map.get(member.name,[]) + [self.unique_id]
        self.phone_map[member.phone] = self.phone_map.get(member.phone,[]) + [self.unique_id]
        self.email_map[member.email] = self.unique_id
        self.year_map[member.birth_year] = self.year_map.get(member.birth_year ,[]) + [self.unique_id]
        self.unique_id += 1

    def remove_member(self, id):
        member = self.members_map.get(id)
        if member != None:
            if len(self.name_map[member.name]) > 1:
                self.name_map[member.name].remove(id)
            else:
                del self.name_map[member.name]
            if len(self.phone_map[member.phone]) > 1:
                self.name_map[member.phone].remove(id)
            else:
                del self.phone_map[member.phone]
            del self.email_map[member.phone]
            if len(self.year_map[member.birth_year]) > 1:
                self.name_map[member.birth_year].remove(id)
            else:
                del self.year_map[member.birth_year]
            del self.members_map[id]
        
    def find_member_by_name(self, name):
        ids = self.name_map.get(name, False)
        if ids:
            listi = []
            for id in ids:
                listi.append([id, self.members_map[id]])
            return listi