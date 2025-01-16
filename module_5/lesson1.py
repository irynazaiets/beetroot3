import requests

# Отримати випадковий жарт
# url = 'https://api.chucknorris.io/jokes/random'
# response = requests.get(url)
# print(response.json())


# Отримати інформацію про країну
response = requests.get('https://restcountries.com/v3.1/name/ukraine')
data = response.json()
# print()
print(f"Столиця: {data[0]['capital'][0]}")

# # Отримати випадкову цитату
# response = requests.get('https://api.quotable.io/random')
# quote = response.json()
# print(f"{quote['content']} - {quote['author']}")
