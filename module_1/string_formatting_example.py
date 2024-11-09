# Форматування стрічки з використанням % (старіший підхід)
# Приклад 1
name = "Олександр"
age = 30
formatted_string = "Мене звуть %s і мені %d років." % (name, age)
print(formatted_string)

# Приклад 2
temperature = 23.5
formatted_string = "Температура зараз становить %f градусів." % temperature
print(formatted_string)



# Форматування стрічки з використанням format (старіший підхід)
# Приклад 1
name = "Олександр"
age = 30
formatted_string = "Мене звуть {} і мені {} років.".format(name, age)
print(formatted_string)

# Приклад 2
temperature = 23.5
city = "Львів"
formatted_string = "У місті {} зараз температура {:f} градусів.".format(city, temperature)
print(formatted_string)



# Форматування стрічки з використанням f-string (найновіший підхід)
# Приклад 1
name = "Олександр"
age = 30
formatted_string = f"Мене звуть {name} і мені {age} років."
print(formatted_string)

# Приклад 2
temperature = 23.5
city = "Львів"
formatted_string = f"У місті {city} зараз температура {temperature} градусів."
print(formatted_string)