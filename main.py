# import csv
#
# with open ("weather.csv") as datas:
#     data = csv.reader(datas)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#
    #more data sp we use pandas library for data analysis

import pandas

data = pandas.read_csv("weather.csv")
print(type(data))#check the type
# print(data["temp"])
