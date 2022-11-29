checklist = []
inputs = input("\nEnter elements of a list (separate them with comma) :\n")
userlist = inputs.split(",")

for i in range(len(userlist)):
    userlist[i] = int(userlist[i])

print("\ninitial list :", userlist)

for i in range(len(userlist)-1) :
    if userlist[i] not in checklist :
       checklist.append(userlist[i])

print("\nlist without duplicates : " ,checklist)

