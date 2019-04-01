import pickle

class MemberRepository:

    def read_members(self):
        try:
            pickle_members = open("./Data/members.pickle", "rb")
            members_dict = pickle.load(pickle_members)
            pickle_members.close()
            return members_dict
        except EOFError:
            return {}

    def write_members(self, members_dict):
        pickle_file = open("./Data/members.pickle", "wb")
        pickle.dump(members_dict, pickle_file)
        pickle_file.close()

    def get_members(self):
        customers = []
        with open("./Data/convertcsv.csv", encoding = "UTF-8") as member_file:
            for row in member_file.readlines():
                customer = row.split(",")
                customers.append(customer)
        return customers