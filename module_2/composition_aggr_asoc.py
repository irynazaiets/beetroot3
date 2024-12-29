# Асоціація (Association)
# Загальний зв’язок між класами, де один клас 
# використовує інший (передача повідомлень). Це 
# найменш обмежуючий зв'язок.
class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self):
        self.employees = []

company = Company()
employee = Employee("Anna")
company.employees.append(employee)


# Композиція (Composition)
# Опис: Тісний вид асоціації, де один клас "володіє" 
# іншим. Це зв’язок "has-a (має)", причому життєві цикли 
# об'єктів пов'язані.
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()


# Агрегація (Aggregation)
# Опис: Слабкий вид композиції, де один клас посилається на 
# інший без прив’язки їх життєвих циклів.
# Об’єкт-підлеглий може існувати самостійно, незалежно від 
# головного об’єкта.
class Course:
    def __init__(self, title):
        self.title = title
        # self.students = []

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

course1 = Course("Math")
student = Student("Ivan")
student.courses.append(course1)
