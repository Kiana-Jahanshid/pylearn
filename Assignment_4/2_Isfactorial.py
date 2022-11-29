num = int(input("\nEnter a number to check if it\'s a FACTORIAL NUMBER :"))
                 
factorial = 1
factlist = []
count = 20 
for i in range (1,count):
          factorial = factorial * i
          factlist.append(factorial)


if num in factlist :
    print("YES")
else :
    print("NO")
        
                

