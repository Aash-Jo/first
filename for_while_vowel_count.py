# example input = aadi output a = 2, i = 1
# example input = coffee output o = 1, e = 2
# ask the user for a string, if user types "quit" quit the program, else keep asking for string in a loop
vStr=input("enter a string:")
vStr=vStr.lower()
# check the vowels in the string and print #vowels and how many times they are in the #string

vA="a"
vE="e"
vI="i"
vO="o"
vU="u"

vCount1=0
vCount2=0
vCount3=0
vCount4=0
vCount5=0

while vStr!="quit":

  for n in vStr:
    if vA==n:
      vCount1=vCount1+1  
    elif vE==n:
     vCount2=vCount2+1
    elif  vI==n:
      vCount3=vCount3+1
    elif vU==n: 
      vCount4=vCount4+1
    elif vU==n:
      vCount5=vCount5+1


  print("a =",vCount1)
  print("e =",vCount2)
  print("i =",vCount3)
  print("o =",vCount4)
  print("u =",vCount5)

  vStr=input("enter a string:")
  vStr=vStr.lower()
  
  vCount1=0
  vCount2=0
  vCount3=0
  vCount4=0
  vCount5=0

print("see ya later,and come back soon gator!")






