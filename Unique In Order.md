# Unique In Order

Implement the function unique_in_order which takes as argument a sequence and returns a list
of items without any elements with the same value next to each other and preserving the
original order of elements.

For example:
```
unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD')
unique_in_order([1,2,2,3,3])
```
unique_in_order(iterable) # returns:
```
['A', 'B', 'C', 'D', 'A', 'B']
['A', 'B', 'C', 'c', 'A', 'D']
[1,2,3]
```

**Solution:**
```python
def unique_in_order(iterable):
    b = []
    for i in range(len(iterable)):
        if len(iterable) == 1:
            b.append(iterable[i])
            break
        elif iterable[i] == iterable[i - 1] and b.count(iterable[i]) == 0:
            b.append(iterable[i])
        elif iterable[i] != iterable[i - 1]:
            b.append(iterable[i])
    return b
```
    
    
Codewars source [link](https://www.codewars.com/kata/54e6533c92449cc251001667/train/python)
