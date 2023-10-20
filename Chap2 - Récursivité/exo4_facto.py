def f(n):
    if n == 0:
        return 1
    if n > 1:
        return n*f(n - 1)