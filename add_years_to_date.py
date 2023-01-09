import datetime

date_string = input()
years_add = int(input())

formatted_date = datetime.datetime.strptime(date_string, "%b %d %Y")

duration = datetime.timedelta(days=years_add * 365)

new_date = formatted_date + duration

print(new_date)
