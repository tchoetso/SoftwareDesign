from swampy.TurtleWorld import *

world = TurtleWorld()
t = Turtle() #t needs to defined outside
t.delay= 0

def Koch (t,length):
    """draw a Koch fractal curve recursively"""

    if length < 3:
       fd(t,length/3.0)
       print length
       return 
    Koch(t,length/3.0) 
    lt (t, 60)
    Koch(t,length/3.0)
    rt (t,120)
    Koch(t,length/3.0)
    lt (t,60)
    Koch(t,length/3.0)



Koch(t,300)

def snowflake (t,length):
    for i in range (3):
        Koch(t,length)
        rt (t,120)

#snowflake (t,300)
