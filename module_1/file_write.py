# Записує один рядок або текстовий вміст у файл.
with open('example.txt', 'w') as file:
    file.write('Hello, Python!\n')
    file.write('This is a second line.')

# Записує список рядків у файл.
lines_to_write = ['First line\n', 'Second line\n', 'Third line\n']
with open('example.txt', 'w') as file:
    file.writelines(lines_to_write)
