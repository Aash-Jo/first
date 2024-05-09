# e.g. user gave AADI ,  and letter A, D print A = 2, D= 1
# ask user for a string
vStr=input("enter a string:")
vStr=vStr.lower()
# ask user for 2 letters to search
vLtr=input("entre a letters that  you want to search:")
vLtr=vLtr.lower()

vLtr2=input("entre another letters that  you want to search:")
vLtr2=vLtr2.lower()
# check how many time each letter comes in the string
vCount2=0
vCount1=0
vCount1=int(vCount1)
vcount2=int(vCount2)
for n in vStr:
  if vLtr==n:
    vCount1=vCount1+1
  elif vLtr2==n:
    vCount2=vCount2+1
    
print(vLtr,"=",vCount1)   
print(vLtr2,"=",vCount2)



  
             