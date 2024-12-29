# Базовий клас
class Vehicle:
    def __init__(self, make, model):
        self.make = make  # Марка
        self.model = model  # Модель

    def description(self):
        return f"Vehicle: {self.make} {self.model}"


# Дочірній клас Car
class Car(Vehicle):
    def __init__(self, make, model, seats):
        self.make = make
        self.model = model
        self.seats = seats  # Кількість місць

    def car_info(self):
        return f"{self.make} {self.model} has {self.seats} seats."


# Дочірній клас Truck
class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        self.make = make
        self.model = model
        self.capacity = capacity  # Вантажопідйомність у кг

    def truck_info(self):
        return f"{self.make} {self.model} can carry {self.capacity} kg."


# Створення екземплярів
car = Car("Toyota", "Corolla", 5)
truck = Truck("Volvo", "FH16", 25000)

# Виклик методів
print(car.description())  # Vehicle: Toyota Corolla
print(car.car_info())     # Toyota Corolla has 5 seats.
print(truck.description())  # Vehicle: Volvo FH16
print(truck.truck_info())   # Volvo FH16 can carry 25000 kg.
