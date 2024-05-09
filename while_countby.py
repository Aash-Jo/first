# ask the user for a number
vInput  = input("Enter a number:" )
# print a series counting by the number for 10 times
# e.g. user number = 5 , program prints 50,45,40,....5
vInput=int(vInput) 
#loop variable
i=10
vSum=vInput*10
while i>=1:
  print (vSum)
  vSum-=vInput
  i-=1
  

