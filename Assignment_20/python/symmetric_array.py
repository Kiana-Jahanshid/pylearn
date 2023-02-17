import math

def symmetry_check(user_input):
    array = []
    array = user_input.split(",")
    last_index = len(array)-1
    if len(array) % 2 == 0 :
        for i in range(int(len(array)/2)):
            if array[i] == array[last_index-i]: 
                flag = True
            else : 
                flag = False
                break
    elif len(array) % 2 == 1 :
        for i in range(len(array)-1):
            if i <= math.ceil(len(array)/2) :            
                if array[i] == array[last_index-i] :
                    flag = True 
                else : 
                    flag = False
                    break
            
    if flag == True :
        print("\n ✅ Your Array is syymetric ✅\n")          
    else :
        print("\n ❌ Your Array is not SYMMETRIC ❌\n")


user_input = input("Enter your Array  numbers to check it's symmetry (separate them with comma) :  ")
symmetry_check(user_input)