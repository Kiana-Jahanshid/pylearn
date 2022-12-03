rows = int(input("Enter number of rows : "))

def pattern(rows) :
    counter = 0
    for i in range(1, rows + 1): 
        for j in range (1, (rows - i) + 1): 
            print(end = " ")          
        while counter != (2 * i - 1):
            print("*", end = "")
            counter +=  1
        counter = 0   
        print("")  
    
    space = 2
    count = 1
    for i in range(1, rows): 
        for j in range (1, space):
            print(end = " ") 
        space +=  1	  
        while count <= (2 * (rows - i) - 1): 
            print("*", end = "") 
            count += 1
        
        print("")
        count = 1	



pattern(rows)  
