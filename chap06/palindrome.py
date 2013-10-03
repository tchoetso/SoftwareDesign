"""Module that provides is_palindrome.

Author of is_palindrome: you
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """returns whether word is a palindrome or not"""
       
    if len(word)<=1:#word can have both odd or even number of letters
       return True
    else:
       if first(word)!= last(word):
          return False
       else:
          return is_palindrome(middle(word))
 
print is_palindrome('tenzin')
print is_palindrome ('hannah')

