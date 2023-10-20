from Liste import creer_vide, est_vide, tete, queue, ajoute, affiche

l = creer_vide()
l = ajoute(l, 0)
l = ajoute(l, 1)
ajoute(l, 2) # ne modifie pas la liste l

l1 = creer_vide()

l2 = creer_vide()
l2 = ajoute(l2, -1)

l3 = creer_vide()
l3 = ajoute(l3, -1)
l3 = ajoute(l3, 9)
l3 = ajoute(l3, 6)
l3 = ajoute(l3, 5)

l4 = creer_vide()
l4 = ajoute(l4, 9)
l4 = ajoute(l4, -5)
l4 = ajoute(l4, 9)
l4 = ajoute(l4, 4)
l4 = ajoute(l4, 9)
l4 = ajoute(l4, -5)

def est_singleton(l):
    """ Liste -> bool """
    return not est_vide(l) and est_vide(queue(l))

def singleton(e):
    """ int -> Liste """
    l = creer_vide()
    l = ajoute(l, e)
    return l

def nombres(n):
    """ int -> Liste
    Renvoie la liste (n, n-1, n-2, ..., 3, 2, 1) """
    # cas de base
    if n == 1:
        return singleton(1)
    # cas général
    else:
        # un appel récursif
        avant = nombres(n-1)
        return ajoute(avant, n)
        
def nombresII_aux(n, i):
    """ int, int -> Liste
    renvoie la liste (i, i + 1, i + 2, ..., n-1, n)"""
    # cas de base
    if i == n:
        return singleton(n)
    else:
        # appel récursif
        avant = nombresII_aux(n, i + 1)
        return ajoute(avant, i)
        
def nombresII(n):
    return nombresII_aux(n, 1)
        
        
def longueur(l):
    """ Liste -> int
    nombre  d'éléments de l """
    if est_vide(l):
        return 0
    else:
        avant = longueur(queue(l))
        return avant + 1
    
def appartient(l, e):
    """ Liste, int -> bool
    Détermine si l'élément e appartient à la liste l """
    # cas de base
    if est_vide(l):
        return False
    # cas général
    else:
        # appel récursif
        avant = appartient(queue(l) , e)
        # True ssi e appartient à queue(l)
        if e == tete(l):
            return True
        else:
            return avant

def que_des_pairs(l):
    # exemples
    # () -> ()
    # (1) -> ()
    # (2) -> (2)
    # (1, 4, 15, 6, 9) -> (4, 6)
    # (42, 3, 9, 4, 1, 4, 2) -> (42, 4, 4, 2)
    # cas de base
    if est_vide(l):
        # return l
        return creer_vide()
    # le cas général
    else:
        # appel récursif
        avant = que_des_pairs(queue(l))
        if tete(l)%2 == 0:
            return ajoute(avant, tete(l))
        else:
            return avant
        
def nombre_occurrences(l, e):
    """ Liste, int -> int
    Compte le nombre d'occurrences de e dans l """
    if est_vide(l):
        return 0
    else:
        navant = nombre_occurrences(queue(l), e)
        if tete(l) == e:
            return navant + 1
        else:
            return navant

def somme(l):
    """ liste -> int
    l est supposée non vide
    Calcule la somme des éléments de la liste l """
    if est_singleton(l):
        # cas de base
        return tete(l)
    else:
        # cas général
        avant = somme(queue(l))
        return tete(l) + avant

def maximum2(a, b):
    """ Renvoie le maximum des éléments a et b """
    if a < b:
        return b
    else:
        return a
    
def maximum(l):
    """ liste -> int
    liste est non vide
    Renvoie le plus grand élément de la liste """
    if est_singleton(l):
        # cas de base
        return tete(l)
    else:
        # Appel récursif
        avant = maximum(queue(l))
        # le plus grand élément dans la queue de l
        # return maximum2(avant, tete(l))
        if avant > tete(l):
            return avant
        else:
            return tete(l)
    
def supprime(l, e):
    """ Liste, int -> Liste
    Supprime la première occurrence de e la liste l """
    if est_singleton(l):
        # on suppose que e appartient à l
        return creer_vide()
    else:
        if tete(l) == e:
            return queue(l)
        avant = supprime(queue(l), e)
        return ajoute(avant, tete(l))
    
# CHAPITRE III : TP 1 : LISTES ET
# ALGORITHMES RÉCURSIFS
# SECTION 3.2 : insérer dans une liste

def inserer(l, e, i):
    """ Liste, int, int -> Liste
     Insère l'élément e à l'indice i dans l """
    if i == 0:
        return ajoute(l, e)
    else:
        # l = (8, 3, 4) et e = 42 et i = 2
        avant = insérer(queue(l), e, i - 1)
        # avant = (3, 42, 4)
        reponse = ajoute(avant, tete(l))
        # reponse = (8, 3, 42, 4)
        return reponse
    
def concatene(l1, l2):
    if est_vide(l1):
        return l2
    else:
        avant = concatene(queue(l1), l2)
        return ajoute(avant, tete(l1))


# 3.4 : division de listes
#

def est_2ton(l):
    """ True ssi la liste est constituée
    de 2 éléments """
    if est_vide(l):
        return False
    elif est_singleton(l):
        return False
    elif est_singleton(queue(l)):
        return True
    else:
        return False

def divise(l):
# def divise(l: Liste) -> Liste, Liste:
    """" Liste -> Liste, Liste """
    if est_vide(l):
        l1 = creer_vide()
        l2 = creer_vide()
        return l1, l2
    elif est_singleton(l):
        l1 = l
        l2 = creer_vide()
        return l1, l2
    else:
        l1, l2 = divise(queue(queue(l)))
        l1 = ajoute(l1, tete(l))
        l2 = ajoute(l2, tete(queue(l)))
        return l1, l2
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














    
    
    
    
    
    
    
    

















    
    
    
    
        
        
        
        
        
        
        

















