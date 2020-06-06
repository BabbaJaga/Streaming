from time import sleep
import os

class Video():
    def __init__ (self):
        self.ID = ""
        self.title = ""
        self.duration = ""
        self.rating = ""

    def get_data(self):
        self.ID = str(input("Enter Id   : "))
        self.title = str(input("Enter Title    : "))
        self.duration = int(input("Enter Duration     : "))
        self.rating = round(float(input("Enter the Rating : ")),1)

    def data_adjust(self):
        self.ID = self.ID.upper()
        self.title = self.title.upper()

    def show_data(self):
        print("ID : ", self.ID)
        print("Title : ", self.title)
        print("Duration : ", self.duration)
        print("Rating : ", self.rating)
    
class Movie(Video):
    def __init__ (self):
        super().__init__()
        self.audience = ""
        self.gender = ""

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
        self.season = ""
        self.episode = ""
        self.episode_title = ""

    def get_data(self):
        super().get_data()
        self.season = int(input("Enter the season : "))
        self.episode = int(input("Enter the episode : "))
        self.episode_title = str(input("Enter the episode title : "))

    def data_adjust(self):
        super().data_adjust()
        self.episode_title = self.episode_title.upper()

    def show_data(self):
        super().show_data()
        print("Season : ", self.season)
        print("Episode : ", self.episode)
        print("Espisode title : ", self.episode_title)

class Documentary(Serie):
    def __init__ (self):
        super().__init__()
        self.topic = ""
    
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

    def data_writing(self):

        with open("movies.csv", "a", encoding="utf-8") as video_append:
            self.duration = str(self.duration)
            self.season = str(self.season)
            self.episode = str(self.episode)
            self.rating = str(self.rating)
            
            video_append.write(self.ID + "," + self.title + "," + self.duration + "," + self.rating + "," + self.audience + "," + self.gender + "," + 
                               self.season + "," + self.episode + "," + self.episode_title + "," + self.topic + "\n" )
                    
    def id_title_verification(self):

        def clear():
            os.system('cls' if os.name == 'nt' else 'clear')

        while (self.rating > 5 or self.rating < 1):
            print("Rating format not accepted, you can only rate from 1 to 5 stars")
            sleep(2)
            clear()
            self.rating = round(float(input("Enter the rating : ")),1)
                
        if (len(self.ID) == 5 and len(self.title) < 30 and self.duration >= 1 and self.duration < 500 
            and len(self.audience) < 15 and len(self.gender) < 15):
            first_char = ['P','S','D']
            second_char = ['A','B','C','D']
            last_three = ["0","1","2","3","4","5","6","7","8","9"]

            working_dick, __ = self.file_processing()

            if (self.ID[0] in first_char and self.ID[1] in second_char and self.ID[2] in last_three
                and self.ID[3] in last_three and self.ID[4] in last_three):
                
                if (self.ID not in working_dick.keys()):
                    
                    #pelicula
                    if(self.ID[0] == first_char[0]):
                        loading = 'The ID is being validated...'
                        for i in range(0,28):
                            print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)

                        if (self.title not in working_dick.values()):
                            print('Successfully added!')
                            self.data_writing()
                            print(working_dick.values())
                        else:
                            print("Oops! You cant register a new ID with an existing movie title")
                    #serie
                    elif (self.ID[0] == first_char[1]):
                        loading = 'The ID is being validated...'

                        for i in range(0,28):
                            print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)
                
                        print("\nThe ID is valid! We can now validate the series properties.")
                        self.season_episode_verification()
                        
                    #else: documental

                else:
                    print("Oops it seems the ID already exists")

            else:
                loading = 'The ID is being validated...'
                for i in range(0,28):
                    print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)
                    
                print("Sorry i guess some of the data entered doesn't match the constraints needed, please verify you are using the following input format :\n")
                print("        ID FORMAT\nFirst character : P or S \nSecond character : A, B, C or D \nLast three characters must be unitary natural numbers each\n")
        
        else:
            print("Sorry i guess some of the data entered doesn't match the constraints needed, please verify you are using the following input format :\n")
            print("        ID FORMAT\nFirst character : P or S \nSecond character : A, B, C or D \nLast three characters must be unitary natural numbers each \n")
            print("        TITLE FORMAT\nTitle lenght must contain less than 30 characters")
            
    def season_episode_verification(self):

        if(self.season <=500 and self.season >= 1 and self.episode <= 500 and self.episode >= 1 and len(self.episode_title) < 30 ):
            __, current_dick = self.file_processing()

            if bool(current_dick) == False:
                print("The series added was non-existent (",self.title, ") it has now been added!")
                self.data_writing()

            else:
                print('\n',current_dick)
                title_dic = {}
                title_dic[self.title] = current_dick.values()
                del current_dick

                episode_ls = []
                season_ls = []
                episode_title_ls = []
                for s in title_dic.get(self.title):
                    season = s[0]
                    season_ls.append(season)
                    episode = s[1]
                    episode_ls.append(episode)
                    ep_title = s[2]
                    episode_title_ls.append(ep_title)

                self.season = str(self.season)
                self.episode = str(self.episode)

                if self.season not in season_ls:
                    print("A new season has been added to the series: ", self.title)
                    self.data_writing()
                else:
                    if self.episode not in episode_ls:
                        if self.episode_title not in episode_title_ls:
                            print("A new episode has been added to the series: ", self.title, " and season : ", self.season)
                            self.data_writing()
                        else:
                            print("The entry cannot be written because the episode title: ", self.episode_title, "already exists!")
                    else:
                        print("The entry cannot be written because the episode number: ", self.episode, "already exists!")

    def file_processing(self):
        with open("movies.csv", "r", encoding="utf-8") as movie_reading:
            working_dick = {}
            current_dick = {}

            lines = movie_reading.readlines()

            for l in lines:
                string = l.split(",")
                serie_key = string[0]
                serie_title = string[1]
                season = string[6]
                episode = string[7]
                ep_title = string[8]

                working_dick[serie_key] = serie_title, season, episode, ep_title

                if self.title == serie_title:
                    current_dick[serie_key] = season,episode,ep_title

        return(working_dick,current_dick)

            
            
    
writer = Writer()
writer.get_data()
writer.data_adjust()
writer.id_title_verification()
