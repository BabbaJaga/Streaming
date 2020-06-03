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

    def show_data(self):
        print("ID : ", self.ID)
        print("Title : ", self.title)
        print("Duration : ", self.duration)
        print("Rating : ", self.rating)
    
    def data_adjust():
        

class Movie(Video):
    def __init__ (self):
        super().__init__()
        self.audience = None
        self.gender = None

    def get_data(self):
        super().get_data()
        self.audience = str(input("Enter the number of viewers : "))
        self.gender = str(input("Enter the gender : "))
    
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

    def show_data(self):
        super().show_data()
        print("Topic : ", self.topic)

class Writer(Documentary):
    def get_data(self):
        super().get_data()
    
    def movie_verification(self):
        def clear():
            os.system('cls' if os.name == 'nt' else 'clear')

        rating = ["*","**","***","****","*****"]
        #if (self.rating not in rating):
        while (self.rating not in rating):
            print("Rating format not accepted, please check you are using the next format ")
            sleep(2)
            clear()
            print("Rate the Movie with the next rating options, from bad to excelent : *  or  **  or  ***  or  ****  or ***** ")
            self.rating = str(input("Enter the rating : "))
        
        if (self.rating in rating):
            if (len(self.rating) == 1 ):
                self.rating = "★"
            elif (len(self.rating) == 2):
                self.rating = "★ ★"
            elif (len(self.rating) == 3):
                self.rating = "★ ★ ★"
            elif (len(self.rating) == 4):
                self.rating = "★ ★ ★ ★"
            elif (len(self.rating) == 5):
                self.rating = "★ ★ ★ ★ ★"

            print("Thanks for your opinion, the rating has been placed!")

        else:
            print("The rating given hasn´t been properly processed :(")
                
        if (len(self.ID) == 5 and len(self.title) < 30 and self.duration >= 1 and self.duration < 500 
            and len(self.audience) < 15 and len(self.gender) < 15):
            first_char = ['P','S','D']
            second_char = ['A','B','C','D']
            last_three = ["0","1","2","3","4","5","6","7","8","9"]

            with open("movies.csv", "r") as movie_file:
                lines = movie_file.readlines()
                movie_info = lines[0].split(",")
               
                if (self.ID[0] in first_char and self.ID[1] in second_char and self.ID[2] in last_three
                    and self.ID[3] in last_three and self.ID[4] in last_three):
        
                    if (self.ID not in movie_info[0]):
                        loading = 'The ID is being validated...'

                        for i in range(0,28):
                            print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)

                        with open("movies.csv", "a") as movie_append:
                            movie_append.write(self.ID + ",")

                            if (self.title not in movie_info[1]):
                                movie_append.write(self.title + ",")
                            else:
                                print("Oops! You cant register a new ID with an existing title")
                            movie_append.write(self.duration + ",")
                            movie_append.write(self.rating + ",")
                            movie_append.write(self.audience + ",")
                            movie_append.write(self.gender + "\n")
                            print("\nThe Movie ID has been succesfully added to the file!!!\n")
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
"""
    def serie_verification(self):
        def clear():
            os.system('cls' if os.name == 'nt' else 'clear')

        rating = ["*","**","***","****","*****"]
        while (self.rating not in rating):
            if (self.rating not in rating):
                print("Rating format not accepted, please check you are using the next format ")
                sleep(2)
                clear()

            print("Rate the Movie with the next rating options, from bad to excelent : *  or  **  or  ***  or  ****  or ***** ")
            self.rating = str(input("Enter the rating : "))
        
        if (self.rating in rating):
            if (len(self.rating == 1)):
                self.rating = "★"
            elif (len(self.rating == 2)):
                self.rating = "★ ★"
            elif (len(self.rating == 3)):
                self.rating = "★ ★ ★"
            elif (len(self.rating == 4)):
                self.rating = "★ ★ ★ ★"
            elif (len(self.rating == 5)):
                self.rating = "★ ★ ★ ★ ★"

            print("Thanks for your opinion, the rating has been placed!")

        else:
            print("The rating given hasn´t been properly processed :(")
                
        if (len(self.ID) == 5 and len(self.title) < 30 and self.duration >= 1 and self.duration < 500 
            and len(self.audience) < 15 and len(self.gender) < 15):
            first_char = ['P','S','D']
            second_char = ['A','B','C','D']
            last_three = ["0","1","2","3","4","5","6","7","8","9"]

            with open("movies.csv", "r") as movie_file:
                lines = movie_file.readlines()
                movie_info = lines[0].split(",")
               
                if (self.ID[0] in first_char and self.ID[1] in second_char and self.ID[2] in last_three
                    and self.ID[3] in last_three and self.ID[4] in last_three):
        
                    if (self.ID not in movie_info[0]):
                        loading = 'The ID is being validated...'
                        for i in range(0,28):
                            print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)
                        with open("movies.csv", "a") as movie_append:
                            movie_append.write(self.ID + ",")
                            if (self.title not in movie_info[1]):
                                movie_append.write(self.title + ",")
                            else:
                                print("Oops! You cant register a new ID with an existing title")
                            movie_append.write(self.duration + ",")
                            movie_append.write(self.rating + ",")
                            movie_append.write(self.audience + ",")
                            movie_append.write(self.gender + "\n")
                            print("\nThe Movie ID has been succesfully added to the file!!!\n")
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

"""

writer = Writer()
writer.get_data()
writer.movie_verification()







