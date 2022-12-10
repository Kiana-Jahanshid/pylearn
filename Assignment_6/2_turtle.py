import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pen(pensize=2, speed = 3)
coordinate  = 40
initial_left  , initial_forward = 127 , 83
count , sides , angle  = 10 , 5 , 150 
first_angle , side_len , sec_angle , z, count1 = 150 , 50 , 120 , 30 ,2

def move_turtle_to_home(x):
    t.penup()
    t.home() #move turtle to [0,0] coordiantes
    t.forward(x)
    t.rt(0)
    t.pendown()

for i in range(2):
    if i == 1 :
        move_turtle_to_home(coordinate/2)    
    t.left(first_angle)
    t.forward(side_len)  
    for j in range(count1):
        t.left(sec_angle)
        t.forward(side_len)
    first_angle-= 15
    side_len += 20
    sec_angle -= z
    count1 += 1

for j in range(6):
     move_turtle_to_home(coordinate)
     coordinate += 25
     t.left(initial_left)
     initial_left -= 4
     t.forward(initial_forward )
     angle = 180 - ((180 * (sides-2))/(sides))

     for i in range(sides - 1):
         t.left(angle)
         t.forward(initial_forward)
     initial_forward += count
     count -= 1
     sides += 1
