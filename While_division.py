#ask user for a number
# ask for a divisor
# find quotient and remainder by subtracting divisor from number in a loop
#eg. user gives 99
# divisor = 25
# Quotient = 3, remainder= 24

vChoice=input("do you quit now ,or go?:").lower()
vQuoient=0
vCom = 0
while vChoice!="quit":
  vNum=int(input("Enter a number:"))
  #vNum=int(vNum)
  # ask for a divisor
  vDivisor=int(input("Enter a divisor:"))
  #vDivisor=int(vDivisor)
  vCom=vNum
  while vCom>=vDivisor:
    vQuoient= vQuoient+1
    vCom=vCom-vDivisor
    
  
  print("the quotient is",vQuoient,"and the Remainder is", vCom,"!")
  vChoice=input("Now do you quit now ,or go?:")

print("hope you had a good time cheating division with me ! come back soon!")
    