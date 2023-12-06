from ds import *

f = creer_file_vide()
enfiler(f,'jaune')
enfiler(f,'rouge')
enfiler(f,'jaune')
enfiler(f,'vert')
enfiler(f,'rouge')

def taille_file(f):
    f2 = creer_file_vide()
    taille = 0
    while not est_file_vide(f):
        enfiler(f2,defiler(f))
        taille+=1
    while not est_file_vide(f2):
        enfiler(f, defiler(f2))
    return taille

def former_pile(f):
    p= creer_pile_vide()
    p_aux = creer_pile_vide()
    while not est_file_vide(f):
        empiler(p_aux,defiler(f))
    while not est_pile_vide(p_aux):
        empiler(p,depiler(p_aux))
    return p
 
def nb_elements(file, elt):
    f_aux = creer_file_vide()
    compteur = 0
    while not est_file_vide(f):
        a = defiler(file)
        if a == elt:
            compteur = compteur + 1
        enfiler(f_aux, a)
    while not est_file_vide(f_aux):
        enfiler(file, defiler(f_aux))
    return compteur

def verifier_contenu(f, nb_rouge, nb_vert, nb_jaune):
    return nb_elements(f, "rouge") <= nb_rouge\
           and nb_elements(f, "vert") <= nb_vert\
           and nb_elements(f, "jaune") <= nb_jaune


















