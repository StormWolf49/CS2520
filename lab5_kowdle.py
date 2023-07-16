#Name: Nikhil Kowdle
#Lab 5
#This program contains the task required for this assignment.

import turtle
from tkinter import * 
from PIL import Image
wd, ht = 500, 500
turtle.setup(width=wd, height=ht, startx=0, starty=0)
turtle.colormode(255)
t = turtle.Turtle()
t.speed(0)
colors = ['turquoise', 'tomato', 'lime green', 'dark orange', 'cornflower blue', 'fuchsia']

def draw_background(a_turtle):
    """ Draw a background rectangle. """
    ts = a_turtle.getscreen()
    canvas = ts.getcanvas()
    height = ts.getcanvas()._canvas.winfo_height()
    width = ts.getcanvas()._canvas.winfo_width()

    turtleheading = a_turtle.heading()
    turtlespeed = a_turtle.speed()
    penposn = a_turtle.position()
    penstate = a_turtle.pen()

    a_turtle.penup()
    a_turtle.speed(0)  # fastest
    a_turtle.goto(-width/2-2, -height/2+3)
    a_turtle.fillcolor(turtle.Screen().bgcolor())
    a_turtle.begin_fill()
    a_turtle.setheading(0)
    a_turtle.forward(width)
    a_turtle.setheading(90)
    a_turtle.forward(height)
    a_turtle.setheading(180)
    a_turtle.forward(width)
    a_turtle.setheading(270)
    a_turtle.forward(height)
    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.setposition(*penposn)
    a_turtle.pen(penstate)
    a_turtle.setheading(turtleheading)
    a_turtle.speed(turtlespeed)

def light():
    color = 0

    for i in range(0, 255, 3):
        nc = color + i
        t.penup()
        t.home()
        t.forward(250-(2.6*(i/3)))
        t.left(90)
        t.pencolor((nc, nc, nc))
        t.fillcolor((nc, nc, nc))
        t.begin_fill()
        t.pendown()
        t.circle(250-(2.6*(i/3)), steps=6)
        t.end_fill()

    t.penup()
    t.home()

def tunnel():
    for i in range(7):
        t.pencolor(colors[i%6])
        t.forward(300)
        t.penup()
        t.setposition(0, 0)
        t.pendown()
        t.left(60)
    
    
    t.penup()
    t.home()
    for i in range(350):
        if i%6 == 0:
            t.penup()
            t.home()
            t.forward(i)
            t.left(90)
            t.pendown()
        
        t.pencolor(colors[i%6])
        t.width(1)
        t.circle((i//6)*6, extent=60, steps=1)

    t.penup()
    t.home()
    t.forward(10)
    t.left(90)
    t.pencolor('white')
    t.fillcolor('white')
    t.begin_fill()
    t.pendown()
    t.circle(10, steps=6)
    t.end_fill()

def main():
    turtle.bgcolor('black')
    draw_background(t)
    light()
    tunnel()
    t.home()
    t.hideturtle()

    canvas = t.getscreen().getcanvas()
    canvas.postscript(file="lab5_image.ps", pagewidth=wd, pageheight=ht)
    psimage = Image.open("lab5_image.ps")
    psimage.save("lab5_image.jpg")

main()