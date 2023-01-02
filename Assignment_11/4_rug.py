def  Rug(n):
    global arraydim
    arraydim = n 
    array= []
    for i in range(arraydim):
        array.append([])
        for j in range(arraydim):
            array[i].append(0)

         
    if n % 2 == 1 :
        for i in range(arraydim):
            for j in range(arraydim):
                if(abs(i - (arraydim // 2)) > abs(j - (arraydim // 2))):
                    array[i][j] = abs(i - (arraydim // 2)) 
                else:
                    array[i][j] = abs(j - (arraydim // 2)) 
    
    else :
        print("\nFor creating a rug, your input should be odd , try again... ")

    return array

def show(array):
        for i in range(arraydim):
            for j in range(arraydim):
                print(array[i][j] , end = "  ")
            print("") 

show(Rug(9))
