def nombre_occurrences_aux(tab, e, i):
    """ [int], int, int -> int
    Renvoie le nombre d'occurrences de e parmi les i premiers éléments """
    # Cas de base
    if i == 0:
        return 0
    # Cas général
    else:
        # appel récursif
        nprime = nombre_occurrences_aux(tab, e, i - 1)
        # nprime est le nombre d'occurrences de e dans les
        # i - 1 premiers élémets du tableau
        # le ième élément du tableau est celui recherché
        if tab[i - 1] == e:
            nprime += 1
        return nprime
    
def nombre_occurrences(tab, e):
    """ [int], int -> int
    Compte le nombre d'occurrences de e dans tab """
    return nombre_occurrences_aux(tab, e, len(tab))

# nombre_occurrences_aux est récursive car elle s'appelle elle-meme
# ligne 14

# nombre_occurrences n'est pas récursive, bien qu'elle fasse appel
# a une fonction récursive (qui n'est pas elle-même !). 
