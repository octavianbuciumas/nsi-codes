def f(n):
    """ int -> int """
    print(f"Appel f({n})")
    if n == 1:
        print(f"f(1) renvoie 1")
        return 1
    else:
        res = f(n - 1) + f(n - 1)
        print(f"f({n}) renvoie {res}")
        return res
