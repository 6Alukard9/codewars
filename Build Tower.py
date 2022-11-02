def tower_builder(n_floors):
    a = []
    b = 1
    for i in range(n_floors):
        c = ' ' * (n_floors - 1) + '*' * b + ' ' * (n_floors - 1)
        b += 2
        n_floors -= 1
        a.append(c)
    return (a)


"""
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive
integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
Go challenge Build Tower Advanced once you have finished this :)


"""