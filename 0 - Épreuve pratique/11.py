  ## sujet 11 Alexandre

liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à déterminer où placer la valeur à ranger
        j = i
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j-1
        tab[j] = valeur_insertion
        
def convertir(tab):
    """List => int"""
    """
    tab est un tableau d'entiers, dont les éléments sont 0 ou 1,
    et représentant un entier écrit en binaire. 
    Renvoie l'écriture décimale de l'entier positif dont la 
    représentation binaire est donnée par le tableau tab
     """

    val = 0
    inv_tab = [tab[i] for i in range(len(tab)-1,-1,-1)]
    for i in range (len(inv_tab)):
        if inv_tab[i] == 1:
            val += 2**i
    return val


print(liste)
tri_insertion(liste)
print(liste)
