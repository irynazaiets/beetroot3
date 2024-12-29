# 1. Як з-під інстансу дочірнього класу доступитися 
# до методів батьківського класу?
class Parent:
    def greet(self):
        print("Hello from Parent!")


class Child(Parent):
    pass

child_instance = Child()
child_instance.greet()  # Виведе: "Hello from Parent!"




# Якщо метод перевизначений у дочірньому класі, але 
# потрібен доступ до оригінального методу батьківського класу:
class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        super().greet()  # Викликаємо greet() з Parent
        print("Hello from Child!")

child_instance = Child()
child_instance.greet()
# Виведе:
# Hello from Parent!
# Hello from Child!



# # method overriding
# # 2. Як в дочірньому класі перевизначити метод батьківського класу?
# class Parent:
#     def greet(self):
#         print("Hello from Parent!")

# class Child(Parent):
#     def greet(self):
#         print("Hello from Child!")  # Перевизначення методу

# child_instance = Child()
# child_instance.greet()  # Виведе: "Hello from Child!"

# 3. Чи можна наслідувати від кількох класів одночасно?
class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method1(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    super().method1()

print('\n')
child_instance = Child()
child_instance.method1()  # Виведе: "Method from Parent1"
# child_instance.method1()  # Виведе: "Method from Parent2"
