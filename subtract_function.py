# create a function that takes two values and returns the larger value
def larger (vNum1,vNum2):
  if vNum1 >= vNum2:
    return vNum1 
  else:
    return vNum2
# create a function that takes two values and returns the smaller value
def smaller (vNum1,vNum2):
  if vNum1 <= vNum2:
    return vNum1 
  else:
    return vNum2
    
# Ask user for two numbers
vNum1 = input ("Enter the first num:")
vNum2 = input ("Enter the second num:")
vNum1=int(vNum1)
vNum2=int(vNum2)
# subtract smaller number from the bigger number
vSum = ( int(larger(vNum1,vNum2)) - int(smaller(vNum1,vNum2)))
print (vSum)