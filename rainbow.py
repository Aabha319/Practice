import turtle

myPen = turtle.Turtle()
myPen.shape("turtle")
myPen.speed(0)

window = turtle.Screen()
window.bgcolor("brown")

rainbowColors = ["red","orange","yellow", "green", "blue","indigo","violet","brown"]

size=200

myPen.penup()
myPen.goto(0,-360)

for color in rainbowColors:
  myPen.color(color)
  myPen.fillcolor(color)
  myPen.begin_fill()
  myPen.circle(size)
  myPen.end_fill()
  size -= 20
  


