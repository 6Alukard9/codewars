iterable = 'AAAABBBCCDAABBB'
# iterable = 'ABBCcAD'
# iterable = [1,2,2,3,3]


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

