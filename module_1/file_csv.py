import csv

# 1. Створення CSV-файлу
data = [
    ["Name", "Age", "City"],
    ["Anna", 25, "Kyiv"],
    ["Ivan", 30, "Lviv"],
    ["Olga", 22, "Odesa"]
]

with open("example.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV-файл 'example.csv' створено.")

# 2. Читання CSV-файлу
with open("example.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("\nВміст файлу 'example.csv':")
    for row in reader:
        print(row)

# 3. Читання CSV з обробкою заголовків
with open("example.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("\nЧитання з використанням DictReader:")
    for row in reader:
        print(f"Ім'я: {row['Name']}, Вік: {row['Age']}, Місто: {row['City']}")


# 4. Додавання нових рядків до існуючого CSV-файлу
new_data = [
    ["Oksana", 28, "Kharkiv"],
    ["Dmytro", 35, "Dnipro"]
]

with open("example.csv", mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(new_data)

print("\nДодано нові рядки до 'example.csv'.")




# 5. Фільтрація даних: створення нового CSV з умовою
filtered_data = []
with open("example.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["Age"]) > 25:  # Вік більше 25
            filtered_data.append(row)

with open("filtered.csv", mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_data)

print("\nФільтрований CSV-файл 'filtered.csv' створено.")
