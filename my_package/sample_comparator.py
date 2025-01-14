from functools import reduce
def greatest(*a):
    return reduce(lambda x, y: x if x > y else y, a)
def least(*a):
    return reduce(lambda x, y: x if x < y else y, a)

