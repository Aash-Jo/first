vWeekday =" 0 hours of tv "
vSun = "3 hours of tv"
vSat =    "3 hours of tv "
vFri = "2 hours of tv"
vDay = input("enter the day today :")
vDay = vDay.capitalize()
print (vDay)
if vDay =="Sunday" or vDay == "Saturday":
  print (vSun)
elif vDay =="Friday":
  print (vFri)
else:
  print (vWeekday)