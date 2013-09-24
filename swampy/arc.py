#Author: Tenzin Choetso
# Chapter 4 -- 5

from swampy.TurtleWorld import *
import math 

world = TurtleWorld()
bob = Turtle() #bob needs to defined outside
bob.delay= 0.05


def arc(t,r,angle):
    print t
    length = (2*math.pi*r)*angle/360 # circumference of the cirlce
    n = int(length/3)+1 
    steplength = length/n
    stepangle = float(angle)/n
    
    for i in range(n):
        fd (t,steplength)
        lt(t,stepangle)
  
 
arc(bob,50,270)

