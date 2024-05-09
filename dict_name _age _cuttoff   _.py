# ask for a variable age_cutoff
#vUser_cuttoff=input("enter a age cuttoff:")
# Keep asking user for name of somebody, then their age
# keep asking until user decides to quit
# when user decides to quit, print all names of people who
#     are below age_cutoff

# ask for a variable age_cutoff
vUser_cuttoff=input("enter a age cuttoff :")
vUser_cuttoff=int(vUser_cuttoff)

vDict={
  
}


vUser_choice = input("Do you want to add new person (add) or quit? :")
vUser_choice=vUser_choice.lower()
while vUser_choice != "quit":
  vUser_Name=input("now enter a name of sombody or something you know!,or quit:")
  vUser_Name=vUser_Name.lower()
  vUser_age=input("Good!,now enter their age!:")
  vUser_age=int(vUser_age)
  vDict[vUser_Name]=vUser_age
  
  #print("vDict = ",vDict)
  vUser_choice = input(" Now do you want to add new person (add) or quit? :")
  
for n in vDict:
  if vDict[n]<= vUser_cuttoff:
    print(n)
    
  
 


print("I hope you had a good time using my program,hope you come back soon!")

