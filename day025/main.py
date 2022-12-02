# import csv
# import pandas
#
# # with open("./weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     print(data)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #           temperature.append(int(row[1]))
# #     print(temperature)
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# #
# # print(data["temp"].mean())
# # print(data["temp"].size())
#
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
# print(((monday.temp)*(9/5))+32)


import pandas

data = {
	"age" : [1,2,3],
	"name" : ['A','B','C']
}

x = pandas.DataFrame(data , index = ["a" , "b" , "c"])

print(x.loc["a"])