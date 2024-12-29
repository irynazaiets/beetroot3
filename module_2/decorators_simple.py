@decorator
def func():
    pass

# Це еквівалентно:

def func():
    pass

func = decorator(func)


# Приклад реалізації декоратора без параметрів
def decorator(func):          # 1. Декоратор приймає функцію
    def wrapper():            # 2. Створюється нова функція (обгортка)
        print("Start")        
        func()                # 3. Виклик оригінальної функції
        print("End")
    return wrapper            # 4. Повертається нова функція

@decorator
def say_hello():
    print("Hello!")


# Приклад реалізації декоратора з параметрами
def take_parameter(n):
    def decorator(func):          # 1. Декоратор приймає функцію
        def wrapper(*args, **kwargs):            # 2. Створюється нова функція (обгортка)
            print("Start") 
            for i in range(n):       
                func(*args, **kwargs)                # 3. Виклик оригінальної функції
            print("End")
        return wrapper            # 4. Повертається нова функція
    return decorator


@take_parameter(3)
def say_hello(a, b, c):
    print("Hello!")

print("\n")
say_hello()