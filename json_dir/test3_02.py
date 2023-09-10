# Преобразование строки JSON в объект Python
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
my_dict = json.loads(json_string)
print(my_dict)
print(type(my_dict))
