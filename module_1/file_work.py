with open("example.txt", "r") as file:
    content = file.read()  # Зчитує весь текст
    print(content)

# # Method 1 (not recommended)
file_object = open('my_file.txt')
data = file_object.read()
file_object.close()

# Method 2 (recommended)
# контекстні менеджери
with open('module_1/my_file.txt', 'r+') as file_object:
    data = file_object.read()
    data = 'Monday'
    file_object.write(data)


# Приклад з file.seek()
with open("module_1/example.txt", "r+") as file:
    my_string = "['el1', 'el2']"
    print("\n")
    file.write(my_string)  # Записуємо нові дані
    file.seek(0)  # Повертаємо вказівник на початок
    print("Write a second time")
    file.write("New content after seek method")
    file.seek(0)
    print(file.read())  # Читаємо весь файл з оновленнями
