#Author: Tenzin Choetso
# Chapter 4 -- 3 

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle() #bob needs to defined outside

def polygon(t,length,n):
    print t
    for i in range(n):
        fd (t,length)
        lt(t,360/n)
polygon(bob,75,6)
