def rotate_word(a,b):
    """Rotates a word by n places.

       a : string
       b : integer

       Returns: string"""
 
    final = ""
    for letter in a:
        ordletter = ord(letter)
        print 
        if letter.isupper():
            upperend = 91
            lowerend = 65
        elif letter.islower(): 
            upperend = 123
            lowerend = 97
     
        new_ordletter = (ordletter + b) % upperend
        if new_ordletter < lowerend :
               new_ordletter += lowerend
               final += chr(new_ordletter)
        else:
            final += chr (new_ordletter)

    return final
               
print rotate_word ('FPENOOYR',13)

       
