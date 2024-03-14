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
        
    def liste_arcs(self):
        """ Graphe -> [str]
        Renvoie la liste des arcs du graphe self """
        l = []
        for source in self.sommets():
            for destination in self.voisins(source):
                l.append((source, destination))
        return l
        # commentaire :
        # c'est très exactement la même méthode
        # que dans le cas où les graphes étaient
        # implémentés avec les matrices d'adj.
        # On n'utilise que des méthodes et pas des
        # attributs de la classe.
    
    def ordre(self):
        """ Graphe -> int """
        return len(self.sommets())
        # return len(self.adj)
        # la taille d'un dictionnaire = nombre
        # de clés qui le composent
        # return len(list(self.adj.keys()))

    def taille(self):
        return len(self.liste_arcs())
    
    def decrire(self):
        print(f"Graphe d'ordre {self.ordre()}")
        for sommet in self.sommets():
            decrire_voisins = " ".join([str(s) for s in self.voisins(sommet)])
            print(f"Sommet {sommet} -> " + decrire_voisins)
        
        # print("Graphe d'ordre", self.ordre(), "et de taille", self.taille())
        # for sommet in self.sommets():
        #    print("Sommet", sommet, "-> ", end='')
        #    for voisin in self.voisins(sommet):
        #        print(voisin, " ", end = '')
        #    print()
        
    def supprimer_arc(self, source, destination):
        """ Graphe, str, str -> bool """
        for i in range(len(self.adj[source])):
            if self.adj[source][i] == destination:
                self.adj[source].pop(i)
                return True
        return False
                
    def supprimer_sommet(self, sommet):
        """ Graphe, str -> Nonetype """
        self.adj.pop(sommet)
        for source in self.sommets():
            while self.supprimer_arc(source, sommet):
                pass
        
    
    

g2 = Graphe()
g2.ajouter_liste_arcs([('A', 'B'),
                       ('A', 'C'),
                       ('A', 'D'),
                       ('A', 'D'),
                       ('A', 'D'),
                       ('B', 'D'),
                       ('C', 'A'),
                       ('C', 'D'),
                       ('D', 'E'),
                       ('E', 'F'),
                       ('F', 'E'),
                       ('F', 'F')])
print(g2.adj)