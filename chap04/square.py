#Author: Tenzin Choetso
# Chapter 4 -- 1,2 

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle() #bob needs to defined outside

def square(t,length):
    print t
    for i in range(4):
        fd (t,length)
        lt(t,45)

square(bob,50)
