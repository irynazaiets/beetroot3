# 6. Напишіть функцію, яка приймає список і 
# повертає кількість елементів у ньому.

def count_elements_in_list(my_list):
    len_of_my_list = len(my_list)
    for el in my_list:
        if el>5:
            return el
    return len_of_my_list


input_list = [1, 2, 3, 4, 5]
print("\n")
print(count_elements_in_list(input_list))

def count_elements_in_list(*args):
    tuple_to_list = list(args)
    len_of_list = len(tuple_to_list)
    return len_of_list

print("\n")
print("Кількість елементів в списку: ", 
      count_elements_in_list(1, 2, 3, 4, 5))