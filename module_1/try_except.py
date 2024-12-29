try:
    num = int(input("Введіть число: "))
    result = 10 / num
    print("Результат:", result)
except ValueError:
    print("Помилка: Ви ввели не число!")
except ZeroDivisionError:
    # print(result, type(result))
    print("Помилка: Ділення на нуль!")
except Exception as e:  # Загальний відлов виключень
    print(f"Невідома помилка: {e}")
finally:
    print("Програма завершена.")

# num = int(input("Введіть число: "))
# result = 10 / num
# print(result)

# валідація даних
def set_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від’ємним.")
    print(f"Ваш вік: {age}")

set_age(-5)  # Викличе помилку ValueError

# створення власних винятків
def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Число не може бути від’ємним.")
    print(f"Число {number} коректне.")

try:
    check_positive(-10)
except NegativeNumberError as e:
    print(f"Помилка: {e}")
