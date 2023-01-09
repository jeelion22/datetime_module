import datetime

year_1, year_2 = map(int, input().split(" "))

mondays = 0
months = range(1, 13)

for year in range(year_1, year_2 + 1):
    for month in months:
        datetime_obj = datetime.datetime(year, month, 1)
        day = datetime.datetime.strftime(datetime_obj, "%A")
        if day == "Monday":
            mondays += 1
print(mondays)
