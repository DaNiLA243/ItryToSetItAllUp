import turtle as trt

t=trt.Pen()

def letterA():

    t.penup()
    t.goto(-30,50) #centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("black")

    t.right(65)
    t.forward(100)

    t.setpos(-30,50)
    t.right(50)
    t.forward(100)

    t.penup()
    t.setpos(-50,-10)
    t.right(65)
    t.pendown()
    t.backward(50)
    
letterA()
trt.done()


