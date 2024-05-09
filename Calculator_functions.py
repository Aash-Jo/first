# write a fucntion add(num1, numn2) 
def add (vNum1, vNum2):
  print ("The sum is " ,int (vNum1) + int (vNum2) )

def sub (vNum1, vNum2):
  print ("The difference is " ,int (vNum1) - int (vNum2) )

def mult (vNum1, vNum2):
  print ("The product is " ,int (vNum1) * int (vNum2) )

def div (vNum1, vNum2):
  print ("The quotient is " ,int (vNum1) / int (vNum2) )
# function should print the addition of the two numbers. 

# ask the user for first num
vUser1 = input ("What is the first num? ")
# ask the user for second num
vUser2 = input ("What is the second num? ")
# call the function
add(vUser1,vUser2)
sub(vUser1,vUser2)
mult(vUser1,vUser2)
div(vUser1,vUser2)