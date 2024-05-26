#ask user for time
#ask how many min to add or sub
#print anwser
#e.g. input:12:00,70
#output:1:10
def add_time(CTime, Mmin):
  vSplit = CTime.rsplit(":")
  vHour = int(vSplit[0])
  vMin = int(vSplit[1])
  print("vSplit=", vSplit)
  vAM = vMin + Mmin
  print("vAM=", vAM)
  while vAM > 60:
    vHour = vHour + 1
    if vHour > 12:
      vHour = 1
    vAM = vAM - 60
  vTTime = [vHour, vAM]
  return vTTime


def add_time_div(CTime, Mmin):
  vSplit = CTime.rsplit(":")
  vHour = int(vSplit[0])
  vMin = int(vSplit[1])
  vMin = vMin + Mmin
  vAdd_Hour = int(vMin / 60)
  vAdd_min = vMin % 60
  print("vAH=", vAdd_Hour)
  print("vAM=", vAdd_min)
  vHour = vHour + vAdd_Hour
  if vHour > 12:
    vHour = vHour - 12
  vTTime = [vHour, vAdd_min]
  return vTTime


def sub_time(CTime, LMin):
  vSplit = CTime.rsplit(":")
  vHour = int(vSplit[0])
  vMin = int(vSplit[1])
  vFMin = 0
  vFHour = 0
  vLmin = LMin
  vFTime = []
  #while vLmin >= 60:
  #  vLmin = vLmin - 60
  #  vSHT = vSHT + 1
  while vMin<vLmin:
    #borrow an hour
    vHour = vHour-1
    vMin = vMin+60

  #vSMT = vLmin
  vFHour = int(vHour)
  vFMin = int(vMin) - int(vLmin)

  vHour_adjust = 0
  if vFHour<1: 
    vHour_adjust = vFHour%12
    vFHour= vFHour - vHour_adjust

  vFTime.append(vFHour)
  vFTime.append(vFMin)
  return vFTime


vOption = input("quit or start?:")
while vOption == "start" or vOption=="again":
  vUtime = input("enter the time:")
  vOp = input("now enter if you want to add or sub minutes:")
  vAmin = int(input("now enter how many minutes to do for your op:"))
  print("vUtime=", vUtime, " vOp=", vOp, " vAmin=", vAmin)


  if vOp == "add":
    vAdd_Time = add_time_div(vUtime, vAmin)
    print("the old time was", vUtime, ",and the New time is", vAdd_Time[0],
          ":", vAdd_Time[1])
  elif vOp == "sub":
    vSub_Time = sub_time(vUtime, vAmin)
    print("the old time was", vUtime, ",and the New time is", vSub_Time[0],
          ":", vSub_Time[1])
  else:
    print("Sorry.Error,Try Again")
  vOption = input("quit or again?:")
print("seeya later!use me soon!")

