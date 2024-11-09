#Приклад 1
counter = 0

while counter <= 5:
    print("\n"*1)
    print(f"Лічильник: {counter}")
    counter += 1
else:
    print("Цикл завершено, умова більше не істинна.")





#Приклад 2
counter = 0

while counter < 5:
    print(f"Лічильник: {counter}")
    counter += 1
    if counter == 3:
        print("Зупинка циклу за допомогою break")
        break
else:
    print("Цикл завершено, умова більше не істинна.")  # Цей рядок не виконається через `break`.
