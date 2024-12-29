class Example:
    def __init__(self, value):
        self.name = 'Iryna'
        self._value = value  # Захищений атрибут

    @staticmethod
    def utility_method(x, y):
        return x + y

    @classmethod
    def create_instance(cls, value):
        return cls(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must be positive!")
        self._value = new_value

# Використання
example = Example(10)
print(example.value)  # 10
example.value = 20    # Встановлено через сеттер
print(Example.utility_method(2, 3))  # 5
new_instance = Example.create_instance(30)
print(new_instance.value)  # 30
