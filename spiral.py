
#spiral pattern 1

import turtle

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")

side=500
myPen.penup()
myPen.goto(-200,-200) #position cursor at the bootom right of the screen
myPen.pendown()

#Start Spiral
for i in range (1,100):
   myPen.forward(side)
   myPen.left(90)
   side=side-4

#spiral pattern 2
x=turtle.clone()

x.speed(0)
x.color("#1E56FC")

side=20
x.penup()
x.goto(40,25) #position cursor at the bootom right of the screen
x.pendown()

for i in range (1,50):
  x.forward(side)
  x.left(92)
  side=side+7


x.penup()
x.goto(500,500)

#Start Spiral
for i in range (1,20):
  for j in range (0,4):
      x.forward(side)
      x.left(90)
  x.left(20)
  side=side+5



