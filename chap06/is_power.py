def is_power(a,b):
    """returns True for a and a/b power of b"""
    if a % b != 0:
       return False

     else:
       return is_power((a/b),b)
    

print is_power(9/3)
