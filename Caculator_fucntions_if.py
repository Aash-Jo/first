#create function to add two nums 
def add (vNum1,vNum2):
  print ("The sum is " ,int (vNum1) + int (vNum2))
#create function to sub two nums
def sub (vNum1,vNum2):
  print ("The difference is " ,int (vNum1) - int (vNum2))
#create function to mult two nums
def mult (vNum1,vNum2):
  print ("The product is " ,int (vNum1) * int (vNum2))
#create function to div two nums
def div (vNum1,vNum2):
  print ("The quotient is " ,int (vNum1) / int (vNum2))
#ask the user the operation they want to do

vOp =input("What do you want to do Add,Sub,Mult,or Div >")
vOp=vOp.lower()
#ask the user the first num
vNum1 = input("What is the first number >")
#ask the user the second num
vNum2 = input("What is the second number >")
#call the function
if vOp == "add":
  add(vNum1,vNum2)

elif vOp =="sub":
  sub(vNum1,vNum2)

elif vOp =="mult":
  mult(vNum1,vNum2)

elif vOp =="div":
  div(vNum1,vNum2)

else:
  print ("Sorry,Wrong input.")





