#Author: Tenzin Choetso
# Chapter 4 

from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle() #bob needs to defined outside
bob.delay = 0.5

def square(t,length):
    print t
    for i in range(4):
        fd (t,length)
        lt(t)


def polygon(t,length,n):
    print t
    for i in range(n):
        fd (t,length)
        lt(t,360/n)

def circle(t,r):
    print t 
    n = int (r/2)
    length = (2*math.pi*r)/n # circumference of the cirlce 
    polygon(t,length,n)

def arc(t,r,angle):
    print t
    length = (2*math.pi*r)*angle/360 # circumference of the cirlce
    n = int(length/3)+1 
    steplength = length/n
    stepangle = float(angle)/n
    
    for i in range(n):
        fd (t,steplength)
        lt(t,stepangle)

#square(bob,50) 
#arc(bob,50,180)
#circle(bob,50)
polygon(bob,75,6)
