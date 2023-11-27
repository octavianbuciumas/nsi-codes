from ds import *

p = creer_pile_vide()
empiler(p, 12)
empiler(p, 14)

def sommet(p):
    if not est_pile_vide(p):
        e = depiler(p)
        empiler(p,e)
        return e

def sommet2(p):
    # attention : ne fonctionne pas comme souhaité !
    p_aux = p
    print(id(p_aux))
    print(id(p))
    print(p_aux is p)
    c = depiler(p_aux)
    return c

f = creer_file_vide()
enfiler(f, 22)
enfiler(f, 19)
enfiler(f, 7)
enfiler(f, 8)
enfiler(f, 14)
enfiler(f, 12)

def tete(f):
    """ File -> int """
    e = defiler(f)
    f_aux = creer_file_vide()
    enfiler(f_aux, e)
    while not est_file_vide(f):
        courant = defiler(f)
        enfiler(f_aux, courant)
    while not est_file_vide(f_aux):
        enfiler(f, defiler(f_aux))
    return e
        












        
        
        
        
        