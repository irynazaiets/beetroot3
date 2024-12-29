import csv
data_2= [
    ["Name", "Age", "City"],
    ["Viki", 25, "Rivne"],
    ["Lara", 45, "Korec"],
    ["Leon", 22, "Goshcha"]
]

def writer_1(data, file):
    writer = csv.writer(file)
    writer.writerows(data)

    return data

with open("module_1/example.csv", mode="w", encoding="utf-8") as file:
    writer_1(data = data_2, file = file)