import datetime
import pytz

# datetime.date (Y, M, D)
# datetime.time (H, M, S, MS)
# datetime.datetime(Y, M, D, H, Min, S, MS)



today=datetime.date.today()
print(today)           #print out today date.


date_time=datetime.datetime.now()       #will tell both time and day
print(date_time)


birthday=datetime.date(2000,12,22)      #you can't put 07 as it will not take 0 as integer.
print(birthday)
type(birthday)                #birthdate is an object


days_since_birth=(today-birthday).days            #.days will not show the datetime
print(days_since_birth)



tdelta=datetime.timedelta(days=10)   #adding 10 days to current day. 
print(today+tdelta)

print(today.month)

print(today.day)

print(today.weekday())  #it starts from monday-0, tue-1, wed-2......
#output : 5 i.e saturday


hour_delta=datetime.timedelta(hours=4)     #adding 4 hours to current day
print(date_time+hour_delta)


#using pytz
datetime_today=(datetime.datetime.now(tz=pytz.UTC))
print(datetime_today)
datetime_pacific=(datetime_today.astimezone(pytz.timezone('US/Pacific')))
# Pacific time zone The Pacific Time Zone (PT) is a time zone encompassing
#  parts of western Canada, the western United States, and western Mexico. 
# Places in this zone observe standard time by subtracting eight hours from 
# Coordinated Universal Time (UTC−08:00). during daytime, a time offset of UTc -7:00 is used
print(datetime_pacific)



for tz in pytz.all_timezones:              #printing all timezones in world
    print(tz)

#string formatting with dates.
#2020-03-14 -> March 14,2020
#strftime (f= formatting )
today_date=datetime.date.today()
print(today_date.strftime('%B %d, %Y'))  #B for month, d for days, Y for year
#out- March 14, 2020


#March 14,2020-> 2020-03-14
#strptime (p=parsing)
date_thing=datetime.datetime.strptime('March 09, 2020','%B %d, %Y')
print(date_thing)