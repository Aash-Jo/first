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
vUser=int(input("enter a number:"))
vPrime=[]


vTally=2
isPrime=True
#print(isPrime)
if vUser==1:
  print("not prime")
while vTally<vUser and isPrime:
  #print("before adding vTally=",vTally)
  #print("in loop vTally= ",vTally)
  vP=vUser%vTally
  #print("in loop vP= ",vP)
  if vP==0:
    isPrime=False
    print("Not prime num")
    

  #print("isPrime= in Loop=",isPrime)
  vTally=vTally+1

if isPrime and vUser!=1 :
  print("is prime")
  
