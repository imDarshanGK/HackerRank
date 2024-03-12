# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
month,day,year = map(int,input().split())
day_week = calendar.weekday(year,month, day)
day_name=calendar .day_name[day_week]
print(day_name.upper())


