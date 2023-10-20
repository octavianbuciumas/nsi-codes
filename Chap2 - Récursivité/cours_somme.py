def somme(n):
    """ int -> int """
    if n == 1:
        return 1
    else:
        Sprime = somme(n - 1) # appel récursif
                              # on fait appel à la fonction
                              # dans le code du corps de la fonction
        return Sprime + n