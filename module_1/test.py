# # import random
# # _list = list(input("Please enter any word: "))
# # for i in range(5):
# #     random.shuffle(_list)
# #     print("".join(_list))
# client_age = 16
# client_location = 'Dnipro'

# if client_age < 18:
#     print('Не продаємо певні групи товарів')
# if client_age >= 18: # else:
#     print("Продаємо все")

# if client_location == 'Kyiv':
#     pass
# if client_location == 'Vinnytsya':
#     pass
# if client_location == 'Dnipro':
#     pass
# else:
#     print("Немає можливості самовивозу")



# def is_product_available(product1, product2, *args, **kwargs):
#     pass  # Ваша реалізація тут

# is_product_available('bread', 
#                      'coca-cola', 'salt', 'water',
#                      store="Sil'po", city='Kyiv')

# is_product_available('coca-cola', 'salt', 'water',
#                      product1='bread', product2='')


import random

variable___ = 'my string'

# DRY - don't repeat yourself, не повторюйся

count = 0
list1 = []
while count < 10:
    random_int = random.randint(1, 10)
    list1.append(random_int)
    count += 1

count = 0
list2 = []
while count < 10:
    random_int = random.randint(1, 10)
    list2.append(random_int)
    count += 1

count = 0
list1 = []
list2 = []
while count < 10:
    # random_int1 = 
    random_int2 = random.randint(1, 10)
    list1.append(random.randint(1, 10))
    list2.append(random_int2)
    count += 1