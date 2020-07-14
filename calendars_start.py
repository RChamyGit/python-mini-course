#calendarios em python

#import the calendar module
import calendar
#create a plain text calendar
c= calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2017,1,0,0)
print(st)

#create an html formatted calendar - retorna o calendario em formato html

hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2017,1)
print(st)

#loop over the days of a month
#zeroes mean that the day of the week is in AN OVERLAPPING MONTH

for i in c.itermonthdays(2017, 8):
    print(i)

#locale calendar

for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)


#funcao reunioes na primeira sexta de todo mes, que dias serao

print("team meetings will be on : ")
for m in range (1,13):
    cal = calendar.monthcalendar(2018, m)
    weekone = cal[0]
    weektwo = cal[1] #nao entendi bem
    print(cal[0], "   ", cal[1])

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone [calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
    
        
