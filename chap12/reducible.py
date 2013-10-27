 
def word_dict():
    w_d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        w_d[word] = word
    w_d['a']='a'
    w_d['i']='i'
    w_d['']=''
    return w_d

def children(word, w_d):
    d  = []
    for i in range(len(word)):
        w_child = word[:i] + word[i+1:]
        if w_child in w_d:
            d.append(w_child)
    return d


memo = {}
memo[''] = ['']


def is_reducible(word, w_d):
    if word in memo:
        return memo[word]

    res = []
    for kid in children(word, w_d):
        t = is_reducible(kid, w_d)
        if t:
            res.append(kid)

    memo[word] = res
    return res

def reduce_every(w_d):

    t = []
    for word in w_d:
        a = is_reducible(word, w_d)
        if a!= []:
            t.append(word)
    return t


def print_trail(word):
    if len(word) == 0:
       return 
    print word
    t = is_reducible(word, w_d)
    print_trail(t[0])


def longest_reduce(w_d):
    all = reduce_every(w_d)
    t = []
    for word in all:
        t.append((len(word), word))
    t.sort(reverse=True)

    for length, word in t[0:5]:
        print_trail(word)
      #  print '\n'
 

w_d = word_dict()
longest_reduce(w_d)
