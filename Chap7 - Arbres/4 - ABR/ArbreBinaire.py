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
            return ""
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

a_vide = ArbreBinaire()    
feuille1 = ArbreBinaire(Noeud(1,
                              ArbreBinaire(),
                              ArbreBinaire()))
feuille2 = ArbreBinaire(Noeud(2,
                              ArbreBinaire(),
                              ArbreBinaire()))
a0 = ArbreBinaire(Noeud(3, feuille1, feuille2))
a1 = ArbreBinaire()
tab = [1, 2, 3] 
a1.ajouter_depuis_tableau(tab)
a2 = ArbreBinaire()
a2.ajouter_depuis_tableau([3, 1, 4, None, 2, None, None])
a3 = ArbreBinaire()
a3.ajouter_depuis_tableau([3, 2, 4, 1])
a4 = ArbreBinaire()
a4.ajouter_depuis_tableau([3, 2, 4, None, 1])
a5 = ArbreBinaire()
a5.ajouter_depuis_tableau([3, 2, 6, 0, 4])
a6 = ArbreBinaire()
a6.ajouter_depuis_tableau([3, 1, 5, None, None, 2, 9])
a7 = ArbreBinaire()
for i in range(7):
    a7.inserer(i)
a8 = ArbreBinaire()
a8.ajouter_depuis_tableau([4, 3, 6, 2, 1, 7, 8])
a9 = ArbreBinaire()
a9.ajouter_depuis_tableau([4, 5, 6, 2, 8, 5, 7])
a10 = ArbreBinaire()
a10.ajouter_depuis_tableau([5, 4, 9, 2, 3, 7, 8])
a11 = ArbreBinaire()
a11.ajouter_depuis_tableau([8, 5, 10, 1, 6, 9, 12])

abr_vide = ABR()    
abr_feuille1 = ABR(Noeud(1,
                     ABR(),
                     ABR()))
abr_feuille2 = ABR(Noeud(3,
                     ABR(),
                     ABR()))
a11 = ABR(Noeud(2, abr_feuille1, abr_feuille2))
a12 = ABR()
a12.inserer(2)
a12.inserer(1)
a12.inserer(3)
a12.inserer(5)
