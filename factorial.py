# factorial 
# ask user for a number
# print number X number -1 X number -2 ... X 1
# e.g Factorial 3 = 3X2X1 = 6
# Factorial 4 = 4X3X2X1 = 24
# 5! = 5X4X3X2X1 

vUser=input("Enter a number,any Number!:")
vNum=vUser
vNum=int(vNum)
#vNum=vNum-1
vSum=1
print("vNum =",vNum)
while vNum>1:
  vSum=vSum*vNum
  vNum=vNum-1

print(vSum)

  
  