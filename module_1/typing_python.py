# простіший приклад
def greet(name: str) -> str:
    return f"Hello, {name}!"

# коли параметр може мати різні типи даних
from typing import Union

def process(value: Union[int, str]) -> str:
    return str(value)

# якщо функція не повертає нічого

def log_message(message: str) -> None:
    print(message)

# параметри з типами за замовчуванням
def repeat_string(s: str, times: int = 1) -> str:
    return s * times

tel_numer = ''
if tel_numer.isdigit():
    if len(tel_numer) == 10:
        print('Введене відповідає умовам')
    elif len(tel_numer) < 10:
        print('Ви ввели недостатньо цифр')
    elif len(tel_numer) > 10:
        print('Ви ввели забагато цифр')
    else:
        print('Введіть будь ласка лише 10 цифр номеру телефона')
else:
    print("Потрібно ввести лише цифри")