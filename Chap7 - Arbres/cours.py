from ArbreBinaire import ArbreBinaire


def parcours_stocke(a, l):
    if a.est_vide():
        pass
    else:
        parcours_stocke(a.gauche(), l)
        l.append(a.etiquette())
        parcours_stocke(a.droit(), l)


a = ArbreBinaire()
a.ajouter_depuis_tableau([5, 2, 9, None, None ,7, 42])

# Utilisation de parcours stocke
l = []
print(parcours_stocke(a, l)) # -> None
print(l) # -> [5, 2, 9, 7, 42]
print(parcours_stocke(a, l)) # -> None
print(l) # -> [5, 2, 9, 7, 42, 5, 2, 9, 7, 42]
# Attention parcours_stocke ne renvoie rien mais est exécutée
# pour son effet de bord : modifier la liste l en lui ajoutant
# les valeurs de a dans l'ordre infixe.

def p1(a, l, m, M):
    """ ArbreBinaire, list, int, int -> [int]
    Stocke les étiquettes e de a vérifiant m < e < M
    dans la liste l (parcours infixe) """
    if a.est_vide():
        pass
    else:
        p1(a.gauche(), l, m, M)
        if m < a.etiquette() < M:
            l.append(a.etiquette())
        p1(a.droit(), l, m, M)

def p2(a, l, m, M):
    """ ArbreBinaire, list, int, int -> [int] 
    Stocke les étiquettes e de a vérifiant m < e < M
    dans la liste l (parcours infixe) """
    if a.est_vide():
        pass
    else:
        if a.etiquette() <= m:
            p2(a.droit(), l, m, M)
        elif a.etiquette() >= M:
            p2(a.gauche(), l, m, M)
        else:
            p2(a.gauche(), l, m, M)
            l.append(a.etiquette())
            p2(a.droit(), l, m, M)
            
a = ArbreBinaire()
a.ajouter_depuis_tableau([5, 3, 7, 1, 4, None, 9, None, 2, None, 4, None, 9])
l = []
print(p1(a, l, 3, 6))
print(l)
