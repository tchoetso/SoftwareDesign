from pronounce import read_dictionary

def dict_words ():
    """ returns words from words.txt in a dictionary
    with words as keys"""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word
    return d

def is_homophone(word1, word2, homophonic):
    h1 = homophonic
    if word1 in h1 and word2 in h1:
       return h1[word1] == h1[word2]

def check(word, w_d,homophonic):
   
    w1 = word[1:]
    w2 = word [0] +word[2:]
    if w1 in w_d and is_homophone(word,w1,homophonic) and w2 in w_d and is_homophone(word,w2, homophonic):
       return True
    else:
       return False


def print_word():
    homophonic = read_dictionary()
    w = dict_words()
    for keyword in dict_words():
        if check(keyword,w,homophonic):
           print keyword,keyword[1:],keyword[0] +keyword[2:]

print_word()
