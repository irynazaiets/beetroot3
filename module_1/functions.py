# def (definition)

INDEX = 25
YEAR = 2024
STATIC_NUMBER = 365

def my_func(par1, par2):
    STATIC_NUMBER = 366 
    sum_ = par1+par2
    print(STATIC_NUMBER, " - inside my_func")
    return sum_

print("\n"*2)
result = my_func(3, 5) # None
print(STATIC_NUMBER, " - outside my_func")

x = " information"
y = ' information'
# age = 16

def check_age(age = 18, type_of_drink = 'живчик'):
    '''
    doc strings (documentation strings)
    '''
    if age < 14:
        x = "Живчик"
        print(f"Продамо тобі лише {x}")
        return x
    elif age >= 14 and age <18:
        # print("Алкоголь не продаємо, лише енергетики")
        return "Енергетики"
    else:
        # print("Продаємо все")
        return "Алкоголь"

check_age()

print(check_age(27))


def market_work(goods_category, customer_age):
    if goods_category == "Toys":
        print("Продаємо без проблем")
    elif goods_category == "Alcohol":
        result = check_age(customer_age) # None


