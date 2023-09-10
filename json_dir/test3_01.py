# Преобразование объекта Python в строку JSON
import json

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(my_dict)
print(json_string)
print(type(json_string))