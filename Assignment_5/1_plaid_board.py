
m = int(input("Enter row of table : "))
n = int(input("Enter column of table : "))

def pattern(m,n):

    for row in range(1,m+1) :
        for column in range(1,n+1):
            
            if row % 2 == 0 :  
                if column % 2 == 0 : 
                    print("# ", end= " ")
                else :
                    print("* ", end= " ")

            if row % 2 != 0 :
                if column % 2 == 0 : 
                    print("* ", end= " ")
                else :
                    print("# ", end= " ")
        print("")


pattern(m,n)            