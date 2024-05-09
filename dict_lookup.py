# ask user for day of the week
vUser_day=input("enter a day of the week or weekend:")
vUser_day=vUser_day.lower()
# print which number day it is starting with 1 for Monday
vDict={
  "monday":1,
  "tuesday":2,
  "wednesday":3,
  "thursday":4,
  "friday":5,
  "saturday":6,
  "sunday":7,
  
}
#print(vDict[vUser_day])
print(vDict.get(vUser_day,"sorry error,try again"))