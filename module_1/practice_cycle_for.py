# Завдання 2: Порахуйте кількість голосних букв у
# рядку text = "Hello World".

text = "Hello World Anna"
vowels_list = ['a', 'e', 'i', 'o', 'u']
counter = 0

for letter in text:
    if letter in vowels_list:
        counter += 1

print("\n"*2)
print(counter)

