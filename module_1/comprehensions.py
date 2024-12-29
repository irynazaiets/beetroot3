# new_list = [вираз for елемент in ітерабельний_об’єкт if умова]

# генератори списків - list comprehension (set, dict)

# Basic List
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]

# print("\n"*2)
# print(numbers)
# print(squares)
# Basic Set
# words = ["apple", "banana", "apple", "cherry"]
# unique_lengths = {len(word) for word in words}

# # Basic Dict
# numbers = [1, 2, 3]
# squares = {x: x**2 for x in numbers}



# LIST
# Using a condition:
even_numbers = [x for x in numbers if x % 2 == 0]
# even_numbers = [2, 4]

# With an if-else statement:
# labeled_numbers = [x for x in numbers "even" if x % 2 == 0 else "odd"]
# labeled_numbers = ["odd", "even", "odd", "even", "odd"]

print("\n"*2)
print(numbers)
print(even_numbers)
# print(labeled_numbers)


# # SET
# # Using a condition:
# numbers = [1, 2, 3, 4, 5, 5, 6]
# even_numbers = {x for x in numbers if x % 2 == 0}
# # even_numbers = {2, 4, 6}

# # DICT
# Using a condition:
numbers = ["a", "b", "c"]
even_squares = {x: x**2 for x in range(len(numbers)) if x % 2 == 0}
# even_squares = {0: 0, 2: 4, 4: 16}

# With an if-else statement:
numbers = range(5)
parity = {x: ("even" if x % 2 == 0 else "odd") for x in numbers}
# parity = {0: "even", 1: "odd", 2: "even", 3: "odd", 4: "even"}


# if at the beginning VS at the end:
# [x if x % 2 == 0 for x in range(5)]

# [x for x in range(5) if x % 2 == 0]