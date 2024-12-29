def my_generator():
    yield 1
    yield 2
    yield 3

item = my_generator()
print('\n')
print(next(item))
print(next(item))
print(next(item))
print(next(item))





# def lazy_range(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1

# custom_generator = lazy_range(5)

# print('\n')
# for num in custom_generator:
#     print(num)