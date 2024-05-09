# read student names and marks from the file
# find the student with the highest marks across three tests
# e.g. line in students.txt > marks will be <100
# name marks1 marks2 makrks3
#Aadi 20 80 90
#Aashvi 20 78 94
#Dad 19 90 99
#
#for every student add marks1, 2,3
# find the student with highest marks
# print name of the student

# Open a file "students.txt"

vMarks={
  
}
#store the student and total marks in dict
students_file=open("students.txt","r")
for line in students_file.readlines():
  #print("line = ",line)
  n=line.rsplit(" ")
  vName=n[0]
  vM1=int(n[1])
  vM2=int(n[2])
  vM3=int(n[3])
  vTotal=vM1+vM2+vM3
  #print("vName=",n[0])
  #print("vM1=",n[1])
  #print("vM2=",n[2])
  #print("vM3=",n[3])
  #print("vTotal=",vM1+vM2+vM3)
  
  
  vMarks[vName]=vTotal

#print(vMarks)
students_file.close()
# find the student with most marks
vMax=0
vMaxname=" "
for x in vMarks:
  if vMarks[x]>vMax:
    vMax=vMarks[x]
    vMaxname=x

print(vMaxname,"got a",vMax,"! wow !")
# find the student with least marks
vMin=10000
vMinname=" "
for x in vMarks:
  if vMarks[x]<vMin:
    vMin=vMarks[x]
    vMinname=x

print(vMinname,"got a",vMin,"!Sorry,Next time try to study harder!")



  
  
  


