sum_of_grades  = 0 
count = 0
print(" \nEnter all of Student's Grades : \nOr type 'exit' to get average")

while True :
    grade = input()
    if grade == "exit" :
       break
    else :
        grade = float(grade)
        sum_of_grades = sum_of_grades + grade
        count = count + 1

student_average = sum_of_grades / count
print("Student's Average is : " , student_average)