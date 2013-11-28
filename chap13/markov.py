"""Think Python: Exercise - 8
Tenzin Choetso
"""

import string
import random
import sys

suffixes = {}
prefix = ()

def process_file(filename, order = 2):
    """Returns map from prefix to suffixes

    filename: string
    skip_header: boolean, whether to skip the Gutenberg
    """
 
    fp = file(filename)

    skip_gutenberg_header(fp)

    for line in fp:
        words = line.strip().split()
        for word in words:
            process_word(word, order)
  


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_word(word, order=2):
    """Maps prefixes to suffixes.

    word: string
    order: integer

    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    if prefix in suffixes:
       suffixes[prefix].append(word)
    else:
        # if there is no entry for this prefix, make one
       suffixes[prefix] = [word]

    prefix = prefix[1:] + (word,)


def markov_text(n=100):
    """Generates random words from text creating a block of text n words long.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    # choose a random prefix 
    choose_prefix = random.choice(suffixes.keys())
    
    for i in range(n):
        suffix = suffixes.get(choose_prefix, None)
        if suffix == None:
            markov_text(n-i)
            return

        # choose a random suffix
        word = random.choice(suffix)
        print word,
        choose_prefix = choose_prefix[1:] + (word,)


def main(name, filename='emma.txt', n=100, order=2, *args):
    try:
        n = int(n)
        order = int(order)
    except:
        print 'Usage: randomtext.py filename [# of words] [prefix length]'
    else: 
        process_file(filename, order)
        markov_text(n)


if __name__ == '__main__':
    main(*sys.argv)

