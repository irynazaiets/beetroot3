# Незмінюваний тип - рядок
original_str = "Hello"
new_str = original_str.replace("H", "J")  # Створення нової копії
print("Original:", original_str)  # "Hello"
print("New:", new_str)  # "Jello"


# Змінюваний тип - список
original_list = [1, 2, 3]
original_list = 99  # Змінюємо без створення нової копії
print("Modified list:", original_list)  # [99, 2, 3]


# Незмінюваний тип - кортеж
original_tuple = (1, 2, 3)
# Оновити значення кортежа можна тільки через створення нового кортежа
new_tuple = (99,) + original_tuple[1:]
print("Original tuple:", original_tuple)  # (1, 2, 3)
print("New tuple:", new_tuple)  # (99, 2, 3)


# Змінюваний тип - множина
original_set = {1, 2, 3}
original_set.add(4)  # Додаємо новий елемент без створення копії
print("Modified set:", original_set)  # {1, 2, 3, 4}
