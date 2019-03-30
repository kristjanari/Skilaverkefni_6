import pickle

class MemberRepository:

    # def read_members(self):
    #     members_dict = {}
    #     with open ("./Data/Members.csv", encoding = "UTF-8") as members_file:
    #         dict_reader = csv.DictReader(members_file)
    #         for row in dict_reader:
    #             members_dict[row[id]] = Member(row["name"], row["phone"], row["email"], row["birth_year"])
    #     return members_dict

    # def write_members(self):
    #     with open ("./Data/Members.csv", "w", encoding = "UTF-8") as price_file:
    #         pass

    def read_members(self):
        try:
            pickle_members = open("./Data/members.picle", "rb")
            members_dict = pickle_members.load(pickle_members)
            pickle_members.close()
            return members_dict
        except EOFError:
            return {}

    def write_members(self, members_dict):
        pickle_file = open("./Data/members.picle", "wb")
        pickle.dump(members_dict, pickle_file)
        pickle_file.close()