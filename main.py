# ask user for a word  to search
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
def partW_find(word,line):
  vRet=False
  vWordLen=len(word)
  vLineLen=len(line)
  
  vWordTally=0
  vLineTally=0

  while vLineTally<vLineLen:
    if line[vLineTally]==word[vWordTally]:
      vWordTally=vWordTally+1
      if vWordTally==vWordLen:
        vRet=True
        return vRet
      vLineTally=vLineTally+1
    else:
      vLineTally=vLineTally+1
      vWordTally=0
  
  return vRet
 
      
vUser=input("enter string you want to search:")
i=open("input_words.txt","r")
vTally=0
vFanything= False
for n in i:
  vTally=vTally+1
  #print(n)
  #s=n.split()
  #vFound=word_find(vUser,n)
  vFound=partW_find(vUser,n)
  if vFound:
    print("line#",vTally,":",n)  
    vFanything = True
if vFanything==False:
   print("sorry, could not find",vUser,"in input_words.txt")
i.close()

