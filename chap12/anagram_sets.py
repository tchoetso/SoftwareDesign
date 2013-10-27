def word_orlist(word):
    t = list(word)
    t.sort()
    t = ''.join(t)
    return t

def find_anagrams(filename):
    word_sort = {}
    fin = open ('words.txt')
    for line in fin:
        word = line.strip().lower()
        l = word_orlist(word)
        if l  in word_sort:
           word_sort[l].append(word) 
        else:
           word_sort[l] = [word] 
    return word_sort


def print_anagrams(d):

    t = []
    for words in d.values():
        if len(words) > 1:
            t.append((len(words),words))
    t.sort()
    for anagram in t:
        print anagram

def eight_anagram():

    d= find_anagrams('words.txt')
    t3 = {}
    for word, anagrams in d.items():
        if len(word) == 8:
            t3[word] = anagrams
    return t3

print eight_anagram()
