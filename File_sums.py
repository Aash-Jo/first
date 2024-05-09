# Read the file input.txt
# for each line do the calculation
# store the results in a new file 
# call the new file output.txt
# e.g. input file line > 5*2
# output file line > 5*2 = 10
input_file=open("input.txt","r")
output_file=open("output.txt","w")

for n in input_file.readlines():
  n1=int(n[0])
  n2=int(n[2]) 
  print("n=",n)
  if n[1]=="+":   
    vSum=n1+n2
    vSum=str(vSum)
  elif n[1]== "-":
    vSum=n1-n2
    vSum=str(vSum)
  elif n[1]== "*":
   vSum=n1*n2
   vSum=str(vSum)
  elif n[1]== "/":
    vSum=n1/n2
    vSum=str(vSum)  
  print(n1+n2)
  output_file.write("\n"+n[0]+n[1]+n[2] +" = " + vSum) 
output_file.close()
input_file.close()
 