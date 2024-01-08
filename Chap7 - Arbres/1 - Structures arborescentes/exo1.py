def f(x):
    """int -> None"""
    if x <= 1:
        print("*")
    else:
        f(x - 1)
        print("*"*x)
        f(x - 1)

def g(x):
    """ int -> Nonetype """
    if x <= 1:
        print("*")
    else:
        g(x - 1)
        g(x - 2)
        print("*"*x)
