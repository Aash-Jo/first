#Take one number input from user
# check list from 1 to the number user gave
# Print lists of numbers
# Even numbers
# odd numbers
# prime numbers
# prime numbers are numbers that only have 1 and themself as a factor 
# factor is a number that is less than #or equal to the number and fully #divides the given number
# e.g user input 7
# output even num = 2,4,6
# odd num = 1,3,5,7
# prime number = 2,3,5,7
def is_prime(n):
  vRet=False
  if n==1:
    vRet=False
    return vRet

  if n==2:
    vRet=True
    return vRet

  vTally=2
  while vTally<n:
    if n%vTally==0:
      vRet=False
      return vRet
    vTally=vTally+1

  vRet=True
  return vRet
def is_even(n):
  vRet=False
  if n%2==0:
    vRet=True
  else:
    vRet=False

  return vRet


vPrime=[]
vEven=[]
vOdd=[]
vTally=1
vUser=int(input("enter a number:"))
while vTally<=vUser:
  vAnsPrime=is_prime(vTally)
  vAnsEven=is_even(vTally)

  if vAnsEven:
    vEven.append(vTally)

  elif not(vAnsEven):
    vOdd.append(vTally)
  
  if vAnsPrime:
    vPrime.append(vTally)

  vTally=vTally+1


print("prime numbers:",vPrime)
print("\n","even numbers:",vEven)
print("\n","odd numbers:",vOdd)
  
