import datetime
import time
import calendar

birth= datetime.date(1996, 8 , 20)
b = birth.year
c = birth.month
d = birth.day
print (birth)
print (b)
print (c)
print (d)
today = datetime.date.today()
if (
    today.month == birth.month
    and today.day >= birth.day
    or today.month > birth.month
):
   nextbirthdayyear = today.year + 1
else :
    nextbirthdayyear = today.year

nextbirthday = datetime.date(
   nextbirthdayyear , birth.month , birth.day
    )
print ("the next birthday: " , nextbirthday )
difference = nextbirthday - today
print ("days left before the next birthday: ", difference)

cal = calendar.month(2017,5)
print (cal)
one_day = datetime.timedelta (days = 1)
two_day = datetime.timedelta (days = 2)
three_day = datetime.timedelta (days = 3)
yesterday = today - one_day
print (yesterday + two_day)
print (yesterday - three_day)


