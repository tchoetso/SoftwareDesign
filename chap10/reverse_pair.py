# Tenzin Choetso
# Chapter 10 question 10-12
# code works though it takes sometime to print all the pairs on the terminal

def list_words ():
    """ returns words from words.txt in a list"""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def reverse_pair():
    """prints pairs of words that are reversed"""
    t = list_words()
    i =0
    while i < len(t):
          for words in t:
             if words[::-1] == t[i]:
                print words,words[::-1]
          i +=1  


reverse_pair()
