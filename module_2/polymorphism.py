from collections.abc import Iterable


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ==
    # method overriding
    def __eq__(self, value: object) -> bool:
        pass

    def __dir__(self) -> Iterable[str]:
        pass

    # +
    def __add__():
        pass

    def get_info(self):
        print(f"This is {self.name} and he/she is {self.age} years old")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Person({self.name}, {self.age})"


person = Person("Anna", 30)
person.__dir__()
print(person)            # Викликає __str__: Name: Anna, Age: 30
print(repr(person))      # Викликає __repr__: Person(Anna, 30)


# == 
"#" * 8
"str1" + "str2"

len()
print()

__dict__ # dunder - Double under
# _variable = 4
# variable_ = 5
# __variable = 7
# __variable__ = 8