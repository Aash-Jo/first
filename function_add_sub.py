#take user input if they want to add sub or quit
#make a function to do acordingly
#e.g input:sub
#in p:enter  a num
#u:7
#  enter another num
#u:2
#output:
#5
#keep going until user enters quit
def add_or_sub (a,b,c):
  if c=="add":
    return "the answer is ",int(a)+int(b)
  elif c=="sub":
    return "the answer is ",int(a)-int(b)


vUser=input("do you want to add,sub,or quit?:")
while vUser!="quit":
  vNum1=input("Great!now enter you first num:")
  vNum2=input("Good job!now enter you second num:")
  vAOS=add_or_sub(vNum1,vNum2,vUser)
  print(vAOS)
  vUser=input("\n"+"Ok,now again,do you want to add,sub,or quit?:")

print("\n"+"see ya later,programy gator!")