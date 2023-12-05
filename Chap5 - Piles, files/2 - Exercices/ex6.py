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