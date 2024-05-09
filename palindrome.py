# ask user for strings till the user types quit
#check!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print the strings that are a palindrome
# aba =palindrome
# camac
# baab
# hint len()
# hint n%2 == 0, n is even, else n is odd
#
vList=[
  
]
vInput=input("Hello there!,ok,enter a string ,OR,Quit.:")
print("vInput =",vInput)
while vInput!="quit":
  vList.append(vInput)
  vInput=input("GREAT job!,ok,Now Again enter a string ,OR,Quit...:")
  vInput=vInput.lower()
    #print("vInput loop =",vInput)

#make 
for word in vList:
  print("word=",word)
  vLen=len(word)
  vLIndex=vLen-1
  #vLIndex=str(vLIndex)
  vFIndex=0
  print(vLIndex)
  
  while (word[vFIndex]==word[vLIndex] and 
         vLIndex >0 and 
         vFIndex<(vLen-1)):
    print("vFIndex = ", vFIndex,"vLindex = ", vLIndex )
    vFIndex =vFIndex+1
    vLIndex=vLIndex-1

  if (vFIndex==(vLen-1) and vLIndex==0):
    print(word,",is a palindrome","\n")

    
    
  



#print("vInput =",vInput)
#print("vList =",vList)
  


