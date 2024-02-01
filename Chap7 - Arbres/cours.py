from ArbreBinaire import ArbreBinaire


def parcours_stocke(a, l):
    if a.est_vide():
        pass
    else:
        parcours_stocke(a.gauche(), l):
        l.append(a.etiquette())
        parcours_stocke(a.gauche(), l):


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

