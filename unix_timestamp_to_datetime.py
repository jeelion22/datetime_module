import datetime

unix_epoch = "January 01 1970"
sec = int(input())

duration = datetime.timedelta(seconds=sec)
datetime_obj = datetime.datetime.strptime(unix_epoch, "%B %d %Y")
exact_datetime = datetime_obj + duration

print(exact_datetime)
