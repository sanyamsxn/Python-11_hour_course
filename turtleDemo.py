import turtle         #turtle is a drawing board ,vector graphic which allows you to draw all over it.


a=turtle.Turtle()
a.speed(3)



### defining a function
def  square():
    a.forward(100)
    a.right(90)
    a.forward(100)       # { making a square}
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(100)  

square()                 #calling a function 
a.forward(100)
square()

turtle.done()