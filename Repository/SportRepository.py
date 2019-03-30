import pickle

class SportRepository:
    
    def read_sports(self):
        try:
            pickle_sports = open("./Data/sports.pickle", "rb")
            sports_dict = pickle.load(pickle_sports)
            pickle_sports.close()
            return sports_dict
        except EOFError:
            return {}

    def write_sports(self, sports_dict):
        pickle_file = open("./Data/sports.pickle", "wb")
        pickle.dump(sports_dict, pickle_file)
        pickle_file.close()