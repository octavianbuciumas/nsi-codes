def fibomem(n, memo):
    """ int -> int
    Renvoie le terme d'indice n de la suite de Fibonacci """
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
    T = [None]*(n + 1) 
    T[0], T[1] = 0, 1
    for i in range(2, n + 1):
        T[i] = T[i - 1] + T[i - 2]
    return T[n]

def nombre_chemins(n, m):
    """ int, int -> int
    Renvoie le nombre de chemins de (haut, gauche) à (bas, droite) dans une grille n×m """
    if n == 1 or m == 1:
        return 1
    else:
        return nombre_chemins(n - 1, m) + nombre_chemins(n, m - 1)

def nombre_chemins_dyn(n, m):
    """ int, int -> int
    Renvoie le nombre de chemins de (haut, gauche) à (bas, droite)
    dans une grille n×m """
    T = [ [None for j in range(m)] for i in range(n)]
    for i in range(n):
        T[i][0] = 1
    for j in range(m):
        T[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            T[i][j] = T[i - 1][j] + T[i][j - 1]
    return T[n - 1][m - 1]

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
        montant -= plus_grande
        nb_pieces += 1
    return nb_pieces

def rendu_monnaie_rec(systeme, montant):
    """ [int], int -> int
    Renvoie le nombre de pièces minimales à utiliser pour rendre
    le montant avec les pièces de systeme """
    if montant == 0:
        return 0
    else:
        rendu = [rendu_monnaie_rec(systeme, montant - p)
                 for p in systeme
                 if montant - p >= 0]
        return min(rendu) + 1

def rendu_monnaie_dyn(systeme, montant):
    """ [int], int -> int
    Renvoie le nombre minimum de pièces de systeme à utiliser pour rendre montant """
    # dans le pire des cas on rend i avec i pièces de 1
    T = [i for i in range(montant + 1)] 
    for i in range(montant + 1):
        for p in systeme:
            if i + p <= montant and T[i + p] > T[i] + 1:
                T[i + p] = T[i] + 1
    return T[montant]

def rendu_monnaie(systeme, montant):
    """ [int], int -> [int]
    Trouve le meilleur rendu de monnaie dans systeme """
    T = [([1]*i) for i in range(montant + 1)] 
    for i in range(montant + 1):
        for p in systeme:
            if i + p <= montant and len(T[i]) + 1 < len(T[i + p]):
                # on ajoute p à la fin de la liste T[i]
                # on n'utilise pas la méthode append qui modifierait
                # la liste T[i] : l1 + l2 créé une nouvelle liste
                T[i + p] = T[i] + [p]
    return T[montant]

