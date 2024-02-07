# Auteur : Samy

import random

# EXERCICE 1

def lancer(n):
    """ int --> List
    Renvoie un tableau de type list de n entiers
    obtenus aléatoirement entre 1 et 6 (1 et 6 inclus)
    """
    l = []
    for i in range(n):
        dé = random.randint(1,6)
        l.append(dé)
    return l


def paire_6(tab):
    """ List --> List
    Renvoie un booléen égal à True si le nombre
    de 6 est supérieur ou égal à 2, False sinon.
    """
    nbr_6 = 0
    nbr_2 = 0
    for val in tab:
        if val == 6:
            nbr_6 += 1
        if val == 2:
            nbr_2 += 1
    return nbr_6 >= 2




# EXERCICE 2

def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le négatif de l'image sous la forme
    d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
    return L

def binaire(image, seuil):
    '''renvoie une image binarisée de l'image sous la forme
    d'une liste de listes contenant des 0 si la valeur
    du pixel est strictement inférieure au seuil
    et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil :
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L
