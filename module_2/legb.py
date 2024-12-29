
# LEGB - Local Enclosing Global Built-in
# Local - всередині функцій
# Enclosing - охоплююча, працює для nested functions (вкладені функції)
# Global - це те, що на рівні файлу (модуля)
# Built-in - вбудоване в пайтоні

print()
int()
len()


# Global Scope
global_var = "I am Global!"
YEAR = 2024
MONTH = 'November'

def outer_function():
    # Enclosing Scope
    enclosing_var = "I am Enclosing!"

    def inner_function():
        # Local Scope
        local_var = "I am Local!"
        
        # Built-in Scope
        print(len("Built-in Scope"))  # Виклик функції з built-in scope
        
        # Використання змінних з різних областей видимості
        print(local_var)  # Local
        print(enclosing_var)  # Enclosing
        print(global_var)  # Global
    
    inner_function()

outer_function()
