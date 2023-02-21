# import csv
#
# with open("weather_data.csv") as data_file:
#     data_file = csv.reader(data_file)
#     temperature = []
#     for row in data_file:
#         print(row)
#         if row[1] == "temp":
#             continue
#
#         temperature.append(int(row[1]))
#
#     print(temperature)
#    #################################################

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print("Temperature:")
# print(data["temp"])


# To dict
# data_dict = data.to_dict()
# print(data_dict)


# To list => Converts to raw python datatype
# data_list = data["temp"].to_list()
# print(data_list)

# Mean or average
# print(data["temp"].mean())

# Max
# print(data["temp"].max())

# Data in columns
# print(f"data.condition: {data.condition}")
# print(f"data['condition']: {data['condition']}")

# Get data in a row
# print(data[data.day == "Monday"])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp) * 9/5 + 32
# print(monday_temp)

#  Get row with the max temp
# print(data[data.temp == data.temp.max()])

# Creating a dataframe
data_dict = {
    "students": ["Amy", "James", "Jane"],
    "scores": [76, 85, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_dataframe.csv")


























