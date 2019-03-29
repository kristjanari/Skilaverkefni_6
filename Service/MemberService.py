from Models.Members import Members

class MemberService:

    def __init__(self):
        self.models_member = Members()

    def add_member(self, name, phone, email, year):
        self.models_member.add_member(name, phone, email, year)
        # Update memberrepo!
        
    def look_up_a_member_by_name(self, name):
        return  self.models_member.find_member_by_name(name)