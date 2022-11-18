import random 
user_score = 0 
computer_score = 0 
times = int(input("how many times do you want to play ? "))
count = 1
while count <= times :
    
    x = random.randint(1,3)

    if x == 1 :
        computer_choice = "rock"
    elif x == 2 :
        computer_choice = "paper"
    elif x == 3 :
        computer_choice = "scissors"

    user_choice = input("** Enter User Choise :  ")

    print ("computer :" , computer_choice)
    print ("user     :" , user_choice)

    if   computer_choice == "rock" and user_choice == "paper" :
         user_score += 1 
    elif computer_choice == "rock" and user_choice == "scissors" :
         computer_score += 1
    elif computer_choice == "paper" and user_choice == "scissors" :
         user_score += 1
    elif computer_choice == "paper" and user_choice == "rock" :
         computer_score += 1
    elif computer_choice == "scissors" and user_choice == "rock" :
         user_score += 1
    elif computer_choice == "scissors" and user_choice == "paper" :
         computer_score += 1    
    print("computer score :" , computer_score)
    print("user score     :" , user_score, "\n---------------------")
    count += 1

if computer_score == times :
    print("Computer Won")
else :
    print("User Won")    

