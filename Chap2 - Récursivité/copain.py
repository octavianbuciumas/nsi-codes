PILIERS = ['A', 'B', 'C']

def autre(d, a):
    for p in PILIERS:
        if p not in {d, a}:
            return p
    return None

def hanoi(n, a, c):
    if n <= 0:
        pass
    else:
        b = autre(a, c)
        hanoi(n - 1, a, b)
        print(f"{a} --> {c}")
        hanoi(n - 1, b, c)
        
mathieu = lambda a, c : hanoi(3, a, c)
hanoi4 = lambda a, c : hanoi(4, a, c)