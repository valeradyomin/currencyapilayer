# Работа с интервалами времени
import datetime

now = datetime.datetime.now()

delta = datetime.timedelta(days=7)
print(now + delta)
