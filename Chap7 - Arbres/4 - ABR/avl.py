from ArbreBinaire import ABR, Noeud


# Source : https://cours.etsmtl.ca/SEG/FHenri/inf145/Suppl%C3%A9ments/arbres%20AVL.htm
class AVL(ArbreBinaire):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = None 
        self.hauteur = -1

    def balancement(self):
        """ AVL -> int
        Facteur de balancement de l'AVL self """
        if self.est_vide():
            return 0
        return self.droit().hauteur - self.gauche().hauteur

    def inserer(self, e):
        """ AVL, e -> None
        Insère e dans l'AVL self """
        # À l'issue de l'exécution de cette méthode, self est un AVL
        z = self.descendre(e)
        pb = self.remonter(z)
        if pb:
            pb.equilibrer()

    def descendre(self, e):
        """ AVL, int -> AVL
        Ajoute l'élément e dans l'AVL self sans équilibrage
        Renvoie la feuille (AVL) correspondante """
        if self.est_vide():
            self.racine = Noeud(e, AVL(), AVL())
            self.hauteur += 1
            return self
        elif e < self.etiquette():
            self.gauche().parent = self
            self.hauteur += 1
            return self.gauche().descendre(e)
        else:
            self.droit().parent = self
            self.hauteur += 1
            return self.droit().descendre(e)

    def remonter(self, z):
        """ AVL, AVL -> AVL | None
        Renvoie le premier AVL non balancé en remontant depuis la feuille z
        Renvoie None si pas d'équilibrage à effectuer """
        while z.parent and z.parent.balancement() in {-1, 0, 1}:
            z = z.parent
        return z.parent

    def equilibrer(self):
        """ Équilibre l'AVL self """
        bg = self.gauche().balancement()
        bb = self.balancement()
        bd = self.droit().balancement()
        if bb in {-1, 0, 1}:
            return
        elif [bb, bd] == [2, 1]:
            print("rg")
            self.rg()
        elif [bg, bb] == [-1, -2]:
            print("rd")
            self.rd()
        elif [bb, bd] == [2, -1]:
            print("rdg")
            self.droit().rd()
            self.rg()
        elif [bg, bb] == [1, -2]:
            print("rgd")
            self.gauche().rg()
            self.rd()
        # si une rotation a été effectuée, la hauteur de tous les
        # parents de self doit être diminuée de 1
        fix_hauteur = self.parent
        while fix_hauteur:
            fix_hauteur.hauteur -= 1
            fix_hauteur = fix_hauteur.parent
            

    def rg(self):
        """ Effectue une rotation gauche sur l'AVL self """
        x = self.droit().etiquette()
        y = self.etiquette()
        a = self.gauche()
        b = self.droit().gauche()
        c = self.droit().droit()
        gauche = AVL(Noeud(y, a, b))
        self.racine = Noeud(x, gauche, c)
        # on met à jour les hauteurs correspondantes
        self.gauche().hauteur = b.hauteur + 1
        self.hauteur = b.hauteur + 2
        
    def rd(self):
        """ Effectue une rotation droite sur l'AVL self """
        x = self.gauche().etiquette()
        y = self.etiquette()
        a = self.gauche().gauche()
        b = self.gauche().droit()
        c = self.droit()
        droit = AVL(Noeud(y, b, c))
        self.racine = Noeud(x, a, droit)
        # on met à jour les hauteurs correspondantes
        self.droit().hauteur = b.hauteur + 1
        self.hauteur = b.hauteur + 2
    
def test1():
    a = AVL()
    n = 25
    for e in range(n):
        a.inserer(e)
    for e in range(2*n, n - 1, -1):
        a.inserer(e)
    print(a)
    print(a.hauteur)

def test2():
    a = AVL()
    for e in [10, 5, 6, 12, 14, 8]:
        a.inserer(e)
    print(a)
    print(a.hauteur)

test1()
test2()
