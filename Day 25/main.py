# with open("Day 25/weather_data.csv") as data_file:
#     data = data_file.readlines()

# print(data)

# import csv

# with open("Day 25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempreatures = []
#     for row in data:
#         if row[1] != 'temp':
#             tempreatures.append(int(row[1]))

# print(tempreatures)

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("Day 25/weather_data.csv")
# print(type(data))
# print(type(data['temp']))

# pandas Data Frame to dictionary
# data_dict = data.to_dict()
# # print(data_dict)

# # pandas Series to list
# temp_list = data['temp'].to_list()
# # print(temp_list)

# # calculation of average temp
# avg_temp = sum(temp_list) / len(temp_list)
# print(round(avg_temp))

# print(data['temp'].mean())
# print(data['temp'].max())

# print(data['condition'])

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a Data Frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

students = pd.DataFrame(data_dict)
students.to_csv("Day 25/students.csv")
