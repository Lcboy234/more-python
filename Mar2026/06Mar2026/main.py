# # # import csv

# # # with open("weather_data.csv") as data_file:
# # #     data = csv.reader(data_file)
# # #     temperatures = []

# # #     for row in data:
# # #         if row[1] != "temp":
# # #             temperatures.append(int(row[1]))

# # #     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data)
# # print(data["temp"])

# # data_dict = data.to_dict()
# # print(data_dict)

# # temp_list = data["temp"].to_list()

# # average = sum(temp_list) / len(temp_list)
# # print(temp_list)

# # # print(data["temp"].mean())
# # # print(data["temp"].max())
# # # print(data["temp"].min())
# # # print(data["temp"].median())

# # print(data["condition"])
# # print(data.condition)

# # search for column for Monday and return Row
# # print(data[data.day == "Monday"])

# # print(data[data.temp == data.temp.max()])

# # don't print, use monday as variable and save the row inside
# # monday = data[data.day == "Monday"]

# # print(monday.temp)

# # monday_temp = monday.temp[0]
# # monday_temp_F = monday_temp * 9 / 5 + 32
# # print(monday_temp_F)

# data_dict = {
#     "people": ["Kai1", "Kai2", "Kai3"],
#     "scores": [77, 56, 70]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["grey", "black", "red"],
    "Count": [grey_count, black_count, red_count]
}

final_data = pandas.DataFrame(data_dict)
print(final_data)
final_data.to_csv("squirrel_count.csv")