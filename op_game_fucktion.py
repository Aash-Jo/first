#make a game where the user gives two nums and do random op on them and user gesses op
def op_random(Fnum,Snum,Count):
  vTotal=[]
  if Count==1 or Count==4:
    vF=int(Fnum)/int(Snum)
    vTotal.append(vF)
    vTotal.append("div")
  elif Count==3 or Count==6 or Count==10:
    vF=int(Fnum)-int(Snum)
    vTotal.append(vF)
    vTotal.append("sub")
  elif Count==2 or Count==5 or Count==8:
    vF=int(Fnum)+int(Snum)
    vTotal.append(vF)
    vTotal.append("add")
  else:
    vF=int(Fnum)*int(Snum)
    vTotal.append(vF)
    vTotal.append("mult")
  return vTotal
vTally=1
vGRight=True
vUOp=input("In this game you are guessing the op,Now quit(q) or start(s)?:")
while vUOp=="s" or vUOp=="a":
  vTally=1
  vGRight=True
  vUnum1=input("enter a RANDOM num more than ten:")
  vUnum2=input("enter a second RANDOM num more than ten:")
  while vTally<10 and vGRight:
    vOp=op_random(vUnum1,vUnum2,vTally)
    print("you get one chance to guess.The anwser was",vOp[0])
    vUGuess=input("what op do YOU think?:")
    if vUGuess==vOp[1]:
      vUOp=input("\nCORRECT!now,quit(q) or again(a)?:\n ")
    else:
      vGRight=False
    vTally=vTally+1
if vGRight==False:
      print("Sorry,you guessed wrong.try again.")
else:
   print("\n","CONGRATS! YOU ARE A WINNER!!!")
  