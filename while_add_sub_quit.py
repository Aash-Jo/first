def add(vNum1,vNum2):
 print("the sum is",int(vNum1) + int(vNum2))

def sub(vNum1,vNum2):
 print("the sum is",int(vNum1) - int(vNum2))

# ask user what operation they want to do (Add, Sub, Quit)
vChoice=input("Do you want to Add,sub,or quit?:")
vChoice=vChoice.lower()
#if quit , close the program, print "bye"  
while vChoice!="quit":
  vNum1=input("enter a num:")
  vNum2=input("enter a second num:")

  
  # otherwise, ask the user for 2numbers
  #print the answer
  if vChoice=="add":
    add(vNum1,vNum2)

  elif vChoice=="sub":
    sub(vNum1,vNum2)

  else :
    print("sorry,error.try again")
  
  vChoice=input("Now do you want to Add,sub,or quit?:")
  vChoice=vChoice.lower()
# Ask the user

print("see ya later,aligator!")






