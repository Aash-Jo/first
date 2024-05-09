# create the series below for as many terms as user inputs
# Fibonacci series 1,1,2,3,5,8,13,...
# e.g. user input how many terms to print = 5
# output 1,1,2,3,5
# use function to find the next term
# fn(term1, term2):
#    return next_term
def fibonacci(term1,term2):
 return(term1+term2) 
  
  
  
vUser= int (input("enter a num:"))
vTally=1
vNum1=1
vNum2=1
while vTally<=vUser:
  
  if vTally==1:
    print("1")
  elif vTally==2:
    print("1")

  else:
    vHolder=fibonacci(vNum1,vNum2)
    print(vHolder)
    vNum1=vNum2
    vNum2=vHolder
  
  vTally=vTally+1
  
  
  
  
  
