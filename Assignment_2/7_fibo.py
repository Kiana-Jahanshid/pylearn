fibo = int(input("enter your fibonacci number : "))
sum = 0 
a = 1 
b = 1
if fibo < 0 :
    fibo = input(" please enter positive integer number : ")   
elif fibo == 0 :
    print("\n0")   
elif fibo == 1  : 
    print(a)    
elif fibo == 2 : 
    print(a)   
    print(b)
elif fibo >= 3 :
    print(a)  
    print(b)   
    for i in range(0 , fibo-2):  
        sum = a + b  
        a = b 
        b = sum 
        print(sum)



