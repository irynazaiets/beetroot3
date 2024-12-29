from abc import ABC, abstractmethod

class Shape(ABC):  # Успадковуємося від ABC
    @abstractmethod
    def area(self):
        """Вираховує площу фігури."""
        pass

    @abstractmethod
    def perimeter(self):
        """Вираховує периметр фігури."""
        pass

# Спроба створити об'єкт Shape викличе помилку
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Тепер можна створити об'єкт Rectangle
rect = Rectangle(10, 20)
print("Area:", rect.area())       # Output: Area: 200
print("Perimeter:", rect.perimeter())  # Output: Perimeter: 60
