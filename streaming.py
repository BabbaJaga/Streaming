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
        try:
            self.duration = int(input("Enter Duration     : "))
        except:
            self.duration = ""
        try:    
            self.rating = round(float(input("Enter the Rating : ")),1)
        except:
            self.rating = ""


    def show_data(self,ID,title,duration,rating):

        self.ID = ID
        self.title = title
        self.duration = duration
        self.rating = rating

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
        self.gender = str(input("Enter the genre : "))
    
    def show_data(self,ID,title,duration,rating,audience,gender):
        super().show_data(ID,title,duration,rating)

        self.audience = audience
        self.gender = gender

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

        except:
            self.season = ""

        try:
            self.episode = int(input("Enter the episode : "))

        except:
            self.episode = ""

        self.episode_title = str(input("Enter the episode title : "))

    def show_data(self,ID,title,duration,rating,audience,gender,season,episode,episode_title):
        super().show_data(ID,title,duration,rating,audience,gender)

        self.season = season
        self.episode = episode
        self.episode_title = episode_title

        if self.season != "":
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
        return(self.ID,self.title,self.duration,self.rating,self.audience,self.gender,self.season,self.episode,self.episode_title,self.topic)

    def show_data(self,ID,title,duration,rating,audience,gender,season,episode,episode_title,topic):
        super().show_data(ID,title,duration,rating,audience,gender,season,episode,episode_title)

        self.topic = topic

        if self.topic != "\n":
            print("Topic : ", self.topic)

class Writer():
    def __init__(self):
        self.ID = ""
        self.title = ""
        self.duration = ""
        self.rating = ""
        self.audience = ""
        self.gender = ""
        self.season = ""
        self.episode = ""
        self.episode_title = ""
        self.topic = ""

    def search(self):

        try:
            working_dic, __ = self.file_processing()

            lst = working_dic[self.ID]

            self.ID = lst[9]
            self.title = lst[0]
            self.duration = lst[1]
            self.rating = lst[2]
            self.audience = lst[3]
            self.gender = lst[4]

            if lst[5] != "":
                self.season = lst[5]
                self.episode = lst[6]
                self.episode_title = lst[7]
            
            if lst[8] != "":
                self.topic = lst[8]
                
            show = Documentary()
            show.show_data(self.ID,self.title,self.duration,self.rating,self.audience,self.gender,self.season,self.episode,self.episode_title,self.topic)

        except:
            print("No video was found for the given ID.")

    def data_adjust(self):

        self.ID = self.ID.upper()
        self.title = self.title.upper()
        self.audience = self.audience.upper()
        self.gender = self.gender.upper()
        self.episode_title = self.episode_title.upper()
        self.topic = self.topic.upper()

    def get_data(self):

        documentary = Documentary()

        self.ID,self.title,self.duration,self.rating,self.audience,self.gender,self.season,self.episode,self.episode_title,self.topic = documentary.get_data()

    def data_writing(self):

        with open("videos.csv", "a", encoding="utf-8") as video_append:
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

    def verify_title_search(self, title):
        
        if (len(title) <= 30 and len(title) >= 1):

                General = Lists()
                search_dic = General.general(title,0)

                if search_dic != None:
                    return search_dic
                else:
                    print("No video was found for the given title.")
 
        else:
            print("Sorry some of the data entered doesn't match the constraints needed, please verify you are using the following input format :\n")
            print("        TITLE FORMAT\nTitle length must contain 30 characters or less.")
            print("You can't leave the title entry blank.")

    def verify_genre_search(self, genre):
            
            if (len(genre) <= 15 and len(genre) >= 1):

                    General = Lists()
                    search_dic = General.general(genre,3)

                    if search_dic != None:
                        return search_dic
                    else:
                        print("No video was found for the given genre.")
    
            else:
                print("Sorry some of the data entered doesn't match the constraints needed, please verify you are using the following input format :\n")
                print("        GENRE FORMAT\nGenre length must contain 15 characters or less.")
                print("You can't leave the genre entry blank.")

    def verify_id_full(self):

        if (len(self.ID) == 5 and self.title != "" and len(self.title) <= 30 and self.duration != "" and self.duration >= 1 and self.duration <= 500 
            and self.audience != "" and len(self.audience) <= 15 and self.gender != "" and len(self.gender) <= 15):
            
            if self.verify_id_complies() == True:
                answer,lst = self.verify_id_general()
                return(answer,lst)
            
            else:
                print("The ID does not comply.")
                return ("Failed", None)

        else:
            print("Sorry some of the data entered doesn't match the constraints needed, please verify you are using the following input format:\n")
            print("        ID FORMAT\nFirst character : P or S or D \nSecond character: A, B, C or D \nLast three characters must be unitary natural numbers.\n")
            print("        TITLE FORMAT\nTitle length must contain less than 30 characters and cannot be left blank.\n")
            print("        DURATION FORMAT\nVideo length must be between 1 and 500 minutes.\n")
            print("        RATING FORMAT\nRating must be between 1 and 5 stars.\n")
            print("        AUDIENCE FORMAT\nAudience length must be less than 15 characters and cannot be left blank.\n")
            print("        GENRE FORMAT\nGenre length must be less than 15 characters and cannot be left blank.\n")

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

        working_dic, __ = self.file_processing()

        lst = []
        for value in working_dic.values():
            if value[0] not in lst:
                lst.append(value[0])

        if (self.ID not in working_dic.keys()):
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

        #movie

        if(self.ID[0] == first_char[0]):

            loading = 'The ID is being validated...'
            for i in range(0,28):
                print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)

            if (self.title not in lst):

                self.data_writing()
                print('Successfully added!')

            else:
                print("Oops! You cant register a new ID with an existing movie title")
        #series

        elif (self.ID[0] == first_char[1]):

            loading = 'The ID is being validated...'

            for i in range(0,28):
                print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)
    
            print("\nThe ID is valid! We can now validate the series properties.")
            self.season_episode_verification()
            
        #documentary

        else:

            loading = 'The ID is being validated...'
            for i in range(0,28):
                print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)
            
            if (self.season != "" and self.episode != "" and self.episode_title != "" and self.topic != ""):

                response = self.season_episode_verification()
                if response != None:
                    print("\nThe Documentary has been added!")

            elif (self.topic != ""):

                self.data_writing()
                print("\nThe Documentary has been added!")
                    
            else:

                print("You must enter a topic, in order to add a documentary to the file!")
            
    def season_episode_verification(self):

        if(self.season != "" and int(self.season) <=500 and int(self.season) >= 1 and self.episode != "" and int(self.episode) <= 500 and int(self.episode) >= 1 and self.episode_title != "" and len(self.episode_title) <= 30 ):

            __, current_dic = self.file_processing()

            if bool(current_dic) == False:
                print("The series was non-existent (",self.title, ") it has now been added!")
                self.data_writing()
                return "Success"
            else:
                title_dic = {}
                title_dic[self.title] = current_dic.values()
                del current_dic

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
                    return "Success"

                else:
                    if self.episode not in episode_ls:
                        if self.episode_title not in episode_title_ls:
                            print("A new episode has been added to the series: ", self.title, " with season number : ", self.season)
                            self.data_writing()
                            return "Success"

                        else:
                            print("The entry cannot be written because the episode title: ", self.episode_title, "already exists!")
                    else:
                        print("The entry cannot be written because the episode number: ", self.episode, "already exists!")
        else:
            print("Sorry some of the data entered doesn't match the constraints needed, please verify you are using the following input format:\n")
            print("        SEASON FORMAT\nSeason number must be between 1 and 500.\n")
            print("        EPISODE FORMAT\nEpisode number must be between 1 and 500.\n")
            print("        EPISODE TITLE FORMAT\nEpisode title length must be less than 30 characters.\n")
            print("        THEME FORMAT\nTheme length must be less than 30 characters.\n")

    def file_processing(self):

        with open("videos.csv", "r", encoding="utf-8") as movie_reading:
            
            working_dic = {}
            current_dic = {}

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

                working_dic[key] = title, duration, rating, audience, gender, season, episode, ep_title, topic, key
                
                if self.title != None and self.title == title:
                    current_dic[key] = season,episode,ep_title

        return(working_dic,current_dic)

class Lists():
    def general(self,data, number, upper = "", lower = ""):

        writer = Writer()
        working_dic, __ = writer.file_processing()

        if data != "D\n" and data != "R\n":
            search_dic = {}
            for value in working_dic.values():
                header = value[number]
                if header.find(data) != -1:
                    search_dic[value[9]] = value
            
            if bool(search_dic) == False:
                return(None)

            else:
                print("The following entries with the given keywords were found:")
                return(search_dic)

        elif data == "D\n" and data != "R\n":
            data = "D"
            search_dic = {}
            for value in working_dic.values():
                header = value[number]
                if header.find(data,0,1) != -1:
                    search_dic[value[9]] = value
            
            if bool(search_dic) == False:
                return(None)

            else:
                print("The following entries with the given keywords were found:")
                return(search_dic)

        else:
            search_dic = {}
            for value in working_dic.values():
                header = value[number]
                if float(header) >= lower and float(header) <= upper:
                    search_dic[value[9]] = value
            
            if bool(search_dic) == False:
                return(None)

            else:
                print("The following entries with the given ratings were found:")
                return(search_dic)
