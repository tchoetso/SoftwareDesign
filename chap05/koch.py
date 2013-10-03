from swampy.TurtleWorld import *

world = TurtleWorld()
t = Turtle() #t needs to defined outside
t.delay= 0

def Koch (t,length,angle):
    """draw a Koch fractal curve recursively"""
    n=360.0/ (angle*2)
    if length < n:
       fd(t,length/n)
       return 
    Koch(t,length/n,angle) 
    lt (t, angle)
    Koch(t,length/n,angle)
    rt (t,angle*2)
    Koch(t,length/n,angle)
    lt (t,angle)
    Koch(t,length/n,angle)

#Koch(t,300)

def snowflake (t,length,angle):
    n=360.0/ (angle*2)
    if 360.0%(angle*2)== 0:
       for i in range (int(n)):
           Koch(t,length,angle)
           rt (t,120)
    else:
         for i in range (int(n)+1):
             Koch(t,length,angle)
             rt (t,120)
      
snowflake (t,300,75)
