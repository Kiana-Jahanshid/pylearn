import random 
myarray = []
n = int(input("\nenter the length of your array : "))
counter = 0 

while  counter != n :
    r = random.randint(0 , 50)
    if r not in myarray :
       myarray.append(r)
       counter += 1 
       
print(myarray)
