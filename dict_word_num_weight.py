# ask user for a string
# use a = 1, b = 2, ... z= 26 to calculate #the weight of the string
#by adding all the letters
# e.g. user gave aba ,program prints  weight = 4
vUser=input("Enter a string/setence:")
vUser=vUser.lower()

vDict={
  "a":1,
  "b":2,
  "c":3,
  "d":4,
  "e":5,
  "f":6,
  "g":7,
  "h":8,
  "i":9,
  "j":10,
  "k":11,
  "l":12,
  "m":13,
  "n":14,
  "o":15,
  "p":16,
  "q":17,
  "r":18,
  "s":19,
  "t":20,
  "u":21,
  "v":22,
  "w":23,
  "x":24,
  "y":25,
  "z":26, 
  "0":0,
  "1":1,
  "2":2,
  "3":3 ,  
  "4":4,
  "5":5,
  "6":6,
  "7":7,
  "8":8,
  "9":9
}
vTotalweight=0
for n in vUser:
  #print("n=",n)
  #print(vDict.get(n))
  vValue=int(vDict.get(n))
 # print(vValue)
  vTotalweight=vTotalweight+vValue
print("weight=",vTotalweight)

