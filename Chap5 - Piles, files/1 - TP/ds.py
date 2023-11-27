#--- HDR ---#
class Chapeau:
    def __init__(self, t):
        self.taille = t

    def __repr__(self):
        return f"Chap. {self.taille}"

    def affiche(self):
        print(self)

class Pile:
    def __init__(self, max_elt = float('inf')):
        self.contenu = []
        self.max_elt = max_elt

    def __repr__(self):
        return "[" + ", ".join(b.__repr__() for b in self.contenu) + "] (Sommet pile)" 

    def __len__(self):
        return len(self.contenu)

    def affiche(self):
        print(self)

    def est_vide(self):
        return self.contenu == []

    def est_pleine(self):
        return self.max_elt == len(self)

    def empiler(self, c):
        # assert isinstance(c, Chapeau)
        if self.est_pleine():
            raise IndexError("Capacité maximale de la pile atteinte")
        self.contenu.append(c)

    def depiler(self):
        if self.est_vide():
            raise IndexError("Impossible de dépiler : la pile est vide.")
        return self.contenu.pop()
#--- HDR ---#

#--- HDR ---#
class Bonhomme:
    def __init__(self, t):
        self.taille = t

    def __repr__(self):
        return f"Bonh. {self.taille}"

    def affiche(self):
        print(self)

    def content(self, c):
        return c.taille == self.taille

class File:
    def __init__(self, max_elt = float('inf')):
        self.contenu = []
        self.max_elt = max_elt

    def __repr__(self):
        return "(Début file) [" + ", ".join(b.__repr__() for b in self.contenu) + "]"

    def __len__(self):
        return len(self.contenu)

    def affiche(self):
        print(self)

    def est_vide(self):
        return self.contenu == []

    def est_pleine(self):
        return len(self) == self.max_elt 

    def enfiler(self, b):
        # assert isinstance(b, Bonhomme)
        if self.est_pleine():
            raise IndexError("Capacité maximale de la file atteinte")
        self.contenu.append(b)

    def defiler(self):
        if self.est_vide():
            raise IndexError("Impossible de défiler : la file est vide.")
        return self.contenu.pop(0)
#--- HDR ---#
