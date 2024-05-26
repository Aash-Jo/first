#ask user for amount of money
#ask to add or sub
#ask minutes to add or sub
#print anwser,and repet till "quit"
#e.g.input 1.00,add,4.20
#output:5.20
def add_money(Sm,em):
  v=Sm.rsplit(".")
  b=em.rsplit(".")
  vnD=v[0]
  vnC=v[1]
  vemD=b[0]
  vemC=b[1]
  vFC=0
  vFD=0
  vFM=[]  
  vFD=int(vnD)+int(vemD)
  vFC=int(vnC)+int(vemC)
  while int(vFC)>=100:
    vFD=vFD+1
    vFC=vFC-60
  vFM.append(vFD)
  vFM.append(vFC)
  return vFM
def sub_money(Sm,em):
  v=Sm.rsplit(".")
  b=em.rsplit(".")
  vnD=v[0]
  vnC=v[1]
  vemD=b[0]
  vemC=b[1]
  vFC=0
  vFD=0
  vFM=[]
  vFD=int(vnD)-int(vemD)
  vFC=int(vnC)-int(vemC)
  if vFD<0:
    vFD=0
  while vFC<0:
    vFD=vFD-1
    if vFD<0:
      return ("none")
    vFC=vFC+100 
vUop=input("quit or start?:")
while vUop=="start" or vUop=="again":
  vUMoney=input("how much money do you have?:")
  vAoS=input("add or sub?:")
  vMoney=input("how much money do you want to add or sub?:")
  if vAoS=="add":
    vAdd=add_money(vUMoney,vMoney)
    print("\n","the OLD amount of money was ",vUMoney,"the NEW money amount is ",vAdd[0],":",vAdd[1],"\n")
  elif vAoS=="sub":
    vSub=sub_money(vUMoney,vMoney)
    if vSub=="none":
      print("\n","the OLD amount of money was ",vUMoney,",but you d'ont have enough money!,Can't by that.","\n")
    else:
      print("\n","the OLD amount of money was ",vUMoney,"the NEW money amount is ",vSub[0],":",vSub[1],"\n")
  else:
    print("Sorry.Error,Try Again")
  vUop=input("Now,quit or again?:")
print("\n","thanks and goodby!")