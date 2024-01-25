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

a_vide = ArbreBinaire()    
feuille1 = ArbreBinaire(Noeud(1,
                              ArbreBinaire(),
                              ArbreBinaire()))
feuille2 = ArbreBinaire(Noeud(2,
                              ArbreBinaire(),
                              ArbreBinaire()))
a0 = ArbreBinaire(Noeud(3, feuille1, feuille2))

