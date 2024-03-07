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
    
    def ajouter_liste_arcs(self, arcs):
        """ Graphe, [(str, str)] -> Nonetype """
        for a in arcs:
            source, destination = a
            self.ajouter_sommet(source)
            self.ajouter_sommet(destination)
            self.ajouter_arc(source, destination)
    
    def voisins(self, sommet):
        """ Graphe, str -> [str]
        Renvoie la liste des voisins de sommet """
        return self.adj[sommet]
    
    def est_voisin(self, source, destination):
        """ Graphe, str, str -> bool
        Renvoie True ssi l'arc source -> destination existe """
        for v in self.adj[source]:
            if v == destination:
                return True
        return False
    
    def sommets(self):
        """ Graphe -> [str]
        Renvoie la liste des sommets du graphe self """
        return [s for s in self.adj]
        # return list(self.adj.keys())
        

g2 = Graphe()
g2.ajouter_liste_arcs([('A', 'B'),
                       ('A', 'C'),
                       ('A', 'D'),
                       ('B', 'D'),
                       ('C', 'A'),
                       ('C', 'D'),
                       ('D', 'E'),
                       ('E', 'F'),
                       ('F', 'E'),
                       ('F', 'F')])
print(g2.adj)