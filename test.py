import pandas

with open("videos.csv", "r") as file:
    df = pandas.DataFrame(file)
    print(type(df))