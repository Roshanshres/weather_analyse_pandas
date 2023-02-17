import csv
with open ("weather.csv") as datas:
    data = csv.reader(datas)
    for row in data:
        print(row)