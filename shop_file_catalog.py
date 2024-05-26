#Read a file called catalog.txt for items and their pricesa
#show user a list of things with prices
# Ask user to pick things by their ID 
# Ask user for quantity
# create a bill for the user
# save the whole bill in a file called Invoice.txt
# example
# 1. ball 0.50 each
# 2. bat  3.00 each
# 3. cap  2.50 each
# user input
# 1, 5
# 2, 1
# 3, 1
# output
# your oder
# 5 ball - 2.50
# 1 bat - 3.00
# 1 cap - 2.50
# Total = 8.00
# your invoice is in invoice.txt
#from typing_extensions import ReadOnly


def find_bill(order,shelf):
  vTotal=0.0
  for k in vTOrder:
    print("k=",k)
    price=shelf.get(k)
    qty=order.get(k)
    print("price=",price)
    print("qty=",qty)
    amt=float(price)*float(qty)
    vTotal=vTotal+amt
    print("in loop amt=",amt)
  print("out loop amt=",vTotal)
  return vTotal
  
vShelf={
  
}
vTOrder={

}

p=open("catalog.txt","r")
for d in p:
  r=d.rsplit(":")
  #print("r=",r)
  vP=r[1].rsplit("\n")
  #print("vp=",vP)
  vShelf.update({r[0]:vP[0]})
  vTOrder.update({r[0]:0})
p.close()
print(vShelf)

#print("vIten outside loop", vItem)
vItem=""
while vItem!= "pay":
  #print("vItem in loop",vItem)
  vItem=input("enter the name of the  item you want to order or pay the bill:")
  if vItem in vTOrder :
      vHowMany=int(input("Now enter how many you want"))
      vTOrder.update({vItem:vHowMany})
    
  elif vItem!="pay":
    print("Sorry we dont have a",vItem)

#print("vOrder=",vTOrder)

vBill=find_bill(vTOrder,vShelf)
print("Total amount needed is ",vBill)
#print("hope you had a fun at aashvi sport stuff!")
# everybody thinks i'm stuped,espeshly ma