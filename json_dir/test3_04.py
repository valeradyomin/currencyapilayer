# Запись данных в файл в формате JSON
import json

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = '{"name": "John", "age": 30, "city": "New York"}'

with open('json_string.json', 'w') as f:
    json.dump(json_string, f)
