# атрибути інстансу

# first_variable

class Dog:
    def __init__(self, name, poroda, age):
        self.name = name
        self.poroda = poroda
        self.age = age
        
    def bark(self):
        return f"{self.name} says Gav!"


# Створення об'єктів
dog1 = Dog("Brovko", "Golden Retriever", 5)
dog2 = Dog("Tuzik", "Bulldog", 7)

print(dog1.bark())  # Brovko says Gav!
print(dog2.bark())  # Tuzik says Gav!


# атрибути класу
class Dog:
    animal_type = "Ссавець"  # Атрибут класу

    def __init__(self, name, poroda):
        self.name = name  # Атрибут представника/екземпляра/інстанса/об‘єкту
        self.poroda = poroda

print(Dog.animal_type)  # Ссавець

dog = Dog("Rex", "Beagle")
print(dog.animal_type)  # Ссавець
print(dog.name)
print(dog.poroda)
