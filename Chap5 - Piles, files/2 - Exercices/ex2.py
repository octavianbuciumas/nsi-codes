from ds import *

def tamis(p):
    """ Pile -> Pile, Pile """
    p_pair = creer_pile_vide()
    p_impair = creer_pile_vide()
    while not est_pile_vide(p):
        i = depiler(p)
        if i%2 == 0:
            empiler(p_pair, i)
        else:
            empiler(p_impair, i)
    return p_pair, p_impair
    
p = creer_pile_vide()
empiler(p, 1)
empiler(p, 2)
empiler(p, 3)
empiler(p, 1)

def maximum(p):
    """Pile -> Int"""
    max = depiler(p)
    while not est_pile_vide(p):
        c = depiler(p)
        if c > max:
            max = c
    return max

def retourne(p):
    """ Pile -> Pile """
    # la pile initiale est détruite
    print("p", id(p))
    pP = creer_pile_vide()
    print("pP", id(pP))
    while not est_pile_vide(p):
        empiler(pP,depiler(p))
    # p = pP # ne fonctionne pas
    # print("p", id(p)) # pas le même id qu'initialement
    # p est une nouvelle pile
    return pP

def retourne2(p):
    """ Pile -> Nonetype """
    # la pile initiale n'est pas détruite
    f_aux = creer_file_vide()
    while not est_pile_vide(p):
        enfiler(f_aux, depiler(p))
    while not est_file_vide(f_aux):
        empiler(p, defiler(f_aux))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

















