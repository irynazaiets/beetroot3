import json

# JSON - JavaScript Object Notation

# Приклад 1
# Читання з JSON-файлу
with open("data.json", "r") as file:
    data = json.load(file)  # Завантажуємо JSON у Python об'єкти
print(data)



# Приклад 2
# Запис Python-об'єктів у JSON
data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding", "hiking"]
}

# Запис у файл
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)  # indent для читабельності
