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
        """ Graphe, int, int -> Nonetype
        Ajoute l'arc source -> destination """
        self.adj[source][destination] = True

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
        # devrait s'appeler est_successeurs
        # il s'agit des sommets que l'on peut atteindre depuis source
        return self.adj[source][destination]

    def sommets(self):
        """ Graphe -> [int]
        Renvoie la liste des sommets du graphe self """
        return [i for i in range(self.n)]
        # s = []
        # for i in range(self.n):
        #     s.append(i)
        # return s

    def voisins(self, sommet):
        """ Graphe, int -> [int]
        Renvoie la liste des voisins de sommet """
        return [destination for destination in self.sommets()
                if self.est_voisin(sommet, destination)] 
        v = []
        for destination in self.sommets():
            if self.est_voisin(sommet, destination):
                v.append(destination)
        return v

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

g1 = Graphe(4)
g1.ajouter_arc(0, 1)
g1.ajouter_arc(1, 3)
g1.ajouter_arc(0, 3)
g1.ajouter_arc(3, 2)
g1.ajouter_arc(2, 1)
