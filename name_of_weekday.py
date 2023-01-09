import datetime

date = input()

formatted_date = datetime.datetime.strptime(date, "%d %b %Y")

new_format = formatted_date.strftime("%A")

print(new_format)
