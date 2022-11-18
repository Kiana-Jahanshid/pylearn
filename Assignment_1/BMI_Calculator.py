print("\n     <<<<     Welcome to BMI CALCULATOR    >>>>")

print("\n1) ENTER YOUR DESIRED WEIGHT UNIT (kg / lbs):")
w_unit = input()
print("2) ENTER YOUR WEIGHT NUMBER: ")
weight= float(input())

print("\n3) ENTER YOUR DESIRED HEIGHT UNIT (centimeter / meter / feet) :")
h_unit = input()
print("4) ENTER YOUR HEIGHT NUMBER : ")
height = float(input())


if w_unit == "lbs" and h_unit =="feet": 
    weight = weight * 0.45359237
    height = height * 0.3048 
    BMI = weight / (height**2)
elif w_unit == "kg" and h_unit =="meter" :
    BMI = weight / (height**2)
elif w_unit == "kg" and h_unit =="centimeter" :
    height = height /100
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
    print("You Have EXTREME OBESITY")
