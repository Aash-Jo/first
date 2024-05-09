
vNDictOnes={
  "0":"zero",
  "1":"one",
  "2":"two",
  "3":"three",
  "4":"four",
  "5":"five",
  "6":"six",
  "7":"seven",
  "8":"eight",
  "9":"nine"
}
vNDictTens={
  "1":"ten",
  "2":"twenty",
  "3":"thrty",
  "4":"forty",
  "5":"fifty",
  "6":"sixty",
  "7":"seventy",
  "8":"eighty",
  "9":"ninety"
}
vNTeens={
  "11":"elevin",
  "12 ":"twelve",
  "13":"thrteen",
  "14":"fourteen",
  "15":"fifteen",
  "16":"sixteen",
  "17":"seventeen",
  "18":"eighteen",
  "19":"nineteen"
}

  
#print a number in words
# ASk user for a number
# print it in words
#e.g. 209
# print Two hundred and nine
#e.g 1200
#print one thousand two hundred
#print(sdf)
vUserNum=input("enter a number,but it has to be < 10,000:")
# max 9,999 9 thou 9 hun ninety nine
vlen=len(vUserNum)
vFIndex=vlen-1
print (vlen)
vPosn =["", "ones", "tens", "hundreds", "thousands"]
vTotal=[]
vTally=0
while vFIndex>=0:
  vTally=vTally+1
  #print(vPosn[vTally])
  n=vUserNum[vFIndex]
  if vTally ==1:
    b=vNDictOnes.get(n)
    vTotal.append(b)
    print("vtally 1", "n = ", n,  "\tb =", b)
  elif vTally==2:
    d=vNDictTens.get(n)
    vTotal.append(d)
    print("vtally 2","n =", n, "\td = ", d)

  elif vTally==3:
    vTotal.append("hundred")
    b=vNDictOnes.get(n)
    vTotal.append(b)

  elif vTally==4:
    vTotal.append("Thousand")
    b=vNDictOnes.get(n)
    vTotal.append(b)

  else:
    print("TRY AGAIN .ERROR")
    
  vFIndex=vFIndex-1

print(vTotal[::-1])




































\

























