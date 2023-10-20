def f(n):
    """ int -> int """
    if n == 1:
        print(f"f(1) renvoie 1")
        return 1
    else:
        print(f"Appel récursif de f({n - 1})")
        res = f(n - 1) + 2**n
        print(f"f({n}) renvoie {res}")
        return res
