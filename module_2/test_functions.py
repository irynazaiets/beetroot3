# Функції, які будемо тестувати
def calculate_discount(price, discount_percent):
    """Розраховує знижку на товар"""
    if not isinstance(price, (int, float)) or not isinstance(discount_percent, (int, float)):
        raise TypeError("Ціна та знижка повинні бути числами")
    if price < 0 or discount_percent < 0:
        raise ValueError("Ціна та знижка не можуть бути від'ємними")
    if discount_percent > 100:
        raise ValueError("Знижка не може бути більше 100%")
    
    return price * (1 - discount_percent / 100)

def get_user_status(age):
    """Повертає статус користувача базуючись на віці"""
    if not isinstance(age, int):
        raise TypeError("Вік повинен бути цілим числом")
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    
    if age < 13:
        return "child"
    elif age < 20:
        return "teenager"
    elif age < 65:
        return "adult"
    else:
        return "senior"

# Тести з використанням unittest
import unittest

class TestFunctions(unittest.TestCase):
    def test_calculate_discount_basic(self):
        self.assertEqual(calculate_discount(100, 20), 80)
        self.assertEqual(calculate_discount(50, 10), 45)
        self.assertEqual(calculate_discount(200, 0), 200)
    
    def test_calculate_discount_errors(self):
        # Перевірка на некоректні типи даних
        with self.assertRaises(TypeError):
            calculate_discount("100", 20)
        
        # Перевірка на від'ємні значення
        with self.assertRaises(ValueError):
            calculate_discount(-100, 20)
        
        # Перевірка на завелику знижку
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)

    def test_get_user_status(self):
        self.assertEqual(get_user_status(10), "child")
        self.assertEqual(get_user_status(15), "teenager")
        self.assertEqual(get_user_status(30), "adult")
        self.assertEqual(get_user_status(70), "senior")
    
    def test_get_user_status_errors(self):
        with self.assertRaises(TypeError):
            get_user_status(10.5)
        with self.assertRaises(ValueError):
            get_user_status(-5)

# # Тести з використанням pytest
# import pytest

# def test_calculate_discount():
#     assert calculate_discount(100, 20) == 80
#     assert calculate_discount(50, 10) == 45
#     assert calculate_discount(200, 0) == 200

# def test_calculate_discount_invalid_input():
#     with pytest.raises(TypeError):
#         calculate_discount("100", 20)
#     with pytest.raises(ValueError):
#         calculate_discount(-100, 20)
#     with pytest.raises(ValueError):
#         calculate_discount(100, 150)

# # Приклад параметризованого тесту
# @pytest.mark.parametrize("age,expected_status", [
#     (10, "child"),
#     (15, "teenager"),
#     (30, "adult"),
#     (70, "senior")
# ])
# def test_get_user_status_parametrized(age, expected_status):
#     assert get_user_status(age) == expected_status

# def test_get_user_status_errors():
#     with pytest.raises(TypeError):
#         get_user_status(10.5)
#     with pytest.raises(ValueError):
#         get_user_status(-5)