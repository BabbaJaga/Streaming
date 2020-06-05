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
    def get_data(self):
        super().get_data()

    def data_adjust(self):
        super().data_adjust()

    def movie_data_writing(self):
        with open("movies.csv", "a", encoding="utf-8") as movie_append:
            self.duration = str(self.duration)
            movie_append.write(self.ID + "," + self.title + "," + self.duration + "," + self.rating + "," + self.audience + "," + self.gender + "\n" )
        
            print("\nThe Movie ID has been succesfully added to the file!!!\n")

    def serie_data_writing(self):
        with open("movies.csv", "a", encoding="utf-8") as movie_append:
            self.duration = str(self.duration)
            self.season = str(self.season)
            self.episode = str(self.episode)
            movie_append.write(self.ID + "," + self.title + "," + self.duration + "," + self.rating + "," + self.audience + "," + self.gender + "," + 
                               self.season + "," + self.episode + "," + self.episode_title + "\n" )
                              
    def id_title_verification(self):
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

            movie_dick, series_dick = self.file_processing()
                
            if (self.ID[0] in first_char and self.ID[1] in second_char and self.ID[2] in last_three
                and self.ID[3] in last_three and self.ID[4] in last_three):
                if (self.ID not in movie_dick.keys() or self.ID not in series_dick.keys()):
                    
                    #Serie
                    if (self.ID[0] == first_char[1]):
                        loading = 'The ID is being validated...'
                        for i in range(0,28):
                            print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)

                        self.season_episode_ep_title_verification()

                    #Pelicula
                    elif(self.ID[0] == first_char[0]):
                        loading = 'The ID is being validated...'
                        for i in range(0,28):
                            print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)

                        if (self.title not in movie_dick.values()):
                            self.movie_data_writing()
                        else:
                            print("Oops! You cant register a new ID with an existing title")

                    #else: documental

                else:
                    print("Oops it seems the ID already exists")

            else:
                loading = 'The ID is being validated...'
                for i in range(0,28):
                    print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)
                    
                print("Sorry i guess some of the data entered doesn't match the constraints needed, please verify you are using the following input format\n")
                print("        ID FORMAT\nFirst character : P or S \nSecond character : A, B, C or D \nLast three characters must be unitary natural numbers each\n")
    
        else:
            print("Sorry i guess some of the data entered doesn't match the constraints needed, please verify you are using the following input format\n")
            print("        ID FORMAT\nFirst character : P or S \nSecond character : A, B, C or D \nLast three characters must be unitary natural numbers each\n")
            print("        TITLE FORMAT\nTitle lenght must contain less than 30 characters")
            
    def season_episode_ep_title_verification(self):

        #validacion de id y titulo

        if(self.season <=500 and self.season > 1 and self.episode <= 500 and self.episode > 1 and len(self.episode_title) < 30 ):
            __, series_dick = self.file_processing()

            title_list = []
            season_list = []
            episode_list = []
            episode_title_list = []

            '''
            for title in series_dick.values():
                title_list.append(title[0])

                if self.title not in title_list:
                    print("We good continue")
                    
                    for season in series.dick.values():
                        season_list.append(season[1])

                        if self.season not in season_list:
                            print("we still good")

                            for episode in series.dick.values():
                                episode_list.append(episode[2])

                                if self.episode not in episode_list:
                                    print("almost")

                                    for episode_title not in episode_title_list:
                                        episode_title_list.append(episode_title[3])
                                        
                                        if self.episode_title not in episode_title_list:
                                            print("writting")  

                else:
                    print("its already there")
            '''

            for title,season,episode,episode_title in series_dick.values():
                title_list.append(title[0])
                season_list.append(season[1])
                episode_list.append(episode[2])
                episode_title_list.append(episode_title[3])

            if self.title in title_list and self.season not in season_list and self.episode not in episode_list and self.episode_title not in episode_title_list:
                print("we write completely")
                self.serie_data_writing()

            elif self.title not in title_list:
                print("we also write completely")
                self.serie_data_writing()

            else:
                print("why we cant write")
        
        else:
            print("Razones por las cuales no paso la verificacion")

    def file_processing(self):
        with open("movies.csv", "r", encoding="utf-8") as movie_reading:
            movie_dick = {}
            series_dick = {}
            lines = movie_reading.readlines()

            for l in lines:
                string = l.split(",")
                if (len(string) == 6):
                    movie_key = string[0]
                    movie_title = string[1]
                    movie_dick[movie_key] = movie_title
                    
                elif (len(string) == 9):
                    serie_key = string[0]
                    serie_title = string[1]
                    season = string[6]
                    episode = string[7]
                    ep_title = string[8]
                    series_dick[serie_key] = serie_title, str(season), str(episode), ep_title

            return(movie_dick, series_dick)            


            
            
    
writer = Writer()
writer.get_data()
writer.data_adjust()
writer.id_title_verification()
