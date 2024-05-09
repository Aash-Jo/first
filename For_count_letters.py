# e.g letter = a, string = aashvi, Ans = 2
# ASk the user for a letter
vUserLtr=input("enter a letter:")
vUserLtr=vUserLtr.upper()
# Ask the user for a string
vUserStr=input("enter a string:")
vUserStr=vUserStr.upper()

# count the number of times the letter is in the string
vTally=0
for vAns in vUserStr:
  if vAns==vUserLtr:
    vTally=vTally+1

print(vTally)
# print the Answer
  



