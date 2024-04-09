def fibo(n):
    """ int -> int """
    if n <= 1:
        return n
    else:
        return fibo(n - 2) + fibo(n - 1)

def fibomem(n, memo):
    """ int, {int:int} -> int
    Calcule le terme d'indice n de la suite de Fibonacci
    memo est un dictionnaire où les calculs intermédaires ont été stockés """
    if n in memo: 
        return memo[n]
    if n <= 1:
        memo[n] = n
        return memo[n]
    else:
        inter1 = fibomem(n - 1, memo) 
        inter2 = fibomem(n - 2, memo)
        memo[n] = inter1 + inter2
        return memo[n]

def fibodyn(n):
    """ int -> int
    Calcule le terme d'indice n de la suite de Fibonacci """
    if n <= 1:
        return n
    T = [None]*(n + 1) 
    T[0], T[1] = 0, 1
    for i in range(2, n + 1):
        T[i] = T[i - 1] + T[i - 2]
    return T[n]

def nbc(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return nbc(n - 1, m) + nbc(n, m - 1)

def nombre_chemins(n, m,dicti):
    """ int, int, {(int, int):int} -> int
    Renvoie le nombre de chemins de (haut, gauche)
    à (bas, droite) dans une grille n×m
    en stockant dans dicti les calculs effectués """
    if (n, m) in dicti:
        return dicti[(n,m)]
    if n == 1 or m == 1:
        dicti[(n,m)] = 1
        return dicti[(n, m)]
    else:
        dicti[(n - 1, m)] = nombre_chemins(n - 1, m, dicti)
        dicti[(n, m - 1)] =  nombre_chemins(n, m  - 1, dicti)
        dicti[(n,m)] = dicti[(n-1,m)] + dicti[(n,m-1)]
        return dicti[(n, m)]

def nombre_chemins_dyn(n, m):
    """ int, int -> int
    Renvoie le nombre de chemins de (haut, gauche) à (bas, droite) dans une grille n×m """
    T = [ [None for j in range(m)] for i in range(n)]
    for i in range(n):
        T[i][0] = 1
    for j in range(m):
        T[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            T[i][j] = T[i - 1][j] + T[i][j - 1]
    return T[n-1][m-1]

def rendu_monnaie_glouton(systeme, montant):
    """ [int], int -> int
    Renvoie le nombre de pièces minimales à utiliser pour rendre
    le montant avec les pièces de systeme """
    nb_pieces = 0
    while montant > 0:
        # On cherche la plus grande pièce à rendre
        plus_grande = systeme[0]
        for p in systeme:
            if p <= montant and p > plus_grande:
                plus_grande = p
        # on rend la pièce trouvée
        # print(plus_grande)
        montant = montant - plus_grande
        nb_pieces += 1
    return nb_pieces

def rendu_monnaie_rec(systeme, montant, memo):
    """ [int], int, {int:int} -> int
    montant >= 0
    Renvoie le nombre de pièces minimales à utiliser pour rendre
le montant avec les pièces de systeme """
    if montant in memo:
        return memo[montant]
    if montant == 0:
        memo[montant] = 0
        return 0
    else:
        # on détermine de manière récursive le nombre minimum
        # de pièce à rendre pour rendre montant - p, ou p est
        # une des pièces du systeme.
        liste = []
        for p in systeme:
            if montant - p >= 0:
                res = rendu_monnaie_rec(systeme, montant - p, memo)
                liste.append(res)
        # On renvoie le minimum de la liste, plus 1.
        # dans le cas général : avant de renvoyer la réponse
        # on la stocke dans mémo
        memo[montant] = min(liste) + 1
        return memo[montant]

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

