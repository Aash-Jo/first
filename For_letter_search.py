# e.g. user gave AADI ,  and letter A print 2
#
# ask user for a string
vStr=input("enter a string:")
vStr=vStr.lower()
# ask user for a letter to search
vLtr=input("entre a leter that  you want to search:")
vLtr=vLtr.lower()
# check how many time letter comes in the string, print the answer
vCount=0
for vChar in vStr:
  #print("vChar =",vChar)
  #print("vLtr =",vLtr)
  #print("vStr =",vStr)
  if vLtr==vChar:
   vCount=vCount+1

print(vCount)




