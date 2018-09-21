import turtle

def draw_square(turtle):
    
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)

##def draw_circle():
##    
##    angie = turtle.Turtle()
##    angie.shape("arrow")
##    angie.color("green")
##    angie.circle(100)    
##    angie.speed(2)
##    
##def draw_triangle():
##    
##    joe = turtle.Turtle()
##    joe.shape("triangle")
##    joe.color("blue")  
##    joe.speed(3)
##    
##    i = 0
##    
##    while i < 3:
##    
##        joe.backward(150)
##        joe.left(120)
##        i = i + 1

window = turtle.Screen()
window.bgcolor("black")

brad = turtle.Turtle()
brad.shape("circle")
brad.color("red")
brad.speed(9)

for i in range(0,36):
    draw_square(brad)
    brad.right(10)
##draw_circle()
##draw_triangle()

window.exitonclick()
