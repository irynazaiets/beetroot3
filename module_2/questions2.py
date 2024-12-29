# Завдання 4: Клас з методом, який приймає аргумент
# Опис: Створіть клас Person з атрибутами name (ім'я)
# і age (вік). Додайте метод introduce, який приймає 
# аргумент city і виводить: 
# "My name is Ім'я, I am Вік years old and I 
# live in Місто."


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def introduce(self, city):
        result = f"My name is {self.name}, I am {self.age} years old and I live in {city}."
        print(result)
        return result

print('\n')
person1 = Person('Anna', 25)
person1.introduce('Kremenchuk')


