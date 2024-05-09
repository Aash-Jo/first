# read an input file with words
# Print how many words start with vowels (a e i o u) and how many do not
# print how many words of each length are there
# create a file word_facts.txt
# write all the print statements in the file

# Input file: Animals
# e.g. 
#tiger
#mudskipper
#Ardvark
# output
# Total words = 3
# words starting with vowels = 1
# words starting with non vowels = 2
# words with lenght 5 = 1
# words with length 10 = 1
# words with length 7 = 1

#THE PLAN (NOT IN DETAIL)

#open the file:

f=open("animals.txt","r")
vWordCT={
  
}
vTotalW=0
vCount=0
vHasVowels=0
vNoHasVowels=0
for word in f.readlines():
  vTotalW=vTotalW+1
  word=word.lower()
  if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u" :
    vHasVowels=vHasVowels+1

  else:
    vNoHasVowels=vNoHasVowels+1

  #dict={len:count}
  vLength=len(word) - 1
  #print("word =", word)
  #print("word len = ", vLength)
  vCount=vWordCT.get(vLength,0)
  if vCount==0:
    vWordCT[vLength]=1
  else:
    vCnt = int(vCount)
    vWordCT[vLength]=vCnt+1

# Total words = 3
# words starting with vowels = 1
# words starting with non vowels = 2
# words with lenght 5 = 1
# words with length 10 = 1
# words with length 7 =  1

print("Total words =",vTotalW)
print("words starting with vowels =",vHasVowels)
print("words starting with non vowels =",vNoHasVowels)
for k in sorted(vWordCT.keys()):
  print("words with length",k,"=",vWordCT[k]) 
#close file:
f.close()

# create a file word_facts.txt
# write all the print statements in the file
b=open("word_facts.txt","w")
b.write("Total words = "+ str(vTotalW)+"\n")
b.write("words starting with vowels = "+str(vHasVowels)+"\n")
b.write("words starting with non vowels = "+str(vNoHasVowels) +"\n")
for k in sorted(vWordCT.keys()):
  b.write("words with length "+str(k)+" = "+str(vWordCT[k])+"\n")


