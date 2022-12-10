import math
from math import sqrt
from math import pi 
import numpy as np 
user_choice =  input("\nIS YOUR EQUATION STANDARD ? ENTER  y/n\n")
if user_choice == "y" :
     print(" Enter 3 coefficients (standard form): ")
     a = float(input("a is : "))
     b = float(input("b is : "))     
     c = float(input("c is : "))  
     print("standard equation : x**3 + ",a,"x**2 + ",b,"x + ",c," = 0" )      
     
   
elif  user_choice == "n" : 
     print(" Enter 4 coefficients : ")
     a = float(input("a is : "))
     if a == 0 :
         print("ERROR , 'a' can not be 0 , enter another value : ")
         a = float(input("a is : "))
     b = float(input("b is : "))     
     c = float(input("c is : "))
     d = float(input("d is : "))
     print("initial equation :" ,a,"x**3 + ",b,"x**2 + ",c,"x + ",d,"  = 0" )
     a = b/a 
     b = c/a
     c = d/a         
     print("standard equation form :" ,a,"x**3 + ",a,"x**2 + ",b,"x + ",c," = 0" )    


def cubic_equation_calculator(a , b , c):
        
        p = b - ( (a**2) / 3 )
        q = ( (2*(a**3)) / (27)) - ((a*b)/3) + c
        Delta = ((q**2)/4) + ((p**3)/27)

        if Delta > 0 :
            x = (((-q) / 2) + sqrt(Delta))**(1/3) + (((-q) / 2) - sqrt(Delta))**(1/3)
            print("equation has one real root :")
            print(" x = " , x)
            return x 
        
        elif  Delta == 0 :
            x1 = (-2)*((q/2)**(1/3)) - (a/3)
            x2 = ((q/2)**(1/3)) - (a/3)
            x3 = ((q/2)**(1/3)) - (a/3)
            print("equation has two distinct and a double roots :")
            print("x1 = ", x1 ,"\nx2 = " , x2 , "\nx3 = " ,x3)
            return x1 , x2 , x3

        elif Delta < 0 :
            x1 =  (2/ sqrt(3)) * (sqrt(-p)) * math.sin( (1/3) * (math.asin( (3*sqrt(3)*q) / (2*(sqrt(-p))**3)))  )  -  (a/3)
            x2 = (-2/ sqrt(3)) * (sqrt(-p)) * math.sin( (1/3) * (math.asin( (3*sqrt(3)*q) / (2*(sqrt(-p))**3)))  + (pi/3))  -  (a/3)
            x3 =  (2/ sqrt(3)) * (sqrt(-p)) * math.cos( (1/3) * (math.asin( (3*sqrt(3)*q) / (2*(sqrt(-p))**3)))  + (pi/6))  -  (a/3)
            print("equation has three distinct roots :")
            print("x1 = ", x1 ,"\nx2 = " , x2 , "\nx3 = " ,x3)            
            return x1 , x2 , x3 


cubic_equation_calculator(a,b,c)