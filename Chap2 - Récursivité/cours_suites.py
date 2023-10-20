def u(n):
    if n == 1:
        return 7
    else:
        uprime = u(n - 1)
        return uprime + 5
    
def v(n):
    if n == 1:
        return 6
    else:
        vprime = v(n - 1)
        return vprime - 2 