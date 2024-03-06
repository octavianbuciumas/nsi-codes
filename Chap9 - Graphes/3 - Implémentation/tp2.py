class Graphe:
    """ Un graphe représenté par un dictionnaire d'adjacence. """
    def __init__(self):
        self.adj = dict()

    def ajouter_sommet(self, s):
        """ Graphe, str -> Nonetype
        Ajoute le sommet s au graphe self """
        # self.adj.setdefault(s,[])
        if not s in self.adj:
            self.adj[s] = []
        
    def ajouter_arc(self, source, destination):
        """ Graphe, str, str -> Nonetype
        Ajoute l'arc source -> destination au graphe self """
        self.adj[source].append(destination)
