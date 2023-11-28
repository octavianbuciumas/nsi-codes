from ds import *

def est_bien_parenthesee(chaine):
    """ str -> bool """
    p = creer_pile_vide()
    # parcourt par indice
    # for i in range(len(chaine)):
    #    c = chaine[i]
    # on parcourt chaine par valeur car on n'a pas besoin
    # des indices
    for c in chaine:
        if est_pile_vide(p) and c==')':
            return False
        if c==')':
            # la pile n'est pas vide
            depiler(p)
        if c=='(':
            empiler(p,'(')
    if est_pile_vide(p):
        return True
    return False

def int2strbin(x, n):
    debut = bin(x)[2:]
    return "0"*(n - len(debut)) + debut
    
def expression(x, n):
    """ int, int -> str """
    pass
    
def liste_bien_parenthesee(n):
    """ n -> [str] """
    pass
    
    
    
    
    
    
    
    
    
    
    