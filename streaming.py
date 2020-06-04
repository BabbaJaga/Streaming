from time import sleep
import os

class Video():
    def __init__ (self):
        self.ID = None
        self.title = None
        self.duration = None
        self.rating = None

    def get_data(self):
        self.ID = str(input("Enter Id   : "))
        self.title = str(input("Enter Title    : "))
        self.duration = int(input("Enter Duration     : "))
        self.rating = str(input("Enter the Rating : "))

    def data_adjust(self):
        self.ID = self.ID.upper()
        self.title = self.title.upper()
        self.rating = self.rating.upper()

    def show_data(self):
        print("ID : ", self.ID)
        print("Title : ", self.title)
        print("Duration : ", self.duration)
        print("Rating : ", self.rating)
    
class Movie(Video):
    def __init__ (self):
        super().__init__()
        self.audience = None
        self.gender = None

    def get_data(self):
        super().get_data()
        self.audience = str(input("Enter the audience : "))
        self.gender = str(input("Enter the gender : "))

    def data_adjust(self):
        super().data_adjust()
        self.audience = self.audience.upper()
        self.gender = self.gender.upper()
    
    def show_data(self):
        super().show_data()
        print("Audience : ", self.audience)
        print("Gender : ", self.gender)

class Serie(Movie):
    def __init__ (self):
        super().__init__()
        self.season = None
        self.episode = None
        self.episode_title = None

    def get_data(self):
        super().get_data()
        self.season = str(input("Enter the season : "))
        self.episode = str(input("Enter the episode : "))
        self.episode_title = str(input("Enter the episode title : "))

    def data_adjust(self):
        super().data_adjust()
        self.season = self.season.upper()
        self.episode = self.episode.upper()
        self.episode_title = self.episode_title.upper()

    def show_data(self):
        super().show_data()
        print("Season : ", self.season)
        print("Episode : ", self.episode)
        print("Espisode title : ", self.episode_title)

class Documentary(Serie):
    def __init__ (self):
        super().__init__()
        self.topic = None
    
    def get_data(self):
        super().get_data()
        self.topic = str(input("Enter the topic : "))

    def data_adjust(self):
        super().data_adjust()
        self.topic = self.topic.upper()

    def show_data(self):
        super().show_data()
        print("Topic : ", self.topic)

class Writer(Documentary):
    def data_adjust(self):
        super().data_adjust()

    def get_data(self):
        super().get_data()
    
    def movie_verification(self):
        def clear():
            os.system('cls' if os.name == 'nt' else 'clear')

        rating = ["*","**","***","****","*****"]

        while (self.rating not in rating):
            print("Rating format not accepted, please check you are using the next format ")
            sleep(2)
            clear()
            print("Rate the Movie with the next rating options, from bad to excelent : *  or  **  or  ***  or  ****  or ***** ")
            self.rating = str(input("Enter the rating : "))
        
        if (self.rating in rating):
            if (len(self.rating) == 1 ):
                self.rating = u"\u2605"
            elif (len(self.rating) == 2):
                self.rating = u"\u2605 \u2605"
            elif (len(self.rating) == 3):
                self.rating = u"\u2605 \u2605 \u2605"
            elif (len(self.rating) == 4):
                self.rating = u"\u2605 \u2605 \u2605 \u2605"
            elif (len(self.rating) == 5):
                self.rating = u"\u2605 \u2605 \u2605 \u2605 \u2605"

        else:
            print("The rating given hasn´t been properly processed :(")
                
        if (len(self.ID) == 5 and len(self.title) < 30 and self.duration >= 1 and self.duration < 500 
            and len(self.audience) < 15 and len(self.gender) < 15):
            first_char = ['P','S','D']
            second_char = ['A','B','C','D']
            last_three = ["0","1","2","3","4","5","6","7","8","9"]

            with open("movies.csv", "r", encoding = "utf-8") as movie_file:
                lines = movie_file.readlines()
                dictionary = {}
                for l in lines:
                    movie_info = l.split(",")
                    ID = movie_info[0]
                    title = movie_info[1]
                    dictionary[ID] = title

                if (self.ID[0] in first_char and self.ID[1] in second_char and self.ID[2] in last_three
                    and self.ID[3] in last_three and self.ID[4] in last_three):
                    
                    if (self.ID not in dictionary.keys()):
                        loading = 'The ID is being validated...'
                    
                        for i in range(0,28):
                            print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)

                        if (self.title not in dictionary.values()):
                            with open("movies.csv", "a", encoding = "utf-8") as movie_append:
                                self.duration = str(self.duration)
                                movie_append.write(self.ID + "," + self.title + "," + self.duration + "," + self.rating + "," + self.audience + "," + self.gender + "\n" )
                            
                                print("\nThe Movie ID has been succesfully added to the file!!!\n")
                        else:
                            print("Oops! You cant register a new ID with an existing title")
                    else:
                        print("Oops it seems the ID already exists")

                else:
                    loading = 'The ID is being validated...'
                    for i in range(0,28):
                        print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)
                    print("Sorry, the ID couldn't be validated, the ID must strictly contain 5 characters with the next format : ")
                    print("First character : P or S ")
                    print("Second character : A, B, C or D")
                    print("Last three characters must be unitary natural numbers, each")

        else:
            print("Sorry, the ID couldn't be validated, the ID must strictly contain 5 characters with the next format : ")
            print("First character : P or S ")
            print("Second character : A, B, C or D")
            print("Last three characters must be unitary natural numbers each")

writer = Writer()
writer.get_data()
writer.data_adjust()
writer.movie_verification()