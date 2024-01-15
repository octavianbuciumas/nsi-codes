from ds import *
from tp import *

a1 = Arbre(0,
           Arbre(-5,
                 Arbre(-3, None, None),
                 Arbre(1, None, None)),
           Arbre(4,
                 Arbre(-3, None, None),
                 Arbre(5, None, None)))

a2 = Arbre(-1,
           Arbre(5,
                 Arbre(-2,
                       Arbre(4, None, None),
                       Arbre(-3, None, None)),
                 None),
                 Arbre(-1,
                       None,
                       Arbre(-5,
                             Arbre(6, None, None),
                             None)))

a3 = Arbre(3,
           None,
           Arbre(4,
                 Arbre(-3,
                       None,
                       Arbre(2, None, None)),
                 None))

a4 = Arbre(5,
           Arbre(2,
                 Arbre(-3,
                       Arbre(-5, None, None),
                       None),
                 None),
           Arbre(-4,
                 None,
                 Arbre(8,
                       Arbre(6, None, None),
                       None)))

def est_parfait(a):
    if est_vide(a):
        return True
    elif est_vide(gauche(a)) and not est_vide(droit(a)):
        return False
    elif est_vide(droit(a)) and not est_vide(gauche(a)):
        return False
    else:
        est_parfait_sag = est_parfait(gauche(a))
        est_parfait_sad = est_parfait(droit(a))
        return est_parfait_sag and est_parfait_sad

def est_peigne(a):
    if est_vide(a):
        return True
    elif est_peigne(gauche(a)) and  est_vide(droit(a)):
        return True
    elif est_peigne(droit(a)) and est_vide(gauche(a)):
        return True
    else:
        return False

def nb_feuilles(a):
    if est_feuille(a):
        return 1
    elif est_vide(gauche(a)):
        return nb_feuilles(droit(a))
    elif est_vide(droit(a)):
        return nb_feuilles(gauche(a))
    else:
        return nb_feuilles(gauche(a)) + nb_feuilles(droit(a))
    
    
    
    
    
    
    

