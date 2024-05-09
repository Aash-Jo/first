def max3 (vNum1,vNum2,vNum3):
  if vNum1 >= vNum2 and vNum1 >= vNum3:
    return (vNum1)
  elif vNum2 >= vNum1 and vNum2 >= vNum3:
    return (vNum2)
  elif vNum3 >= vNum1 and vNum3 >= vNum2:
    return (vNum3)
  else :
    print ("Sorry, try again")

# Ask user for three numbers
vNum1 = input ("Enter the first num:")
vNum2 = input ("Enter the second num:")
vNum3 = input ("Enter the third num:")
vNum1new=int(vNum1)
vNum2new=int(vNum2)
vNum3new=int(vNum3)

#print largest number
vMax=max3(vNum1new,vNum2new,vNum3new)
print (vMax)

