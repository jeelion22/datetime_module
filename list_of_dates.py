import datetime

start_date = input()
end_date = input()

initial_date = datetime.datetime.strptime(start_date, "%b %d %Y")
final_date = datetime.datetime.strptime(end_date, "%b %d %Y")

duration = datetime.timedelta(days=1)

date = initial_date

while date <= final_date:
    print(date)
    date += duration
