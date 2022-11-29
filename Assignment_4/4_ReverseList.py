checklist = []
inputs = input("\nEnter all elements in a line (separate them with comma) :\n")
userlist = inputs.split(",")

for i in range(len(userlist)):
    userlist[i] = int(userlist[i])

print("\n initial list :", userlist)
print("\nReversed list :", userlist[::-1])



