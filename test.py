import datetime

# calculates total number of Saturdays and Sundays in given dates of
# interval (includes both dates)

start_date = input()
end_date = input()

saturdays = 0
sundays = 0
duration = datetime.timedelta(days=1)

start_date_object = datetime.datetime.strptime(start_date, "%d %b %Y")
end_date_object = datetime.datetime.strptime(end_date, "%d %b %Y")

date = start_date_object - duration
while date < end_date_object:
    date = date + duration

    day = datetime.datetime.strftime(date, "%A")
    if day == "Saturday":
        saturdays += 1
    if day == "Sunday":
        sundays += 1
print("Saturday: {}".format(saturdays))
print("Sunday: {}".format(sundays))
