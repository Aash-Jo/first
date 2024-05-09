# ask user for a word to search
# Open the file "input_words.txt"
# search for word in each line
# print the line number and the line where word is found
# use a function word_comp(line,word) return True/False to compare two words and find if they match
# example user input find word = good
# output
# line#1: Waffle is good
# line#3: Aashvi and Waffle make a good team
def word_find(Uword,line):
  vTF=False
  s=line.split()
  for W in s:
    if W==Uword:
      vTF=True
      return vTF

  return vTF
  
vUser=input("enter a word you want to search:")
i=open("input_words.txt","r")
vTally=0
for n in i:
  vTally=vTally+1
  #print(n)
  #s=n.split()
  vFound=word_find(vUser,n)
  if vFound:
    print("line#",vTally,":",n)  
i.close()

