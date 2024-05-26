# ask user for a number
# print all the factors of the number
#e.g. input:6
#output:1,2,3,6
def is_factor(num,factor):
  vRet=False
  if num%factor==0:
    vRet=True
  return vRet

vUser=int(input("enter a number:"))
vFactor=[]
vTally=1
while vTally<=vUser:
  if vTally==1 or vTally==vUser:
    vFactor.append(vTally)
  else:
    vF=is_factor(vUser,vTally)
    if vF:
      vFactor.append(vTally)
  vTally=vTally+1
print(vFactor)