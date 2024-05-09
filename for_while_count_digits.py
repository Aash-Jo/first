# example input = 501 output 0 = 1, 1= 1, 5 = 1
# Ask user for a number 
# print how many times every digit is repeated


vUser_num=input ("enter a number or quit:")


vCount0=0
vCount1=0
vCount2=0
vCount3=0
vCount4=0
vCount5=0
vCount6=0
vCount7=0
vCount8=0
vCount9=0

vUser_num=vUser_num.lower()

while vUser_num!="quit":
 #vUser_num=int(vUser_num)
  for n in vUser_num:
    if n=="0":
      vCount0=vCount0+1
    elif n=="1":
     vCount1=vCount1+1
    elif n=="2":
       vCount2=vCount2+1
    elif n=="3":
       vCount3=vCount3+1
    elif n=="4":
         vCount4=vCount4+1
    elif n=="5":
         vCount5=vCount5+1
    elif n=="6":
     vCount6=vCount6+1
    elif n=="7":
       vCount7=vCount7+1
    elif n=="8":
       vCount8=vCount8+1
    elif n=="9":
         vCount9=vCount9+1

  if vCount0>= 1:
    print("0 = ", vCount0)

  if vCount1>= 1:
    print("1 = ", vCount1)

  if vCount2>= 1:
    print("2 = ", vCount2)

  if vCount3>= 1:
    print("3 = ", vCount3)

  if vCount4>= 1:
    print("4 = ", vCount4)

  if vCount5>= 1:
    print("5 = ", vCount5)

  if vCount6>= 1:
    print("6 = ", vCount6)

  if vCount7>= 1:
    print("7 = ", vCount7)

  if vCount8>= 1:
    print("8 = ", vCount8)

  if vCount9>= 1:
    print("9 = ", vCount9)
                            

  

                 
  
  vUser_num=input ("Now again, Enter a number,or quit:")

      
  #till user types quit
   # print the number in expanded form
print("thank for playing,come back soon!")