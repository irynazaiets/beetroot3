# 1. Присвоєння функції змінній
def greet(name):
    return f"Hello, {name}!"

say_hello = greet
print(say_hello("Danylo"))  # Hello, Danylo!


# 2. Функції як аргументи інших функцій
def square(x):
    return x ** 2

def execute(func, value):
    return func(value)

result = execute(square, 4)
print(result)  # 16


# 3. Вкладені функції (nested functions)
def func1():  #Outer function
    msg = 'I belong to func1'
    def func2(): #Nested function
        msg2 = 'tuesday'
        print (msg)
    return func2


# 4. Зберігання функцій у структурах даних
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

operations = {
    "add": add,
    "subtract": subtract
}

print(operations["add"](x = 10, y = 5))      # 15
print(operations["subtract"](10, 5))  # 5


# 5. Анонімні (одноразові) функції (lambda)
square = lambda x: x ** 2
print(square(3))  # 9

# Використання в списках
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # [1, 4, 9, 16]


# 6. Використання assert
def divide(a, b):
    assert b != 0, "Ділення на нуль неможливе"
    return a / b

print(divide(10, 2))  # Виведе: 5.0
print(divide(10, 0))  # AssertionError: Ділення на нуль неможливе
