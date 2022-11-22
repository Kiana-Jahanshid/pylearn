first_number = int(input("enter First number :"))
second_number = int(input("enter second number :"))
if first_number > second_number : 
     n = second_number
else: 
     n = first_number 
for i in range(1, n+1): 
      if((first_number % i == 0) and (second_number % i == 0)): 
            bmm = i     

print ("The gcd value is :" , bmm)
