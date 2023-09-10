# Преобразование строки в объект datetime
import datetime

date_string = '2022-12-31'
date_format = '%Y-%m-%d'
date = datetime.datetime.strptime(date_string, date_format)
print(date)

da_st = "2023-09-18"
da_fr = '%Y-%m-%d'
da = datetime.datetime.strptime(da_st, da_fr)
print(da)
