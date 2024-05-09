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
vUser=input("Hello! Plese enter your name and then we can get started!: ")

vMarks={
  
}
#store the student and total marks in dict
students_file=open("students.txt","r")
for line in students_file.readlines():
  #print("line = ",line)
  n=line.rsplit(" ")
  #print("n = ",n)

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
students_file.close()


vN1=" "
vleastTestMarks1= 400
vN2=" "
vleastTestMarks2=400
vN3=" "
vleastTestMarks3=400
vMn1=" "
vMtm1 = 0
vMn2=" "
vMtm2 = 0
vMn3=" "
vMtm3 = 0
students_file=open("students.txt","r")
for line in students_file.readlines():
  n=line.rsplit(" ")
  #print("n=",n)
  #print(vleastTestMarks1)
  #print("line =",line)
  #print(n[1])
  #print(n[0])
  if int (n[1])<int(vleastTestMarks1):
    vleastTestMarks1=n[1]
    vN1=n[0]
  if int (n[2])<int(vleastTestMarks2):
      vleastTestMarks2=n[2]
      vN2=n[0]
  if int (n[3])<int(vleastTestMarks3):
      vleastTestMarks3=n[3]
      vN3=n[0]
  if int(n[1])>int(vMtm1):
    vMtm1=n[1]
    vMn1=n[0]
  if int(n[2])>int(vMtm2):
    vMtm2=n[2]
    vMn2=n[0]
  if int(n[3])>int(vMtm3):
      vMtm3=n[3]
      vMn3=n[0]  
students_file.close()
print(vN1,"got the lowest in the first one,They gota",vleastTestMarks1,"!")
print("\n",vN2,"got the lowest in the 2nd one,They gota",vleastTestMarks2,"!")
print("\n",vN3  ,"got the lowest in the 3rd one,They got a",vleastTestMarks3,"!")
print("\n",vMn1,"got the highest in the first one,and they got a ",vMtm1,"! wow!")
print("\n",vMn2,"got the highest in the second one,and they got a ",vMtm2,"! wow!Amazeing!")
print("\n",vMn2,"got the highest in the third one,and they got a ",vMtm3,"! wow!Great Job!")
#print(vMarks)
# find the student with most marks
vMax=0
vMaxname=" "
for x in vMarks:
  if vMarks[x]>vMax:
    vMax=vMarks[x]
    vMaxname=x
students_file.close()
print("\n",vMaxname,"got a",vMax,"!,o, and ,",vUser,",this is who got the highest total!")
# find the student with least marks
vMin=10000
vMinname=" "
for x in vMarks:
  if vMarks[x]<vMin:
    vMin=vMarks[x]
    vMinname=x

print("\n", vMinname,"got a",vMin,"!,This person,",vUser,",is the one with the lowest total!")

print("\n Thanks for using my program!,if you ever need to find who got the highest and the lowest,i'm your program! ")

  
  
  









