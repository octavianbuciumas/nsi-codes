class Graphe:
    """ Un graphe représenté par une matrice d'adjacence.
    Les sommets sont les nombres 0, 1, ..., n - 1. """
    def __init__(self, n):
        self.n = n
        self.adj = [[False]*n for _ in range(n)]

    def ajouter_sommet(self):
        """ Graphe -> Nonetype
        Ajoute un sommet au graphe """
        pass

    def ajouter_arc(self, source, destination):
        """ Graphe, int, int -> int
        Ajoute l'arc source -> destination """
        pass

    def supprimer_sommet(self, i):
        """ Graphe, int -> Nonetype
        Supprime le sommet i du graphe. Les sommets j > i sont renommés en j - 1. """
        pass

    def supprimer_arc(self, source, destination):
        """ Graphe, int, int -> Nonetype
        Supprime l'arc source -> destination """
        pass

    def est_voisin(self, source, destination):
        """ Graphe, int, int -> bool
        Détermine si source et destination sont voisins """
        pass

    def sommets(self):
        """ Graphe -> [int]
        Renvoie la liste des sommets du graphe self """
        pass

    def voisins(self, sommet):
        """ Graphe, int -> [int]
        Renvoie la liste des voisins de sommet """
        pass

    def liste_arcs(self):
        """ Graphe -> [(int, int)]
        Renvoie la liste des arcs du graphe """
        pass

    def ordre(self):
        """ Graphe -> int
        Renvoie l'ordre du graphe  """
        pass

    def taille(self):
        """ Graphe -> int
        Renvoie la taille du graphe """
        pass

    def decrire(self):
        """ Graphe -> Nonetype
        Affiche une description du graphe self """
        pass


