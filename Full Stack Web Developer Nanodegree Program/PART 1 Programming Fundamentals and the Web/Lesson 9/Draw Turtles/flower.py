import turtle

def draw_diamond(turtle):
    
    for i in range(0,4):
        if i == 0 or i == 2:
            turtle.forward(100)
            turtle.right(40)
            
        if i == 1 or i == 3:
            turtle.forward(100)
            turtle.right(140)

window = turtle.Screen()
window.bgcolor("blue")

brad = turtle.Turtle()
brad.shape("circle")
brad.color("yellow")
brad.speed(10)

for i in range(0,45):
    draw_diamond(brad)
    brad.right(8)

brad.right(90)
brad.forward(350)

window.exitonclick()
