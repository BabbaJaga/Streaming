with open("movies.csv", "r", encoding="utf-8") as movie_reading:
    movie_dick = {}
    serie_dick = {}
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
            serie_dick[serie_key] = serie_title, str(season), str(episode), ep_title

        else:
           print("useless")


for value in serie_dick.values():
    print(value[1])
