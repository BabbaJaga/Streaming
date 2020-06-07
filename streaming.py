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
        try:
            self.season = int(input("Enter the season : "))

        except ValueError:
            self.season = ""

        try:
            self.episode = int(input("Enter the episode : "))

        except ValueError:
            self.episode = ""

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

    def search(self):

        working_dick, __ = self.file_processing()

        try:
            lst = working_dick[self.ID]

            self.title = lst[0]
            self.duration = lst[1]
            self.rating = lst[2]
            self.audience = lst[3]
            self.gender = lst[4]
            self.season = lst[5]
            self.episode = lst[6]
            self.episode_title = lst[7]
            self.topic = lst[8]

            self.show_data()

        except:
            print("No video was found for the given ID.")

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
                    
    def verify_id_search(self, ID):
        
        self.ID = ID

        if (len(self.ID) == 5):

            if self.verify_id_complies() == True:
                self.search()
            
            else:
                print("The ID does not comply.")  
 
        else:
            print("Sorry some of the data entered doesn't match the constraints needed, please verify you are using the following input format :\n")
            print("        ID FORMAT\nFirst character : P or S \nSecond character : A, B, C or D \nLast three characters must be unitary natural numbers each \n")
            print("        TITLE FORMAT\nTitle lenght must contain less than 30 characters")

    def verify_id_full(self):

        if (len(self.ID) == 5 and len(self.title) < 30 and self.duration >= 1 and self.duration < 500 
            and len(self.audience) < 15 and len(self.gender) < 15):
            
            if self.verify_id_complies() == True:
                answer,lst = self.verify_id_general()
                return(answer,lst)
            
            else:
                print("The ID does not comply.")
                return("Failed",lst)

        else:
            print("Sorry some of the data entered doesn't match the constraints needed, please verify you are using the following input format :\n")
            print("        ID FORMAT\nFirst character : P or S \nSecond character : A, B, C or D \nLast three characters must be unitary natural numbers each \n")
            print("        TITLE FORMAT\nTitle lenght must contain less than 30 characters")
            return ("Failed", None)


    def verify_id_complies(self):

        first_char = ['P','S','D']
        second_char = ['A','B','C','D']
        last_three = ["0","1","2","3","4","5","6","7","8","9"]

        if (self.ID[0] in first_char and self.ID[1] in second_char and self.ID[2] in last_three
            and self.ID[3] in last_three and self.ID[4] in last_three):

            return(True)


        else:
            loading = 'The ID is being validated...'
            for i in range(0,28):
                print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)
                
            print("Sorry some of the data entered doesn't match the constraints needed, please verify you are using the following input format :\n")
            print("        ID FORMAT\nFirst character : P or S \nSecond character : A, B, C or D \nLast three characters must be unitary natural numbers each\n")
            return (False)


    def verify_id_general(self):

        working_dick, __ = self.file_processing()

        lst = []
        for value in working_dick.values():
            if value[0] not in lst:
                lst.append(value[0])

        if (self.ID not in working_dick.keys()):
            return ("Successfull",lst)

        else:
            print("Oops it seems the ID already exists")
            return ("Failed",lst)


    def verify_writing(self, lst):

        first_char = ['P','S','D']

        def clear():
            os.system('cls' if os.name == 'nt' else 'clear')

        while (self.rating > 5 or self.rating < 1):
            print("Rating format not accepted, you can only rate from 1 to 5 stars")
            sleep(2)
            clear()
            self.rating = round(float(input("Enter the rating : ")),1)

        #pelicula

        if(self.ID[0] == first_char[0]):

            loading = 'The ID is being validated...'
            for i in range(0,28):
                print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)

            if (self.title not in lst):
                print('Successfully added!')
                self.data_writing()
                print(lst)
                print(self.title)

            else:
                print("Oops! You cant register a new ID with an existing movie title")
        #serie

        elif (self.ID[0] == first_char[1]):

            loading = 'The ID is being validated...'

            for i in range(0,28):
                print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)
    
            print("\nThe ID is valid! We can now validate the series properties.")
            self.season_episode_verification()
            
        #documental

        else:

            loading = 'The ID is being validated...'
            for i in range(0,28):
                print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)
            if (self.topic != ""):
                print("\nThe ID is valid! We can now validate the documentary properties.")
                self.season_episode_verification()
            else:
                print("You must enter a topic, in order to add a documentary to the file!")
            
    def season_episode_verification(self):

        if(int(self.season) <=500 and int(self.season) >= 1 and int(self.episode) <= 500 and int(self.episode) >= 1 and len(self.episode_title) < 30 ):
            __, current_dick = self.file_processing()

            if bool(current_dick) == False:
                print("The series was non-existent (",self.title, ") it has now been added!")
                self.data_writing()

            else:
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
                            print("A new episode has been added to the series: ", self.title, " with season number : ", self.season)
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
                key = string[0]
                title = string[1]
                duration = string[2]
                rating = string[3]
                audience = string[4]
                gender = string[5]
                season = string[6]
                episode = string[7]
                ep_title = string[8]
                topic = string[9]

                working_dick[key] = title,duration, rating, audience, gender, season, episode, ep_title, topic
                
                if self.title == title:
                    current_dick[key] = season,episode,ep_title

        return(working_dick,current_dick)

class Lists(Writer):
    def general_list(self):
        pass