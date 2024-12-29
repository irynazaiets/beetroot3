# Порожній словник
my_dict = {}
my_set = {'name', 'surname', 'age', 'city'}

# Словник з даними
my_dict = {'name': 'Anna', 'age': 25, 'family': {'father':{}, 'mother':{}}}

print("\n"*2)
print(my_dict[4])
print(my_dict.get(4))

print(my_dict['name'])
my_dict['city'] = 'Kyiv'

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)


# if my_dict.get(4) is None:
#     pass

# my_list = ['Anna', 25, 'Kyiv']
# my_list_2 = ['Kyiv', 'Anna', 25]
# my_list[2]

# Методи словника

dict.keys() # отримує список усіх ключів.
dict.values() # отримує список усіх значень.
dict.items() # отримує список пар (ключ, значення).

for item in my_dict.items():
    print(item)

# for key, value in my_dict.items():
#     print(f"{key}: {value}")

my_simple_list = ["el1", "el2", "el3", 4, 5, 78, 14]

for el in my_simple_list:
    print(el)

range()
