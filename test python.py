today = date.today()
bday = date(today.year,6,30)
diff = (bday-today).days
if diff>0:
    print("birthday in %d days" % diff) 
else:
    print("birthday in %d days " % (diff+365)) 