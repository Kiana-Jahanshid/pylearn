myarray = []
user_input = []
temp = []
while user_input != "quit" : 
    user_input = input("\n 1_Enter your Array Numbers : ")
    if user_input ==  "quit":
        break
    else :
        myarray.append(int(user_input))

print("\nThis is Your Array : " , myarray)

flag = 0
k = 1
while k < len(myarray):
	if(myarray[k] < myarray[k - 1]):
		flag = 1
	k += 1
	
if (not flag) :
	print ("Your Array is sorted.")
else :
    print ("Your Array is not sorted.")
    for i in range(len(myarray)):
        for j in range(i + 1, len(myarray)):

            if myarray[i] > myarray[j]:
                myarray[i], myarray[j] = myarray[j], myarray[i]

    print("Sorted array is : " , myarray)


              
