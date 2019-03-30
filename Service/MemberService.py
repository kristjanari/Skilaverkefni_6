from Models.Member import Member
from Repository.MemberRepository import MemberRepository
from sortedcontainers import SortedDict

class MemberService:

    def __init__(self):
        self.member_repo = MemberRepository()
        self.members_map = self.member_repo.read_members()
        self.name_map = SortedDict()
        self.phone_map = {}
        self.email_map = {}
        self.year_map = SortedDict()
        self.unique_id = self.create_name_phone_email_year_map_and_return_unique_id()

    def add_member(self, name, phone, email, year):
        member = Member(name, phone, email, year)
        self.members_map[self.unique_id] = member
        self.name_map[member.name] = self.name_map.get(member.name,[]) + [self.unique_id]
        self.phone_map[member.phone] = self.phone_map.get(member.phone,[]) + [self.unique_id]
        self.email_map[member.email] = self.email_map.get(member.email,[]) + [self.unique_id]
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
            if len(self.email_map[member.email]) > 1:
                self.name_map[member.email].remove(id)
            else:
                del self.email_map[member.email]
            if len(self.year_map[member.birth_year]) > 1:
                self.name_map[member.birth_year].remove(id)
            else:
                del self.year_map[member.birth_year]
            del self.members_map[id]
        

    def find_member(self, looking_for, type):
        if type == "name":
            ids = self.name_map.get(looking_for, False)
        elif type == "phone":
            ids = self.phone_map.get(looking_for, False)
        elif type == "email":
            ids = self.email_map.get(looking_for, False)
        elif type == "year":
            ids = self.year_map.get(looking_for, False)
        if ids:
            listi = []
            for id in ids:
                listi.append([id, self.members_map[id]])
            return listi
        return ids

    def create_name_phone_email_year_map_and_return_unique_id(self):
        max_id = 0
        for key in self.members_map:
            member = self.members_map[key]
            self.name_map[member.name] = self.name_map.get(member.name,[]) + [key]
            self.phone_map[member.phone] = self.phone_map.get(member.phone,[]) + [key]
            self.email_map[member.name] = self.email_map.get(member.email,[]) + [key]
            self.year_map[member.birth_year] = self.year_map.get(member.birth_year ,[]) + [key]
            if key > max_id:
                max_id = key
        return max_id