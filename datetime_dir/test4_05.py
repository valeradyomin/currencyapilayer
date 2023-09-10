# Замена атрибутов объекта datetime
import datetime

now = datetime.datetime.now()

delta = datetime.timedelta(days=365*50)
new_delta = datetime.timedelta(seconds=60)

date = now + delta
print(date)

new_date = date.replace(year=2023)
print(new_date)
