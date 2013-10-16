from swampy.TurtleWorld import *

world = TurtleWorld()
t = Turtle()
t.delay= 0

angle = 90 
length = 5

def dragon_curve(t,n):
    """makes a dragon curve where n is an integer and greater than zero"""
    def x_func(t,n):
        if n == 0:
           return
        x_func(t,n-1)
        rt(t,angle)
        y_func(t,n-1)
        fd(t,length)

    def y_func(t,n):
        if n == 0:
           return
        fd(t,length)
        x_func(t,n-1)
        lt(t,angle)
        y_func(t,n-1)
       
    fd(t)
    x_func(t,n)

dragon_curve(t,30)


         
