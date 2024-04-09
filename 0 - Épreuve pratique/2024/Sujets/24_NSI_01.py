def taille(arbre, lettre):
    if arbre[lettre] == ['', '']:
        return 1
    else:
        if arbre[lettre][1] == '':
            return 1 + taille(arbre, arbre[lettre][0])
        elif arbre[lettre][
            0] == '':
            return 1 + taille(arbre, arbre[lettre][1])
        else:
            return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = tab[i]

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(k+1, N):
            if tab[i] < tab[imin]:
                imin = i
        echange(tab,k, imin)
