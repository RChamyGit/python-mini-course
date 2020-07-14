from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
#timedelta - time math
def main():
    print(timedelta(days=365))

    #data hj
    now = datetime.now()
    print("today is: "+str(now))


    #print todays date one year from now

    print("one year from now it will be" + str(now + timedelta(days=365)))

    #timedelta com +de 1 argumento
    print("in 2 days and 3 weeks, it will be " + str(now + timedelta (days=2, weeks=3)))

    # a data 1 semana atras , formatada como string
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("One week ago it was: " + s)

    ###how many days until 1o de abril
    today = date.today()
    afd = date(today.year, 4,1)

    if afd<today:
        print("1o de abril ja passou a %d dias atras" % ((today-afd).days))
        afd = afd.replace(year = today.year+1)
        print("")

        #quanto tempo ate o proximo 1o de abril
    time_to_afd = afd-today
    print("so faltam ",time_to_afd.days, "dias ate 1o de abril")

if __name__ == "__main__":
    main();
