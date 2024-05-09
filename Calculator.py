# Ask the user what do you want to do Add, Sub, Multiply, or Divide
vSym = input ("What do you want to do Add, Sub, multiply, or Divide :")
# Ask user for first number
vNum1 = input ("Enter the first number :")
# Ask user for second number
vNum2 = input ("Enter the second number :")
# do the operation and return the result to the user 
vSym = vSym.capitalize()
if vSym == "Add" :
  vAns =int(vNum1) + int(vNum2)
  print ("The answer is " + str(vAns))

elif vSym == "Sub":
  vAns =int(vNum1) - int(vNum2)
  print ("The answer is " + str(vAns))


elif vSym == "Multiply":
 vAns =int(vNum1) * int(vNum2)
 print ("The answer is " + str(vAns))

elif  vSym == "Divide" :
 vAns =int(vNum1) / int(vNum2)
 print ("The answer is " + str(vAns))

else :
 print ("Error.Sorry, Wrong input.")