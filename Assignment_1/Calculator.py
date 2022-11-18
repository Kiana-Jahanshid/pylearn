import math
print("welcome to my calculator\n")
print("Sum : + \tSub : - ")
print("Mul : * \tDiv : / ")
print("Sin     \tcos")
print("tan     \tcot")
print("log     \tfact")
print("sqrt")

op = input("ENTER Your Operator :")

if op == "+" or op == "-" or op == "*" or op == "/" :
    a = float(input("Enter 1st number :"))
    b = float(input("Enter 2nd number :"))
elif op == "sin" or op == "cos" or op == "tan" or op == "cot" :
    degree = float(input("Enter a Degree :")) 
    R = degree * (math.pi /180)    
elif op == "log" or op == "fact" or op == "sqrt" :
    z = float(input("Enter a Number :"))    


if op == "+" :
    result = a + b
elif op == "-" :
    result = a - b 
elif op == "*" :
    result = a * b 
elif op == "/" :
    if b == 0 :
        result = "can't devide by zero"
    else :
        result = a / b 

elif op == "sin" :
    result = math.sin(R)             
elif op == "cos" :
    result = math.cos(R) 
elif op == "tan" :
    result = math.tan(R) 
elif op == "cot" :
    result = 1/math.tan(R)      

elif op == "log" :
    if z <= 0 :
        result = "ERROR"
    else :    
        result = math.log(z , 10) 
elif op == "sqrt" :
    if z < 0 :
        result = "ERROR"
    else :
        result = math.sqrt(z) 
elif op == "fact" :
     result = math.factorial(z)     

print(result)









