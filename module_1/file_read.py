# Читає весь вміст файлу як єдиний рядок.
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Читає один рядок з файлу (до символу нового рядка \n).
with open('example.txt', 'r') as file:
    line = file.readline()
    print(line)

# Читає всі рядки з файлу і повертає список рядків.
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
