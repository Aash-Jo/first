# ask user for names and marks a student got

vDict={
  
}
vChoice=input("do you want to quit,or add a person?:")
vChoice=vChoice.lower()
while vChoice!="quit" and vChoice=="add":
  
 vName=input("enter in name of somebody you know:")
 vMarks=input("Good!now enter the marks they got on their last test!oh and pleze no -eneythings.:")
 vMarks=int(vMarks) 
 vDict[vName] = vMarks
#print(vDict[vName]=vMarks)
 vChoice=input("Great!Now do you want to quit,or add a person?:")
 vChoice=vChoice.lower()
# print the name of the student who got the most marks
# print the name of the student who got least marks
#print(vDict)
vSmallName="  "
vSmallMarks=999
vBigMarks=-1
vBigName="  "
for n in vDict:
  
  #print("n =",n)
  #print(vDict[n])
 
  if vDict[n]>vBigMarks:
    vBigName=n
    vBigMarks=vDict[n]
  if vDict[n]<vSmallMarks:
    vSmallMarks=vDict[n]
    vSmallName=n
  #print(type(vSmallMarks))
    #dfghjkkkkkkkkkkjiputthisherfortestingkay
print("the person with the highest test score is ",vBigName,"and they got a ",vBigMarks,"! Good job!")
print("the person with lowest test score is",vSmallName,"and they got a",vSmallMarks,"!,Keep trying!")
  
  