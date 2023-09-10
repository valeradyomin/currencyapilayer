# Преобразование объекта datetime в строку
import datetime

# Преобразование строки в объект datetime
date_string = '2022-12-31'
date_format = '%Y-%m-%d'
date = datetime.datetime.strptime(date_string, date_format)
print(date)

# Преобразование объекта datetime в строку
date_string = date.strftime(date_format)
print(date_string)