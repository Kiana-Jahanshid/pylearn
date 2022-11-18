print("\n     <<<<     Welcome to BMI CALCULATOR    >>>>")


print("2) ENTER YOUR WEIGHT NUMBER: ")
weight= float(input())

print("4) ENTER YOUR HEIGHT NUMBER : ")
height = float(input())



BMI = weight / (height**2)
print("\nYOUR BMI IS  ------->> " , round(BMI,2))      

if BMI < 18.5 :
    print("You are UNDERWEIGHT")
elif 18.5 <= BMI <= 24.9 :
    print("You have NORMAL WEIGHT")
elif 25 <= BMI <= 29.9 :
    print("You are OVERWEIGHT")
elif 30 <= BMI <= 34.9 :
    print("You Have OBESITY ")
elif 35 <= BMI <= 39.9 :
    print("You Have EXTREME OBESITY.")
