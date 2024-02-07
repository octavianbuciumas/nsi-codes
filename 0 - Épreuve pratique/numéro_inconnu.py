# Auteur : Zacharie

#exercice 1
def maxliste(tab):
    """ list -> Int """
    """ Renvoie le plus grand élément de tab """
    n = len(tab)
    valeur = tab[0]
    for i in range(n):
        if tab[i] > valeur:
            valeur = tab[i]
    return valeur


# Exercice 2
class Pile:
    """
    Classe definissant une pile
    """
    def __init__(self):
        self.valeurs = []

        def est_vide(self):
            """
            Renvoie True si la pile est vide, False sinon
            """
            return self.valeurs == []

        def empiler(self, c):
            """
            Place l'element c au sommet de la pile
            """
            self.valeurs.append(c)
            
    def depiler(self):
        """
        Supprime l'element place au sommet de la pile, a condition qu'elle soit non vide
        """
        if self.est_vide() == False:
            self.valeurs.pop()
        

def parenthesage(ch):
    """
    Str -> Bool
    Renvoie True si la chaine ch est bien parenthesee et False sinon
    """
    p = Pile()
    for c in ch:
        if c == '(':
            p.empiler(c)
        elif c == ')':
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()

assert parenthesage('') == True
assert parenthesage('()') == True
assert parenthesage(')(') == False
assert parenthesage('((())())()') == True




class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None


def taille(a):
    """ Arbre -> Int"""
    """Revoie la taille de l'arbre a"""
    if a.fg == None and a.fd == None:
        return 1
    elif a.fg == None:
        return taille(a.fd) + 1
    elif a.fd == None:
        return taille(a.fg) + 1
    else:
        return taille(a.fg) + taille(a.fd) + 1

def hauteur(a):
    if a.fg == None and a.fd == None:
        return 1
    elif a.fg == None:
        return hauteur(a.fd) + 1
    elif a.fd == None:
        return hauteur(a.fg) + 1
    else:
        g = hauteur(a.fg)
        d = hauteur(a.fd)
        if g > d:
            return g + 1
        else:
            return d + 1
