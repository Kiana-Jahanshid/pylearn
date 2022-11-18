print("Enter Student's First Name :")
firstname = input()
print("Enter Student's Last Name :")
lastname = input()
print("Enter her/his 1st Grade :")
first_grade = float(input())
print("Enter her/his 2nd Grade :")
second_grade = float(input())
print("Enter her/his 3rd Grade :" )
third_grade = float(input())



Average_Number = (first_grade + second_grade + third_grade) / 3
print("\nThe Average Result Is : " , Average_Number )

if Average_Number >= 17 :
    status = "GREAT"
elif 12 <= Average_Number < 17 : 
    status = "NORMAL"  
elif Average_Number < 12 :
    status = "FAIL"    

print( firstname , lastname , "'s" , " Average Status is :" , " <<", status ,">> ")





