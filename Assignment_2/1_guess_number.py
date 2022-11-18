import random 

comp_num = random.randint(10 , 40)
user_num = int(input("Guess a Number : "))
counter = 1 
while comp_num != user_num  :
    counter = counter + 1
    if comp_num > user_num :
        print("go up")   
    elif comp_num < user_num :
        print("go down")     
    
    user_num = int(input("Guess a Number : "))
else :
    print("\n** You Won, After" , counter , "Times **")
    
