m = int(input("Enter row of table : "))
n = int(input("Enter column of table : "))

def multiply_table(row , column) :
    
    for i in range(1 , row+1):
        for j in range(1 , column+1):
            result = i * j
            print(result  ,  end="    ")

        print("\n")  



multiply_table(m,n)