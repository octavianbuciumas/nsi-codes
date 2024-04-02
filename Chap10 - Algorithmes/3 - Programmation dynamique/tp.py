def fibomem(n, memo):
    """ int, {int:int} -> int
    Calcule le terme d'indice n de la suite de Fibonacci
    memo est un dictionnaire où les calculs intermédaires ont été stockés """
    if n in memo: 
        return ...
    if n <= 1:
        memo[n] = n
        return memo[n]
    else:
        inter1 = ...
        inter2 = ...
        memo[n] = ...
        return ...

def fibodyn(n):
    """ int -> int
    Calcule le terme d'indice n de la suite de Fibonacci """
    pass
    T = [None]*(n + 1) 
    T[0], T[1] = ..., ...
    for i in range(..., ...):
        T[i] = ...
    return ...

def nombre_chemins(n, m):
    """ int, int -> int
    Renvoie le nombre de chemins de (haut, gauche) à (bas, droite) dans une grille n×m """
    pass

def nombre_chemins_dyn(n, m):
    """ int, int -> int
    Renvoie le nombre de chemins de (haut, gauche) à (bas, droite) dans une grille n×m """
    T = [ [None for j in range(m)] for i in range(n)]
    for i in range(n):
        T[...][...] = 1
    for j in range(m):
        ...
    for i in range(1, n):
        for j in range(1, m):
            T[i][j] = ...
    return ...

def rendu_monnaie_glouton(systeme, montant):
    """ [int], int -> int
    Renvoie le nombre de pièces minimales à utiliser pour rendre
    le montant avec les pièces de systeme """
    nb_pieces = 0
    while montant > 0:
        # On cherche la plus grande pièce à rendre
        plus_grande = systeme[0]
        for p in systeme:
            if ...:
                ...
        # on rend la pièce trouvée 
        montant = ...
        nb_pieces = ...
    return nb_pieces

def rendu_monnaie_rec(systeme, montant):
    """ [int], int -> int
    montant >= 0
    Renvoie le nombre de pièces minimales à utiliser pour rendre
le montant avec les pièces de systeme """
    if ...:
        ...
    else:
        # on détermine de manière récursive le nombre minimum
        # de pièce à rendre pour rendre montant - p, ou p est
        # une des pièces du systeme.
        liste = []
        for p in systeme:
            ... # à compléter
        # On renvoie le minimum de la liste, plus 1.
        ...

def rendu_monnaie_dyn(systeme, montant):
    """ [int], int -> int
    Renvoie le nombre minimum de pièces de systeme à utiliser pour rendre montant """
   # dans le pire des cas on rend i avec i pièces de 1
   T = [... for i in range(montant + 1)] 
   for i in range(montant + 1):
       for p in systeme:
           if i + p <= montant and ...:
               ...
   return ...

def rendu_monnaie(systeme, montant):
    """ [int], int -> [int]
    Trouve le meilleur rendu de monnaie dans systeme """
    pass

