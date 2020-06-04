dictionary = {}

with open('movies.csv','r', encoding = 'utf-8') as movies:
    reading = movies.readlines()
    for line in reading:
        string = line.split(',')
        ID = string[0]
        dictionary[ID] = string[1]

print(dictionary)