def gcd(a, b):
    """returns the greatest common divisor of a and b"""
    if a > b:
       r = a % b
       if r == 0:
           return b
       else:
           return gcd(b,r)

    if a < b:
       r = b % a
       if r == 0:
           return a
       else:
           return gcd(a,r)

    if a == b:
       return a

print gcd(9,3)
