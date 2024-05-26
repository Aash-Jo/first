# ask user for number of terms 
# print terms from the below series
# 1 5 9 13 17...
#starting from 1 and + 4 to it then your anwser + 4
# 1 2 4 8 16...
# starting from 1 and * it by 2 and the anwser you *by 2
def add_series(sNum):
  return(sNum+4)
def mult_series(sNum):
  return(sNum*2)


vUterm=int(input("Enter how many terms:"))
vTally=1
vAddStart=1
vMultStart=1
vAddlist=[]
vMultList=[]
while vTally<=vUterm:
  if vTally==1:
    vAddlist.append(vAddStart)
    vMultList.append(vMultStart)
  else:
    vAddTerm=add_series(vAddStart)
    vAddlist.append(vAddTerm)
    vAddStart=vAddTerm
    vMultTerm=mult_series(vMultStart)
    vMultList.append(vMultTerm)
    vMultStart=vMultTerm
  vTally=vTally+1
print(vAddlist,"\n") 
print(vMultList)