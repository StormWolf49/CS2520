#Name: Nikhil Kowdle
#Lab 5
#This program contains the task required for this assignment.

import turtle
from tkinter import * 
t = turtle.Turtle()
t.speed(0)
colors = ['salmon', 'lime green', 'cornflower blue']

def main():
    canvas = t.getscreen().getcanvas()
    canvas.postscript(file="lab5_image.ps")

main()