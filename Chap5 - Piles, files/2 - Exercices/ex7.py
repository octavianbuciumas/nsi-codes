from ds import *

p = creer_pile_vide()
empiler(p, 8)
empiler(p, 2)
empiler(p, 5)
empiler(p, 10)


def hauteur(pile):
    h = 0
    aux  = creer_pile_vide()
    while not est_pile_vide(pile):
        empiler(aux, depiler(pile))
        h +=1
    while not est_pile_vide(aux):
        empiler(pile, depiler(aux))
    return h

def max_pile(p, i):
    position_max = 1
    valeur_max = depiler(p)
    # il faut utiliser une Pile auxiliaire
    p_aux = creer_pile_vide()
    empiler(p_aux, valeur_max)
    pos = 1
    while pos < i and not est_pile_vide(p):
        pos += 1
        elt = depiler(p)
        if valeur_max < elt:
            valeur_max = elt
            position_max = pos
        empiler(p_aux, elt)
    while not est_pile_vide(p_aux):
        empiler(p, depiler(p_aux))
    return position_max
    
def retourner(p, i):
    if est_pile_vide(p) or i > n:
        raise IndexError("pb d'arguments")
    n = hauteur(p)
    f = creer_file_vide()
    for _ in range(min(i, n)):
        enfiler(f, depiler(p))
    while not est_file_vide(f):
        empiler(p, defiler(f))
    return p
    
def tri_crepe(p):
    n = hauteur(p)
    for j in range(4, 1, -1):
        position_max = max_pile(p, j)
        retourner(p, position_max)
        retourner(p, j)
    affiche_pile(p)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    