import random

press_enter = input("press enter to roll a dice ")
dice_input = random.randint(1 , 6)
print(dice_input)

while dice_input == 6 :
    reward = input("You Can 'Roll A DICE AGAIN' , press enter to roll :\n ")
    dice_input = random.randint(1 , 6)
    print(dice_input)   
else  :
    print("END")
