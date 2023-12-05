from ds import *

p = creer_pile_vide()
empiler(p, 4)
empiler(p, 2)
empiler(p, 5)
empiler(p, 8)


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
    # à finir !
    
    
    
    
    
    
    