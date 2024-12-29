import csv
from json import decoder


# 2. Читання CSV-файлу
with open("module_1/example.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("\nВміст файлу 'example.csv':")
    for row in reader:
        print(row)

with open("module_1/example.csv", mode='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    # print("\nЧитання з використанням DictReader:")
    for row in reader:
        # print(row)
        print(f"Ім'я: {row['Name']}, Прізвище: {row['Surname']} Вік: {row['Age']}, Місто: {row['City']} Країна {row['Country']}")



my_str = 'Beetroot lesson'
for i in my_str:
    print(i)

if 'e' in my_str:
    print("Так, цей елемент присутній в стрічці")
else:
    pass


def my_function():
    pass

my_variable = my_function()

print(my_function())