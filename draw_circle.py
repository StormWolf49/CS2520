#credit to Spring 2023 CS2520 students
#Completed:  02/28/2023
#Circle drawing

import turtle
from tkinter import * 
t = turtle.Turtle()
t.speed(0)
colors = ['hot pink', 'sky blue', 'medium purple']
    

def circleStyle():
    for i in range(180):
        if(i % 3 == 0):
            t.pencolor(colors[0])
        elif(i % 3 == 1):
            t.pencolor(colors[1])
        else:
            t.pencolor(colors[2])

        t.forward(250)
        t.right(30)
        t.forward(50)
        t.left(60)
        t.forward(80)
        t.right(30)
        t.penup()
        t.setposition(0, 0)
        t.pendown()
        t.right(2)



def spiral():
    for i in range(360):
        t.pencolor(colors[i%3])
        t.width(i/100+1)
        t.forward(i)
        t.left(59)

    t.penup()
    t.setposition(0,-360)
    t.pendown()
    t.circle(360)
    turtle.bgcolor('plum')
    t.penup()
    t.setposition(0,0)
    t.pendown()


def bloom():
    for i in range (18) :
        t.pencolor(colors[i%3])
        t.circle(360)
        t.right(20)
        
def main():
    circleStyle()
    spiral()
    bloom()
    canvas = t.getscreen().getcanvas()
    canvas.postscript(file="lab5_image.ps")

    
main()
