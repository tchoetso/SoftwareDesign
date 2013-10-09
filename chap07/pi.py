import math

def factorial(n):
    """Returns factorial of n."""
    if n==0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n*recurse
        return result 
   


def estimate_pi():
    """Returns estimate value of pi."""
    a = 2*math.sqrt(2)/ 9801 
    k = 0
    final_pi = 0 
    while True:
          inverse_pi = a *factorial(4*k) * (1103 + 26390*k)/( factorial(k)**4  * 396**(4*k))
          k += 1 
          pi = 1/inverse_pi
          final_pi += pi
          
          if abs(pi)>1e-15:
             break
    return final_pi

print estimate_pi()

    
      
    
