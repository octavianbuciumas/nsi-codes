# Auteur : David

# Attention : fonction recherche probablement incorrecte
def recherche(elt,tab):
    """
    Écrire une fonction recherche qui prend en paramètres un nombre entier elt et un
    tableau tab de nombres entiers, et qui renvoie l’indice de la première occurrence de
    elt dans tab si elt est dans tab et -1 sinon"""
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
        else:
            return -1


def insere(a, tab):
    """ Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau. """
    l =list(tab)
    l.append(a)
    i = len(l) - 2
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l
