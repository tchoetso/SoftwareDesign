"""Solution to chapter 3 in Think Python.

Author: Tenzin Choetso
"""

def grid(x,y):
    first = '+ - - - -'
    second = '|        '
    end1 = '+'
    end2 = '|'

    for i in range (y):
        print first*x + end1
        print second*x + end2
        print second*x + end2
        print second*x + end2
        print second*x + end2        
        
    print first*x + end1

grid(2,2)

grid(4,4)
    
     
