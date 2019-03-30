from Service.MemberService import MemberService
from Service.SportService import SportService

class ChangeService:

    def __init__(self):
        self.member_service = MemberService()
        self.sport_service = SportService()

    def delete_member_from_sports(self, member_id):
        pass

    def delete_sport_from_members(self):
        pass