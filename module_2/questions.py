# Змінювані і незмінювані типи - при копіюванні 
# змінюваного типу в іншу змінну і подальші 
# операції над новою змінною змінюють першу 
# змінну яку скопіювали… для мене це не зовсім ясно. 

list1 = ['a', 'b', 'c']
print("\n")
print("list1: ", list1)
list2 = list1
print("list2: ", list2)
list2.pop(2)
print("list1 after pop: ", list1)
print("list2 after pop: ", list2)
print("ID list1: ", id(list1))
print("ID list2: ", id(list2))