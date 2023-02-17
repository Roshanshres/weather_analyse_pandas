import csv

with open ("weather.csv") as datas:
    data = csv.reader(datas)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)