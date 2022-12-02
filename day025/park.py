import pandas

x = pandas.read_csv("centralPark.csv")

grey_count = len(x[x["Primary Fur Color"] == 'Gray'])
red_count = len(x[x["Primary Fur Color"] == 'Cinnamon'])
black_count = len(x[x["Primary Fur Color"] == 'Black'])

data_dict = {
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count" : [grey_count,red_count,black_count]
}

y = pandas.DataFrame(data_dict)
y.to_csv("central.csv")