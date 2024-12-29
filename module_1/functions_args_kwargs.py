# Приклад без використання позиційних аргументів
# ARGS
def sum_all(*args): #arguments
    return sum(args)

# print(sum_all(1, 2, 3))  # 6

# KWARGS
def print_info(**kwargs): #key-word-arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info = {'name':'Alice', 'age': 25, 'city': 'Kyiv'}
# print_info(info=info)  
# name: Alice
# age: 25


# *args збирає усі позиційні аргументи, що залишилися після звичайних параметрів
def example(a, b, *args):
    if len(args) == 0:
        print("*args is empty")
        return 'empty'
    else:
        print(f"a = {a}, b = {b}, args = {args}")
    

result = example(1, 2)
# Вивід:
# a = 1, b = 2, args = (3, 4, 5)


# Іменовані аргументи, які залишилися після звичайних параметрів, збираються у kwargs
def example(a, b, **kwargs):
    print(f"a = {a}, b = {b}, kwargs = {kwargs}")

# example(1, 2, name="Alice", age=30)
# Вивід:
# a = 1, b = 2, kwargs = {'name': 'Alice', 'age': 30}


# ARGS та KWARGS разом
def example(a, *args, **kwargs):
    print(f"a = {a}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

# print("\n"*2)
# example(1, 2, 3, name="Alice", age=30, city = 'Kyiv')
# print("\n")
# Вивід:
# a = 1
# args = (2, 3)
# kwargs = {'name': 'Alice', 'age': 30}




