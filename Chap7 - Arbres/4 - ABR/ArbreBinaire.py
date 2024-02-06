class Noeud:
    def __init__(self, v, g, d):
        self.etiquette = v
        self.gauche = g
        self.droit = d

class ArbreBinaire:
    """Représente un arbre binaire"""
    def __init__(self, n = None):
        """ArbreBinaire, Noeud -> NoneType"""
        self.racine = n

    def est_vide(self):
        """ ArbreBinaire -> bool """
        return self.racine is None
    
    def etiquette(self):
        """ ArbreBinaire -> int """
        return self.racine.etiquette
    
    def gauche(self):
        """ ArbreBinaire -> ArbreBinaire """
        return self.racine.gauche
    
    def droit(self):
        """ ArbreBinaire -> ArbreBinaire """
        return self.racine.droit
    
    def est_feuille(self):
        """ ArbreBinaire -> bool """
        return not self.est_vide() and self.gauche().est_vide() and self.droit().est_vide()
    
    def __str__(self):
        """ ArbreBinaire -> str """
        if self.est_vide():
            return "×"
        return f"({self.gauche()}) {self.etiquette()} ({self.droit()})"
    
    def to_latex(self):
        if self.est_vide():
            return "[,phantom]"
        else:
            return f"[${self.etiquette()}$ {self.gauche().to_latex()} {self.droit().to_latex()}]"
    
    def ajouter_depuis_tableau(self, tab):
        """ ArbreBinaire, [int] -> Nonetype
        Ajoute à l'arbre binaire self (supposé initiallement vide) les éléments de tab (correspondant à un parcours en largeur de l'arbre) """
        file = [self]
        while tab != []:
            a = file.pop(0)
            # ajout de l'étiquette et création des enfants
            elem = tab.pop(0)
            if elem is not None:
                a.racine = Noeud(elem,
                                ArbreBinaire(),
                                ArbreBinaire())
            # ajouts des enfants à la file si besoin ultérieurement
            if elem is not None:
                file.append(a.gauche())
                file.append(a.droit())

    def taille(self):
        """ ArbreBinaire -> int
        Renvoie le nombre de nœuds dont est composé self """
        if self.est_vide():
            return 0
        else:
            return 1 + self.gauche().taille() + self.droit().taille()
    
    def appartient(self, e):
        """ ArbreBinaire, int -> bool
        Détermine si l'entier e est une étiquette de l'arbre self """
        if self.est_vide():
            return False
        elif self.etiquette() == e:
            return True
        else:
            return self.gauche().appartient(e) or self.droit().appartient(e)
    
    def inserer(self, e):
        """ ArbreBinaire, int
        Insère l'entier e dans l'arbre binaire self """
        if self.est_vide():
            self.racine = Noeud(e, ArbreBinaire(), ArbreBinaire())
        else:
            ng = self.gauche().taille()
            nd = self.droit().taille()
            if ng <= nd:
                self.gauche().inserer(e)
            else:
                self.droit().inserer(e)

class ABR(ArbreBinaire):
    """ Représentation dun ABR (Arbre Binaire de Recherche) """
    def inserer(self, e):
        """ ABR, int -> NoneType
        Insère l'élément e dans l'ABR self """
        if self.est_vide():
            self.racine = Noeud(e, ABR(), ABR())
        elif e < self.etiquette():
            self.gauche().inserer(e)
        else:
            self.droit().inserer(e)

    def appartient(self, e):
        """ ABR, int -> bool
        Détermine si l'élément e est une des étiquettes de l'ABR """
        if self.est_vide():
            return False
        elif self.etiquette() == e:
            return True
        elif e <= self.etiquette():
            return self.gauche().appartient(e)
        else:
            return self.droit().appartient(e)

    def parcours_stocke(self, l):
        """ ABR, list -> None
        Stocke dans la liste l les étiquettes de self dans l'ordre infixe """
        if self.est_vide():
            pass
        else:
            self.gauche().parcours_stocke(l)
            l.append(self.etiquette())
            self.droit().parcours_stocke(l)

    def vers_tableau(self):
        """ ABR -> list
        Renvoie la liste des étiquettes de self dans l'ordre infixe """
        l = []
        self.parcours_stocke(l)
        return l

