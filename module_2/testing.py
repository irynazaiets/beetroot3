# Припустимо, у нас є простий клас Calculator
class Calculator:
    def add(self, x, y):
        return x + y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

# Тестування з використанням unittest
import unittest

class TestCalculatorUnittest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(4, 2), 6)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)






# Тестування з використанням pytest
import pytest

class TestCalculatorPytest:
    @pytest.fixture
    def calculator(self):
        return Calculator()
    
    def test_add(self, calculator):
        assert calculator.add(4, 2) == 6
        assert calculator.add(-1, 1) == 0
        assert calculator.add(-1, -1) == -2
    
    def test_divide(self, calculator):
        assert calculator.divide(6, 2) == 3
        assert calculator.divide(5, 2) == 2.5
    
    def test_divide_by_zero(self, calculator):
        with pytest.raises(ValueError):
            calculator.divide(10, 0)

# Приклад параметризованого тесту з pytest
@pytest.mark.parametrize("x, y, expected", [
    (4, 2, 6),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 5, 5)
])
def test_add_parametrized(calculator, x, y, expected):
    assert calculator.add(x, y) == expected

# Приклад використання фікстур з областю видимості
@pytest.fixture(scope="module")
def expensive_resource():
    # Підготовка ресурсу
    resource = "Expensive Resource"
    yield resource
    # Очищення ресурсу
    resource = None
