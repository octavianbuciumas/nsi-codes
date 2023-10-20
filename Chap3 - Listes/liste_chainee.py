class Maillon:
    """ Un maillon d'une liste chainée. """
    def __init__(self, v, s):
        """ int, Maillon -> None """
        self.valeur = v
        self.suivant = s

maillon4 = Maillon(1, None)
maillon3 = Maillon(42, maillon4)
maillon2 = Maillon(8, maillon3)
maillon1 = Maillon(3, maillon2)

print(maillon2.valeur)
print(maillon2.suivant)
print(maillon2.suivant.valeur)

m = Maillon(1, None)
m = Maillon(42, m)
m = Maillon(8, m)
m = Maillon(3, m)
# encore plus court :
# m = Maillon(3, Maillon(8, Maillon(42, Maillon(1, None))))

print(m.valeur)
print(m.suivant)
print(m.suivant.valeur)

m1 = None # liste vide est représentée par None
m2 = Maillon(-1, None)
m3 = Maillon(5, Maillon(6, Maillon(9, Maillon(-1, None))))
m4 = Maillon(-5, Maillon(9, Maillon(13, None)))

print(m4.valeur)
print(m4.suivant.valeur)
print(m4.suivant.suivant.valeur)
# print(m4.suivant.suivant.suivant.valeur)

#  maillon2.suivant is maillon3
# renvoie True : maillon2.suivant et maillon3
# font tous les deux référence à la même adresse
# mémoire
#
# maillon3 is Maillon(42, maillon4)
# renvoie False
# car Maillon(42, maillon4) créé un nouveau
# maillon, indépendant de maillon3.

def creer_vide():
    return None

def est_vide(m):
    return m is None
    # return m == None

def tete(m):
    # m est non vide
    return m.valeur

def queue(m):
    """Maillon -> Maillon"""
    # m est non vide
    return m.suivant
    
def ajoute(m, e):
    return Maillon(e, m)
    
def affiche_i(m):
    """ Affiche les valeurs de la chaîne dont le premier maillon est m """
    maillon_courant = m
    while not est_vide(maillon_courant):
        print(tete(maillon_courant), end=' - ')
        maillon_courant = queue(maillon_courant)
    print("x")
    
affiche = affiche_i
        
# remarque : l'instruction
# maillon5 = ajoute(maillon1, 1)
# créé un nouveau maillon dont la valeur est 1
# est l'attribut suivant est maillon1
# Ainsi, affiche(maillon5) affiche
# 1 - 3 - 8 - 42 - 1
# Attention, si on exécute
# maillon4.suivant = maillon5
# on relie le dernier maillon de la chaine
# au premier. On obtient alors une liste
# cyclique et l'intruction affiche(maillon5)
# ne termine pas.

def longueur(m):
    # version itérative
    maillon_courant = m
    cpt = 0
    while maillon_courant != None:
        cpt += 1
        maillon_courant = maillon_courant.suivant        
    return cpt

def element(m, i):
    # version itérative
    maillon_courant = m
    k = 0 # indice du maillon courant
    while k != i:
        maillon_courant = maillon_courant.suivant
        k += 1
    return maillon_courant.valeur 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    












    
    
    
    
    
    
    
    












































