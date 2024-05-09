`# take a list of numbers from the user till user types quit
# check if each number is even or odd
# print Total numbers given
# print even number count = X, evn 
#number list
# print odd number count = X, odd number list
#e.g.
#user enters 2,3,4,5,6,7
#Output: Total numbers given = 6
#Even number count = 3, even numbers = 2,4,6
#Odd number count = 3, odd numbers = 3,5,7
vE=[]
vEc=0
vO=[]
vOc=0
vTotal=0
vUser=input("enter a num or quit :")
while vUser !="quit":
  vUser=int(vUser)
  vCheck=vUser%2
  if int(vCheck)==0:
    vE.append(vUser)
    vEc=vEc+1
  else :
    vO.append(vUser)
    vOc=vOc+1
  vTotal=vTotal+1
  vUser=input("enter a num again ...OR quit:")
print("Total numbers given  =",vTotal)

print("\n even num count=",vEc,"even nums=",vE) 
print("\n","odd num count=",vOc,"even nums=",vO )
  
