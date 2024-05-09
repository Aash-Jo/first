#print a number in words
# ASk user for a number
# print it in words
#e.g. 209
# print Two hundred and nine
#e.g 1200
#print one thousand two hundred
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
  "9":"ninety",
}
#print(sdf)
vUserNum=input("enter a number,but it has to be < 10,000:")
# max 9,999 9 thou 9 hun ninety nine
vLen=len(vUserNum)
vTotal =[]
vTally=0

if vUserNum==11:
  print("eleven")

elif vUserNum==12:
  print("twelve")

elif vUserNum==13:
  print("thrteen")

elif vUserNum==14:
  print("forteen")

elif vUserNum==15:
  print("fifteen")

elif vUserNum==16:
  print("sixteen")

elif vUserNum==17:
  print("seventeen")

elif vUserNum==18:
  print("eighteen")
  
elif vUserNum==19:
  print("nineteen")

elif vLen==2:
  for g in vUserNum :
    #print("vtally = ", vTally, "\t g = ", g)
    if vTally==0:
      vN=vNDictTens.get(g)
      vTotal.append(vN)
      #vN=vNDictOnes.get(g)
      #vTotal.append(vN)
      vTally=vTally+1
      
      vN=vNDictOnes.get(g)
      vTotal.append(vN)

    print(vTotal)


if vLen==3 :
  for g in vUserNum :
    #print("vtally = ", vTally, "\t g = ", g)
    if vTally==0:
      vN=vNDictOnes.get(g)
      vTotal.append(vN)
      vTotal.append("hundred")
      #vN=vNDictOnes.get(g)
      #vTotal.append(vN)
    elif vTally==1:
        vN=vNDictTens.get(g)
        vTotal.append(vN)
    elif vTally==2:
      vN=vNDictOnes.get(g)
      vTotal.append(vN)
    vTally=vTally+1
  print(vTotal)
    





  

  #vFlen=n[vTally]
  #vWord1=vNDictOnes.get(n)
  #vWord2=vNDictTens.get(n)
  #print(vWord1)
  #print(vWord2)
  