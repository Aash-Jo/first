#take input from the user of ANY number
#print the list of numbers from 1 to user input number
# when the number is divisble by 3 print FIZZ
# when the number is divisble by 5 print BUZZ
# when the number is divisble by both 3 and 5 print FIZZBUZZ
# if the number if not divisble by 3 or 5 print the number
# e.g. user enter 10
# output 1, 2, FIZZ, 4, BUZZ, FIZZ, 7,8, FIZZ, BUZZ
def if_3(n):
  return n %3

def if_5(n):
  
  return n%5

vUserNum=int(input("enter ANY number you want:"))
vTally=1
while vTally<=vUserNum:
  vRet3=if_3(vTally)
  vRet5=if_5(vTally)
  if vRet3==0 and vRet5==0:
    print("FIZZBUZZ")
  elif vRet3==0:
    print("FIZZ")
  elif vRet5==0:
    print("BUZZ")
  else:
    print(vTally)
  vTally=vTally+1
  
  
    
    
    
    
  
