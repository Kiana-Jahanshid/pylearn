user_input = int(input("\nEnter number of Rows : "))
def Triangle(Rows):

    myArray = []
    for i in range(Rows):
        myArray.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                myArray[i].append(1)               
            else:
                myArray[i].append(myArray[i - 1][j - 1] + myArray[i - 1][j])
        print(myArray[i])          
    
    return myArray


Triangle(user_input)