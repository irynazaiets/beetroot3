class MyClass:
    def __init__(self):
        self.public_attr = 42             # Публічний атрибут
        self._protected_attr = 100        # Захищений атрибут
        self.__private_attr = 200         # Приватний атрибут

    def __add__():
        pass

    def __str__():
        pass

    def show_public(self):
        print(f"Public attribute: {self.public_attr}")

    def show_protected(self):
        # return self._protected_attr
        print(f"Protected attribute: {self._protected_attr}")

    def __show_private(self):
        print(f"Private attribute: {self.__private_attr}")


# 1. Name mangling: доступ до приватного атрибута через маніпуляцію з іменами
obj = MyClass()
print(obj._MyClass__private_attr)  # За допомогою name mangling можна доступити приватний атрибут

# 2. Використання getattr(): доступ до атрибуту через reflection
# Пряме використання не можна, але можна через getattr
print(getattr(obj, "_protected_attr"))  # Захищений атрибут доступний через getattr()

# 3. Виведення приватного атрибуту через відповідний метод (запуск метода для отримання приватного атрибута)
obj._MyClass__show_private()  # Доступ до приватного методу через його ім'я, використовуючи name mangling

# Приклад для публічних, захищених та приватних атрибутів:
obj.show_public()          # Публічний атрибут доступний без обмежень
obj.show_protected()       # Захищений атрибут доступний в межах цього класу
# obj.__show_private()      # Цей метод не можна викликати так (він призначений як приватний, для виклику через name mangling)


