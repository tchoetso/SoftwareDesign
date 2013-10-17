# Tenzin Choetso
# Chapter 10 question 10-13

def list_words ():
    """ returns words from words.txt in a list"""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def check_in (t, word):
    if word in t:
       return True
    else: 
       return False 

def is_interlock(t,word):
    even = word[::2]
    odd = word [1::2]
    return check_in(t,even) and check_in(t,odd)# check whether even or odd

def interlock():
    """prints pairs of words that are interlocked"""
    t = list_words()
    #i =0
    #while i < len(t):
    for i in range(len(t)):
       words = t[i]
       if is_interlock(t, words):
           print words, words[::2], words[1::2]

interlock()
