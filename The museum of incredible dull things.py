numbers = [1, 2, 5, 1, 1]


def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a
