# Auteur : Kévin 


def indices_maxi(tab):
    """ [int] -> (int,[int])
    Renvoie la valeur ainsi que les indices de l'élement maximal d'une
    liste"""
    liste_maxi = []
    elem_max = tab[0]
    for elem in tab:
        if elem > elem_max:
            elem_max = elem
    for i in range(len(tab)):
        if tab[i] == elem_max:
            liste_maxi.append(i)
    return (elem_max,liste_maxi)

def positif(pile):
    """ [int] -> [int]
    Renvoie la liste des élements positifs d'une liste."""
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
    if x >= 0:
        pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1

