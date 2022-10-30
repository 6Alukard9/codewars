def pig_it(text):
    text = text.split()
    b = ''
    for i in text:
        if i.isascii() and not i.isalnum():
            b += i
        else:
            i = i[1:] + i[0] + 'ay '
            b += i
    return b.strip()


"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""