def solution(s):
    a = ''
    for char in s:
        if char.islower():
            a += char
        else:
            a += ' ' + char
    return a


"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""