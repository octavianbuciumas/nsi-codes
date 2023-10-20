def f(x, a=3, l=None):
    if l is None:
        l = []
    l.append(1)
    a += 1
    return x + 1, l, a
