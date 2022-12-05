import pandas

data = {
    "name": ["raj", "ram", "somu"],
    "age": [1, 2, 3]
}

data_frame = pandas.DataFrame(data)

for (index, value) in data_frame.iterrows():
    print(value["age"])
