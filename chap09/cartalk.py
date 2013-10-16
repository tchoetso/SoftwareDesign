# Tenzin Choetso
# Chapter 9

def triple_doubleletters1 ():
    """ Prints words with three consecutive double letters"""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        triple_doubleletters2(word)

def triple_doubleletters2 (w):  
    """Checks whether a word has three consecutive double letters and 
       prints it if it does
       w: string"""
    i = 0
    total = 0
    while i < (len(w)-1):
        if w[i]== w[i+1]:
           total += 1
           if total == 3:
              print w
              
           i = i + 2 # avoids same triple letters 
        else:  
            i = i+1
            total = 0 #to attain consecutive double letters
 
triple_doubleletters1()

def is_palindrome(s):
    """ Checks whether n is palindrome
    s:  string
    Returns: bool """
    return s == s[::-1]

def checker1(nn):
    """ Checks whether string has the behaviors
      described in the question 9.8
      num:  integer
      Returns: bool """
    ns  = str(nn)
    ns1 = str(ns[2:6])
    ns2 = str(int(ns)+1)
    ns3 = ns2[1:6]
    ns4 = str(int(ns)+2)
    ns5 = ns4[1:5]
    ns6 = str(int(ns)+3)
    if is_palindrome(ns1)and is_palindrome(ns3)and is_palindrome (ns5)and is_palindrome(ns6):
       return True
    else: 
       return False

def checker2():
    """ prints numbers that satisfy the requirement 
    described in question 9.8"""
    i = 100000
    while i < 1000000:
        if checker1(i):
            print i
        i = i+1

checker2()

  

