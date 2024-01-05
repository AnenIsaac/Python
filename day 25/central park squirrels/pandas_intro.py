"""with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)"""

"""import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])
            
    print(temperatures)
"""
# import pandas
# import math

# data = pandas.read_csv("weather_data.csv")
# data_list = data["temp"].to_list()
# print(data_list)
# avg = sum(data_list) / len(data_list)
# print(f"average = {avg}")

# print(f"average = {data['temp'].mean()}")

# print(f"Maximum = {data['temp'].max()}")

# #getting data in columns
# data['condition']
# data.condition

# #getting data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# monday = data[data.day == "Monday"]
# print(data[data.day == "Monday"])
# print(monday.condition)
# monday_temp = int(monday.temp.iloc[0])
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# creating a dataframe from scratch
# data_dict = {"student": ["Anen", "Isaac", "Angela"], "scores": [90, 70, 67]}

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
list = data["Primary Fur Color"]

# get the data for each type of squirrel into seperate dfs
grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]

# count the number of occurences
grey_squirrel_count = len(grey_squirrel)
cinnamon_squirrel_count = len(cinnamon_squirrel)
black_squirrel_count = len(black_squirrel)

# make a dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count],
}

# make a dataframe
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(df)

# print(data_dict)
# # new colors dataframe
# colors_data = pandas.DataFrame(data_dict)
# print(colors_data)
# value_counts = list.value_counts()
# print(value_counts)
