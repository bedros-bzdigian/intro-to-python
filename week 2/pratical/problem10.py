import time
import datetime
import calendar

x = datetime.date.today()
print ("today's date:" , x)
print ("current year:" ,x.year)
print ("current month:" , x.month)
print ("current day:" , x.isoweekday())

c = datetime.timedelta (days = 5)
print ("date today - 5: " , x - c)
print ("date today + 5: " , x + c)