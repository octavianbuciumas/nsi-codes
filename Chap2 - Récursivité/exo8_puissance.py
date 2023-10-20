def pow(x, n):
    """ float, int -> float
    Calcule x**n """
    if n == 0:
        return 1
    else:
        return pow(x, n -1)*x
    
def pow_fast(x, n):
    """ int, int -> int
    Détermine x^n à l'aide de l'algorithme d'exponentiation rapide. """
    if n == 0:
        return 1
    else:
        p = pow_fast(x, n//2)
        if n%2 == 0:
            return p*p
        else:
            return p*p*x
