class Maillon:
    def __init__(self, v, n):
        self.valeur = v
        self.suivant = n

class Pile:
    """Une pile d'entiers"""
    def __init__(self):
        """ Pile -> Nonetype """
        self.sommet = None

    def est_vide(self):
        """ Pile -> bool
        Détermine si la pile est vide """
        return self.sommet is None
    
    def empiler(self, v):
        """ Pile, int -> Nonetype
        Empile la valeur v au sommet de la pile self """
        m = Maillon(v, self.sommet)
        self.sommet = m
    
    def depiler(self):
        """ Pile -> int
        Renvoie l'élément présent au sommet de la pile self, en le supprimant de la pile """
        if self.est_vide():
            raise IndexError("Impossible de dépiler : la pile est vide")
        else:
            valeur_e = self.sommet
            self.sommet = self.sommet.suivant
            return valeur_e.valeur
    
    def __str__(self):
        """ Pile -> str
        Construit la chaîne de caractère représentant la pile self """
        # s='[Sommet]'
        s = ["[Sommet]"]
        maillon_courant=self.sommet
        while maillon_courant != None:
            # s=s+f' {maillon_courant.valeur}'
            s.append(f' {maillon_courant.valeur}')
            maillon_courant=maillon_courant.suivant
        return "".join(s)

class File:
    """Une file d'entiers"""
    def __init__(self):
        """File -> Nonetype"""
        self.debut = None
        self.fin = None

    def est_vide(self):
        """ File -> bool
        Détermine si la file self est vide """
        return self.debut is None and self.fin is None
    
    def enfiler(self, v):
        """ File, int -> Nonetype
        Ajoute l'élément v à la file self """
        
    
    def defiler(self):
        """ File -> int
        Renvoie le premier élément de la file en le supprimant de celle-ci """
        pass
    
    def __str__(self):
        """ self -> str
        Construit la chaîne de caractères représentant la file self """
        pass

