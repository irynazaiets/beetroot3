# Завдання на практику
# Створіть модуль для управління бібліотечними книгами з 
# двома функціями та покрийте їх тестами, використовуючи 
# unittest.
# Функція 1: calculate_fine(days_overdue) Розраховує штраф
# за прострочення повернення книги. Правила:
# Перші 3 дні: безкоштовно (штраф 0)
# 4-10 днів: 10 грн за кожен день прострочки
# 11+ днів: 20 грн за кожен день прострочки
# Вхідний параметр має бути цілим невід‘ємним числом
# Функція 2: can_borrow_books(current_borrowed, age, 
# has_overdue=False) Перевіряє, чи може користувач 
# позичити ще книги. Правила:
# Діти (до 18 років) можуть мати максимум 3 книги
# Дорослі можуть мати максимум 5 книг
# Якщо є прострочені книги (has_overdue=True), 
# нові книги позичити не можна
# Вхідні параметри current_borrowed та age мають бути 
# цілими невід’ємними числами
# Завдання:
# Реалізуйте ці дві функції
# Напишіть юніт тести використовуючи unittest бібліотеку
# Протестуйте:
# Звичайні випадки використання
# Граничні випадки
# Обробку помилок (TypeError, ValueError)
# Різні комбінації вхідних параметрів
# Тести повинні бути організовані в клас, що наслідується 
# від unittest.TestCase.

def calculate_fine(days_overdue):
    if not isinstance(days_overdue, int):
        raise TypeError("Кількість прострочених днів має бути цілим числом")
    if days_overdue < 0:
        raise ValueError("Кількість прострочених днів не може бути від'ємною")
    
    if days_overdue <= 3:
        return 0
    elif days_overdue > 3 and days_overdue <= 10:
        fine = 10
        return days_overdue * fine
    else:
        fine = 20
        return days_overdue * fine


def can_borrow_books(current_borrowed, age, has_overdue=False):
    if not isinstance(current_borrowed, int):
        raise TypeError("Кількість позичених книг має бути цілим числом")
    if not isinstance(age, int):
        raise TypeError("Вік має бути цілим числом")
    if current_borrowed < 0:
        raise ValueError("Кількість позичених книг не може бути від'ємною")
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    
    if has_overdue:
        return False
    
    max_books = 0
    if age < 18:
        max_books = 3
    else:
        max_books = 5
    return current_borrowed < max_books

import unittest

class TestFunctions(unittest.TestCase):
    def test_calculate_fine(self):
        self.assertEqual(calculate_fine(2), 0)
        self.assertEqual(calculate_fine(5), 50)
        self.assertEqual(calculate_fine(11), 220)
    
    def test_calculate_fine_errors(self):
        with self.assertRaises(TypeError):
            calculate_fine("2", 0)

        with self.assertRaises(TypeError):
            calculate_fine(2.5, 0)
        
        with self.assertRaises(ValueError):
            calculate_fine(-10, 0)
    
    def test_can_borrow_books_errors(self):
        with self.assertRaises(TypeError):
            can_borrow_books("2", 0)

        with self.assertRaises(TypeError):
            can_borrow_books(2.5, 0)
        
        with self.assertRaises(ValueError):
            can_borrow_books(-10, 0)

        