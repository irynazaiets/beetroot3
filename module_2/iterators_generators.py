# Приклад: Користувацький Ітератор
def fibonacci_iterator(n):
    class Fibonacci:
        def __init__(self, n):
            self.n = n
            self.current = 0
            self.next = 1
            self.count = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.count >= self.n:
                raise StopIteration
            result = self.current
            self.current, self.next = self.next, self.current + self.next
            self.count += 1
            return result

    return Fibonacci(n)

# Використання:
print("Користувацький Ітератор:")
for num in fibonacci_iterator(10):
    print(num)


# Приклад: Генераторна функція
def fibonacci_generator(n):
    current, next_ = 0, 1
    for _ in range(n):
        yield current
        current, next_ = next_, current + next_

# Використання:
print("\nГенераторна Функція:")
for num in fibonacci_generator(10):
    print(num)


# Приклад "лінивої" обчислюваності
# lazy evaluation
def large_sequence_sum(limit):
    print("Обчислення суми великої послідовності...")
    for i in range(limit):
        yield i

lazy_sum = sum(large_sequence_sum(1000000))
# print(f"Сума з використанням "лінивої" обчислюваності: {lazy_sum}")


# itertools Приклади
from itertools import count, cycle, repeat, product, permutations, combinations, combinations_with_replacement, compress, filterfalse, groupby, chain, islice, accumulate
import operator

# Нескінченні ітератори
print("\nНескінченні Ітератори:")
for i in count(5, 2):
    print(i)
    if i > 15:
        break

print(list(repeat(10, 3)))

# Комбінаторика
print("\nКомбінаторика:")
print(list(product("AB", [1, 2])))
print(list(permutations("ABC", 2)))
print(list(combinations("ABC", 2)))
print(list(combinations_with_replacement("AB", 2)))

# Фільтрація
print("\nФільтрація:")
data = "ABCDEFG"
selectors = [1, 0, 1, 0, 0, 1, 0]
print(list(compress(data, selectors)))

data = [1, 2, 3, 4]
print(list(filterfalse(lambda x: x % 2 == 0, data)))

# Групування
print("\nГрупування:")
data = [1, 1, 2, 2, 3]
for key, group in groupby(data):
    print(key, list(group))

# Об'єднання послідовностей
print("\nОб'єднання Послідовностей:")
print(list(chain([1, 2], ["A", "B"])))
print(list(islice(range(10), 2, 7, 2)))

# Арифметичні операції
print("\nАрифметичні Операції:")
data = [1, 2, 3, 4]
print(list(accumulate(data, operator.mul)))
